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

## 8. Limitations

* **Selection and survivorship bias.** Universes are chosen today, from companies that
  survived and grew. Backtests on them flatter buy & hold and momentum.
* **Short histories.** Recent IPOs (e.g. ALAB, listed March 2024) give few independent
  observations.
* **Costs and execution.** A flat 5 bp per side ignores spreads in volatile moments,
  slippage, taxes and market impact.
* **Regime dependence.** 2022-2026 was dominated by an AI-driven bull market; rules that
  failed in it may work in other regimes, and vice versa.
* **Fundamentals** from Yahoo are current snapshots, so they cannot be backtested without
  look-ahead and are used only for today's screen.
