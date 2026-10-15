import numpy as np
import pandas as pd

from stocklab import data, forecast, indicators, portfolio, screener, sell_signals


# ------------------------------------------------------------------ sell signals
def test_crash_triggers_exit():
    df = data.synthetic("CRASH", years=3)
    df = df.copy()
    crash = np.linspace(1.0, 0.55, 40)  # steady 45% slide over the last 40 days
    df.iloc[-40:, df.columns.get_loc("Close")] *= crash
    for col in ("Open", "High", "Low"):
        df.iloc[-40:, df.columns.get_loc(col)] *= crash
    r = sell_signals.check_holding(indicators.add_all(df))
    assert r["status"] in {"REDUCE", "EXIT"}
    assert any("50-day" in x for x in r["reasons"])


def test_hard_stop_overrides_score(ind):
    entry = ind["Close"].iloc[-1] * 1.5  # we're down 33% from entry
    r = sell_signals.check_holding(ind, entry_price=entry, stop_pct=0.15)
    assert r["status"] == "EXIT" and r["reasons"][0].startswith("[position]")


def test_onsets_respect_cooldown():
    s = pd.DataFrame({"x": [False, True, False, True, False, False, False, True]})
    ev = sell_signals.onsets(s, cooldown=3)["x"].tolist()
    assert ev == [False, True, False, False, False, False, False, True]


def test_event_study_shape_and_qvalues(panel):
    res = sell_signals.event_study(panel, horizons=(5, 21), n_sims=100)
    assert len(res) == len(sell_signals.RULES) * 2
    q = res["q_value"].dropna()
    assert ((q >= 0) & (q <= 1)).all()


# ---------------------------------------------------------------------- forecast
def test_walk_forward_never_trains_on_test_rows(ind):
    X, y = forecast.build_features(ind)
    preds = forecast.walk_forward(X, y, min_train=300, step=50)
    first_test = preds.index[0]
    usable = X.join(y).dropna()
    assert usable.index.get_loc(first_test) >= 252
    assert preds.filter(like="P(up)").stack().between(0, 1).all()


def test_forecast_target_is_next_day(ind):
    X, y = forecast.build_features(ind)
    r = np.log(ind["Close"]).diff()
    assert np.isclose(y.iloc[100], r.iloc[101])


def test_predict_tomorrow_range_contains_expectation(ind):
    X, y = forecast.build_features(ind)
    out = forecast.predict_tomorrow(X, y)
    assert out["80% range low"] < out["expected return (ridge)"] < out["80% range high"]


# ----------------------------------------------------------------------- screen
def test_screen_ranks_and_sizes(panel):
    t = screener.screen(panel, use_fundamentals=False, capital=100_000, risk_per_trade=0.01, max_weight=0.1)
    assert list(t["rank"]) == list(range(1, len(t) + 1))
    assert (t["max_loss_$"].astype(float) <= 1_000 + 1).all()  # never risk more than 1% of capital
    assert (t["position_$"].astype(float) <= 10_000 + 1).all()


# -------------------------------------------------------------------- portfolio
def test_portfolio_weights_valid(panel):
    px = data.close_matrix({t: d[["Close"]] for t, d in panel.items()})
    w, diag = portfolio.build(px.pct_change().dropna().iloc[-252:])
    weights = w["weight"]
    assert np.allclose(weights.sum(), 1) and (weights.to_numpy() >= -1e-9).all()


def test_risk_parity_equalizes_risk():
    rng = np.random.default_rng(0)
    rets = pd.DataFrame(rng.normal(0, [0.01, 0.02, 0.04], (500, 3)), columns=list("abc"))
    w, _ = portfolio.build(rets)
    rc = w[("risk share", "Risk parity")]
    assert rc.max() - rc.min() < 0.02


def test_walk_forward_portfolio_runs(panel):
    px = data.close_matrix({t: d[["Close"]] for t, d in panel.items()})
    summ, eq = portfolio.walk_forward(px, lookback=252)
    assert set(summ.index) == set(portfolio.METHODS)
    assert (eq > 0).all().all()
