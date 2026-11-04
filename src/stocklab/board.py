"""Daily buy/sell decision board for a watchlist.

`action_panel` labels every stock on every trading day using only data known at that
day's close. Today's board is the last row of the panel, and `evaluate` trades the
earlier rows, so the rule that is published each day is exactly the rule that was tested.

How a label is chosen (first match wins):

    NO SIGNAL  fewer than 60 trading days of history
    SELL       sell-warning score at 60%+ of its maximum, or your own stop-loss is hit
    REDUCE     sell-warning score at 40-59% of its maximum
    AVOID      below its trend line (200-day average; 50-day for listings under 200 days),
               illiquid, or 50%+ below its high
    WATCH      sell-warning score at 20-39% of its maximum
    BUY        none of the above, and a buy score in the top half of the watchlist
    HOLD       none of the above, buy score in the bottom half

The sell-warning score is the weighted rule scorecard from `sell_signals`; the buy score
is the cross-sectional factor score from `screener` (momentum, trend quality, low
volatility, shallow drawdown), computed among the watchlist on each date.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats as st

from . import stats
from .screener import PRICE_FACTORS, entry_plan
from .sell_signals import RULES, rule_states

TRADING_DAYS = 252
MIN_SIGNAL_DAYS = 60  # below this, no label at all
FULL_HISTORY_DAYS = 200  # below this, the trend test uses the 50-day average and the label is provisional
MIN_DOLLAR_VOLUME_M = 20
MAX_DRAWDOWN = -0.50

ORDER = ["BUY", "HOLD", "WATCH", "AVOID", "REDUCE", "SELL", "NO SIGNAL"]
ACTIONS = {
    #          (why it gets this label,                               if you own it,                 if you don't)
    "BUY": ("Healthy trend, few sell warnings, top half of the watchlist", "Keep or add", "Buy near the pullback entry or on a breakout"),
    "HOLD": ("Healthy trend, few sell warnings, bottom half of the watchlist", "Keep", "Wait until it ranks higher"),
    "WATCH": ("Some sell warnings (20-39% of the maximum score)", "Keep, tighten your stop", "Wait"),
    "AVOID": ("Below its trend line, illiquid, or 50%+ below its high", "Exit, or keep only with a tight stop", "Don't buy"),
    "REDUCE": ("Several sell warnings (40-59% of the maximum score)", "Trim the position", "Don't buy"),
    "SELL": ("Most sell warnings triggered (60%+), or your stop-loss was hit", "Exit", "Don't buy"),
    "NO SIGNAL": ("Fewer than 60 trading days of history", "No rule-based view yet", "No rule-based view yet"),
}
SHORT_RULE = {
    "below_sma50": "below 50-day",
    "below_sma200": "below 200-day",
    "death_cross": "death cross",
    "rsi_divergence": "RSI divergence",
    "rsi_rollover": "RSI rollover",
    "macd_bearish": "MACD bearish",
    "distribution_cluster": "distribution days",
    "high_volume_breakdown": "high-volume breakdown",
    "drawdown_20": "20%+ off high",
    "volatility_spike": "volatility spike",
    "chandelier_stop": "below chandelier stop",
}
EXIT_LABELS = {"SELL", "REDUCE", "AVOID", "NO SIGNAL"}


# ------------------------------------------------------------ daily signals
def ticker_signals(d: pd.DataFrame) -> pd.DataFrame:
    """Per-day inputs for one stock: history length, sell score, trend tests and buy factors."""
    n = np.arange(1, len(d) + 1)
    states = rule_states(d)
    score = np.zeros(len(d))
    max_score = np.zeros(len(d))
    for r in RULES:
        avail = n >= r.min_days
        score += r.weight * (states[r.key].to_numpy() & avail)
        max_score += r.weight * avail
    c = d["Close"]
    trend_ok = pd.Series(np.where(n >= FULL_HISTORY_DAYS, c > d["SMA200"], c > d["SMA50"]), index=d.index)
    dollar_vol = (c * d["Volume"]).rolling(20, min_periods=10).mean() / 1e6
    liquid = dollar_vol.isna() | (dollar_vol >= MIN_DOLLAR_VOLUME_M)  # CSVs without volume are not penalised
    log_ret = np.log(c).diff()
    out = pd.DataFrame(
        {
            "close": c,
            "days": n,
            "sell_score": score,
            "sell_max": max_score,
            "passes_filters": trend_ok & liquid & (d["DrawdownFrom52wHigh"] > MAX_DRAWDOWN),
            "momentum_12_1": c.shift(21) / c.shift(252) - 1,
            "momentum_6m": c / c.shift(126) - 1,
            "trend_quality": d["SMA50"] / d["SMA200"] - 1,
            "low_volatility": -log_ret.rolling(63, min_periods=40).std() * np.sqrt(TRADING_DAYS),
            "shallow_drawdown": d["DrawdownFrom52wHigh"],
        },
        index=d.index,
    )
    return out


def _cross_sectional_z(x: pd.DataFrame) -> pd.DataFrame:
    """Winsorised (5th/95th percentile) z-score across stocks on each date."""
    lo, hi = x.quantile(0.05, axis=1), x.quantile(0.95, axis=1)
    x = x.clip(lo, hi, axis=0)
    sd = x.std(axis=1).replace(0, np.nan)
    return x.sub(x.mean(axis=1), axis=0).div(sd, axis=0)


def action_panel(frames: dict[str, pd.DataFrame]) -> dict[str, pd.DataFrame]:
    """Label every stock on every date. Returns panels (dates x tickers)."""
    sig = {t: ticker_signals(d) for t, d in frames.items()}
    dates = sorted(set().union(*[s.index for s in sig.values()]))

    def panel(col):
        return pd.DataFrame({t: s[col] for t, s in sig.items()}).reindex(dates)

    days = panel("days")
    eligible = days >= MIN_SIGNAL_DAYS

    num = pd.DataFrame(0.0, index=days.index, columns=days.columns)
    den = num.copy()
    for f, w in PRICE_FACTORS.items():
        z = _cross_sectional_z(panel(f).where(eligible))
        num += w * z.fillna(0)
        den += w * z.notna()
    buy_score = (num / den.replace(0, np.nan)).where(eligible)
    top_half = buy_score.ge(buy_score.median(axis=1), axis=0) & buy_score.notna()

    s, m = panel("sell_score"), panel("sell_max")
    passes = panel("passes_filters").eq(True)
    conditions = [
        ~eligible,
        5 * s >= 3 * m,
        5 * s >= 2 * m,
        ~passes,
        5 * s >= m,
        top_half,
    ]
    choices = ["NO SIGNAL", "SELL", "REDUCE", "AVOID", "WATCH", "BUY"]
    labels = np.select([c.to_numpy() for c in conditions], choices, default="HOLD")
    action = pd.DataFrame(labels, index=days.index, columns=days.columns).where(days.notna())
    return {
        "action": action,
        "buy_score": buy_score,
        "buy_rank": buy_score.rank(axis=1, ascending=False),
        "sell_score": s,
        "sell_max": m,
        "days": days,
        "close": panel("close"),
    }


# ------------------------------------------------------------- today's board
def today(frames, entries=None, stop_pct=0.15, capital=100_000, risk_per_trade=0.01, max_weight=0.10):
    """Today's board: one row per stock with its label, the reasons and the levels to act on."""
    entries = entries or {}
    pan = action_panel(frames)
    states_today = {t: rule_states(d).iloc[-1] for t, d in frames.items()}
    rows = []
    n_ranked = int(pan["buy_score"].iloc[-1].notna().sum())
    for t, d in frames.items():
        d_last = d.index[-1]
        act = pan["action"].at[d_last, t]
        days = int(pan["days"].at[d_last, t])
        last = d.iloc[-1]
        close = float(last["Close"])
        triggered = [
            SHORT_RULE[r.key] for r in RULES if days >= r.min_days and bool(states_today[t][r.key])
        ]
        rank = pan["buy_rank"].at[d_last, t]
        row = {
            "ticker": t,
            "action": act,
            "provisional": MIN_SIGNAL_DAYS <= days < FULL_HISTORY_DAYS,
            "as_of": d_last.date().isoformat(),
            "close": close,
            "change_1d": close / float(d["Close"].iloc[-2]) - 1 if len(d) > 1 else np.nan,
            "change_1m": close / float(d["Close"].iloc[-22]) - 1 if len(d) > 22 else np.nan,
            "vs_sma50": close / float(last["SMA50"]) - 1 if pd.notna(last["SMA50"]) else np.nan,
            "vs_sma200": close / float(last["SMA200"]) - 1 if pd.notna(last["SMA200"]) else np.nan,
            "rsi": float(last["RSI"]),
            "buy_score": pan["buy_score"].at[d_last, t],
            "buy_rank": f"{int(rank)}/{n_ranked}" if pd.notna(rank) else "",
            "sell_warnings": f"{int(pan['sell_score'].at[d_last, t])}/{int(pan['sell_max'].at[d_last, t])}",
            "triggered": ", ".join(triggered),
            "history_days": days,
        }
        if days >= 50 and pd.notna(last["ATR"]):
            plan = entry_plan(d, capital, risk_per_trade, max_weight)
            row.update({k: plan[k] for k in ("pullback_entry", "breakout_trigger", "stop", "stop_%", "shares", "max_loss_$")})
        entry = entries.get(t)
        if entry:
            row["entry"] = entry
            row["pnl"] = close / entry - 1
            row["your_stop"] = entry * (1 - stop_pct)
            if close <= row["your_stop"]:
                row["action"] = "SELL"
                row["triggered"] = (f"your {stop_pct:.0%} stop-loss hit; " + row["triggered"]).rstrip("; ")
        rows.append(row)
    table = pd.DataFrame(rows).set_index("ticker")
    table["_order"] = table["action"].map({a: i for i, a in enumerate(ORDER)})
    table = table.sort_values(["_order", "buy_score"], ascending=[True, False]).drop(columns="_order")
    return table, pan


def why(row) -> str:
    """One-line plain-English reason for a board row."""
    if row["action"] == "NO SIGNAL":
        return f"only {row['history_days']} trading days of history"
    parts = []
    if row["action"] in ("BUY", "HOLD") and row["buy_rank"]:
        parts.append(f"buy rank {row['buy_rank']}")
    trend = row["vs_sma200"] if pd.notna(row["vs_sma200"]) else row["vs_sma50"]
    label = "200-day" if pd.notna(row["vs_sma200"]) else "50-day"
    if pd.notna(trend):
        parts.append(f"{trend:+.0%} vs {label} average")
    parts.append(row["triggered"] if row["triggered"] else "no sell warnings")
    text = "; ".join(parts)
    if row["provisional"]:
        text += f" (provisional: {row['history_days']} days of history)"
    return text


# ------------------------------------------------- historical evaluation
def _portfolio_returns(weights: pd.DataFrame, rets: pd.DataFrame, cost_bps: float) -> pd.Series:
    """Weights decided at close t are traded at close t+1, so they earn returns from t+2."""
    held = weights.shift(2).fillna(0)
    turnover = weights.shift(1).fillna(0).diff().abs().sum(axis=1).fillna(0)
    return (held * rets.fillna(0)).sum(axis=1) - turnover * cost_bps / 10_000


def _summary(r: pd.Series) -> dict:
    years = len(r) / TRADING_DAYS
    total = float(np.prod(1 + r.to_numpy())) - 1
    return {
        "CAGR": (1 + total) ** (1 / years) - 1 if years > 0 and total > -1 else np.nan,
        "Volatility": r.std() * np.sqrt(TRADING_DAYS),
        "Sharpe": stats.sharpe(r),
        "Max drawdown": stats.max_drawdown(r),
    }


def evaluate(pan: dict, benchmark: pd.Series | None = None, rebalance: int = 5, cost_bps: float = 5,
             n_boot: int = 1000, min_eligible: int = 4, seed: int = 0):
    """Backtest the board as a trading rule and test whether its labels separate winners from losers.

    Board strategy: on each rebalance day, buy every stock labelled BUY, sell any holding
    labelled SELL, REDUCE or AVOID, keep the rest; equal weight across holdings, cash when
    nothing qualifies. It is compared with holding every eligible watchlist stock in equal
    weight (same universe, same rebalance days) and with the benchmark.
    """
    action, close = pan["action"], pan["close"]
    eligible = pan["days"] >= MIN_SIGNAL_DAYS
    start_ok = eligible.sum(axis=1) >= min_eligible
    if not start_ok.any():
        raise ValueError(f"fewer than {min_eligible} stocks with {MIN_SIGNAL_DAYS}+ days of history")
    start = start_ok.idxmax()
    action, close, eligible = action.loc[start:], close.loc[start:], eligible.loc[start:]
    rets = close.pct_change()

    board_w = pd.DataFrame(0.0, index=action.index, columns=action.columns)
    ew_w = board_w.copy()
    held: set[str] = set()
    current_board = pd.Series(0.0, index=action.columns)
    current_ew = current_board.copy()
    for i, day in enumerate(action.index):
        if i % rebalance == 0:
            acts = action.loc[day]
            held = {t for t in held if acts.get(t) not in EXIT_LABELS}
            held |= {t for t, a in acts.items() if a == "BUY"}
            current_board = pd.Series({t: (1 / len(held) if t in held else 0.0) for t in action.columns})
            elig = [t for t in action.columns if eligible.at[day, t]]
            current_ew = pd.Series({t: (1 / len(elig) if t in elig else 0.0) for t in action.columns})
        board_w.loc[day] = current_board
        ew_w.loc[day] = current_ew

    series = {
        "Board strategy": _portfolio_returns(board_w, rets, cost_bps),
        "Equal-weight watchlist": _portfolio_returns(ew_w, rets, cost_bps),
    }
    if benchmark is not None:
        b = benchmark.reindex(action.index).pct_change().fillna(0)
        series[f"{benchmark.name or 'Benchmark'} (buy & hold)"] = b
    returns = pd.DataFrame(series).iloc[2:]

    table = pd.DataFrame({k: _summary(v) for k, v in returns.items()}).T
    invested = (board_w.sum(axis=1) > 0).iloc[2:]
    table.loc["Board strategy", "Time invested"] = invested.mean()
    table.loc["Board strategy", "Avg holdings"] = (board_w > 0).sum(axis=1).iloc[2:].mean()
    table.loc["Equal-weight watchlist", "Time invested"] = 1.0
    table.loc["Equal-weight watchlist", "Avg holdings"] = (ew_w > 0).sum(axis=1).iloc[2:].mean()
    test = None
    if n_boot:
        test = stats.bootstrap_diff_ci(returns["Board strategy"], returns["Equal-weight watchlist"], n_boot=n_boot, seed=seed)

    labels = label_study(pan, start)
    return {"table": table, "equity": (1 + returns).cumprod(), "sharpe_test": test, "labels": labels,
            "start": action.index[0], "end": action.index[-1]}


def label_study(pan: dict, start=None, horizon: int = 21) -> pd.DataFrame:
    """Forward return after each label, relative to the watchlist average on the same date.

    Sampled every `horizon` days so forward windows don't overlap; each date contributes one
    observation per label (the average excess return of the stocks with that label), and a
    t-test on those per-date values asks whether the label's excess return differs from zero.
    """
    action, close = pan["action"], pan["close"]
    if start is not None:
        action, close = action.loc[start:], close.loc[start:]
    fwd = close.shift(-horizon) / close - 1
    eligible = action.notna() & (action != "NO SIGNAL")
    sample = action.index[::horizon]
    rows = []
    for label in ORDER[:-1]:
        per_date, n_obs = [], 0
        for day in sample:
            f = fwd.loc[day][eligible.loc[day]]
            if f.isna().all() or len(f.dropna()) < 2:
                continue
            excess = f - f.mean()
            mask = action.loc[day][eligible.loc[day]] == label
            vals = excess[mask].dropna()
            if len(vals):
                per_date.append(vals.mean())
                n_obs += len(vals)
        if len(per_date) >= 3:
            arr = np.array(per_date)
            t_stat, p = st.ttest_1samp(arr, 0.0)
            rows.append({"label": label, "observations": n_obs, "dates": len(arr),
                         f"mean {horizon}d excess return": arr.mean(), "hit rate": np.mean(arr > 0), "p_value": p})
        else:
            rows.append({"label": label, "observations": n_obs, "dates": len(per_date),
                         f"mean {horizon}d excess return": np.nan, "hit rate": np.nan, "p_value": np.nan})
    return pd.DataFrame(rows).set_index("label")
