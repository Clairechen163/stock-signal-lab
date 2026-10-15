"""Next-day return forecasting, evaluated the way it has to be: walk-forward, against baselines.

Every model is retrained on an expanding window and only ever predicts days it has not
seen. The headline question is not "what does the model say about tomorrow?" but
"has this model beaten a coin flip / a zero forecast out of sample, by more than luck?"
Daily stock returns are close to unpredictable, so the honest expected answer is "barely".
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.stats import norm
from sklearn.ensemble import HistGradientBoostingClassifier, HistGradientBoostingRegressor
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.metrics import brier_score_loss, roc_auc_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from . import stats

FEATURES_DOC = {
    "ret_1d..ret_5d": "log return on each of the last 5 days",
    "ret_21d": "cumulative log return over the last month",
    "dist_sma20/50/200": "distance of close from each moving average",
    "rsi": "14-day RSI",
    "macd_hist": "MACD histogram scaled by price",
    "vol_21d, vol_ratio": "21-day volatility and 5-day / 21-day volatility ratio",
    "atr_pct": "average true range as % of price",
    "volume_z": "log volume vs its 20-day mean, in standard deviations",
    "mkt_ret_1d, mkt_ret_5d": "benchmark (e.g. SPY) returns, if a benchmark is supplied",
}


def build_features(df_ind: pd.DataFrame, market: pd.Series | None = None) -> tuple[pd.DataFrame, pd.Series]:
    """Features known at the close of day t, and the target: log return from t to t+1."""
    c = df_ind["Close"]
    r = np.log(c).diff()
    X = pd.DataFrame(index=df_ind.index)
    for k in range(1, 6):
        X[f"ret_{k}d"] = r.shift(k - 1)
    X["ret_21d"] = r.rolling(21).sum()
    for n in (20, 50, 200):
        X[f"dist_sma{n}"] = c / df_ind[f"SMA{n}"] - 1
    X["rsi"] = df_ind["RSI"]
    X["macd_hist"] = df_ind["MACDHist"] / c
    vol5 = r.rolling(5).std()
    vol21 = r.rolling(21).std()
    X["vol_21d"] = vol21
    X["vol_ratio"] = vol5 / vol21
    X["atr_pct"] = df_ind["ATR"] / c
    lv = np.log(df_ind["Volume"].replace(0, np.nan))
    X["volume_z"] = (lv - lv.rolling(20).mean()) / lv.rolling(20).std()
    if market is not None:
        mr = np.log(market.reindex(df_ind.index).ffill()).diff()
        X["mkt_ret_1d"] = mr
        X["mkt_ret_5d"] = mr.rolling(5).sum()
    y = r.shift(-1).rename("next_ret")
    return X, y


def _models():
    clf = {
        "Majority class (baseline)": None,
        "Logistic regression": lambda: make_pipeline(StandardScaler(), LogisticRegression(C=0.1, max_iter=1000)),
        "Gradient boosting": lambda: HistGradientBoostingClassifier(
            max_depth=3, learning_rate=0.05, max_iter=150, min_samples_leaf=40, random_state=0
        ),
    }
    reg = {
        "Zero / random walk (baseline)": None,
        "Ridge regression": lambda: make_pipeline(StandardScaler(), Ridge(alpha=10.0)),
        "Gradient boosting": lambda: HistGradientBoostingRegressor(
            max_depth=3, learning_rate=0.05, max_iter=150, min_samples_leaf=40, random_state=0
        ),
    }
    return clf, reg


def walk_forward(X: pd.DataFrame, y: pd.Series, min_train: int = 504, step: int = 21) -> pd.DataFrame:
    """Expanding-window walk-forward predictions for every model.

    The model used for day t was fitted only on rows whose target (t'+1) is <= t,
    so no future information leaks into any prediction.
    """
    data = X.join(y).dropna()
    Xv, yv = data[X.columns], data[y.name]
    n = len(data)
    min_train = min(min_train, max(252, n // 2))
    if n - min_train < 42:
        raise ValueError(f"only {n} usable rows; need at least {min_train + 42}")
    clf_models, reg_models = _models()
    preds = pd.DataFrame(index=data.index[min_train:])
    preds["actual"] = yv.iloc[min_train:]
    cols = {}
    for start in range(min_train, n, step):
        end = min(start + step, n)
        # Train on rows whose next-day target was already realised before the first test row
        # (one extra row of buffer on top of that, to be conservative).
        X_tr, y_tr = Xv.iloc[: start - 1], yv.iloc[: start - 1]
        X_te = Xv.iloc[start:end]
        up_rate = (y_tr > 0).mean()
        for name, make in clf_models.items():
            key = f"P(up) | {name}"
            if make is None:
                p = np.full(len(X_te), up_rate)
            else:
                m = make().fit(X_tr, (y_tr > 0).astype(int))
                p = m.predict_proba(X_te)[:, 1]
            cols.setdefault(key, []).append(pd.Series(p, index=X_te.index))
        for name, make in reg_models.items():
            key = f"E[ret] | {name}"
            if make is None:
                p = np.zeros(len(X_te))
            else:
                p = make().fit(X_tr, y_tr).predict(X_te)
            cols.setdefault(key, []).append(pd.Series(p, index=X_te.index))
    for key, parts in cols.items():
        preds[key] = pd.concat(parts)
    return preds


def evaluate(preds: pd.DataFrame, cost_bps: float = 5) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Out-of-sample scorecards for the classification and regression models."""
    actual = preds["actual"]
    up = (actual > 0).astype(int)
    base_acc = max(up.mean(), 1 - up.mean())  # accuracy of always guessing the more common side
    rows = []
    for col in [c for c in preds if c.startswith("P(up)")]:
        p = preds[col]
        guess = (p > 0.5).astype(int)
        correct = int((guess == up).sum())
        try:
            auc = roc_auc_score(up, p) if p.nunique() > 1 else 0.5
        except ValueError:
            auc = np.nan
        # Trading test: hold the stock only on days the model says P(up) > 0.5.
        # Assumes the order is placed at the same close the forecast uses (market-on-close).
        pos = guess.astype(float)
        trades = pos.diff().abs().fillna(pos.iloc[0])
        strat = pos * (np.exp(actual) - 1) - trades * cost_bps / 10_000
        rows.append(
            {
                "model": col.split("| ")[1],
                "accuracy": correct / len(up),
                "always-majority accuracy": base_acc,
                "p (beats majority)": stats.binomial_accuracy_test(correct, len(up), base_acc),
                "AUC": auc,
                "Brier": brier_score_loss(up, p.clip(0, 1)),
                "strategy Sharpe": stats.sharpe(strat),
                "buy & hold Sharpe": stats.sharpe(np.exp(actual) - 1),
            }
        )
    clf_table = pd.DataFrame(rows).set_index("model")

    rows = []
    zero_err = actual.to_numpy()
    for col in [c for c in preds if c.startswith("E[ret]")]:
        f = preds[col].to_numpy()
        err = actual.to_numpy() - f
        sse, sse0 = np.sum(err**2), np.sum(zero_err**2)
        dm = stats.diebold_mariano(err, zero_err)
        rows.append(
            {
                "model": col.split("| ")[1],
                "RMSE (bps)": np.sqrt(np.mean(err**2)) * 1e4,
                "R2 out-of-sample vs zero": 1 - sse / sse0,
                "direction hit rate": np.mean(np.sign(f) == np.sign(actual)) if np.any(f != 0) else np.nan,
                "DM p (beats zero)": dm["p_value"] if np.any(f != 0) else np.nan,
            }
        )
    reg_table = pd.DataFrame(rows).set_index("model")
    return clf_table, reg_table


def predict_tomorrow(X: pd.DataFrame, y: pd.Series) -> dict:
    """Fit on all available history and forecast the next session from the latest row."""
    data = X.join(y).dropna()
    X_tr, y_tr = data[X.columns], data[y.name]
    x_last = X.dropna().iloc[[-1]]
    clf_models, reg_models = _models()
    out = {"as_of": x_last.index[0].date().isoformat()}
    for name, make in clf_models.items():
        if make is not None:
            out[f"P(up) | {name}"] = float(make().fit(X_tr, (y_tr > 0).astype(int)).predict_proba(x_last)[0, 1])
    out["P(up) | historical base rate"] = float((y_tr > 0).mean())
    ridge = reg_models["Ridge regression"]().fit(X_tr, y_tr)
    mu = float(ridge.predict(x_last)[0])
    sigma = float(x_last["vol_21d"].iloc[0])  # recent daily volatility
    z = norm.ppf(0.9)
    out["expected return (ridge)"] = float(np.exp(mu) - 1)
    out["80% range low"] = float(np.exp(mu - z * sigma) - 1)
    out["80% range high"] = float(np.exp(mu + z * sigma) - 1)
    out["daily volatility"] = sigma
    return out


def feature_importance(X: pd.DataFrame, y: pd.Series) -> pd.Series:
    """Standardized logistic-regression coefficients (sign = direction of effect on P(up))."""
    data = X.join(y).dropna()
    m = make_pipeline(StandardScaler(), LogisticRegression(C=0.1, max_iter=1000))
    m.fit(data[X.columns], (data[y.name] > 0).astype(int))
    coef = pd.Series(m[-1].coef_[0], index=X.columns)
    return coef.reindex(coef.abs().sort_values(ascending=False).index)
