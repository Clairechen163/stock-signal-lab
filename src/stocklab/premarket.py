"""Pre-market check: where each stock is trading before the US open, and what history says
about opening gaps.

Two separate things, kept separate on purpose:

1. A snapshot (`snapshot`, `view`): the latest pre-market (or intraday / after-hours) price,
   its change from the last close, which of the board's price levels it has crossed, and an
   untested "what-if" label: the board's rules applied as if today closed at that price.
   The published board and its track record keep using closing prices only.

2. A gap study (`gap_study`): over five years of daily data, does the opening gap (the
   overnight move, which is where pre-market trading ends up) say anything about the
   regular session that follows? Pooled regression of the open-to-close return on the gap,
   with a block bootstrap over dates, plus a table by gap size.
"""

from __future__ import annotations

import zlib

import numpy as np
import pandas as pd

from . import board, data, indicators

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
def _what_if_frames(frames: dict, snap: pd.DataFrame) -> dict:
    """Daily frames with one hypothetical bar added: today 'closing' at the latest price.

    The bar has no volume (pre-market volume is not comparable with a full session), so the
    two volume rules cannot fire on it; every other rule is evaluated as usual.
    """
    out = {}
    for t, d in frames.items():
        raw = d[data.COLUMNS]
        if t in snap.index:
            p = float(snap.at[t, "price"])
            day = pd.Timestamp(pd.Timestamp(snap.at[t, "time"]).date())
            if raw.index[-1] < day:
                bar = pd.DataFrame({"Open": [p], "High": [p], "Low": [p], "Close": [p], "Volume": [np.nan]}, index=[day])
                raw = pd.concat([raw, bar])
        out[t] = indicators.add_all(raw)
    return out


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
    hyp_table, _ = board.today(_what_if_frames(frames, snap), entries=entries, stop_pct=stop_pct)
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
                        "crossed": "", "what_if": "", "history": ""})
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
        what_if = hyp_table.at[t, "action"] if t in hyp_table.index else ""
        row.update({
            "price": price,
            "change": change,
            "session": s["session"] + (" (no trades yet today)" if stale else ""),
            "time": ts.strftime("%Y-%m-%d %H:%M") + " ET",
            "premarket_volume": s.get("premarket_volume", np.nan),
            "crossed": "; ".join(_crossings(close, price, levels)),
            "what_if": what_if + (" (changed)" if what_if and what_if != r["action"] else ""),
            "history": hist,
        })
        rows.append(row)
    return pd.DataFrame(rows).set_index("ticker")


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
