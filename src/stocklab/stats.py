"""Statistical tools used to decide whether a result is real or noise.

Financial returns are autocorrelated in volatility and heavy-tailed, so we lean on
resampling methods (block bootstrap, Monte Carlo nulls) rather than textbook t-tests,
and correct for multiple testing whenever many rules are tested at once.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats as st

TRADING_DAYS = 252


def sharpe(returns: np.ndarray | pd.Series) -> float:
    r = np.asarray(returns, dtype=float)
    sd = r.std(ddof=1)
    return float(r.mean() / sd * np.sqrt(TRADING_DAYS)) if sd > 0 else float("nan")


def max_drawdown(returns: np.ndarray | pd.Series) -> float:
    eq = np.cumprod(1 + np.asarray(returns, dtype=float))
    return float((eq / np.maximum.accumulate(eq) - 1).min())


def circular_block_bootstrap_idx(n: int, block: int, rng: np.random.Generator) -> np.ndarray:
    """Indices for one circular block bootstrap sample (keeps short-range dependence)."""
    n_blocks = int(np.ceil(n / block))
    starts = rng.integers(0, n, n_blocks)
    idx = (starts[:, None] + np.arange(block)[None, :]).ravel() % n
    return idx[:n]


def bootstrap_diff_ci(a, b, stat=sharpe, n_boot=2000, block=21, alpha=0.05, seed=0):
    """Paired block-bootstrap CI and two-sided p-value for stat(a) - stat(b).

    a and b are aligned daily return series (e.g. a strategy and buy & hold over the
    same dates). Resampling the same blocks for both keeps their correlation intact.
    """
    a, b = np.asarray(a, float), np.asarray(b, float)
    rng = np.random.default_rng(seed)
    observed = stat(a) - stat(b)
    diffs = np.empty(n_boot)
    for i in range(n_boot):
        idx = circular_block_bootstrap_idx(len(a), block, rng)
        diffs[i] = stat(a[idx]) - stat(b[idx])
    lo, hi = np.nanquantile(diffs, [alpha / 2, 1 - alpha / 2])
    # p-value: how often the bootstrap distribution, re-centred at zero, is as extreme as observed
    centred = diffs - np.nanmean(diffs)
    p = float(np.mean(np.abs(centred) >= abs(observed)))
    return {"diff": observed, "ci_low": lo, "ci_high": hi, "p_value": p}


def benjamini_hochberg(pvals) -> np.ndarray:
    """False-discovery-rate adjusted q-values (Benjamini-Hochberg step-up)."""
    p = np.asarray(pvals, dtype=float)
    q = np.full_like(p, np.nan)
    ok = ~np.isnan(p)
    pv = p[ok]
    m = len(pv)
    if m == 0:
        return q
    order = np.argsort(pv)
    ranked = pv[order] * m / np.arange(1, m + 1)
    ranked = np.minimum.accumulate(ranked[::-1])[::-1]
    out = np.empty(m)
    out[order] = np.minimum(ranked, 1.0)
    q[ok] = out
    return q


def binomial_accuracy_test(n_correct: int, n_total: int, p0: float = 0.5) -> float:
    """One-sided p-value that accuracy exceeds p0 (e.g. coin flip or 'always up' rate)."""
    if n_total == 0:
        return float("nan")
    return float(st.binomtest(n_correct, n_total, p0, alternative="greater").pvalue)


def diebold_mariano(e_model, e_bench, h: int = 1, power: int = 2) -> dict:
    """Diebold-Mariano test of equal predictive accuracy (Harvey-Leybourne-Newbold correction).

    e_model, e_bench: forecast errors on the same targets. A negative statistic means
    the model has lower loss than the benchmark. Returns the one-sided p-value that
    the model is better.
    """
    d = np.abs(np.asarray(e_model, float)) ** power - np.abs(np.asarray(e_bench, float)) ** power
    d = d[~np.isnan(d)]
    n = len(d)
    if n < 10:
        return {"dm_stat": float("nan"), "p_value": float("nan")}
    dbar = d.mean()
    gamma = [np.sum((d[k:] - dbar) * (d[: n - k] - dbar)) / n for k in range(h)]
    var = (gamma[0] + 2 * sum(gamma[1:])) / n
    if var <= 0:
        return {"dm_stat": float("nan"), "p_value": float("nan")}
    dm = dbar / np.sqrt(var)
    hln = np.sqrt((n + 1 - 2 * h + h * (h - 1) / n) / n)
    stat = dm * hln
    return {"dm_stat": float(stat), "p_value": float(st.t.cdf(stat, df=n - 1))}


def monte_carlo_event_pvalue(series: pd.Series, event_mask: pd.Series, n_sims=2000, seed=0, alternative="less"):
    """Compare the mean of `series` on event dates against random dates.

    Null hypothesis: event dates are no different from randomly chosen dates in the
    same sample. Draw the same number of random dates many times and see how often
    their mean is as low (or high) as the event mean.
    """
    valid = series.dropna()
    events = valid[event_mask.reindex(valid.index).fillna(False).astype(bool)]
    k = len(events)
    if k < 3:
        return float("nan"), k
    rng = np.random.default_rng(seed)
    pool = valid.to_numpy()
    sims = np.array([pool[rng.choice(len(pool), k, replace=False)].mean() for _ in range(n_sims)])
    obs = events.mean()
    if alternative == "less":
        p = (np.sum(sims <= obs) + 1) / (n_sims + 1)
    else:
        p = (np.sum(sims >= obs) + 1) / (n_sims + 1)
    return float(p), k
