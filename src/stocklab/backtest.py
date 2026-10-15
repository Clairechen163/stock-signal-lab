"""Long-only signal backtests with next-day execution, trading costs and bootstrap significance."""

from __future__ import annotations

import numpy as np
import pandas as pd

from . import stats

TRADING_DAYS = 252


# ---------------------------------------------------------------- strategies
# Each strategy maps an indicator frame to a 0/1 Series: 1 = hold the stock at that close.
def stateful(entry: pd.Series, exit_: pd.Series) -> pd.Series:
    """Turn entry/exit event series into a position series (enter on entry, leave on exit)."""
    pos, out = 0, []
    for e, x in zip(entry.fillna(False), exit_.fillna(False)):
        if pos == 0 and e:
            pos = 1
        elif pos == 1 and x:
            pos = 0
        out.append(pos)
    return pd.Series(out, index=entry.index)


def buy_hold(df):
    return pd.Series(1, index=df.index)


def golden_cross(df):
    return (df["SMA50"] > df["SMA200"]).astype(int)


def above_sma50(df):
    return (df["Close"] > df["SMA50"]).astype(int)


def rsi_30_70(df):
    return stateful(df["RSI"] < 30, df["RSI"] > 70)


def macd_cross(df):
    return (df["MACD"] > df["MACDSignal"]).astype(int)


def trailing_stop(df, pct=0.20):
    """Hold; exit after a `pct` drop from the peak; re-enter on a close above the 50-day SMA."""
    pos, peak, out = 1, df["Close"].iloc[0], []
    for close, sma in zip(df["Close"], df["SMA50"]):
        if pos:
            peak = max(peak, close)
            if close <= peak * (1 - pct):
                pos = 0
        elif not np.isnan(sma) and close > sma:
            pos, peak = 1, close
        out.append(pos)
    return pd.Series(out, index=df.index)


def volume_breakout(df):
    entry = (df["Close"] > df["High20Prior"]) & (df["Volume"] >= 1.5 * df["VolAvg20"])
    return stateful(entry, df["Close"] < df["SMA50"])


STRATEGIES = {
    "Buy & Hold": buy_hold,
    "50/200 SMA cross": golden_cross,
    "Close > 50-day SMA": above_sma50,
    "MACD > signal": macd_cross,
    "RSI 30/70": rsi_30_70,
    "Trailing stop 20%": trailing_stop,
    "Volume breakout": volume_breakout,
}


# --------------------------------------------------------------------- engine
def run(df: pd.DataFrame, signal: pd.Series, cost_bps: float = 5, lag: int = 1):
    """Daily strategy returns.

    A signal computed from the close of day t is traded at the close of day t + lag
    (default: the next day's close), so it first earns the return from t+1 to t+2.
    lag=0 would assume you can trade at the very close that produced the signal,
    which is slightly optimistic.
    """
    ret = df["Close"].pct_change().fillna(0)
    pos = signal.shift(1 + lag).fillna(0)
    trades = pos.diff().abs().fillna(pos.iloc[0])
    strat = pos * ret - trades * cost_bps / 10_000
    return strat, pos, trades


def summarize(strat: pd.Series, pos: pd.Series, trades: pd.Series) -> dict:
    years = len(strat) / TRADING_DAYS
    eq_end = float(np.prod(1 + strat.to_numpy()))
    return {
        "Total return": eq_end - 1,
        "CAGR": eq_end ** (1 / years) - 1 if years > 0 else np.nan,
        "Max drawdown": stats.max_drawdown(strat),
        "Volatility": strat.std() * np.sqrt(TRADING_DAYS),
        "Sharpe": stats.sharpe(strat),
        "Round trips": int(trades.sum() // 2),
        "Time in market": pos.mean(),
    }


def backtest_ticker(df_ind: pd.DataFrame, cost_bps=5, n_boot=1000, seed=0):
    """Run every strategy on one ticker. Returns (summary table, equity curves).

    Each strategy's Sharpe ratio is compared with buy & hold using a paired block
    bootstrap, so the table says whether any edge is distinguishable from luck.
    """
    df = df_ind.dropna(subset=["SMA200"])  # common window once all indicators exist
    rows, curves = {}, {}
    base, *_ = run(df, buy_hold(df), cost_bps)
    for name, fn in STRATEGIES.items():
        strat, pos, trades = run(df, fn(df), cost_bps)
        row = summarize(strat, pos, trades)
        if name != "Buy & Hold" and n_boot:
            test = stats.bootstrap_diff_ci(strat, base, n_boot=n_boot, seed=seed)
            row["Sharpe vs B&H"] = test["diff"]
            row["95% CI"] = f"[{test['ci_low']:+.2f}, {test['ci_high']:+.2f}]"
            row["p-value"] = test["p_value"]
        rows[name] = row
        curves[name] = (1 + strat).cumprod()
    table = pd.DataFrame(rows).T
    return table, pd.DataFrame(curves)


def format_table(table: pd.DataFrame) -> pd.DataFrame:
    out = table.copy()
    pct = ["Total return", "CAGR", "Max drawdown", "Volatility"]
    for c in pct:
        out[c] = out[c].map(lambda v: f"{v:+.1%}")
    out["Time in market"] = out["Time in market"].map(lambda v: f"{v:.0%}")
    out["Sharpe"] = out["Sharpe"].map(lambda v: f"{v:.2f}")
    out["Round trips"] = out["Round trips"].map(lambda v: f"{int(v)}")
    if "Sharpe vs B&H" in out:
        out["Sharpe vs B&H"] = out["Sharpe vs B&H"].map(lambda v: "" if pd.isna(v) else f"{v:+.2f}")
        out["p-value"] = out["p-value"].map(lambda v: "" if pd.isna(v) else f"{v:.2f}")
        out["95% CI"] = out["95% CI"].fillna("")
    out.index.name = "strategy"
    return out
