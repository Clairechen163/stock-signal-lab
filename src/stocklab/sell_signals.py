"""Sell signals: a rule library, a holdings check, and an event study that tests each rule.

Two questions are kept separate on purpose:

1. "What are my rules saying about my position right now?"  -> check_holding()
   A transparent scorecard that turns triggered rules into HOLD / WATCH / REDUCE / EXIT,
   with the price levels that would change the verdict.

2. "Do these rules actually predict worse returns?"            -> event_study()
   For each rule, compare forward returns after the rule fires against randomly chosen
   days from the same stocks (a Monte Carlo null), then control the false discovery
   rate across all rules and horizons. Many popular sell signals fail this test, and
   knowing which ones is the point.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np
import pandas as pd

from .stats import benjamini_hochberg


@dataclass(frozen=True)
class Rule:
    key: str
    category: str
    weight: int
    description: str
    fn: Callable[[pd.DataFrame], pd.Series]


def _distribution_days(df: pd.DataFrame) -> pd.Series:
    """O'Neil-style distribution day: close down >= 0.2% on higher volume than the prior day."""
    down = df["Close"].pct_change() <= -0.002
    heavier = df["Volume"] > df["Volume"].shift(1)
    return down & heavier


def _rsi_bearish_divergence(df: pd.DataFrame) -> pd.Series:
    """Price at a 20-day closing high while RSI sits 5+ points below its own 20-day high."""
    at_high = df["Close"] >= df["Close"].rolling(20).max()
    weaker_rsi = df["RSI"] < df["RSI"].rolling(20).max().shift(1) - 5
    return at_high & weaker_rsi


RULES: list[Rule] = [
    # Trend
    Rule("below_sma50", "trend", 1, "Close below the 50-day moving average", lambda d: d["Close"] < d["SMA50"]),
    Rule("below_sma200", "trend", 2, "Close below the 200-day moving average", lambda d: d["Close"] < d["SMA200"]),
    Rule("death_cross", "trend", 2, "50-day average below the 200-day average", lambda d: d["SMA50"] < d["SMA200"]),
    # Momentum
    Rule("rsi_divergence", "momentum", 1, "New 20-day high without a new RSI high (bearish divergence)", _rsi_bearish_divergence),
    Rule(
        "rsi_rollover",
        "momentum",
        1,
        "RSI was overbought (>70) in the last 5 days and has dropped below 65",
        lambda d: (d["RSI"].rolling(5).max() > 70) & (d["RSI"] < 65),
    ),
    Rule("macd_bearish", "momentum", 1, "MACD line below its signal line", lambda d: d["MACD"] < d["MACDSignal"]),
    # Volume
    Rule(
        "distribution_cluster",
        "volume",
        1,
        "5+ distribution days in the last 25 sessions (institutional selling)",
        lambda d: _distribution_days(d).rolling(25).sum() >= 5,
    ),
    Rule(
        "high_volume_breakdown",
        "volume",
        2,
        "Down day closing below the 50-day average on 1.5x+ average volume",
        lambda d: (d["Close"] < d["SMA50"]) & (d["Volume"] >= 1.5 * d["VolAvg50"]) & (d["Close"].diff() < 0),
    ),
    # Risk
    Rule("drawdown_20", "risk", 1, "20%+ below the 52-week high", lambda d: d["DrawdownFrom52wHigh"] <= -0.20),
    Rule(
        "volatility_spike",
        "risk",
        1,
        "21-day volatility 1.5x+ its 1-year median",
        lambda d: d["Vol21"] > 1.5 * d["Vol252Median"],
    ),
    Rule(
        "chandelier_stop",
        "risk",
        2,
        "Close below the chandelier stop (22-day high minus 3x ATR)",
        lambda d: d["Close"] < d["HighestHigh22"] - 3 * d["ATR"],
    ),
]
RULES_BY_KEY = {r.key: r for r in RULES}

STATUS_BANDS = [(0, "HOLD"), (3, "WATCH"), (6, "REDUCE"), (9, "EXIT")]


def rule_states(df_ind: pd.DataFrame) -> pd.DataFrame:
    """Boolean frame: whether each rule's condition holds on each day."""
    return pd.DataFrame({r.key: r.fn(df_ind).fillna(False).astype(bool) for r in RULES}, index=df_ind.index)


def onsets(states: pd.DataFrame, cooldown: int = 10) -> pd.DataFrame:
    """Days a rule switches from off to on, ignoring re-triggers within `cooldown` days."""
    out = {}
    for col in states:
        s = states[col]
        fresh = s & ~s.shift(1, fill_value=False)
        keep, last = [], -10**9
        for i, v in enumerate(fresh.to_numpy()):
            if v and i - last > cooldown:
                keep.append(True)
                last = i
            else:
                keep.append(False)
        out[col] = pd.Series(keep, index=s.index)
    return pd.DataFrame(out)


def _status(score: int) -> str:
    label = "HOLD"
    for threshold, name in STATUS_BANDS:
        if score >= threshold:
            label = name
    return label


# ------------------------------------------------------------- holdings check
def check_holding(df_ind: pd.DataFrame, entry_price: float | None = None, stop_pct: float = 0.15) -> dict:
    """Score the latest day for one holding.

    The weighted rule score maps to HOLD (0-2), WATCH (3-5), REDUCE (6-8) or EXIT (9+).
    A hard stop-loss you set yourself (entry minus `stop_pct`) overrides to EXIT: the
    point of a pre-committed stop is that you don't renegotiate it in the moment.
    """
    last = df_ind.iloc[-1]
    states = rule_states(df_ind).iloc[-1]
    triggered = [RULES_BY_KEY[k] for k, on in states.items() if on]
    score = sum(r.weight for r in triggered)
    status = _status(score)
    reasons = [f"[{r.category}] {r.description} (+{r.weight})" for r in triggered]

    close = float(last["Close"])
    levels = {
        "50-day SMA": float(last["SMA50"]),
        "200-day SMA": float(last["SMA200"]),
        "Chandelier stop": float(last["HighestHigh22"] - 3 * last["ATR"]),
    }
    result = {
        "date": df_ind.index[-1].date().isoformat(),
        "close": close,
        "rsi": float(last["RSI"]),
        "off_52w_high": float(last["DrawdownFrom52wHigh"]),
        "score": score,
        "max_score": sum(r.weight for r in RULES),
        "status": status,
        "reasons": reasons,
        "levels": levels,
    }
    if entry_price:
        pnl = close / entry_price - 1
        hard_stop = entry_price * (1 - stop_pct)
        result.update({"entry": entry_price, "pnl": pnl, "hard_stop": hard_stop})
        levels[f"Your {stop_pct:.0%} stop-loss"] = hard_stop
        if close <= hard_stop:
            result["status"] = "EXIT"
            reasons.insert(0, f"[position] Price is below your {stop_pct:.0%} stop-loss at {hard_stop:.2f} (overrides score)")
    return result


def format_check(ticker: str, r: dict) -> str:
    lines = [f"{ticker}  {r['status']}  (score {r['score']}/{r['max_score']}, close {r['close']:.2f} on {r['date']})"]
    if "entry" in r:
        lines.append(f"  Entry {r['entry']:.2f} -> P&L {r['pnl']:+.1%}")
    lines.append(f"  RSI {r['rsi']:.0f} | {r['off_52w_high']:+.1%} from 52-week high")
    lines.append("  Triggered:" if r["reasons"] else "  Triggered: none")
    lines += [f"    - {x}" for x in r["reasons"]]
    lines.append("  Levels to watch:")
    for name, lvl in sorted(r["levels"].items(), key=lambda kv: -kv[1]):
        side = "above" if r["close"] >= lvl else "below"
        lines.append(f"    {name:<22} {lvl:>10.2f}  (price is {side}, {r['close'] / lvl - 1:+.1%})")
    return "\n".join(lines)


# ---------------------------------------------------------------- event study
def _forward_returns(close: pd.Series, horizons) -> pd.DataFrame:
    out = {f"fwd_{h}d": close.shift(-h) / close - 1 for h in horizons}
    # Did the stock fall 10%+ below today's close at any point in the next 63 days?
    future_min = close[::-1].rolling(63, min_periods=63).min()[::-1].shift(-1)
    out["drop10_63d"] = (future_min / close - 1 <= -0.10).astype(float).where(future_min.notna())
    return pd.DataFrame(out)


def event_study(
    indicator_frames: dict[str, pd.DataFrame],
    horizons=(5, 21, 63),
    cooldown: int = 10,
    n_sims: int = 2000,
    seed: int = 0,
) -> pd.DataFrame:
    """Test every sell rule across a panel of stocks.

    For each rule and horizon:
      * mean forward return after the rule first fires (onset events),
      * mean forward return on random days drawn from the same stocks, matching the
        number of events per stock (stratified Monte Carlo null),
      * one-sided p-value that post-signal returns are lower than random-day returns,
      * how often a 10%+ drop followed within 63 days, vs the base rate,
      * Benjamini-Hochberg q-values across all rule x horizon tests.

    A sell rule earns the label "useful" only if returns after it are significantly
    worse than random (q < 0.10).
    """
    rng = np.random.default_rng(seed)
    panel = []
    for ticker, d in indicator_frames.items():
        d = d.dropna(subset=["SMA200"])
        fwd = _forward_returns(d["Close"], horizons)
        ev = onsets(rule_states(d), cooldown)
        panel.append((ticker, fwd, ev))

    rows = []
    for rule in RULES:
        for h in horizons:
            col = f"fwd_{h}d"
            ev_vals, pools, counts = [], [], []
            drop_ev, drop_all = [], []
            for _, fwd, ev in panel:
                valid = fwd[col].notna()
                hits = ev[rule.key] & valid
                ev_vals.append(fwd.loc[hits, col].to_numpy())
                pools.append(fwd.loc[valid, col].to_numpy())
                counts.append(int(hits.sum()))
                dvalid = fwd["drop10_63d"].notna()
                drop_ev.append(fwd.loc[ev[rule.key] & dvalid, "drop10_63d"].to_numpy())
                drop_all.append(fwd.loc[dvalid, "drop10_63d"].to_numpy())
            n = sum(counts)
            all_ev = np.concatenate(ev_vals) if n else np.array([])
            if n >= 5:
                obs = all_ev.mean()
                sims = np.empty(n_sims)
                for i in range(n_sims):
                    draws = [p[rng.choice(len(p), k, replace=False)] for p, k in zip(pools, counts) if k]
                    sims[i] = np.concatenate(draws).mean()
                p_val = (np.sum(sims <= obs) + 1) / (n_sims + 1)
                baseline = sims.mean()
            else:
                obs, baseline, p_val = np.nan, np.nan, np.nan
            de, da = np.concatenate(drop_ev), np.concatenate(drop_all)
            rows.append(
                {
                    "rule": rule.key,
                    "category": rule.category,
                    "horizon": f"{h}d",
                    "events": n,
                    "mean_after_signal": obs,
                    "mean_random_days": baseline,
                    "difference": obs - baseline if n >= 5 else np.nan,
                    "p_value": p_val,
                    "drop10_after_signal": de.mean() if len(de) else np.nan,
                    "drop10_base_rate": da.mean() if len(da) else np.nan,
                }
            )
    res = pd.DataFrame(rows)
    res["q_value"] = benjamini_hochberg(res["p_value"])
    res["verdict"] = np.select(
        [res["q_value"] < 0.10, res["difference"] < 0, res["events"] < 5],
        ["useful", "weak (not significant)", "too few events"],
        default="no edge",
    )
    res.loc[res["events"] < 5, "verdict"] = "too few events"
    return res


def format_event_study(res: pd.DataFrame) -> pd.DataFrame:
    out = res.copy()
    for c in ["mean_after_signal", "mean_random_days", "difference"]:
        out[c] = out[c].map(lambda v: "" if pd.isna(v) else f"{v:+.2%}")
    for c in ["drop10_after_signal", "drop10_base_rate"]:
        out[c] = out[c].map(lambda v: "" if pd.isna(v) else f"{v:.0%}")
    for c in ["p_value", "q_value"]:
        out[c] = out[c].map(lambda v: "" if pd.isna(v) else f"{v:.3f}")
    return out
