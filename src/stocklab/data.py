"""Price data loading: Yahoo Finance, local CSV files, or synthetic data for offline demos and tests."""

from __future__ import annotations

import os
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


def from_yahoo(ticker: str, years: int) -> pd.DataFrame:
    import yfinance as yf

    df = yf.download(ticker, period=f"{years}y", auto_adjust=True, progress=False)
    if df is None or df.empty:
        raise ValueError(f"{ticker}: no data returned from Yahoo Finance")
    return _standardize(df)


def from_csv(ticker: str, csv_dir: str) -> pd.DataFrame:
    path = os.path.join(csv_dir, f"{ticker}.csv")
    df = pd.read_csv(path, parse_dates=["Date"], index_col="Date")
    return _standardize(df)


def synthetic(ticker: str, years: int = 5, seed: int | None = None) -> pd.DataFrame:
    """Regime-switching geometric Brownian motion with volume, for offline demos and tests.

    Bull and bear regimes alternate with random durations, so sell signals and
    drawdowns actually occur. The seed is derived from the ticker so results are
    reproducible but differ across tickers.
    """
    if seed is None:
        seed = zlib.crc32(ticker.encode())
    rng = np.random.default_rng(seed)
    n = years * 252
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


def load(ticker: str, years: int = 5, source: str = "yahoo", csv_dir: str | None = None) -> pd.DataFrame:
    """Load daily OHLCV for one ticker. source: 'yahoo', 'csv' or 'synthetic'."""
    if source == "yahoo":
        return from_yahoo(ticker, years)
    if source == "csv":
        if not csv_dir:
            raise ValueError("source='csv' needs csv_dir")
        return from_csv(ticker, csv_dir)
    if source == "synthetic":
        return synthetic(ticker, years)
    raise ValueError(f"unknown source {source!r}")


def load_many(tickers, years=5, source="yahoo", csv_dir=None, min_rows=0, verbose=True):
    """Load several tickers; skip (and report) any that fail or are too short."""
    out = {}
    for t in tickers:
        try:
            df = load(t, years, source, csv_dir)
            if len(df) < min_rows:
                raise ValueError(f"only {len(df)} rows, need {min_rows}")
            out[t] = df
        except Exception as e:  # network errors, delisted tickers, missing files
            if verbose:
                print(f"  {t}: skipped ({e})")
    return out


def close_matrix(prices: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Aligned close prices, one column per ticker, dates where all tickers trade."""
    return pd.DataFrame({t: df["Close"] for t, df in prices.items()}).dropna()
