"""Stock selection and entry planning.

Selection is a transparent multi-factor score, not a black box:
  1. Hard filters remove stocks that break basic rules (downtrend, illiquid, collapsing).
  2. Factor z-scores rank what is left: momentum, trend quality, low volatility,
     shallow drawdown, and, when available, valuation and quality fundamentals.
  3. Each candidate gets an entry plan: a pullback zone, a breakout trigger, a stop
     based on volatility (ATR), and a position size that caps the loss if the stop hits.

Momentum and low volatility are among the most studied equity factors; valuation and
quality are added when Yahoo Finance fundamentals are reachable.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

DEFAULT_UNIVERSE = [
    # Technology and semiconductors
    "AAPL", "MSFT", "NVDA", "AVGO", "KLAC", "ALAB", "GOOGL", "AMZN",
    # Industrials and infrastructure
    "VRT", "CAT", "GE",
    # Financials
    "JPM", "V",
    # Health care
    "LLY", "UNH", "JNJ",
    # Consumer
    "COST", "PG", "KO",
    # Energy, utilities, materials, real estate
    "XOM", "NEE", "LIN", "AMT",
]

PRICE_FACTORS = {
    "momentum_12_1": 0.30,  # 12-month return excluding the latest month (avoids short-term reversal)
    "momentum_6m": 0.15,
    "trend_quality": 0.15,  # how far the 50-day average sits above the 200-day
    "low_volatility": 0.15,
    "shallow_drawdown": 0.10,
}
FUNDAMENTAL_FACTORS = {
    "value_forward_pe": 0.05,
    "growth_revenue": 0.05,
    "quality_margin": 0.05,
}


def price_factors(df_ind: pd.DataFrame) -> dict:
    c = df_ind["Close"]
    last = df_ind.iloc[-1]
    vol63 = np.log(c).diff().iloc[-63:].std() * np.sqrt(252)
    return {
        "close": float(last["Close"]),
        "momentum_12_1": float(c.iloc[-22] / c.iloc[-253] - 1) if len(c) > 253 else np.nan,
        "momentum_6m": float(c.iloc[-1] / c.iloc[-127] - 1) if len(c) > 127 else np.nan,
        "trend_quality": float(last["SMA50"] / last["SMA200"] - 1),
        "low_volatility": -float(vol63),
        "shallow_drawdown": float(last["DrawdownFrom52wHigh"]),
        "above_sma200": bool(last["Close"] > last["SMA200"]),
        "dollar_volume_m": float((c * df_ind["Volume"]).iloc[-20:].mean() / 1e6),
        "volatility": float(vol63),
        "rsi": float(last["RSI"]),
    }


def fundamentals(ticker: str) -> dict:
    """Valuation and quality from Yahoo Finance. Returns NaNs if unavailable (offline, ETF, etc.)."""
    try:
        import yfinance as yf

        info = yf.Ticker(ticker).info
    except Exception:
        info = {}
    fpe = info.get("forwardPE")
    return {
        "forward_pe": fpe,
        "value_forward_pe": -np.log(fpe) if fpe and fpe > 0 else np.nan,  # cheaper = higher score
        "growth_revenue": info.get("revenueGrowth", np.nan),
        "quality_margin": info.get("profitMargins", np.nan),
        "sector": info.get("sector", ""),
    }


def _zscore(s: pd.Series) -> pd.Series:
    s = s.astype(float)
    lo, hi = s.quantile([0.05, 0.95])
    s = s.clip(lo, hi)  # winsorize so one extreme stock can't dominate
    sd = s.std()
    return (s - s.mean()) / sd if sd and sd > 0 else s * 0


def entry_plan(df_ind: pd.DataFrame, capital: float, risk_per_trade: float, max_weight: float, atr_mult: float = 2.0):
    """Entry zone, stop and position size for one stock.

    Position size = (capital x risk per trade) / (entry - stop), capped at max_weight of
    capital. If the stop is hit you lose about `risk_per_trade` of capital, whatever the
    stock's volatility, which is what keeps one bad pick from sinking the portfolio.
    """
    last = df_ind.iloc[-1]
    close, a = float(last["Close"]), float(last["ATR"])
    supports = [float(last[k]) for k in ("SMA20", "SMA50") if float(last[k]) < close]
    pullback = max(supports) if supports else close - a
    breakout = float(df_ind["Close"].iloc[-20:].max())
    entry = pullback
    stop = entry - atr_mult * a
    risk_per_share = entry - stop
    shares = int(min(capital * risk_per_trade / risk_per_share, capital * max_weight / entry))
    return {
        "pullback_entry": round(entry, 2),
        "breakout_trigger": round(breakout * 1.002, 2),
        "stop": round(stop, 2),
        "stop_%": -risk_per_share / entry,
        "target_2R": round(entry + 2 * risk_per_share, 2),
        "shares": shares,
        "position_$": round(shares * entry, 0),
        "max_loss_$": round(shares * risk_per_share, 0),
    }


def screen(
    indicator_frames: dict[str, pd.DataFrame],
    use_fundamentals: bool = True,
    capital: float = 100_000,
    risk_per_trade: float = 0.01,
    max_weight: float = 0.10,
    min_dollar_volume_m: float = 20,
) -> pd.DataFrame:
    rows = {}
    for t, d in indicator_frames.items():
        d = d.dropna(subset=["SMA200", "ATR"])
        if len(d) < 130:
            continue
        row = price_factors(d)
        if use_fundamentals:
            row.update(fundamentals(t))
        row.update(entry_plan(d, capital, risk_per_trade, max_weight))
        rows[t] = row
    table = pd.DataFrame(rows).T

    # Hard rules: each one is a reason to skip, recorded rather than silently dropped
    reasons = pd.Series("", index=table.index)
    reasons[~table["above_sma200"].astype(bool)] += "below 200-day SMA; "
    reasons[table["dollar_volume_m"].astype(float) < min_dollar_volume_m] += "illiquid; "
    reasons[table["shallow_drawdown"].astype(float) < -0.5] += "down >50% from high; "
    table["passes_filters"] = reasons == ""
    table["filter_notes"] = reasons.str.rstrip("; ")

    weights = dict(PRICE_FACTORS)
    if use_fundamentals:
        weights.update(FUNDAMENTAL_FACTORS)
    score = pd.Series(0.0, index=table.index)
    used = pd.Series(0.0, index=table.index)
    for f, w in weights.items():
        if f not in table:
            continue
        z = _zscore(table[f])
        ok = z.notna()
        score[ok] += w * z[ok]
        used[ok] += w
    table["score"] = score / used.replace(0, np.nan)  # renormalize when some factors are missing
    table = table.sort_values(["passes_filters", "score"], ascending=[False, False])
    table["rank"] = range(1, len(table) + 1)
    return table


def format_screen(table: pd.DataFrame, top: int = 15) -> pd.DataFrame:
    cols = ["rank", "score", "passes_filters", "close", "momentum_12_1", "momentum_6m", "volatility",
            "shallow_drawdown", "forward_pe", "pullback_entry", "breakout_trigger", "stop", "stop_%",
            "shares", "position_$", "max_loss_$", "filter_notes"]
    out = table[[c for c in cols if c in table]].head(top).copy()
    for c in ["momentum_12_1", "momentum_6m", "volatility", "shallow_drawdown", "stop_%"]:
        if c in out:
            out[c] = out[c].map(lambda v: "" if pd.isna(v) else f"{float(v):+.1%}")
    out["score"] = out["score"].map(lambda v: f"{float(v):+.2f}")
    if "forward_pe" in out:
        out["forward_pe"] = out["forward_pe"].map(lambda v: "" if v is None or pd.isna(v) else f"{float(v):.1f}")
    out["close"] = out["close"].map(lambda v: f"{float(v):.2f}")
    return out.rename(columns={"shallow_drawdown": "off_52w_high"})
