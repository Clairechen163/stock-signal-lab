"""Price data loading: Yahoo Finance, local CSV files, or synthetic data for offline demos and tests."""

from __future__ import annotations

import os
import time
import zlib

import numpy as np
import pandas as pd

COLUMNS = ["Open", "High", "Low", "Close", "Volume"]


def _standardize(df: pd.DataFrame) -> pd.DataFrame:
    if isinstance(df.columns, pd.MultiIndex):  # newer yfinance returns (field, ticker)
        df.columns = df.columns.get_level_values(0)
    df = df.copy()
    df.index = pd.to_datetime(df.index).tz_localize(None)
    if "Close" not in df:
        raise ValueError("price data needs a Close column")
    for col in ["Open", "High", "Low"]:
        if col not in df:
            df[col] = df["Close"]  # CSVs with only Close still work; ATR degrades gracefully
    if "Volume" not in df:
        df["Volume"] = np.nan
    return df[COLUMNS].dropna(subset=["Close"]).sort_index()


def drop_incomplete_bar(df: pd.DataFrame, now: pd.Timestamp | None = None) -> pd.DataFrame:
    """Drop today's bar while the US market is still open, so signals only use closing prices.

    Yahoo returns a partial bar for the current session; a run during US trading hours
    (for example in the evening in Asia) would otherwise treat a mid-day price as a close.
    """
    now = now if now is not None else pd.Timestamp.now(tz="America/New_York")
    if len(df) and df.index[-1].date() == now.date() and (now.hour, now.minute) < (16, 15):
        return df.iloc[:-1]
    return df


def from_yahoo(ticker: str, years: int, retries: int = 3) -> pd.DataFrame:
    """Daily adjusted prices from Yahoo Finance, retrying with backoff on network errors."""
    import yfinance as yf

    last_err = None
    for attempt in range(retries):
        try:
            df = yf.download(ticker, period=f"{years}y", auto_adjust=True, progress=False, threads=False)
            if df is not None and not df.empty:
                return drop_incomplete_bar(_standardize(df))
            last_err = ValueError(f"{ticker}: no data returned from Yahoo Finance")
        except Exception as e:  # rate limits and transient network errors
            last_err = e
        if attempt < retries - 1:
            time.sleep(2 * 2**attempt)
    raise last_err


def from_csv(ticker: str, csv_dir: str) -> pd.DataFrame:
    path = os.path.join(csv_dir, f"{ticker}.csv")
    df = pd.read_csv(path, parse_dates=["Date"], index_col="Date")
    return _standardize(df)


# Recent listings get a matching short history in offline mode, so the synthetic run
# exercises the same short-history code paths as real data (SpaceX listed June 2026,
# the SK Hynix ADR in July 2026).
SYNTHETIC_LISTING_DAYS = {"SPCX": 100, "SKHY": 82}


def synthetic(ticker: str, years: int = 5, seed: int | None = None) -> pd.DataFrame:
    """Regime-switching geometric Brownian motion with volume, for offline demos and tests.

    Bull and bear regimes alternate with random durations, so sell signals and
    drawdowns actually occur. The seed is derived from the ticker so results are
    reproducible but differ across tickers.
    """
    if seed is None:
        seed = zlib.crc32(ticker.encode())
    rng = np.random.default_rng(seed)
    n = min(years * 252, SYNTHETIC_LISTING_DAYS.get(ticker, years * 252))
    dates = pd.bdate_range(end=pd.Timestamp("2026-10-14"), periods=n)

    common = rng.normal(0, 0.012, n)  # shared "market" factor creates realistic correlation
    mu_bull, mu_bear = rng.uniform(0.25, 0.6), rng.uniform(-0.45, -0.15)
    sigma = rng.uniform(0.25, 0.6) / np.sqrt(252)
    regime, rets = 1, np.empty(n)
    remaining = rng.integers(60, 250)
    for i in range(n):
        if remaining == 0:
            regime = 1 - regime
            remaining = rng.integers(60, 250) if regime else rng.integers(20, 90)
        remaining -= 1
        mu = (mu_bull if regime else mu_bear) / 252
        vol = sigma * (1.0 if regime else 1.6)
        rets[i] = mu + 0.8 * common[i] + rng.normal(0, vol)

    close = 100 * np.exp(np.cumsum(rets))
    spread = np.abs(rng.normal(0, sigma, n)) * close
    high = close + spread
    low = np.maximum(close - spread, 0.01)
    open_ = np.r_[close[0], close[:-1]] * (1 + rng.normal(0, sigma / 3, n))
    base_vol = rng.lognormal(15, 0.3)
    volume = base_vol * np.exp(rng.normal(0, 0.35, n) + 8 * np.abs(rets))  # big moves, big volume
    df = pd.DataFrame(
        {"Open": open_, "High": np.maximum(high, open_), "Low": np.minimum(low, open_), "Close": close, "Volume": volume},
        index=dates,
    )
    df.index.name = "Date"
    return df


_CACHE: dict[tuple, pd.DataFrame] = {}
_FAILED: dict[tuple, str] = {}


def _split_batch(raw: pd.DataFrame, ticker: str) -> pd.DataFrame | None:
    """One ticker's columns from a multi-ticker yfinance download (either column layout)."""
    if not isinstance(raw.columns, pd.MultiIndex):
        return raw
    for level in (0, 1):
        if ticker in raw.columns.get_level_values(level):
            return raw.xs(ticker, axis=1, level=level)
    return None


def prefetch(tickers, years: int = 5, source: str = "yahoo", csv_dir: str | None = None, retries: int = 3) -> None:
    """Download many tickers from Yahoo in one request and fill the cache.

    One batched request is far less likely to hit Yahoo's rate limits than dozens of
    single-ticker requests, which matters when the refresh runs on a shared cloud runner.
    Tickers missing from the batch are fetched one by one later by `load`.
    """
    if source != "yahoo":
        return
    todo = [t for t in dict.fromkeys(tickers) if (t, years, source, csv_dir) not in _CACHE]
    if not todo:
        return
    import yfinance as yf

    raw = None
    for attempt in range(retries):
        try:
            raw = yf.download(todo, period=f"{years}y", auto_adjust=True, progress=False, threads=True, group_by="ticker")
            if raw is not None and not raw.empty:
                break
        except Exception:  # fall back to single-ticker downloads
            raw = None
        if attempt < retries - 1:
            time.sleep(2 * 2**attempt)
    if raw is None or raw.empty:
        return
    for t in todo:
        sub = _split_batch(raw, t)
        if sub is None or sub.dropna(how="all").empty:
            continue
        try:
            df = drop_incomplete_bar(_standardize(sub))
        except ValueError:
            continue
        if len(df):
            _CACHE[(t, years, source, csv_dir)] = df


def load(ticker: str, years: int = 5, source: str = "yahoo", csv_dir: str | None = None) -> pd.DataFrame:
    """Load daily OHLCV for one ticker. source: 'yahoo', 'csv' or 'synthetic'.

    Results are cached for the life of the process, so a full report downloads each
    ticker once even though several modules use it.
    """
    key = (ticker, years, source, csv_dir)
    if key in _CACHE:
        return _CACHE[key].copy()
    if key in _FAILED:  # don't retry a ticker that already failed in this run
        raise ValueError(_FAILED[key])
    if source == "yahoo":
        try:
            df = from_yahoo(ticker, years)
        except Exception as e:
            _FAILED[key] = str(e)
            raise
    elif source == "csv":
        if not csv_dir:
            raise ValueError("source='csv' needs csv_dir")
        df = from_csv(ticker, csv_dir)
    elif source == "synthetic":
        df = synthetic(ticker, years)
    else:
        raise ValueError(f"unknown source {source!r}")
    _CACHE[key] = df
    return df.copy()


def load_many(tickers, years=5, source="yahoo", csv_dir=None, min_rows=0, verbose=True, skipped=None):
    """Load several tickers; skip (and report) any that fail or are too short.

    If `skipped` is a dict, each skipped ticker is recorded there with the reason.
    """
    out = {}
    for t in tickers:
        try:
            df = load(t, years, source, csv_dir)
            if len(df) < min_rows:
                raise ValueError(f"only {len(df)} trading days of history, needs {min_rows}")
            out[t] = df
        except Exception as e:  # network errors, delisted tickers, missing files
            if verbose:
                print(f"  {t}: skipped ({e})")
            if skipped is not None:
                skipped[t] = str(e)
    return out


def close_matrix(prices: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Aligned close prices, one column per ticker, dates where all tickers trade."""
    return pd.DataFrame({t: df["Close"] for t, df in prices.items()}).dropna()
