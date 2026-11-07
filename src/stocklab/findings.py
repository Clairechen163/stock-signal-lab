"""Headline results, a run-by-run log of them, and how stable each one has been.

A result that is significant today but not yesterday is close to its threshold, and
should be read as noise until it holds up. Every `update` run appends one row per data
date to `reports/findings_log.csv`; each headline line in the README then says how many of
the last runs agreed with today's verdict.
"""

from __future__ import annotations

import os

import numpy as np
import pandas as pd
from scipy import stats as st

from .stats import benjamini_hochberg

WINDOW = 10  # how many recent runs (distinct data dates) the stability counts look back over


# -------------------------------------------------------------- verdicts
def ci_verdict(test: dict | None) -> str:
    """'better', 'worse' or 'not distinguishable' from a confidence interval of a difference."""
    if not test:
        return ""
    if test["ci_low"] > 0:
        return "better"
    if test["ci_high"] < 0:
        return "worse"
    return "not distinguishable"


def gap_verdict(g: dict | None) -> str:
    if not g:
        return ""
    return "reverse" if g["ci_high"] < 0 else "continue" if g["ci_low"] > 0 else "none"


def backtest_counts(tables: dict) -> dict:
    """Rule-by-stock tests whose Sharpe interval excludes zero, and whether the wins exceed chance."""
    better = worse = total = 0
    for tab in tables.values():
        rows = tab.drop(index="Buy & Hold", errors="ignore")
        if "_ci_low" in rows:
            better += int((rows["_ci_low"] > 0).sum())
            worse += int((rows["_ci_high"] < 0).sum())
            total += len(rows)
    # Each 95% interval misses zero on either side 2.5% of the time by chance alone; a binomial
    # tail says whether the number of wins is more than that (tests on one stock are correlated,
    # so this is approximate).
    p_more = float(st.binomtest(better, total, 0.025, alternative="greater").pvalue) if total else float("nan")
    return {"better": better, "worse": worse, "total": total, "expected": total * 0.025, "p_more": p_more,
            "beyond_chance": bool(total and p_more < 0.05)}


def rule_results(tables: dict) -> pd.DataFrame:
    """One row per rule and stock: Sharpe difference vs buy & hold with its 95% CI, and how the
    rule changed the worst drawdown (positive = shallower than holding)."""
    rows = []
    for t, tab in tables.items():
        if "Buy & Hold" not in tab.index or "_ci_low" not in tab:
            continue
        bh = tab.loc["Buy & Hold"]
        for rule, r in tab.drop(index="Buy & Hold").iterrows():
            rows.append({"ticker": t, "rule": rule, "diff": float(r["Sharpe vs B&H"]),
                         "ci_low": float(r["_ci_low"]), "ci_high": float(r["_ci_high"]),
                         "dd_change": float(r["Max drawdown"] - bh["Max drawdown"]),
                         "time_in_market": float(r["Time in market"])})
    out = pd.DataFrame(rows, columns=["ticker", "rule", "diff", "ci_low", "ci_high", "dd_change", "time_in_market"])
    out["verdict"] = np.select([out["ci_low"] > 0, out["ci_high"] < 0], ["better", "worse"], "not distinguishable")
    return out


def forecast_tests(fc: dict) -> dict:
    """Every model-vs-baseline test across stocks, with false-discovery-rate control.

    Each stock contributes four tests: two classifiers against the majority-class rate
    (one-sided binomial test of accuracy) and two regressions against a zero forecast
    (Diebold-Mariano). Taking the best of many models and stocks is itself a multiple
    comparison, so the verdict uses Benjamini-Hochberg q-values across all of them.
    """
    rows = pd.DataFrame(fc.get("pvals", []), columns=["ticker", "model", "test", "p"])
    if rows.empty:
        return {"tests": 0, "significant": 0, "hits": [], "median_auc": float("nan"), "min_p": float("nan")}
    rows["q"] = benjamini_hochberg(rows["p"])
    hits = rows[rows["q"] < 0.10]
    auc = pd.Series(fc.get("auc", {}), dtype=float)
    return {"tests": int(rows["p"].notna().sum()), "significant": len(hits),
            "hits": [f"{r.ticker} {r.model.lower()} ({r.test})" for r in hits.itertuples()],
            "median_auc": float(auc.median()) if len(auc) else float("nan"),
            "min_p": float(rows["p"].min()), "stocks": int(rows["ticker"].nunique())}


# ------------------------------------------------------------------ log
def record(res: dict, as_of: str) -> dict:
    study = res.get("study")
    useful = study[study["verdict"] == "useful"] if study is not None and len(study) else pd.DataFrame()
    bt = backtest_counts(((res.get("backtest") or {}).get("tables")) or {})
    fc = forecast_tests(res.get("forecast") or {})
    board_eval = (res.get("board") or {}).get("evaluation") or {}
    tm = res.get("timing") or {}
    return {
        "as_of": as_of,
        "watchlist": ";".join(res.get("watchlist") or []),
        "event_tests": len(study) if study is not None else 0,
        "event_significant": ";".join(f"{r.rule} ({r.horizon})" for r in useful.itertuples()),
        "backtest_tests": bt["total"],
        "backtest_better": bt["better"],
        "backtest_worse": bt["worse"],
        "backtest_beyond_chance": bt["beyond_chance"],
        "forecast_tests": fc["tests"],
        "forecast_significant": fc["significant"],
        "forecast_median_auc": round(fc["median_auc"], 4) if pd.notna(fc["median_auc"]) else np.nan,
        "board_verdict": ci_verdict(board_eval.get("sharpe_test")),
        "timing_verdict": ci_verdict(tm.get("sharpe_test")),
        "gap_verdict": gap_verdict(res.get("gaps")),
    }


def append(rec: dict, path: str) -> pd.DataFrame:
    """Add today's row (replacing an earlier run on the same data date) and return the whole log."""
    new = pd.DataFrame([rec])
    if os.path.exists(path):
        old = pd.read_csv(path, dtype={"as_of": str}, keep_default_na=False, na_values=[""])
        new = pd.concat([old, new], ignore_index=True).drop_duplicates("as_of", keep="last")
    new = new.sort_values("as_of").reset_index(drop=True)
    new.to_csv(path, index=False)
    return new


# ------------------------------------------------------------ stability
def _runs(n: int) -> str:
    return f"{n} run" if n == 1 else f"{n} runs"


def stability(log: pd.DataFrame, as_of: str | None = None, window: int = WINDOW) -> dict[str, str]:
    """For each headline, how many of the last `window` runs (up to `as_of`) reached that run's verdict."""
    if log is None or log.empty:
        return {}
    if as_of is not None:
        log = log[log["as_of"].astype(str) <= str(as_of)]
        if log.empty:
            return {}
    recent = log.tail(window)
    n = len(recent)
    today = recent.iloc[-1]
    if n == 1:
        first = "first logged run, so no stability record yet"
        return {k: first for k in ("study", "backtest", "forecast", "board", "timing", "gaps")}

    def same(col):
        vals = recent[col].astype(str)
        return int((vals == str(today[col])).sum())

    out = {}
    sig_today = [s for s in str(today["event_significant"] or "").split(";") if s and s != "nan"]
    lists = recent["event_significant"].fillna("").astype(str).map(lambda s: [x for x in s.split(";") if x and x != "nan"])
    any_sig = int(lists.map(bool).sum())
    if sig_today:
        each = ", ".join(f"{s} in {int(lists.map(lambda L: s in L).sum())}" for s in sig_today)
        out["study"] = f"significant in the last {_runs(n)}: {each}"
    else:
        out["study"] = f"at least one rule was significant in {any_sig} of the last {_runs(n)}"
    out["backtest"] = f"same verdict in {same('backtest_beyond_chance')} of the last {_runs(n)}"
    fc_runs = recent[pd.to_numeric(recent["forecast_tests"], errors="coerce") > 0]
    if len(fc_runs):
        edge = int((pd.to_numeric(fc_runs["forecast_significant"], errors="coerce") > 0).sum())
        out["forecast"] = f"a test survived correction in {edge} of the last {_runs(len(fc_runs))}"
    for key, col in (("board", "board_verdict"), ("timing", "timing_verdict"), ("gaps", "gap_verdict")):
        if str(today[col]):
            out[key] = f"same verdict in {same(col)} of the last {_runs(n)}"
    return out
