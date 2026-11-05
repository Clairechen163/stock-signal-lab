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


def test_trailing_window_with_offset_reproduces_full_history_labels():
    frames = _frames()
    full = board.action_panel(frames)["action"]
    day = full.index[-200]
    sub, off = {}, {}
    for t, d in frames.items():
        i = d.index.get_loc(day)
        lo = max(0, i + 1 - 320)
        sub[t] = indicators.add_all(d[data.COLUMNS].iloc[lo:i + 1])
        off[t] = lo
    windowed = board.action_panel(sub, off)["action"].iloc[-1]
    pd.testing.assert_series_equal(windowed, full.loc[day], check_names=False)


def test_opening_labels_ignore_the_same_days_close():
    frames = _frames()
    day = frames["AAA"].index[-50]
    base = premarket.opening_labels(frames, [day])
    shocked = dict(frames)
    raw = data.synthetic("AAA", years=3).copy()
    raw.loc[day:, "Close"] *= 0.5  # crash from that day's close onwards
    shocked["AAA"] = indicators.add_all(raw)
    pd.testing.assert_frame_equal(base, premarket.opening_labels(shocked, [day]))


def test_timing_comparison_shape():
    frames = _frames()
    c = premarket.compare_timing(frames, n_boot=50)
    assert set(c["table"].index) == {"Board on the previous close", "Board on the pre-market price", "Equal-weight watchlist"}
    assert 0 <= c["agreement"] <= 1
    assert "deciding before the open" in premarket.timing_sentence(c)


def test_premarket_view_has_labels_and_levels():
    frames = _frames()
    table, _ = board.today(frames)
    snap = premarket._synthetic_snapshot(frames)
    v = premarket.view(frames, table, snap)
    assert v["premarket_label"].str.rstrip("*").isin(board.ORDER).all()
    buyable = v["premarket_label"].str.rstrip("*").isin(["BUY", "HOLD", "WATCH"])
    assert v.loc[buyable, "pm_stop"].notna().all()


def _breakdown_frame(n=400, seed=3):
    """An uptrend that ends with a heavy-volume drop below the 50-day average on the last day."""
    rng = np.random.default_rng(seed)
    dates = pd.bdate_range(end="2026-11-04", periods=n)
    close = 100 * np.exp(np.cumsum(0.001 + rng.normal(0, 0.01, n)))
    close[-1] = close[-2] * 0.85
    vol = np.full(n, 5e6)
    vol[-1] = 2e7
    raw = pd.DataFrame({"Open": close, "High": close * 1.01, "Low": close * 0.99, "Close": close, "Volume": vol},
                       index=dates)
    return raw


def test_volume_rules_keep_their_last_close_value_on_a_premarket_bar():
    raw = _breakdown_frame()
    at_close = board.board_states(indicators.add_all(raw)).iloc[-1]
    assert at_close["high_volume_breakdown"]
    bar = premarket._price_bar(float(raw["Close"].iloc[-1]) * 0.97, raw.index[-1] + pd.Timedelta(days=1))
    pre = board.board_states(indicators.add_all(pd.concat([raw, bar])))
    for k in board.VOLUME_RULES:
        assert pre[k].iloc[-1] == at_close[k]
    # a further fall before the open cannot lower the sell-warning score through missing volume
    sig_close = board.ticker_signals(indicators.add_all(raw)).iloc[-1]
    sig_pre = board.ticker_signals(indicators.add_all(pd.concat([raw, bar]))).iloc[-1]
    assert sig_pre["sell_max"] == sig_close["sell_max"]
    assert sig_pre["sell_score"] >= sig_close["sell_score"] - 1  # only a price rule can switch off


def test_data_without_any_volume_is_unchanged():
    raw = _breakdown_frame()
    raw["Volume"] = np.nan
    st = board.board_states(indicators.add_all(raw))
    assert not st[board.VOLUME_RULES].any().any()


def test_every_changed_premarket_label_is_explained():
    frames = _frames(("AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG", "HHH"))
    table, _ = board.today(frames)
    explained = checked = 0
    for move in (-0.12, -0.06, 0.06, 0.12):
        snap = premarket._synthetic_snapshot(frames)
        snap["price"] = [float(frames[t]["Close"].iloc[-1]) * (1 + move) for t in snap.index]
        v = premarket.view(frames, table, snap)
        changed = v[v["changed"]]
        checked += len(changed)
        explained += int((changed["crossed"].str.len() > 0).sum())
    assert checked > 0 and explained == checked
