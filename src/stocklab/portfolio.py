"""Portfolio construction that spreads risk, not just dollars.

Equal dollar weights can still leave most of the risk in a few volatile, highly
correlated stocks (e.g. three AI-hardware names). This module estimates the covariance
matrix with Ledoit-Wolf shrinkage (more stable than the sample covariance), builds
several long-only portfolios, reports where each one's risk actually comes from, and
compares them out of sample with a monthly-rebalanced walk-forward backtest.

Maximum-Sharpe optimisation is deliberately left out: it needs expected-return
estimates, which are far noisier than risk estimates and tend to produce extreme,
unstable weights.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.optimize import minimize
from sklearn.covariance import LedoitWolf

from . import stats

TRADING_DAYS = 252


def shrunk_cov(returns: pd.DataFrame) -> np.ndarray:
    return LedoitWolf().fit(returns.to_numpy()).covariance_ * TRADING_DAYS


def effective_cap(max_weight: float, n: int) -> float:
    """A per-stock weight cap only makes sense with enough stocks; loosen it for small portfolios."""
    return min(1.0, max(max_weight, 2 / n))


def risk_contributions(w: np.ndarray, cov: np.ndarray) -> np.ndarray:
    """Share of total portfolio variance coming from each holding (sums to 1)."""
    port_var = w @ cov @ w
    return w * (cov @ w) / port_var


def _solve(objective, n, max_weight):
    cons = [{"type": "eq", "fun": lambda w: w.sum() - 1}]
    bounds = [(0.0, max_weight)] * n
    x0 = np.full(n, 1 / n)
    res = minimize(objective, x0, method="SLSQP", bounds=bounds, constraints=cons, options={"maxiter": 500, "ftol": 1e-12})
    w = np.clip(res.x, 0, None)
    return w / w.sum()


def equal_weight(cov, max_weight=1.0):
    n = len(cov)
    return np.full(n, 1 / n)


def inverse_volatility(cov, max_weight=1.0):
    w = 1 / np.sqrt(np.diag(cov))
    w = w / w.sum()
    if w.max() > max_weight:  # respect the cap by re-solving as a projection
        w = _solve(lambda x: np.sum((x - w) ** 2), len(w), max_weight)
    return w


def minimum_variance(cov, max_weight=0.35):
    return _solve(lambda w: w @ cov @ w * 1e4, len(cov), max_weight)


def risk_parity(cov, max_weight=1.0):
    """Equal risk contribution: each holding contributes the same share of portfolio risk."""
    n = len(cov)

    def obj(w):
        rc = w * (cov @ w)
        return np.sum((rc - rc.mean()) ** 2) * 1e6

    return _solve(obj, n, max_weight)


METHODS = {
    "Equal weight": equal_weight,
    "Inverse volatility": inverse_volatility,
    "Risk parity": risk_parity,
    "Minimum variance": minimum_variance,
}


def build(returns: pd.DataFrame, max_weight: float = 0.35) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Weights and risk diagnostics for every method on the given return history."""
    cov = shrunk_cov(returns)
    max_weight = effective_cap(max_weight, returns.shape[1])
    vols = np.sqrt(np.diag(cov))
    weights, diag = {}, {}
    for name, fn in METHODS.items():
        w = fn(cov, max_weight)
        rc = risk_contributions(w, cov)
        port_vol = np.sqrt(w @ cov @ w)
        weights[name] = w
        diag[name] = {
            "expected volatility": port_vol,
            "diversification ratio": (w @ vols) / port_vol,  # >1 means correlations are helping
            "effective number of bets": 1 / np.sum(rc**2),
            "largest risk share": rc.max(),
            "largest risk holder": returns.columns[int(np.argmax(rc))],
        }
    w_table = pd.DataFrame(weights, index=returns.columns)
    rc_table = pd.DataFrame({k: risk_contributions(v, cov) for k, v in weights.items()}, index=returns.columns)
    w_table = pd.concat({"weight": w_table, "risk share": rc_table}, axis=1)
    return w_table, pd.DataFrame(diag).T


def walk_forward(prices: pd.DataFrame, lookback: int = 252, rebalance: int = 21, max_weight: float = 0.35, cost_bps=5):
    """Out-of-sample comparison: re-estimate weights monthly from trailing data only."""
    rets = prices.pct_change().dropna()
    n = len(rets)
    if n <= lookback + rebalance:
        raise ValueError(f"need more than {lookback + rebalance} days of overlapping history, have {n}")
    max_weight = effective_cap(max_weight, rets.shape[1])
    out = {name: [] for name in METHODS}
    idx = []
    prev = {name: np.zeros(rets.shape[1]) for name in METHODS}
    for start in range(lookback, n, rebalance):
        end = min(start + rebalance, n)
        window = rets.iloc[start - lookback : start]
        cov = shrunk_cov(window)
        period = rets.iloc[start:end].to_numpy()
        idx.extend(rets.index[start:end])
        for name, fn in METHODS.items():
            w = fn(cov, max_weight)
            turnover = np.abs(w - prev[name]).sum()
            # Weights drift with prices inside the month (buy-and-hold between rebalances)
            growth = np.cumprod(1 + period, axis=0)
            value = growth @ w
            daily = np.r_[value[0] - 1, value[1:] / value[:-1] - 1]
            daily[0] -= turnover * cost_bps / 10_000
            out[name].extend(daily)
            drifted = w * growth[-1]
            prev[name] = drifted / drifted.sum()
    daily = pd.DataFrame(out, index=idx)
    summary = {}
    for name in METHODS:
        r = daily[name]
        years = len(r) / TRADING_DAYS
        total = float(np.prod(1 + r)) - 1
        summary[name] = {
            "CAGR": (1 + total) ** (1 / years) - 1,
            "Volatility": r.std() * np.sqrt(TRADING_DAYS),
            "Sharpe": stats.sharpe(r),
            "Max drawdown": stats.max_drawdown(r),
        }
    return pd.DataFrame(summary).T, (1 + daily).cumprod()


def correlation_warnings(returns: pd.DataFrame, threshold: float = 0.7) -> list[str]:
    corr = returns.corr()
    notes = []
    cols = corr.columns
    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
            if corr.iloc[i, j] >= threshold:
                notes.append(f"{cols[i]} and {cols[j]} have correlation {corr.iloc[i, j]:.2f}: they tend to fall together")
    return notes
