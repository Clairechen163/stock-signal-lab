import numpy as np
import pandas as pd

from stocklab import board, data, indicators, premarket, readme

NY = premarket.NY


def _frames(tickers=("AAA", "BBB", "CCC", "DDD", "EEE")):
    return {t: indicators.add_all(data.synthetic(t, years=3)) for t in tickers}


def test_sessions():
    assert premarket.session_of(pd.Timestamp("2026-11-05 07:00", tz=NY)) == "pre-market"
    assert premarket.session_of(pd.Timestamp("2026-11-05 09:30", tz=NY)) == "regular session"
    assert premarket.session_of(pd.Timestamp("2026-11-05 17:00", tz=NY)) == "after-hours"
    assert premarket.session_of(pd.Timestamp("2026-11-05 02:00", tz=NY)) == "closed"
    assert premarket.session_of(pd.Timestamp("2026-11-07 07:00", tz=NY)) == "closed"  # Saturday


def test_yahoo_minute_bars_are_parsed(monkeypatch):
    """Batch 1-minute download (UTC timestamps) -> latest price, session and today's pre-market volume."""
    idx = pd.DatetimeIndex(["2026-11-04 20:59", "2026-11-05 12:30", "2026-11-05 13:46"], tz="UTC")
    fields = ["Open", "High", "Low", "Close", "Volume"]
    cols = pd.MultiIndex.from_product([["AAA", "BBB"], fields])
    raw = pd.DataFrame(np.nan, index=idx, columns=cols)
    for t, base in (("AAA", 100.0), ("BBB", 50.0)):
        for f in fields[:4]:
            raw[(t, f)] = [base, base * 1.01, base * 1.02]
        raw[(t, "Volume")] = [1000, 200, 300]
    raw.loc[idx[2], ("BBB", "Close")] = np.nan  # no trade in BBB's last minute

    import yfinance as yf

    monkeypatch.setattr(yf, "download", lambda *a, **k: raw)
    snap = premarket._yahoo_snapshot(["AAA", "BBB"], pd.Timestamp("2026-11-05 08:50", tz=NY))
    assert snap.at["AAA", "price"] == 102.0
    assert snap.at["AAA", "session"] == "pre-market"  # 13:46 UTC = 08:46 New York in November
    assert snap.at["AAA", "premarket_volume"] == 500
    assert snap.at["BBB", "price"] == 50.5  # falls back to its last actual trade


def test_what_if_bar_and_crossings():
    frames = _frames()
    table, _ = board.today(frames)
    t = "AAA"
    close = frames[t]["Close"].iloc[-1]
    sma200 = frames[t]["SMA200"].iloc[-1]
    price = sma200 * (0.9 if close > sma200 else 1.1)  # a move that crosses the 200-day average
    day = frames[t].index[-1] + pd.Timedelta(days=1)
    snap = pd.DataFrame({"price": [price], "time": [pd.Timestamp(f"{day.date()} 08:30", tz=NY)],
                         "session": ["pre-market"], "premarket_volume": [np.nan]}, index=[t])
    hyp = premarket._what_if_frames(frames, snap)
    assert len(hyp[t]) == len(frames[t]) + 1 and hyp[t]["Close"].iloc[-1] == price
    assert len(hyp["BBB"]) == len(frames["BBB"])  # stocks without a snapshot are untouched
    v = premarket.view(frames, table, snap)
    assert "200-day average" in v.at[t, "crossed"]
    assert v.at["BBB", "session"] == "no extended-hours data"


def test_gap_study_finds_nothing_in_random_data_and_finds_a_planted_reversal():
    frames = _frames(("AAA", "BBB", "CCC", "DDD"))
    g = premarket.gap_study(frames, n_boot=200)
    assert g["ci_low"] <= 0 <= g["ci_high"]

    planted = {}
    rng = np.random.default_rng(0)
    for t, d in frames.items():
        d = d.copy()
        gap = d["Open"] / d["Close"].shift(1) - 1
        d["Close"] = d["Open"] * (1 - 0.5 * gap.fillna(0) + rng.normal(0, 0.002, len(d)))  # half of every gap reverses
        planted[t] = d
    g2 = premarket.gap_study(planted, n_boot=200)
    assert g2["ci_high"] < 0 and "reverse" in g2["verdict"]


def test_readme_gets_a_premarket_section_after_the_board(tmp_path):
    p = tmp_path / "README.md"
    p.write_text(f"top\n{readme.START}\nboard\n{readme.END}\nbottom\n", encoding="utf-8")
    readme.write(str(p), "pre-market table", readme.PM_START, readme.PM_END)
    text = p.read_text(encoding="utf-8")
    assert text.index(readme.END) < text.index("pre-market table") < text.index("bottom")
    readme.write(str(p), "new table", readme.PM_START, readme.PM_END)
    text = p.read_text(encoding="utf-8")
    assert "new table" in text and "pre-market table" not in text and text.count(readme.PM_START) == 1
