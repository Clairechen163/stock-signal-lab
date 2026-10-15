import numpy as np
import pandas as pd

from stocklab import backtest, data, indicators


def test_synthetic_is_reproducible():
    a, b = data.synthetic("XYZ"), data.synthetic("XYZ")
    pd.testing.assert_frame_equal(a, b)
    assert (a["High"] >= a["Low"]).all()


def test_rsi_bounds(ind):
    assert ind["RSI"].between(0, 100).all()


def test_sma_matches_manual(prices):
    sma = indicators.sma(prices["Close"], 50)
    assert np.isclose(sma.iloc[-1], prices["Close"].iloc[-50:].mean())


def test_indicators_do_not_look_ahead(prices):
    """Changing a future price must not change any indicator value before it."""
    base = indicators.add_all(prices)
    shocked = prices.copy()
    shocked.iloc[-10:, shocked.columns.get_loc("Close")] *= 3
    after = indicators.add_all(shocked)
    cut = base.index[-11]
    pd.testing.assert_frame_equal(base.loc[:cut], after.loc[:cut])


def test_signal_is_traded_next_day(ind):
    """A perfect-foresight signal must NOT earn perfect returns, because trades lag one day."""
    df = ind.dropna(subset=["SMA200"])
    tomorrow_up = (df["Close"].shift(-1) > df["Close"]).astype(int)  # cheating signal
    strat, pos, _ = backtest.run(df, tomorrow_up.fillna(0), cost_bps=0)
    perfect = df["Close"].pct_change().clip(lower=0).fillna(0)
    assert strat.sum() < 0.6 * perfect.sum()


def test_buy_hold_matches_price_change(ind):
    df = ind.dropna(subset=["SMA200"])
    strat, pos, trades = backtest.run(df, backtest.buy_hold(df), cost_bps=0)
    total = np.prod(1 + strat) - 1
    # first signal on day 0 is traded at the next close (day 1), so returns start after that
    assert np.isclose(total, df["Close"].iloc[-1] / df["Close"].iloc[1] - 1)


def test_backtest_table_has_all_strategies(ind):
    table, curves = backtest.backtest_ticker(ind, n_boot=50)
    assert set(table.index) == set(backtest.STRATEGIES)
    assert table.loc["Buy & Hold", "Time in market"] > 0.99
