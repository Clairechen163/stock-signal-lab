"""Technical indicators. Every value at date t uses data up to and including t only."""

from __future__ import annotations

import numpy as np
import pandas as pd

TRADING_DAYS = 252


def sma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n).mean()


def ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()


def rsi(close: pd.Series, n: int = 14) -> pd.Series:
    """Wilder's RSI, bounded in [0, 100]."""
    delta = close.diff()
    gain = delta.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    rs = gain / loss.replace(0, np.nan)
    out = 100 - 100 / (1 + rs)
    return out.where(loss != 0, 100.0).fillna(50.0)


def macd(close: pd.Series, fast=12, slow=26, signal=9) -> pd.DataFrame:
    line = ema(close, fast) - ema(close, slow)
    sig = ema(line, signal)
    return pd.DataFrame({"MACD": line, "MACDSignal": sig, "MACDHist": line - sig})


def atr(df: pd.DataFrame, n: int = 14) -> pd.Series:
    prev = df["Close"].shift(1)
    tr = pd.concat([df["High"] - df["Low"], (df["High"] - prev).abs(), (df["Low"] - prev).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1 / n, adjust=False).mean()


def realized_vol(close: pd.Series, n: int) -> pd.Series:
    """Annualized rolling volatility of daily log returns."""
    return np.log(close).diff().rolling(n).std() * np.sqrt(TRADING_DAYS)


def add_all(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of OHLCV data with the indicator columns used across the project."""
    out = df.copy()
    c = out["Close"]
    for n in (20, 50, 200):
        out[f"SMA{n}"] = sma(c, n)
    out["RSI"] = rsi(c)
    out = out.join(macd(c))
    out["ATR"] = atr(out)
    out["Vol21"] = realized_vol(c, 21)
    out["Vol252Median"] = out["Vol21"].rolling(252, min_periods=126).median()
    out["VolAvg20"] = out["Volume"].rolling(20).mean()
    out["VolAvg50"] = out["Volume"].rolling(50).mean()
    out["High20Prior"] = c.rolling(20).max().shift(1)  # breakout level known before today
    out["High252"] = c.rolling(252, min_periods=1).max()
    out["DrawdownFrom52wHigh"] = c / out["High252"] - 1
    out["HighestHigh22"] = out["High"].rolling(22).max()
    return out
