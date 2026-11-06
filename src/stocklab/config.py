"""Watchlist configuration.

The watchlist lives in `watchlist.csv` at the repository root: one ticker per row and
an optional entry price. Entry prices switch on the stop-loss check in `sell-check`;
leave the cell empty for stocks you only want to monitor.
"""

from __future__ import annotations

import csv
import os

DEFAULT_WATCHLIST = ["ALAB", "AMD", "NVDA", "MRVL", "GOOG", "FSLR", "SKHY", "ETN", "TSLA", "SPCX", "AMZN", "IBM"]
DEFAULT_PATH = "watchlist.csv"


def read_watchlist(path: str | None = DEFAULT_PATH) -> dict[str, float | None]:
    """Return {ticker: entry price or None}, in file order. Falls back to the default list."""
    if not path or not os.path.exists(path):
        return {t: None for t in DEFAULT_WATCHLIST}
    out: dict[str, float | None] = {}
    with open(path, newline="", encoding="utf-8") as f:
        rows = [line for line in f if line.strip() and not line.lstrip().startswith("#")]
    for row in csv.DictReader(rows):
        ticker = (row.get("ticker") or "").strip().upper()
        if not ticker:
            continue
        price = (row.get("entry_price") or "").strip()
        out[ticker] = float(price) if price else None
    return out or {t: None for t in DEFAULT_WATCHLIST}
