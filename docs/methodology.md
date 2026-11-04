# Methodology

This project treats trading ideas as hypotheses. The engineering goal is to make it hard
to fool ourselves: no look-ahead, honest baselines, resampling-based uncertainty, and
multiple-testing control.

## 1. Data

* Daily OHLCV from Yahoo Finance via `yfinance`, split- and dividend-adjusted (`auto_adjust=True`).
* `--source csv` reads `<TICKER>.csv` files with `Date, Open, High, Low, Close, Volume`.
* `--source synthetic` generates regime-switching geometric Brownian motion (bull and bear
  regimes with random durations, a shared market factor, and volume that rises with large
  moves). It exists for offline runs, tests and CI. Because synthetic returns are
  unpredictable by construction, every "edge" found on them should be insignificant:
  this is a built-in false-positive check.

## 2. Preventing look-ahead bias

* Every indicator at date *t* uses data up to *t* only. A unit test shocks future prices
  and verifies no earlier indicator value changes.
* **Backtests:** a signal computed from the close of day *t* is executed at the close of
  *t + 1*, so its first return is *t+1 → t+2*. A unit test confirms that a "cheating"
  signal built from tomorrow's return does not earn the perfect-foresight return.
* **Forecasts:** walk-forward with an expanding window, re-fitted every 21 trading days.
  Each model only trains on rows whose targets were realised before the first test day.

## 3. Strategy backtests (`backtest`)

Long-only rules (moving-average trend, MACD, RSI mean reversion, trailing stop, volume
breakout) are compared with buy & hold over the same window, with 5 bp cost per trade side.

**Significance.** Daily returns show volatility clustering, so i.i.d. resampling
understates uncertainty. We use a **paired circular block bootstrap** (21-day blocks):
the same resampled blocks are applied to the strategy and to buy & hold, preserving
their correlation, and the bootstrap distribution of the Sharpe-ratio difference gives
a 95% interval and p-value.

## 4. Sell-signal event study (`sell-study`)

For each rule we take its **onset** days (the rule switches from off to on, with a 10-day
cooldown so one episode isn't counted many times), then measure forward returns at 5, 21
and 63 days.

* **Null hypothesis:** post-signal returns are drawn from the same distribution as returns
  on any day for that stock.
* **Test:** stratified Monte Carlo. For each simulation we draw, per stock, as many random
  dates as that stock had events, and average their forward returns. The one-sided
  p-value is the share of simulations with a mean at or below the observed mean.
  Stratifying by stock prevents a rule that fires mostly in weak stocks from looking
  predictive just because of which stocks it picks.
* **Multiple testing:** 11 rules x 3 horizons = 33 tests. Benjamini-Hochberg q-values
  control the false discovery rate; a rule is labelled *useful* only if q < 0.10.
* **Tail risk:** for each rule we also report how often a 10%+ drawdown followed within
  63 days, compared with the unconditional base rate.

Caveat: forward windows of nearby events overlap, which makes events less independent
than their count suggests. The random-date null shares this property, which partly
offsets it, but p-values should be read as approximate.

## 5. Next-day forecasting (`forecast`)

* **Target:** next-day log return (regression) and its sign (classification).
* **Features** (all known at the close of day *t*): last five daily returns, 21-day return,
  distance from the 20/50/200-day averages, RSI, MACD histogram, 21-day volatility,
  5/21-day volatility ratio, ATR %, volume z-score, and benchmark (SPY) returns.
* **Models:** regularised logistic regression, Ridge regression, and gradient-boosted trees,
  each against a naive baseline (majority class; zero-return random walk).
* **Evaluation:**
  * accuracy with a one-sided **binomial test** against the majority-class rate,
  * ROC AUC and Brier score (probability quality),
  * out-of-sample R² relative to the zero forecast (Campbell-Thompson style),
  * **Diebold-Mariano** test (Harvey-Leybourne-Newbold correction) of squared-error loss vs zero,
  * a simple trading check: hold only when P(up) > 0.5, compared with buy & hold.
* **Tomorrow's forecast** refits on all history and reports P(up), the expected return,
  and an 80% range from recent volatility. The report places it next to the model's
  out-of-sample AUC so it is read with appropriate scepticism.

The efficient-market prior is that daily returns are close to unpredictable. An
out-of-sample AUC near 0.50 is the expected, and informative, result.

## 6. Stock screening and entry rules (`screen`)

1. **Hard filters**: above the 200-day average, average daily dollar volume > $20M,
   less than 50% below the 52-week high. Failures are recorded, not silently dropped.
2. **Factor score**: cross-sectional, winsorised (5th/95th percentile) z-scores of
   12-1 month momentum (30%), 6-month momentum (15%), trend quality (15%), low
   volatility (15%), shallow drawdown (10%), and, when available, forward P/E (value),
   revenue growth and profit margin (5% each). Weights renormalise when data is missing.
3. **Entry plan**: pullback entry at the nearest moving average below price, breakout
   trigger just above the 20-day high, stop at entry minus 2x ATR, and position size
   `capital x risk per trade / (entry - stop)`, capped at a maximum weight. Each position
   therefore risks about the same amount, regardless of its volatility.

## 7. Portfolio construction (`portfolio`)

* Covariance: **Ledoit-Wolf shrinkage** of the sample covariance (more stable with many
  assets and limited history).
* Methods: equal weight, inverse volatility, **equal risk contribution (risk parity)** and
  **minimum variance**, all long-only with a per-asset cap (relaxed automatically for
  very small portfolios).
* Diagnostics: each holding's share of portfolio variance (risk contribution),
  diversification ratio, and effective number of bets (inverse Herfindahl of risk shares).
* **Walk-forward comparison**: weights re-estimated monthly from the trailing 252 days,
  drifting with prices between rebalances, turnover costs charged.
* Max-Sharpe optimisation is excluded on purpose: expected-return estimates are too noisy
  and produce unstable, concentrated portfolios.

## 8. Daily decision board (`board`, `update`)

**Labels.** For each watchlist stock and each date, `board.action_panel` computes:

* the sell-warning score (section 4's 11 rules, weighted as in the playbook), counting only
  rules the stock has enough history for, and expressed as a share of the maximum it could reach;
* trend, liquidity and collapse filters (close above the 200-day average, or the 50-day
  average for listings under 200 days; average daily dollar volume of $20M+; less than 50%
  below the high);
* the buy score: section 6's price factors (12-1 month momentum, 6-month momentum, trend
  quality, low volatility, shallow drawdown), winsorised at the 5th/95th percentile and
  z-scored **across the watchlist on that date**, combined with the screen's weights and
  renormalised when a factor is missing.

The first matching rule gives the label: NO SIGNAL (under 60 days), SELL (warnings ≥ 60%
of the maximum, or the user's own stop-loss is hit), REDUCE (40-59%), AVOID (fails a
filter), WATCH (20-39%), BUY (top half by buy score), otherwise HOLD. All inputs at date
*t* use data up to *t*; a unit test shocks one stock's last 10 prices and checks that no
earlier label changes.

**Evaluation.** The same panel is traded: every 5 trading days, holdings labelled SELL,
REDUCE, AVOID or NO SIGNAL are sold and stocks labelled BUY are bought; holdings are
equally weighted, idle money earns nothing, decisions made at close *t* are executed at
close *t + 1*, and turnover costs 5 bp per side. The comparison is an equal-weight
portfolio of every eligible watchlist stock, rebalanced on the same days, plus SPY. The
Sharpe-ratio difference gets a paired block-bootstrap interval (section 3).

The **label study** asks whether labels sort winners from losers. Every 21 trading days
(so forward windows don't overlap), each stock's next-21-day return is measured relative
to the watchlist average on that date; for each label, the per-date mean of those excess
returns is tested against zero with a one-sample t-test across dates.

**Live record.** Each run appends the day's labels to `reports/board_log.csv`. Unlike the
backtest, which applies the rule to history chosen in hindsight, the log records labels
before the prices that judge them exist, so it becomes a genuine out-of-sample test as it
grows.

**Automation.** A scheduled GitHub Actions workflow runs `python -m stocklab update` after
each US close. Prices for all tickers are requested in one batched Yahoo download (fewer
rate-limit failures than one request per ticker), bars for a session that has not closed
yet are dropped, and the README's live section is rewritten between two marker comments,
leaving the rest of the README untouched. If fewer than half of the watchlist stocks load,
the run stops without changing anything.

## 9. Pre-market board, timing test and opening gaps (`premarket`)

**Snapshot.** One batched Yahoo request downloads 1-minute bars for the last five days
including extended hours (`prepost=True`). For each stock the latest bar gives the price,
its New York time and its session (pre-market 04:00-09:30, regular 09:30-16:00,
after-hours 16:00-20:00; exchange holidays are not modelled). A stock with no trades yet
today is flagged rather than shown as moving.

**Pre-market board.** Each stock's daily history (to the last close) gets one more bar for
today, with open, high, low and close equal to the latest pre-market price and no volume,
and the board's rules are re-run on it. The labels, buy ranks, pullback entries, breakout
levels and stops therefore reflect the overnight move. Without volume the two volume rules
cannot fire on that bar. The check also lists which levels from the last close the move
crosses (50- and 200-day averages, chandelier stop, breakout level, stops).

**Timing test.** Does deciding before the open beat deciding at the previous close? On the
same review days (every 5 trading days), two versions of the label-trading rule (buy on
BUY; exit on SELL, REDUCE, AVOID or NO SIGNAL; equal weight) are compared:

* close board: labels from the previous close, traded at the open;
* pre-market board: labels from a bar at today's open, traded at the open.

Positions are held open to open with 5 bp turnover costs, so the only difference is the
information set. Free pre-market history from Yahoo covers days, not years, so the official
opening price stands in for the last pre-market trade. That flatters the pre-market version
slightly (an 08:47 price is a noisier guide to the open than the open itself), which is the
conservative direction for a test that asks whether it helps. The labels for each past day
are recomputed on a trailing 320-day window (enough for every indicator; a unit test checks
the result matches the full-history labels), with the true history length passed on so
young listings stay provisional. A unit test also checks that a day's own close never
enters that day's pre-market label. The Sharpe-ratio difference gets a paired circular
block-bootstrap interval, and the share of stock-weeks where the two labels agree is
reported. Each run appends the real pre-market labels to `reports/premarket_log.csv`, so a
direct test with actual pre-market prices becomes possible as the log grows.

**Gap study.** Over the watchlist's five years of daily data, the opening gap is
open / previous close - 1 (where pre-market trading ends up) and the session return is
close / open - 1. Both are winsorised at the 0.5th/99.5th percentile, and the pooled
least-squares slope of session return on gap measures continuation (positive) or reversal
(negative). Its 95% interval comes from a circular block bootstrap over dates (21-day
blocks), which resamples whole cross-sections so same-day moves across stocks stay
correlated. A table by gap size gives the average session return and how often the stock
closed above its open. On the synthetic data used in CI the overnight and intraday moves
are generated independently, so the interval should include zero; a unit test also plants
a reversal and checks that it is found.

## 10. Limitations

* **Selection and survivorship bias.** Universes are chosen today, from companies that
  survived and grew. Backtests on them flatter buy & hold and momentum.
* **Short histories.** Recent listings give few independent observations: ALAB listed in
  March 2024, SpaceX (SPCX) in June 2026 and the SK Hynix ADR (SKHY) in July 2026. The
  last two get provisional board labels and are left out of the event study, single-stock
  backtests, forecasts and portfolio estimates until they have enough history.
* **Label instability.** Labels near a threshold can flip from week to week; the board
  backtest includes the trading costs of that turnover.
* **Costs and execution.** A flat 5 bp per side ignores spreads in volatile moments,
  slippage, taxes and market impact.
* **Regime dependence.** 2022-2026 was dominated by an AI-driven bull market; rules that
  failed in it may work in other regimes, and vice versa.
* **Fundamentals** from Yahoo are current snapshots, so they cannot be backtested without
  look-ahead and are used only for today's screen.
