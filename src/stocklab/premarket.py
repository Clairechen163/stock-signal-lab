"""Pre-market board: the board's rules with the latest pre-market price as today's price,
plus the evidence on whether deciding before the open helps.

Daily closing prices still supply each stock's history (averages, momentum, volatility);
the latest pre-market trade stands in for today's close. Three parts:

1. A snapshot (`snapshot`, `view`): latest extended-hours price per stock, its change from
   the last close, which of the board's levels it crosses, and the pre-market label with
   entry and stop levels recomputed at that price.

2. A timing test (`compare_timing`): five years of the same rules applied just before each
   open, with the official opening price standing in for the last pre-market trade (free
   pre-market history is only days long), against the close-based board. Both trade at the
   open on the same days, so the only difference is whether the overnight move was seen.

3. A gap study (`gap_study`): does the opening gap say anything about the regular session
   that follows?
"""

from __future__ import annotations

import zlib

import numpy as np
import pandas as pd

from . import board, data, indicators, stats

NY = "America/New_York"
GAP_BUCKETS = [
    (-np.inf, -0.03, "gap down 3%+"),
    (-0.03, -0.01, "down 1-3%"),
    (-0.01, 0.01, "within 1%"),
    (0.01, 0.03, "up 1-3%"),
    (0.03, np.inf, "gap up 3%+"),
]


# ------------------------------------------------------------------ sessions
def session_of(ts: pd.Timestamp) -> str:
    """US equity session for a New York timestamp (exchange holidays are not modelled)."""
    if ts.weekday() >= 5:
        return "closed"
    m = ts.hour * 60 + ts.minute
    if 4 * 60 <= m < 9 * 60 + 30:
        return "pre-market"
    if 9 * 60 + 30 <= m < 16 * 60:
        return "regular session"
    if 16 * 60 <= m < 20 * 60:
        return "after-hours"
    return "closed"


def now_ny() -> pd.Timestamp:
    return pd.Timestamp.now(tz=NY)


# ------------------------------------------------------------------ snapshot
def _yahoo_snapshot(tickers, now: pd.Timestamp, retries: int = 3) -> pd.DataFrame:
    """Latest 1-minute bar for each ticker, including pre- and after-market trading."""
    import time

    import yfinance as yf

    raw = None
    for attempt in range(retries):
        try:
            raw = yf.download(list(tickers), period="5d", interval="1m", prepost=True, auto_adjust=True,
                              group_by="ticker", progress=False, threads=True)
            if raw is not None and not raw.empty:
                break
        except Exception:
            raw = None
        if attempt < retries - 1:
            time.sleep(2 * 2**attempt)
    rows = {}
    if raw is None or raw.empty:
        return pd.DataFrame(rows)
    for t in tickers:
        sub = data._split_batch(raw, t)
        if sub is None or "Close" not in sub:
            continue
        sub = sub.dropna(subset=["Close"])
        if sub.empty:
            continue
        idx = pd.DatetimeIndex(sub.index)
        idx = idx.tz_localize("UTC") if idx.tz is None else idx
        sub.index = idx.tz_convert(NY)
        minutes = sub.index.hour * 60 + sub.index.minute
        pre = (sub.index.date == now.date()) & (minutes >= 240) & (minutes < 570)
        last_ts = sub.index[-1]
        rows[t] = {
            "price": float(sub["Close"].iloc[-1]),
            "time": last_ts,
            "session": session_of(last_ts),
            "premarket_volume": float(sub.loc[pre, "Volume"].sum()) if "Volume" in sub else np.nan,
            "premarket_high": float(sub.loc[pre, "High"].max()) if pre.any() and "High" in sub else np.nan,
            "premarket_low": float(sub.loc[pre, "Low"].min()) if pre.any() and "Low" in sub else np.nan,
        }
    return pd.DataFrame(rows).T


def _synthetic_snapshot(frames: dict, now: pd.Timestamp | None = None) -> pd.DataFrame:
    """Offline stand-in: a small random pre-market move from each stock's last close."""
    rows = {}
    for t, d in frames.items():
        last_day = d.index[-1]
        day = pd.bdate_range(last_day + pd.Timedelta(days=1), periods=1)[0]
        ts = pd.Timestamp(f"{day.date()} 08:47", tz=NY)
        rng = np.random.default_rng(zlib.crc32(f"{t}{day.date()}".encode()))
        price = float(d["Close"].iloc[-1]) * float(np.exp(rng.normal(0, 0.02)))
        rows[t] = {"price": price, "time": ts, "session": "pre-market", "premarket_volume": np.nan,
                   "premarket_high": price, "premarket_low": price}
    return pd.DataFrame(rows).T


def snapshot(tickers, source: str, frames: dict, now: pd.Timestamp | None = None) -> pd.DataFrame:
    """Latest extended-hours price per ticker: price, time (New York), session, pre-market volume/range."""
    if source == "yahoo":
        return _yahoo_snapshot(tickers, now or now_ny())
    return _synthetic_snapshot({t: frames[t] for t in tickers if t in frames}, now)


# ---------------------------------------------------------------- the view
def _price_bar(price: float, day: pd.Timestamp) -> pd.DataFrame:
    """A bar for a price seen before the session: open = high = low = close, no volume.

    Pre-market volume is not comparable with a full session, so the two volume rules cannot
    fire on this bar; every other rule is evaluated as usual.
    """
    return pd.DataFrame({"Open": [price], "High": [price], "Low": [price], "Close": [price], "Volume": [np.nan]},
                        index=[pd.Timestamp(day)])


def _premarket_frames(frames: dict, snap: pd.DataFrame) -> dict:
    """Daily frames with today's bar set to the latest pre-market price (where there is one)."""
    out = {}
    for t, d in frames.items():
        raw = d[data.COLUMNS]
        if t in snap.index:
            day = pd.Timestamp(pd.Timestamp(snap.at[t, "time"]).date())
            if raw.index[-1] < day:
                raw = pd.concat([raw, _price_bar(float(snap.at[t, "price"]), day)])
        out[t] = indicators.add_all(raw)
    return out


_what_if_frames = _premarket_frames  # earlier name, kept for compatibility


def _crossings(close: float, price: float, levels: dict) -> list[str]:
    out = []
    for name, lvl in levels.items():
        if lvl is None or pd.isna(lvl):
            continue
        if close >= lvl > price:
            out.append(f"now below {name} ({lvl:,.2f})")
        elif close <= lvl < price:
            out.append(f"now above {name} ({lvl:,.2f})")
    return out


def bucket_of(gap: float) -> str:
    for lo, hi, name in GAP_BUCKETS:
        if lo <= gap < hi:
            return name
    return ""


def view(frames: dict, table: pd.DataFrame, snap: pd.DataFrame, gaps: dict | None = None,
         entries: dict | None = None, stop_pct: float = 0.15) -> pd.DataFrame:
    """One row per stock: the board's close-based label, the latest price and what it changes."""
    entries = entries or {}
    hyp_table, _ = board.today(_premarket_frames(frames, snap), entries=entries, stop_pct=stop_pct)
    rows = []
    for t in table.index:
        d = frames[t]
        last = d.iloc[-1]
        close = float(last["Close"])
        r = table.loc[t]
        row = {"ticker": t, "board": r["action"] + ("*" if r["provisional"] else ""), "close": close,
               "close_date": d.index[-1].date().isoformat()}
        if t not in snap.index:
            row.update({"price": np.nan, "change": np.nan, "session": "no extended-hours data", "time": "",
                        "crossed": "", "premarket_label": "", "changed": False, "history": ""})
            rows.append(row)
            continue
        s = snap.loc[t]
        price = float(s["price"])
        ts = pd.Timestamp(s["time"])
        stale = ts.date() <= d.index[-1].date() and s["session"] != "after-hours"
        levels = {
            "50-day average": last.get("SMA50"),
            "200-day average": last.get("SMA200"),
            "chandelier stop": last["HighestHigh22"] - 3 * last["ATR"] if pd.notna(last.get("ATR")) else np.nan,
        }
        if r["action"] in ("BUY", "HOLD", "WATCH"):
            levels["breakout level"] = r.get("breakout_trigger")
            levels["board stop"] = r.get("stop")
        if entries.get(t):
            levels["your stop-loss"] = entries[t] * (1 - stop_pct)
        change = price / close - 1
        hist = ""
        if gaps and gaps.get("buckets") is not None:
            b = gaps["buckets"]
            name = bucket_of(change)
            if name in b.index and b.at[name, "days"] > 0:
                hist = (f"{name}: open-to-close avg {b.at[name, 'avg open-to-close']:+.2%}, closed above the open "
                        f"{b.at[name, 'closed above open']:.0%} of {int(b.at[name, 'days']):,} days")
        h = hyp_table.loc[t] if t in hyp_table.index else None
        label = "" if h is None else h["action"] + ("*" if h["provisional"] else "")
        buyable = h is not None and h["action"] in ("BUY", "HOLD", "WATCH")
        row.update({
            "price": price,
            "change": change,
            "session": s["session"] + (" (no trades yet today)" if stale else ""),
            "time": ts.strftime("%Y-%m-%d %H:%M") + " ET",
            "premarket_volume": s.get("premarket_volume", np.nan),
            "crossed": "; ".join(_crossings(close, price, levels)),
            "premarket_label": label,
            "changed": bool(h is not None and h["action"] != r["action"]),
            "pm_pullback_entry": h.get("pullback_entry") if buyable else np.nan,
            "pm_breakout": h.get("breakout_trigger") if buyable else np.nan,
            "pm_stop": h.get("stop") if buyable else np.nan,
            "pm_why": board.why(h) if h is not None else "",
            "history": hist,
        })
        rows.append(row)
    return pd.DataFrame(rows).set_index("ticker")


# ------------------------------------------------------------ timing test
def opening_labels(frames: dict, dates, keep: int = 320) -> pd.DataFrame:
    """Board labels as they would have looked just before each open on `dates`.

    For each date, every stock's history runs to the previous close and today's bar is the
    official opening price (the closest free stand-in for the last pre-market trade). Only
    the trailing `keep` days are recomputed, which is enough for every indicator; the true
    history length is passed on, so young listings are still treated as young.
    """
    raws = {t: d[data.COLUMNS] for t, d in frames.items()}
    out = {}
    for day in dates:
        sub, offsets = {}, {}
        for t, r in raws.items():
            i = r.index.searchsorted(day)
            if i >= len(r) or r.index[i] != day or i < 1:
                continue
            lo = max(0, i - keep)
            sub[t] = indicators.add_all(pd.concat([r.iloc[lo:i], _price_bar(float(r["Open"].iat[i]), day)]))
            offsets[t] = lo
        if len(sub) >= 2:
            out[day] = board.action_panel(sub, offsets)["action"].iloc[-1]
    return pd.DataFrame(out).T.reindex(columns=list(frames))


def _hold_weights(labels: pd.DataFrame, days: pd.DatetimeIndex) -> pd.DataFrame:
    """Enter on BUY, exit on SELL / REDUCE / AVOID / NO SIGNAL, equal weight; held until the next decision."""
    w = pd.DataFrame(0.0, index=days, columns=labels.columns)
    held: set[str] = set()
    current = pd.Series(0.0, index=labels.columns)
    decisions = labels.index
    for day in days:
        if day in decisions:
            acts = labels.loc[day]
            held = {t for t in held if acts.get(t) not in board.EXIT_LABELS and pd.notna(acts.get(t))}
            held |= {t for t, a in acts.items() if a == "BUY"}
            current = pd.Series({t: (1 / len(held) if t in held else 0.0) for t in labels.columns})
        w.loc[day] = current
    return w


def compare_timing(frames: dict, rebalance: int = 5, cost_bps: float = 5, n_boot: int = 1000,
                   min_eligible: int = 4, seed: int = 0) -> dict:
    """Does deciding just before the open, with the overnight move in view, beat deciding on the last close?

    On the same review days (every `rebalance` trading days):
      * close board:      labels from the previous close, traded at today's open;
      * pre-market board: labels with today's opening price as today's bar, traded at today's open.
    Positions are held open to open, with costs on turnover. Because the stand-in price is the
    open itself, the pre-market version is slightly flattered: a real 8:47 price is a noisier
    guide to the open than the open is to itself.
    """
    close_pan = board.action_panel(frames)
    action = close_pan["action"]
    eligible = close_pan["days"] >= board.MIN_SIGNAL_DAYS
    ok = eligible.sum(axis=1) >= min_eligible
    if ok.sum() < 3 * rebalance:
        return {}
    days = action.index[action.index.get_loc(ok.idxmax()) + 1:]
    review = days[::rebalance]

    opens = pd.DataFrame({t: d["Open"] for t, d in frames.items()}).reindex(action.index)
    oo = (opens.shift(-1) / opens - 1).reindex(days)  # held from today's open to tomorrow's open

    prev_close_labels = action.shift(1).reindex(review)  # decided at yesterday's close
    pre_labels = opening_labels(frames, review)

    def run(weights):
        turnover = weights.diff().abs().sum(axis=1).fillna(weights.abs().sum(axis=1))
        return (weights * oo.fillna(0)).sum(axis=1) - turnover * cost_bps / 10_000

    w_close = _hold_weights(prev_close_labels, days)
    w_pre = _hold_weights(pre_labels, days)
    elig_review = eligible.shift(1).reindex(review).fillna(False)
    ew_labels = pd.DataFrame(np.where(elig_review, "BUY", "NO SIGNAL"), index=review, columns=action.columns)
    w_ew = _hold_weights(ew_labels, days)

    returns = pd.DataFrame({
        "Board on the previous close": run(w_close),
        "Board on the pre-market price": run(w_pre),
        "Equal-weight watchlist": run(w_ew),
    }).iloc[:-1]  # the last day has no next open yet
    table = pd.DataFrame({k: board._summary(v) for k, v in returns.items()}).T
    test = None
    if n_boot:
        test = stats.bootstrap_diff_ci(returns["Board on the pre-market price"], returns["Board on the previous close"],
                                       n_boot=n_boot, seed=seed)
    both = pre_labels.notna() & prev_close_labels.notna()
    agree = float((pre_labels[both] == prev_close_labels[both]).sum().sum() / both.sum().sum()) if both.any().any() else np.nan
    return {"table": table, "equity": (1 + returns).cumprod(), "sharpe_test": test, "agreement": agree,
            "start": returns.index[0], "end": returns.index[-1], "reviews": len(review)}


def timing_sentence(c: dict) -> str:
    if not c:
        return ""
    t = c["table"]
    pre, cl = t.loc["Board on the pre-market price"], t.loc["Board on the previous close"]
    test = c.get("sharpe_test")
    verdict = ""
    if test:
        if test["ci_low"] > 0:
            word = "better than"
        elif test["ci_high"] < 0:
            word = "worse than"
        else:
            word = "not distinguishable from"
        verdict = (f" Sharpe ratio difference {test['diff']:+.2f} (95% block-bootstrap CI [{test['ci_low']:+.2f}, "
                   f"{test['ci_high']:+.2f}]): deciding before the open has been **{word} deciding on the previous close**.")
    return (f"From {c['start'].date()} to {c['end'].date()} ({c['reviews']} weekly decisions, both traded at the open), "
            f"labels set with the pre-market price returned {pre['CAGR']:+.1%} a year (worst drawdown {pre['Max drawdown']:.1%}) "
            f"against {cl['CAGR']:+.1%} ({cl['Max drawdown']:.1%}) for labels set at the previous close; the two agreed on "
            f"{c['agreement']:.0%} of stock-weeks.{verdict}")


# --------------------------------------------------------------- gap study
def gap_panel(frames: dict) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Opening gap (open / previous close - 1) and open-to-close return, dates x tickers."""
    gap = pd.DataFrame({t: d["Open"] / d["Close"].shift(1) - 1 for t, d in frames.items()})
    day = pd.DataFrame({t: d["Close"] / d["Open"] - 1 for t, d in frames.items()})
    ok = gap.notna() & day.notna() & (gap.abs() < 0.5)  # drops bad prints and unadjusted splits
    return gap.where(ok), day.where(ok)


def _slope(x: np.ndarray, y: np.ndarray) -> float:
    x, y = x - x.mean(), y - y.mean()
    vx = (x * x).sum()
    return float((x * y).sum() / vx) if vx > 0 else np.nan


def gap_study(frames: dict, n_boot: int = 1000, block: int = 21, seed: int = 0) -> dict:
    """Do opening gaps continue or reverse during the regular session?

    Slope: pooled least-squares slope of the open-to-close return on the opening gap, after
    winsorising both at the 0.5th/99.5th percentile. Uncertainty: circular block bootstrap
    over dates (whole cross-sections are resampled together, so same-day moves across stocks
    stay correlated). A negative slope means gaps tend to partly reverse; positive, continue.
    """
    gap, day = gap_panel(frames)
    if gap.notna().sum().sum() < 250:
        return {}
    lo_g, hi_g = np.nanquantile(gap.to_numpy(), [0.005, 0.995])
    lo_d, hi_d = np.nanquantile(day.to_numpy(), [0.005, 0.995])
    G, D = gap.clip(lo_g, hi_g).to_numpy(), day.clip(lo_d, hi_d).to_numpy()
    mask = ~np.isnan(G) & ~np.isnan(D)
    slope = _slope(G[mask], D[mask])

    rng = np.random.default_rng(seed)
    n = len(G)
    boots = np.empty(n_boot)
    for i in range(n_boot):
        starts = rng.integers(0, n, int(np.ceil(n / block)))
        idx = ((starts[:, None] + np.arange(block)[None, :]).ravel() % n)[:n]
        g, d, m = G[idx], D[idx], mask[idx]
        boots[i] = _slope(g[m], d[m])
    ci_low, ci_high = np.nanquantile(boots, [0.025, 0.975])
    p = float(np.mean(np.abs(boots - np.nanmean(boots)) >= abs(slope)))

    rows = []
    g_raw, d_raw = gap.to_numpy(), day.to_numpy()
    for lo, hi, name in GAP_BUCKETS:
        sel = mask & (g_raw >= lo) & (g_raw < hi)
        vals = d_raw[sel]
        rows.append({"gap": name, "days": int(sel.sum()), "avg gap": float(np.mean(g_raw[sel])) if sel.any() else np.nan,
                     "avg open-to-close": float(np.mean(vals)) if sel.any() else np.nan,
                     "closed above open": float(np.mean(vals > 0)) if sel.any() else np.nan})
    buckets = pd.DataFrame(rows).set_index("gap")

    if ci_high < 0:
        verdict = "gaps have tended to partly reverse during the regular session"
    elif ci_low > 0:
        verdict = "gaps have tended to continue during the regular session"
    else:
        verdict = "no reliable relationship, so the size of a gap has not told you which way the session goes"
    return {"slope": slope, "ci_low": float(ci_low), "ci_high": float(ci_high), "p_value": p, "verdict": verdict,
            "buckets": buckets, "stock_days": int(mask.sum()), "stocks": int((~np.isnan(G)).any(axis=0).sum()),
            "start": gap.index[np.where(mask.any(axis=1))[0][0]].date().isoformat(),
            "end": gap.index[np.where(mask.any(axis=1))[0][-1]].date().isoformat()}


def gap_sentence(g: dict) -> str:
    if not g:
        return ""
    # The slope is return per unit of gap, so it reads directly as "% of session move per 1% of gap".
    return (f"Across {g['stock_days']:,} stock-days ({g['stocks']} watchlist stocks, {g['start']} to {g['end']}), "
            f"each 1% of opening gap went with a {g['slope']:+.2f}% move from the open to the close "
            f"(95% block-bootstrap CI [{g['ci_low']:+.2f}%, {g['ci_high']:+.2f}%]): {g['verdict']}.")
