import numpy as np
import pandas as pd
import pytest

from stocklab import board, cli, config, data, indicators, readme

VALID = set(board.ORDER)


@pytest.fixture(scope="module")
def frames():
    tickers = ["AAA", "BBB", "CCC", "DDD", "EEE", "SPCX"]  # SPCX gets a short, recent-listing history
    return {t: indicators.add_all(data.synthetic(t, years=4)) for t in tickers}


def _trend(name, slope, n=600, seed=0, noise=0.004):
    rng = np.random.default_rng(seed)
    dates = pd.bdate_range(end="2026-10-14", periods=n)
    close = 100 * np.exp(np.cumsum(slope + rng.normal(0, noise, n)))
    df = pd.DataFrame({"Open": close, "High": close * 1.01, "Low": close * 0.99, "Close": close, "Volume": 5e6}, index=dates)
    return indicators.add_all(df)


def test_labels_are_valid_and_new_listings_start_without_signal(frames):
    pan = board.action_panel(frames)
    labels = set(pan["action"].stack().dropna().unique())
    assert labels <= VALID
    spcx = pan["action"]["SPCX"].dropna()
    assert (spcx.iloc[: board.MIN_SIGNAL_DAYS - 1] == "NO SIGNAL").all()
    assert spcx.iloc[-1] != "NO SIGNAL"  # 100 days of history: provisional label


def test_labels_do_not_look_ahead(frames):
    """Changing the last 10 days of one stock must not change any earlier label."""
    base = board.action_panel(frames)["action"]
    shocked = dict(frames)
    raw = data.synthetic("AAA", years=4).copy()
    raw.iloc[-10:, raw.columns.get_loc("Close")] *= 0.5
    shocked["AAA"] = indicators.add_all(raw)
    after = board.action_panel(shocked)["action"]
    cut = base.index[-11]
    pd.testing.assert_frame_equal(base.loc[:cut], after.loc[:cut])


def test_strong_uptrend_is_buy_and_crash_is_not():
    frames = {f"UP{i}": _trend(f"UP{i}", 0.002, seed=i) for i in range(3)}
    frames.update({f"DN{i}": _trend(f"DN{i}", -0.002, seed=10 + i) for i in range(3)})
    table, _ = board.today(frames)
    assert set(table.loc[["UP0", "UP1", "UP2"], "action"]) <= {"BUY", "HOLD", "WATCH"}
    assert "BUY" in set(table.loc[["UP0", "UP1", "UP2"], "action"])
    assert set(table.loc[["DN0", "DN1", "DN2"], "action"]) <= {"SELL", "REDUCE", "AVOID"}


def test_your_stop_loss_forces_sell(frames):
    close = frames["BBB"]["Close"].iloc[-1]
    table, _ = board.today(frames, entries={"BBB": close * 1.5}, stop_pct=0.15)
    assert table.loc["BBB", "action"] == "SELL"
    assert "stop-loss" in table.loc["BBB", "triggered"]


def test_evaluate_returns_strategies_and_labels(frames):
    pan = board.action_panel(frames)
    res = board.evaluate(pan, frames["AAA"]["Close"].rename("SPY"), n_boot=50)
    assert {"Board strategy", "Equal-weight watchlist", "SPY (buy & hold)"} <= set(res["table"].index)
    assert (res["equity"] > 0).all().all()
    assert res["labels"].index.isin(VALID).all()


def test_readme_block_replacement():
    text = f"intro\n{readme.START}\nold\n{readme.END}\nrest\n"
    new = readme.replace_block(text, "new board")
    assert "old" not in new and "new board" in new and new.startswith("intro") and new.endswith("rest\n")
    with pytest.raises(ValueError):
        readme.replace_block("no markers here", "x")


def test_partial_bar_is_dropped_during_market_hours():
    idx = pd.bdate_range(end="2026-11-04", periods=3)
    df = pd.DataFrame({"Close": [1.0, 2.0, 3.0]}, index=idx)
    open_ = pd.Timestamp("2026-11-04 11:00", tz="America/New_York")
    closed = pd.Timestamp("2026-11-04 17:00", tz="America/New_York")
    assert len(data.drop_incomplete_bar(df, open_)) == 2
    assert len(data.drop_incomplete_bar(df, closed)) == 3


@pytest.mark.parametrize("layout", ["ticker", "column"])
def test_batch_download_split(layout):
    idx = pd.bdate_range(end="2026-11-04", periods=3)
    fields = ["Open", "High", "Low", "Close", "Volume"]
    cols = pd.MultiIndex.from_product([["AAA", "BBB"], fields] if layout == "ticker" else [fields, ["AAA", "BBB"]])
    raw = pd.DataFrame(np.arange(30, dtype=float).reshape(3, 10), index=idx, columns=cols)
    sub = data._split_batch(raw, "BBB")
    assert list(sub.columns) == fields or set(sub.columns) == set(fields)
    assert data._split_batch(raw, "ZZZ") is None


def test_watchlist_file(tmp_path):
    p = tmp_path / "watchlist.csv"
    p.write_text("# comment\nticker,entry_price\nnvda,180\nAMD,\n", encoding="utf-8")
    assert config.read_watchlist(str(p)) == {"NVDA": 180.0, "AMD": None}
    assert list(config.read_watchlist(str(tmp_path / "missing.csv"))) == config.DEFAULT_WATCHLIST


def test_signal_log_appends_without_duplicates(tmp_path, frames):
    table, _ = board.today(frames)
    path = str(tmp_path / "log.csv")
    cli.append_log(table, path)
    cli.append_log(table, path)
    log = pd.read_csv(path)
    assert len(log) == len(table)
