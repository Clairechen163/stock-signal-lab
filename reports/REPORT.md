# stocklab report
Generated 2026-11-09 | data source: `yahoo` | history: 5 years | watchlist: ALAB, AMD, NVDA, MRVL, GOOG, FSLR, SKHY, ETN, TSLA, SPCX, AMZN, IBM, GEV, CEG, VST

> Educational research code, not investment advice. Past results do not predict future returns.

## 1. Decision board

Data as of the 2026-11-06 close. `*` = provisional (under 200 trading days of history).

| ticker | action | close | 1 day | 1 month | buy rank | sell warnings | pullback entry | breakout | stop | why |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | BUY | 259.30 | -0.3% | +2.1% | 3/15 | 1/15 | 254.28 | 266.56 | 235.90 | buy rank 3/15; +6% vs 200-day average; distribution days |
| FSLR | AVOID | 201.14 | +2.7% | +12.5% | 12/15 | 5/15 |  |  |  | -6% vs 200-day average; below 200-day, death cross, 20%+ off high |
| AMD | REDUCE | 449.04 | +11.0% | -27.7% | 1/15 | 7/15 |  |  |  | +8% vs 200-day average; below 50-day, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| NVDA | REDUCE | 186.64 | +2.8% | -19.0% | 4/15 | 8/15 |  |  |  | -9% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, below chandelier stop |
| IBM | REDUCE | 245.00 | -0.9% | +8.1% | 5/15 | 6/15 |  |  |  | -0% vs 200-day average; below 200-day, death cross, MACD bearish, 20%+ off high |
| ALAB | REDUCE | 190.71 | +6.3% | -45.0% | 6/15 | 8/15 |  |  |  | -26% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, below chandelier stop |
| MRVL | SELL | 141.20 | +5.7% | -48.6% | 2/15 | 9/15 |  |  |  | -24% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| ETN | SELL | 341.72 | +4.5% | -19.5% | 7/15 | 9/15 |  |  |  | -14% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| GEV | SELL | 774.11 | +0.5% | -22.5% | 8/15 | 10/15 |  |  |  | -18% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, 20%+ off high, below chandelier stop |
| GOOG | SELL | 283.93 | +0.8% | -17.7% | 9/15 | 11/15 |  |  |  | -16% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| SPCX | SELL* | 134.27 | +8.6% | -16.4% | 10/15 | 6/10 |  |  |  | -10% vs 50-day average; below 50-day, MACD bearish, distribution days, 20%+ off high, below chandelier stop (provisional: 103 days of history) |
| TSLA | SELL | 358.22 | +4.2% | -4.5% | 11/15 | 10/15 |  |  |  | -7% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, 20%+ off high, below chandelier stop |
| CEG | SELL | 249.95 | +4.3% | -12.3% | 13/15 | 10/15 |  |  |  | -10% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, 20%+ off high, below chandelier stop |
| VST | SELL | 124.80 | +10.6% | -20.1% | 14/15 | 11/15 |  |  |  | -18% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| SKHY | SELL* | 127.34 | +2.8% | -25.3% | 15/15 | 6/10 |  |  |  | -24% vs 50-day average; below 50-day, MACD bearish, distribution days, 20%+ off high, below chandelier stop (provisional: 85 days of history) |

![Board label each week](board_history.png)

**Trading the labels** (2022-02-02 to 2026-11-06): buy on BUY, exit on SELL, REDUCE or AVOID, reviewed weekly with next-day execution and 5 bp costs.

| strategy | CAGR | Volatility | Sharpe | Max drawdown | Time invested | Avg holdings |
|---|---|---|---|---|---|---|
| Board strategy | +37.0% | 31.4% | 1.16 | -29.5% | 97% | 5.4 |
| Equal-weight watchlist | +38.0% | 33.1% | 1.14 | -37.1% | 100% | 12.0 |
| SPY (buy & hold) | +12.6% | 17.3% | 0.77 | -22.1% |  |  |

Sharpe difference vs equal weight: +0.02, 95% block-bootstrap CI [-0.45, +0.50].

Forward 21-day return after each label, relative to the watchlist average on the same date (sampled every 21 days, t-test across dates):

| label | observations | dates | mean 21d excess return | hit rate | p_value |
|---|---|---|---|---|---|
| BUY | 217 | 55 | -0.3% | 45% | 0.72 |
| HOLD | 89 | 37 | +0.8% | 41% | 0.74 |
| WATCH | 130 | 48 | +1.1% | 48% | 0.51 |
| AVOID | 37 | 21 | +1.7% | 57% | 0.22 |
| REDUCE | 130 | 46 | -1.3% | 46% | 0.41 |
| SELL | 65 | 31 | -0.5% | 52% | 0.78 |

![Board strategy vs holding](board_equity.png)

## 2. Sell check, stock by stock

```
ALAB  REDUCE  (score 8/15, close 190.71 on 2026-11-06)
  RSI 29 | -60.5% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    Chandelier stop            308.68  (price is below, -38.2%)
    50-day SMA                 300.46  (price is below, -36.5%)
    200-day SMA                256.06  (price is below, -25.5%)
```

```
AMD  REDUCE  (score 7/15, close 449.04 on 2026-11-06)
  RSI 38 | -30.9% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 546.81  (price is below, -17.9%)
    Chandelier stop            534.03  (price is below, -15.9%)
    200-day SMA                415.98  (price is above, +7.9%)
```

```
NVDA  REDUCE  (score 8/15, close 186.64 on 2026-11-06)
  RSI 31 | -22.0% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 219.77  (price is below, -15.1%)
    Chandelier stop            213.76  (price is below, -12.7%)
    200-day SMA                204.39  (price is below, -8.7%)
```

```
MRVL  EXIT  (score 9/15, close 141.20 on 2026-11-06)
  RSI 26 | -55.4% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 234.27  (price is below, -39.7%)
    Chandelier stop            229.77  (price is below, -38.5%)
    200-day SMA                184.98  (price is below, -23.7%)
```

```
GOOG  EXIT  (score 11/15, close 283.93 on 2026-11-06)
  RSI 30 | -28.8% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    200-day SMA                337.23  (price is below, -15.8%)
    50-day SMA                 329.76  (price is below, -13.9%)
    Chandelier stop            323.42  (price is below, -12.2%)
```

```
FSLR  WATCH  (score 5/15, close 201.14 on 2026-11-06)
  RSI 67 | -36.8% from 52-week high
  Triggered:
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [risk] 20%+ below the 52-week high (+1)
  Levels to watch:
    200-day SMA                214.65  (price is below, -6.3%)
    50-day SMA                 186.99  (price is above, +7.6%)
    Chandelier stop            183.53  (price is above, +9.6%)
```

```
SKHY  EXIT  (score 6/10, close 127.34 on 2026-11-06)
  RSI 36 | -35.9% from high since listing
  Only 85 trading days of history; not scored yet: below_sma200, death_cross, volatility_spike
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the high since listing (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 166.79  (price is below, -23.7%)
    Chandelier stop            146.81  (price is below, -13.3%)
```

```
ETN  EXIT  (score 9/15, close 341.72 on 2026-11-06)
  RSI 37 | -25.7% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 405.27  (price is below, -15.7%)
    200-day SMA                396.20  (price is below, -13.8%)
    Chandelier stop            380.26  (price is below, -10.1%)
```

```
TSLA  EXIT  (score 10/15, close 358.22 on 2026-11-06)
  RSI 42 | -26.9% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    200-day SMA                383.87  (price is below, -6.7%)
    50-day SMA                 372.14  (price is below, -3.7%)
    Chandelier stop            364.11  (price is below, -1.6%)
```

```
SPCX  EXIT  (score 6/10, close 134.27 on 2026-11-06)
  RSI 43 | -36.5% from high since listing
  Only 103 trading days of history; not scored yet: below_sma200, death_cross, volatility_spike
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the high since listing (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 149.18  (price is below, -10.0%)
    Chandelier stop            142.68  (price is below, -5.9%)
```

```
AMZN  HOLD  (score 1/15, close 259.30 on 2026-11-06)
  RSI 54 | -8.7% from 52-week high
  Triggered:
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
  Levels to watch:
    50-day SMA                 253.95  (price is above, +2.1%)
    Chandelier stop            245.66  (price is above, +5.6%)
    200-day SMA                243.94  (price is above, +6.3%)
```

```
IBM  REDUCE  (score 6/15, close 245.00 on 2026-11-06)
  RSI 51 | -25.1% from 52-week high
  Triggered:
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [risk] 20%+ below the 52-week high (+1)
  Levels to watch:
    200-day SMA                245.97  (price is below, -0.4%)
    Chandelier stop            237.42  (price is above, +3.2%)
    50-day SMA                 236.75  (price is above, +3.5%)
```

```
GEV  EXIT  (score 10/15, close 774.11 on 2026-11-06)
  RSI 35 | -34.1% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    200-day SMA                947.88  (price is below, -18.3%)
    50-day SMA                 923.06  (price is below, -16.1%)
    Chandelier stop            858.18  (price is below, -9.8%)
```

```
CEG  EXIT  (score 10/15, close 249.95 on 2026-11-06)
  RSI 43 | -33.7% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    200-day SMA                278.15  (price is below, -10.1%)
    50-day SMA                 270.02  (price is below, -7.4%)
    Chandelier stop            268.19  (price is below, -6.8%)
```

```
VST  EXIT  (score 11/15, close 124.80 on 2026-11-06)
  RSI 40 | -34.3% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    200-day SMA                152.28  (price is below, -18.0%)
    50-day SMA                 143.83  (price is below, -13.2%)
    Chandelier stop            143.06  (price is below, -12.8%)
```

## 3. Which sell signals actually work? (event study)

Panel: 44 stocks, 5 years. Null hypothesis: returns after a signal look like returns on random days from the same stocks.

| rule | horizon | events | mean_after_signal | mean_random_days | difference | p_value | q_value | drop10_after_signal | drop10_base_rate | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| below_sma50 | 5d | 1032 | +0.20% | +0.63% | -0.44% | 0.009 | 0.079 | 39% | 35% | useful |
| below_sma50 | 21d | 1005 | +2.41% | +2.87% | -0.46% | 0.098 | 0.323 | 39% | 35% | weak (not significant) |
| below_sma50 | 63d | 961 | +8.44% | +9.53% | -1.08% | 0.069 | 0.268 | 39% | 35% | weak (not significant) |
| below_sma200 | 5d | 486 | -0.00% | +0.55% | -0.55% | 0.012 | 0.079 | 38% | 35% | useful |
| below_sma200 | 21d | 473 | +1.12% | +2.46% | -1.34% | 0.008 | 0.079 | 38% | 35% | useful |
| below_sma200 | 63d | 448 | +8.71% | +8.20% | +0.51% | 0.692 | 0.952 | 38% | 35% | no edge |
| death_cross | 5d | 148 | -0.48% | +0.58% | -1.06% | 0.010 | 0.079 | 44% | 35% | useful |
| death_cross | 21d | 141 | +0.20% | +2.63% | -2.42% | 0.008 | 0.079 | 44% | 35% | useful |
| death_cross | 63d | 135 | +10.74% | +8.70% | +2.04% | 0.865 | 1.000 | 44% | 35% | no edge |
| rsi_divergence | 5d | 473 | +0.45% | +0.72% | -0.27% | 0.166 | 0.422 | 36% | 35% | weak (not significant) |
| rsi_divergence | 21d | 470 | +2.96% | +3.28% | -0.31% | 0.282 | 0.517 | 36% | 35% | weak (not significant) |
| rsi_divergence | 63d | 464 | +9.14% | +11.12% | -1.98% | 0.031 | 0.148 | 36% | 35% | weak (not significant) |
| rsi_rollover | 5d | 615 | +1.79% | +0.70% | +1.09% | 1.000 | 1.000 | 33% | 35% | no edge |
| rsi_rollover | 21d | 605 | +3.34% | +3.24% | +0.10% | 0.577 | 0.911 | 33% | 35% | no edge |
| rsi_rollover | 63d | 592 | +9.04% | +11.00% | -1.96% | 0.020 | 0.110 | 33% | 35% | weak (not significant) |
| macd_bearish | 5d | 1547 | +0.59% | +0.66% | -0.07% | 0.319 | 0.554 | 35% | 35% | weak (not significant) |
| macd_bearish | 21d | 1519 | +3.06% | +2.99% | +0.07% | 0.587 | 0.911 | 35% | 35% | no edge |
| macd_bearish | 63d | 1451 | +10.46% | +10.04% | +0.42% | 0.754 | 0.957 | 35% | 35% | no edge |
| distribution_cluster | 5d | 1025 | +0.98% | +0.66% | +0.32% | 0.956 | 1.000 | 35% | 35% | no edge |
| distribution_cluster | 21d | 1005 | +2.70% | +3.01% | -0.31% | 0.215 | 0.482 | 35% | 35% | weak (not significant) |
| distribution_cluster | 63d | 970 | +9.57% | +10.14% | -0.56% | 0.225 | 0.482 | 35% | 35% | weak (not significant) |
| high_volume_breakdown | 5d | 722 | +0.67% | +0.62% | +0.06% | 0.607 | 0.911 | 34% | 35% | no edge |
| high_volume_breakdown | 21d | 690 | +3.51% | +2.78% | +0.73% | 0.943 | 1.000 | 34% | 35% | no edge |
| high_volume_breakdown | 63d | 671 | +11.61% | +9.31% | +2.30% | 0.995 | 1.000 | 34% | 35% | no edge |
| drawdown_20 | 5d | 375 | +0.88% | +0.75% | +0.13% | 0.663 | 0.952 | 49% | 35% | no edge |
| drawdown_20 | 21d | 365 | +2.34% | +3.39% | -1.06% | 0.073 | 0.268 | 49% | 35% | weak (not significant) |
| drawdown_20 | 63d | 346 | +13.29% | +11.54% | +1.76% | 0.878 | 1.000 | 49% | 35% | no edge |
| volatility_spike | 5d | 314 | +0.35% | +0.66% | -0.32% | 0.165 | 0.422 | 46% | 35% | weak (not significant) |
| volatility_spike | 21d | 309 | +2.66% | +3.11% | -0.45% | 0.278 | 0.517 | 46% | 35% | weak (not significant) |
| volatility_spike | 63d | 307 | +9.16% | +10.50% | -1.34% | 0.156 | 0.422 | 46% | 35% | weak (not significant) |
| chandelier_stop | 5d | 1295 | +0.53% | +0.65% | -0.12% | 0.234 | 0.482 | 36% | 35% | weak (not significant) |
| chandelier_stop | 21d | 1268 | +3.21% | +2.98% | +0.23% | 0.747 | 0.957 | 36% | 35% | no edge |
| chandelier_stop | 63d | 1213 | +11.23% | +10.00% | +1.23% | 0.963 | 1.000 | 36% | 35% | no edge |

**5 of 33 rule-by-horizon tests** show significantly weaker returns after the signal (q < 0.10).

![Sell signal event study](sell_event_study.png)

## 4. Strategy backtests

Not included: SKHY (only 85 trading days of history, needs 452); SPCX (only 103 trading days of history, needs 452).

### ALAB (2025-01-03 to 2026-11-06)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +32.7% | +16.6% | -63.2% | +96.9% | 0.64 | 0 | 100% |  |  |  |
| 50/200 SMA cross | -70.9% | -48.9% | -74.0% | +87.3% | -0.33 | 2 | 75% | -0.97 | [-1.90, -0.26] | 0.02 |
| Close > 50-day SMA | +7.6% | +4.1% | -66.4% | +70.2% | 0.41 | 10 | 52% | -0.23 | [-1.27, +0.79] | 0.66 |
| MACD > signal | +14.8% | +7.8% | -70.4% | +65.4% | 0.44 | 21 | 50% | -0.21 | [-1.46, +1.01] | 0.75 |
| RSI 30/70 | -2.2% | -1.2% | -50.3% | +35.8% | 0.14 | 1 | 16% | -0.50 | [-2.24, +1.35] | 0.56 |
| Trailing stop 20% | -11.8% | -6.6% | -69.1% | +72.1% | 0.27 | 10 | 56% | -0.38 | [-1.45, +0.63] | 0.47 |
| Volume breakout | +91.8% | +42.6% | -55.7% | +63.4% | 0.87 | 4 | 41% | +0.23 | [-0.99, +1.42] | 0.70 |

### AMD (2022-08-24 to 2026-11-06)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +361.8% | +44.1% | -63.0% | +58.0% | 0.92 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +321.0% | +40.9% | -39.1% | +48.1% | 0.95 | 1 | 65% | +0.03 | [-0.54, +0.59] | 0.91 |
| Close > 50-day SMA | +156.9% | +25.3% | -41.8% | +43.8% | 0.73 | 37 | 54% | -0.19 | [-0.73, +0.32] | 0.52 |
| MACD > signal | +343.0% | +42.6% | -42.4% | +41.4% | 1.06 | 39 | 50% | +0.15 | [-0.45, +0.77] | 0.64 |
| RSI 30/70 | +30.3% | +6.5% | -54.7% | +31.2% | 0.36 | 3 | 33% | -0.56 | [-1.60, +0.43] | 0.26 |
| Trailing stop 20% | +177.9% | +27.6% | -58.9% | +49.6% | 0.74 | 10 | 71% | -0.18 | [-0.64, +0.29] | 0.46 |
| Volume breakout | +177.7% | +27.6% | -36.9% | +37.1% | 0.84 | 10 | 38% | -0.08 | [-0.93, +0.65] | 0.82 |

### NVDA (2022-08-24 to 2026-11-06)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +945.4% | +75.1% | -37.3% | +49.2% | 1.38 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +620.8% | +60.2% | -28.4% | +42.9% | 1.31 | 1 | 84% | -0.07 | [-0.60, +0.46] | 0.79 |
| Close > 50-day SMA | +293.7% | +38.7% | -39.1% | +39.3% | 1.03 | 39 | 69% | -0.36 | [-0.89, +0.16] | 0.20 |
| MACD > signal | +152.9% | +24.8% | -46.7% | +34.4% | 0.81 | 40 | 51% | -0.57 | [-1.30, +0.21] | 0.13 |
| RSI 30/70 | +64.6% | +12.6% | -22.6% | +18.2% | 0.74 | 2 | 7% | -0.64 | [-1.71, +0.33] | 0.19 |
| Trailing stop 20% | +561.0% | +56.9% | -36.6% | +44.6% | 1.23 | 7 | 88% | -0.15 | [-0.49, +0.17] | 0.37 |
| Volume breakout | +211.5% | +31.1% | -19.8% | +26.3% | 1.16 | 7 | 31% | -0.22 | [-1.09, +0.61] | 0.62 |

### MRVL (2022-08-24 to 2026-11-06)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +160.0% | +25.6% | -60.8% | +67.1% | 0.67 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +37.4% | +7.9% | -65.2% | +57.1% | 0.42 | 2 | 68% | -0.25 | [-0.78, +0.19] | 0.28 |
| Close > 50-day SMA | +47.3% | +9.7% | -51.5% | +52.9% | 0.43 | 37 | 58% | -0.24 | [-0.85, +0.35] | 0.42 |
| MACD > signal | +101.6% | +18.2% | -62.5% | +50.2% | 0.58 | 44 | 51% | -0.09 | [-0.84, +0.68] | 0.84 |
| RSI 30/70 | +47.0% | +9.6% | -32.1% | +28.3% | 0.47 | 2 | 19% | -0.20 | [-1.13, +0.79] | 0.69 |
| Trailing stop 20% | +66.8% | +13.0% | -53.3% | +56.7% | 0.49 | 15 | 76% | -0.18 | [-0.69, +0.29] | 0.50 |
| Volume breakout | +76.0% | +14.4% | -46.2% | +42.0% | 0.53 | 11 | 36% | -0.14 | [-1.06, +0.71] | 0.73 |

### GOOG (2022-08-24 to 2026-11-06)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +143.4% | +23.6% | -30.2% | +31.8% | 0.83 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +151.5% | +24.6% | -29.4% | +25.9% | 0.98 | 2 | 76% | +0.15 | [-0.38, +0.68] | 0.59 |
| Close > 50-day SMA | +83.9% | +15.6% | -22.2% | +23.6% | 0.73 | 35 | 63% | -0.09 | [-0.80, +0.61] | 0.79 |
| MACD > signal | +36.1% | +7.6% | -18.1% | +21.5% | 0.45 | 42 | 50% | -0.38 | [-1.14, +0.36] | 0.33 |
| RSI 30/70 | +29.5% | +6.4% | -20.4% | +18.1% | 0.43 | 4 | 25% | -0.40 | [-1.23, +0.52] | 0.38 |
| Trailing stop 20% | +55.3% | +11.1% | -40.4% | +29.6% | 0.50 | 6 | 92% | -0.32 | [-0.74, +0.05] | 0.10 |
| Volume breakout | +105.6% | +18.8% | -17.4% | +19.4% | 0.98 | 8 | 46% | +0.16 | [-0.72, +1.00] | 0.70 |

### FSLR (2022-08-24 to 2026-11-06)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +65.2% | +12.7% | -60.0% | +55.0% | 0.49 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +15.6% | +3.5% | -51.1% | +41.8% | 0.29 | 4 | 59% | -0.20 | [-0.77, +0.33] | 0.48 |
| Close > 50-day SMA | +54.3% | +10.9% | -46.8% | +40.2% | 0.45 | 28 | 50% | -0.03 | [-0.57, +0.53] | 0.89 |
| MACD > signal | -52.4% | -16.2% | -74.1% | +40.5% | -0.24 | 48 | 49% | -0.72 | [-1.40, -0.11] | 0.03 |
| RSI 30/70 | +30.1% | +6.5% | -42.8% | +30.4% | 0.35 | 2 | 27% | -0.14 | [-1.14, +0.74] | 0.77 |
| Trailing stop 20% | +38.0% | +8.0% | -52.3% | +45.1% | 0.39 | 11 | 69% | -0.10 | [-0.56, +0.38] | 0.71 |
| Volume breakout | -14.2% | -3.6% | -53.8% | +32.1% | 0.05 | 13 | 37% | -0.44 | [-1.29, +0.39] | 0.32 |

### ETN (2022-08-24 to 2026-11-06)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +144.1% | +23.7% | -34.5% | +33.9% | 0.80 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +61.6% | +12.1% | -35.7% | +30.3% | 0.53 | 2 | 83% | -0.27 | [-0.71, +0.08] | 0.21 |
| Close > 50-day SMA | +25.7% | +5.6% | -37.5% | +24.6% | 0.35 | 46 | 66% | -0.45 | [-1.03, +0.14] | 0.13 |
| MACD > signal | +37.3% | +7.9% | -25.8% | +22.3% | 0.45 | 48 | 50% | -0.35 | [-1.02, +0.31] | 0.33 |
| RSI 30/70 | +15.7% | +3.5% | -18.6% | +11.5% | 0.36 | 1 | 5% | -0.44 | [-1.36, +0.72] | 0.38 |
| Trailing stop 20% | +165.3% | +26.2% | -23.6% | +31.0% | 0.91 | 2 | 95% | +0.11 | [-0.10, +0.36] | 0.31 |
| Volume breakout | +21.6% | +4.8% | -29.3% | +18.1% | 0.35 | 10 | 38% | -0.45 | [-1.25, +0.40] | 0.28 |

### TSLA (2022-08-24 to 2026-11-06)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +20.9% | +4.6% | -65.0% | +58.2% | 0.37 | 0 | 100% |  |  |  |
| 50/200 SMA cross | -26.4% | -7.1% | -56.8% | +40.1% | 0.01 | 4 | 47% | -0.35 | [-1.21, +0.47] | 0.41 |
| Close > 50-day SMA | +45.3% | +9.3% | -41.1% | +38.5% | 0.42 | 42 | 53% | +0.06 | [-0.66, +0.86] | 0.90 |
| MACD > signal | +396.7% | +46.6% | -39.8% | +40.8% | 1.14 | 41 | 51% | +0.77 | [+0.15, +1.39] | 0.02 |
| RSI 30/70 | +39.1% | +8.2% | -52.7% | +40.1% | 0.39 | 4 | 42% | +0.03 | [-0.75, +0.78] | 0.94 |
| Trailing stop 20% | +23.3% | +5.1% | -47.9% | +44.9% | 0.34 | 11 | 71% | -0.03 | [-0.65, +0.59] | 0.92 |
| Volume breakout | +40.5% | +8.4% | -35.4% | +25.7% | 0.44 | 9 | 18% | +0.08 | [-0.87, +1.05] | 0.88 |

### AMZN (2022-08-24 to 2026-11-06)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +88.8% | +16.4% | -40.4% | +34.1% | 0.61 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +33.3% | +7.1% | -41.4% | +27.7% | 0.38 | 2 | 73% | -0.23 | [-0.93, +0.39] | 0.46 |
| Close > 50-day SMA | +21.2% | +4.7% | -41.0% | +23.3% | 0.31 | 35 | 63% | -0.30 | [-0.95, +0.39] | 0.41 |
| MACD > signal | -3.2% | -0.8% | -28.7% | +22.7% | 0.08 | 50 | 49% | -0.54 | [-1.20, +0.19] | 0.14 |
| RSI 30/70 | +94.0% | +17.1% | -22.0% | +21.6% | 0.84 | 4 | 33% | +0.22 | [-0.46, +1.04] | 0.55 |
| Trailing stop 20% | +93.7% | +17.1% | -24.2% | +29.9% | 0.68 | 3 | 87% | +0.06 | [-0.37, +0.51] | 0.77 |
| Volume breakout | +3.7% | +0.9% | -35.7% | +18.7% | 0.14 | 11 | 45% | -0.47 | [-1.33, +0.46] | 0.31 |

### IBM (2022-08-24 to 2026-11-06)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +110.6% | +19.4% | -37.5% | +31.5% | 0.73 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +57.1% | +11.4% | -28.7% | +22.8% | 0.59 | 3 | 73% | -0.14 | [-0.77, +0.54] | 0.68 |
| Close > 50-day SMA | +53.0% | +10.7% | -42.6% | +25.1% | 0.53 | 27 | 59% | -0.19 | [-0.66, +0.40] | 0.46 |
| MACD > signal | +105.5% | +18.7% | -43.1% | +24.0% | 0.84 | 30 | 50% | +0.12 | [-0.48, +0.84] | 0.71 |
| RSI 30/70 | +175.4% | +27.3% | -16.5% | +17.4% | 1.48 | 8 | 35% | +0.75 | [-0.20, +1.63] | 0.12 |
| Trailing stop 20% | +59.9% | +11.8% | -45.9% | +30.3% | 0.53 | 3 | 92% | -0.20 | [-0.45, +0.01] | 0.09 |
| Volume breakout | +64.8% | +12.7% | -25.6% | +17.0% | 0.79 | 10 | 40% | +0.06 | [-0.90, +0.95] | 0.90 |

### GEV (2025-01-13 to 2026-11-06)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +103.2% | +47.7% | -38.3% | +56.0% | 0.98 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +133.0% | +59.3% | -38.3% | +55.0% | 1.12 | 1 | 98% | +0.14 | [-0.00, +0.43] | 0.18 |
| Close > 50-day SMA | +79.1% | +37.8% | -32.7% | +44.0% | 0.95 | 15 | 64% | -0.03 | [-0.69, +0.57] | 0.93 |
| MACD > signal | +60.6% | +29.8% | -31.0% | +42.1% | 0.83 | 17 | 48% | -0.15 | [-0.91, +0.71] | 0.72 |
| RSI 30/70 | +20.5% | +10.8% | -34.4% | +34.5% | 0.47 | 1 | 31% | -0.51 | [-1.71, +0.67] | 0.43 |
| Trailing stop 20% | +44.2% | +22.3% | -45.9% | +50.3% | 0.65 | 5 | 88% | -0.32 | [-0.90, +0.12] | 0.24 |
| Volume breakout | +24.5% | +12.8% | -24.6% | +33.6% | 0.53 | 3 | 36% | -0.45 | [-1.69, +0.68] | 0.46 |

### CEG (2022-11-02 to 2026-11-06)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +172.8% | +28.6% | -50.7% | +49.1% | 0.75 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +96.8% | +18.5% | -50.7% | +43.6% | 0.60 | 3 | 72% | -0.15 | [-0.59, +0.28] | 0.47 |
| Close > 50-day SMA | +139.1% | +24.4% | -40.9% | +37.3% | 0.77 | 47 | 57% | +0.01 | [-0.57, +0.57] | 0.97 |
| MACD > signal | +25.6% | +5.9% | -41.5% | +36.9% | 0.34 | 41 | 49% | -0.42 | [-1.07, +0.25] | 0.20 |
| RSI 30/70 | +84.9% | +16.6% | -28.6% | +31.8% | 0.64 | 3 | 37% | -0.12 | [-0.91, +0.72] | 0.78 |
| Trailing stop 20% | +90.1% | +17.4% | -52.8% | +43.8% | 0.58 | 8 | 84% | -0.17 | [-0.60, +0.26] | 0.41 |
| Volume breakout | +86.0% | +16.8% | -30.0% | +30.7% | 0.66 | 9 | 39% | -0.10 | [-0.81, +0.64] | 0.80 |

### VST (2022-08-24 to 2026-11-06)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +418.0% | +48.1% | -48.8% | +52.0% | 1.02 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +406.4% | +47.3% | -48.8% | +44.1% | 1.10 | 3 | 69% | +0.08 | [-0.27, +0.49] | 0.67 |
| Close > 50-day SMA | +45.4% | +9.4% | -67.2% | +38.1% | 0.43 | 45 | 64% | -0.59 | [-1.19, +0.02] | 0.06 |
| MACD > signal | +66.6% | +13.0% | -49.0% | +37.2% | 0.52 | 47 | 51% | -0.50 | [-1.17, +0.16] | 0.14 |
| RSI 30/70 | +181.1% | +28.0% | -27.3% | +26.5% | 1.06 | 3 | 20% | +0.04 | [-0.80, +0.87] | 0.92 |
| Trailing stop 20% | +205.7% | +30.6% | -56.3% | +44.7% | 0.82 | 9 | 88% | -0.19 | [-0.63, +0.24] | 0.39 |
| Volume breakout | +278.5% | +37.4% | -31.2% | +31.4% | 1.18 | 9 | 43% | +0.16 | [-0.59, +1.00] | 0.70 |

![Strategy equity curves](backtest_equity.png)

## 5. Next-day forecasts

Not included: SKHY (only 85 trading days of history, needs 452); SPCX (only 103 trading days of history, needs 452).

### ALAB

Walk-forward test on 210 unseen days (2026-01-07 to 2026-11-05).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.524 | 0.524 | 0.528 | 0.454 | 0.25 | 0.677 | 0.677 |
| Logistic regression | 0.49 | 0.524 | 0.85 | 0.489 | 0.258 | 0.072 | 0.677 |
| Gradient boosting | 0.471 | 0.524 | 0.944 | 0.449 | 0.284 | 0.151 | 0.677 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 649.0 | 0.0 |  |  |
| Ridge regression | 668.1 | -0.0597 | 0.471 | 0.966 |
| Gradient boosting | 684.4 | -0.1121 | 0.448 | 0.994 |

Forecast for the next session:

```
  P(up) | Logistic regression      59.7%
  P(up) | Gradient boosting        75.8%
  P(up) | historical base rate     51.9%
  expected return (ridge)          +1.63%
  80% range low                    -7.30%
  80% range high                   +11.41%
  daily volatility                 +7.18%
```

Best out-of-sample AUC **0.489**; smallest p-value against a naive baseline 0.850, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![ALAB feature effects](forecast_ALAB.png)

### AMD

Walk-forward test on 551 unseen days (2024-08-27 to 2026-11-05).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.508 | 0.528 | 0.837 | 0.491 | 0.25 | 1.053 | 1.095 |
| Logistic regression | 0.477 | 0.528 | 0.992 | 0.486 | 0.256 | 0.412 | 1.095 |
| Gradient boosting | 0.47 | 0.528 | 0.997 | 0.479 | 0.269 | 0.076 | 1.095 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 400.6 | 0.0 |  |  |
| Ridge regression | 403.7 | -0.0154 | 0.492 | 0.813 |
| Gradient boosting | 408.8 | -0.0414 | 0.492 | 0.983 |

Forecast for the next session:

```
  P(up) | Logistic regression      63.1%
  P(up) | Gradient boosting        78.8%
  P(up) | historical base rate     51.3%
  expected return (ridge)          +0.82%
  80% range low                    -7.27%
  80% range high                   +9.63%
  daily volatility                 +6.53%
```

Best out-of-sample AUC **0.486**; smallest p-value against a naive baseline 0.813, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![AMD feature effects](forecast_AMD.png)

### NVDA

Walk-forward test on 551 unseen days (2024-08-27 to 2026-11-05).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.523 | 0.523 | 0.517 | 0.495 | 0.25 | 0.61 | 0.61 |
| Logistic regression | 0.519 | 0.523 | 0.585 | 0.521 | 0.252 | 0.593 | 0.61 |
| Gradient boosting | 0.53 | 0.523 | 0.383 | 0.486 | 0.268 | 0.897 | 0.61 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 282.1 | 0.0 |  |  |
| Ridge regression | 284.0 | -0.0131 | 0.506 | 0.692 |
| Gradient boosting | 288.9 | -0.0481 | 0.543 | 0.934 |

Forecast for the next session:

```
  P(up) | Logistic regression      50.1%
  P(up) | Gradient boosting        44.6%
  P(up) | historical base rate     53.6%
  expected return (ridge)          -0.53%
  80% range low                    -4.21%
  80% range high                   +3.28%
  daily volatility                 +2.94%
```

Best out-of-sample AUC **0.521**; smallest p-value against a naive baseline 0.383, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![NVDA feature effects](forecast_NVDA.png)

### MRVL

Walk-forward test on 551 unseen days (2024-08-27 to 2026-11-05).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.535 | 0.535 | 0.517 | 0.488 | 0.249 | 0.806 | 0.806 |
| Logistic regression | 0.534 | 0.535 | 0.551 | 0.549 | 0.252 | 0.641 | 0.806 |
| Gradient boosting | 0.528 | 0.535 | 0.65 | 0.548 | 0.26 | 0.748 | 0.806 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 480.0 | 0.0 |  |  |
| Ridge regression | 482.1 | -0.009 | 0.519 | 0.725 |
| Gradient boosting | 487.7 | -0.0324 | 0.499 | 0.955 |

Forecast for the next session:

```
  P(up) | Logistic regression      49.9%
  P(up) | Gradient boosting        52.0%
  P(up) | historical base rate     52.4%
  expected return (ridge)          -2.03%
  80% range low                    -10.39%
  80% range high                   +7.11%
  daily volatility                 +6.96%
```

Best out-of-sample AUC **0.549**; smallest p-value against a naive baseline 0.551, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![MRVL feature effects](forecast_MRVL.png)

### GOOG

Walk-forward test on 551 unseen days (2024-08-27 to 2026-11-05).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.521 | 0.521 | 0.517 | 0.482 | 0.25 | 0.936 | 0.937 |
| Logistic regression | 0.544 | 0.521 | 0.143 | 0.531 | 0.253 | 0.388 | 0.937 |
| Gradient boosting | 0.523 | 0.521 | 0.483 | 0.528 | 0.263 | 0.725 | 0.937 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 201.5 | 0.0 |  |  |
| Ridge regression | 204.2 | -0.0275 | 0.523 | 0.979 |
| Gradient boosting | 209.0 | -0.0757 | 0.517 | 0.999 |

Forecast for the next session:

```
  P(up) | Logistic regression      45.9%
  P(up) | Gradient boosting        59.2%
  P(up) | historical base rate     52.9%
  expected return (ridge)          +0.37%
  80% range low                    -3.62%
  80% range high                   +4.52%
  daily volatility                 +3.16%
```

Best out-of-sample AUC **0.531**; smallest p-value against a naive baseline 0.143, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![GOOG feature effects](forecast_GOOG.png)

### FSLR

Walk-forward test on 551 unseen days (2024-08-27 to 2026-11-05).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.508 | 0.514 | 0.617 | 0.466 | 0.25 | 0.344 | 0.163 |
| Logistic regression | 0.521 | 0.514 | 0.383 | 0.533 | 0.25 | 0.017 | 0.163 |
| Gradient boosting | 0.519 | 0.514 | 0.416 | 0.526 | 0.259 | 0.247 | 0.163 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 363.3 | 0.0 |  |  |
| Ridge regression | 363.6 | -0.0017 | 0.503 | 0.557 |
| Gradient boosting | 373.8 | -0.0584 | 0.514 | 0.998 |

Forecast for the next session:

```
  P(up) | Logistic regression      66.0%
  P(up) | Gradient boosting        57.1%
  P(up) | historical base rate     49.4%
  expected return (ridge)          +0.51%
  80% range low                    -2.64%
  80% range high                   +3.77%
  daily volatility                 +2.49%
```

Best out-of-sample AUC **0.533**; smallest p-value against a naive baseline 0.383, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![FSLR feature effects](forecast_FSLR.png)

### ETN

Walk-forward test on 551 unseen days (2024-08-27 to 2026-11-05).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.525 | 0.525 | 0.517 | 0.482 | 0.25 | 0.393 | 0.393 |
| Logistic regression | 0.515 | 0.525 | 0.681 | 0.509 | 0.255 | 0.54 | 0.393 |
| Gradient boosting | 0.543 | 0.525 | 0.209 | 0.527 | 0.26 | 0.506 | 0.393 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 247.2 | 0.0 |  |  |
| Ridge regression | 248.7 | -0.0122 | 0.517 | 0.748 |
| Gradient boosting | 252.5 | -0.0434 | 0.51 | 0.951 |

Forecast for the next session:

```
  P(up) | Logistic regression      57.8%
  P(up) | Gradient boosting        36.4%
  P(up) | historical base rate     53.9%
  expected return (ridge)          +0.28%
  80% range low                    -5.02%
  80% range high                   +5.89%
  daily volatility                 +4.24%
```

Best out-of-sample AUC **0.527**; smallest p-value against a naive baseline 0.209, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![ETN feature effects](forecast_ETN.png)

### TSLA

Walk-forward test on 551 unseen days (2024-08-27 to 2026-11-05).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.503 | 0.503 | 0.517 | 0.458 | 0.25 | 0.708 | 0.708 |
| Logistic regression | 0.506 | 0.503 | 0.449 | 0.512 | 0.253 | 0.826 | 0.708 |
| Gradient boosting | 0.503 | 0.503 | 0.517 | 0.52 | 0.263 | 0.189 | 0.708 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 369.5 | 0.0 |  |  |
| Ridge regression | 374.2 | -0.0256 | 0.495 | 0.958 |
| Gradient boosting | 376.1 | -0.0364 | 0.528 | 0.922 |

Forecast for the next session:

```
  P(up) | Logistic regression      44.2%
  P(up) | Gradient boosting        43.6%
  P(up) | historical base rate     50.5%
  expected return (ridge)          -0.08%
  80% range low                    -4.57%
  80% range high                   +4.63%
  daily volatility                 +3.59%
```

Best out-of-sample AUC **0.520**; smallest p-value against a naive baseline 0.449, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![TSLA feature effects](forecast_TSLA.png)

### AMZN

Walk-forward test on 551 unseen days (2024-08-27 to 2026-11-05).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.515 | 0.515 | 0.517 | 0.463 | 0.25 | 0.711 | 0.711 |
| Logistic regression | 0.55 | 0.515 | 0.057 | 0.56 | 0.248 | 1.067 | 0.711 |
| Gradient boosting | 0.519 | 0.515 | 0.449 | 0.531 | 0.261 | 0.369 | 0.711 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 212.2 | 0.0 |  |  |
| Ridge regression | 213.8 | -0.0158 | 0.537 | 0.861 |
| Gradient boosting | 221.1 | -0.0858 | 0.528 | 1.0 |

Forecast for the next session:

```
  P(up) | Logistic regression      60.0%
  P(up) | Gradient boosting        44.3%
  P(up) | historical base rate     51.2%
  expected return (ridge)          +0.82%
  80% range low                    -2.52%
  80% range high                   +4.27%
  daily volatility                 +2.63%
```

Best out-of-sample AUC **0.560**; smallest p-value against a naive baseline 0.057, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![AMZN feature effects](forecast_AMZN.png)

### IBM

Walk-forward test on 551 unseen days (2024-08-27 to 2026-11-05).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.546 | 0.546 | 0.518 | 0.475 | 0.248 | 0.509 | 0.51 |
| Logistic regression | 0.541 | 0.546 | 0.618 | 0.478 | 0.254 | 0.733 | 0.51 |
| Gradient boosting | 0.515 | 0.546 | 0.933 | 0.494 | 0.265 | 0.589 | 0.51 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 253.2 | 0.0 |  |  |
| Ridge regression | 258.5 | -0.0422 | 0.53 | 0.996 |
| Gradient boosting | 259.4 | -0.0492 | 0.544 | 0.999 |

Forecast for the next session:

```
  P(up) | Logistic regression      47.8%
  P(up) | Gradient boosting        39.7%
  P(up) | historical base rate     55.0%
  expected return (ridge)          -0.41%
  80% range low                    -2.55%
  80% range high                   +1.78%
  daily volatility                 +1.70%
```

Best out-of-sample AUC **0.494**; smallest p-value against a naive baseline 0.618, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![IBM feature effects](forecast_IBM.png)

### GEV

Walk-forward test on 205 unseen days (2026-01-14 to 2026-11-05).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.532 | 0.532 | 0.528 | 0.469 | 0.25 | 0.693 | 0.694 |
| Logistic regression | 0.502 | 0.532 | 0.819 | 0.496 | 0.258 | 0.389 | 0.694 |
| Gradient boosting | 0.532 | 0.532 | 0.528 | 0.536 | 0.267 | 1.06 | 0.694 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 336.0 | 0.0 |  |  |
| Ridge regression | 343.3 | -0.044 | 0.551 | 0.844 |
| Gradient boosting | 347.1 | -0.0671 | 0.532 | 0.877 |

Forecast for the next session:

```
  P(up) | Logistic regression      64.3%
  P(up) | Gradient boosting        61.9%
  P(up) | historical base rate     54.3%
  expected return (ridge)          +1.78%
  80% range low                    -4.04%
  80% range high                   +7.95%
  daily volatility                 +4.59%
```

Best out-of-sample AUC **0.536**; smallest p-value against a naive baseline 0.528, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![GEV feature effects](forecast_GEV.png)

### CEG

Walk-forward test on 503 unseen days (2024-11-04 to 2026-11-05).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.505 | 0.505 | 0.518 | 0.484 | 0.251 | 0.378 | 0.378 |
| Logistic regression | 0.479 | 0.505 | 0.886 | 0.491 | 0.26 | -0.015 | 0.378 |
| Gradient boosting | 0.483 | 0.505 | 0.847 | 0.472 | 0.274 | -0.183 | 0.378 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 349.9 | 0.0 |  |  |
| Ridge regression | 359.0 | -0.0524 | 0.481 | 0.992 |
| Gradient boosting | 362.1 | -0.0706 | 0.505 | 0.997 |

Forecast for the next session:

```
  P(up) | Logistic regression      55.0%
  P(up) | Gradient boosting        58.1%
  P(up) | historical base rate     52.1%
  expected return (ridge)          +0.48%
  80% range low                    -3.64%
  80% range high                   +4.78%
  daily volatility                 +3.27%
```

Best out-of-sample AUC **0.491**; smallest p-value against a naive baseline 0.847, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![CEG feature effects](forecast_CEG.png)

### VST

Walk-forward test on 551 unseen days (2024-08-27 to 2026-11-05).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.517 | 0.517 | 0.517 | 0.495 | 0.25 | 0.614 | 0.614 |
| Logistic regression | 0.486 | 0.517 | 0.932 | 0.484 | 0.26 | 1.076 | 0.614 |
| Gradient boosting | 0.552 | 0.517 | 0.057 | 0.553 | 0.257 | 1.374 | 0.614 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 394.7 | 0.0 |  |  |
| Ridge regression | 396.8 | -0.0109 | 0.488 | 0.697 |
| Gradient boosting | 400.3 | -0.0287 | 0.506 | 0.89 |

Forecast for the next session:

```
  P(up) | Logistic regression      56.6%
  P(up) | Gradient boosting        54.1%
  P(up) | historical base rate     52.7%
  expected return (ridge)          +1.07%
  80% range low                    -5.67%
  80% range high                   +8.30%
  daily volatility                 +5.39%
```

Best out-of-sample AUC **0.553**; smallest p-value against a naive baseline 0.057, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![VST feature effects](forecast_VST.png)

## 6. Stock screen and entry plans

| ticker | rank | score | passes_filters | close | momentum_12_1 | momentum_6m | volatility | off_52w_high | forward_pe | pullback_entry | breakout_trigger | stop | stop_% | shares | position_$ | max_loss_$ | filter_notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 1 | +0.73 | True | 449.04 | +142.1% | -1.4% | +73.6% | -30.9% | 25.4 | 412.43 | 606.74 | 339.22 | -17.8% | 13 | 5362.0 | 952.0 |  |
| XOM | 2 | +0.70 | True | 165.87 | +52.5% | +16.3% | +26.3% | -11.4% | 13.3 | 161.13 | 187.62 | 151.65 | -5.9% | 62 | 9990.0 | 588.0 |  |
| KO | 3 | +0.60 | True | 95.67 | +31.5% | +23.5% | +17.3% | -0.2% | 27.1 | 93.28 | 96.02 | 89.62 | -3.9% | 107 | 9981.0 | 392.0 |  |
| JNJ | 4 | +0.60 | True | 276.22 | +41.0% | +26.1% | +24.7% | -0.8% | 23.8 | 265.79 | 276.87 | 250.96 | -5.6% | 37 | 9834.0 | 549.0 |  |
| LLY | 5 | +0.59 | True | 1354.00 | +27.1% | +43.2% | +30.6% | -4.5% | 26.9 | 1301.95 | 1420.83 | 1207.25 | -7.3% | 7 | 9114.0 | 663.0 |  |
| V | 6 | +0.59 | True | 422.65 | +11.2% | +33.1% | +21.7% | -3.2% | 24.7 | 408.86 | 437.44 | 390.32 | -4.5% | 24 | 9813.0 | 445.0 |  |
| MSFT | 7 | +0.56 | True | 530.61 | +3.9% | +28.3% | +26.7% | -4.5% | 21.9 | 516.65 | 556.91 | 485.77 | -6.0% | 19 | 9816.0 | 587.0 |  |
| AAPL | 8 | +0.51 | True | 342.37 | +26.5% | +16.9% | +21.8% | -2.0% | 32.4 | 336.01 | 350.21 | 318.47 | -5.2% | 29 | 9744.0 | 509.0 |  |
| JPM | 9 | +0.35 | True | 334.49 | +8.4% | +11.8% | +19.9% | -7.9% | 13.1 | 326.45 | 352.81 | 310.37 | -4.9% | 30 | 9794.0 | 482.0 |  |
| UNH | 10 | +0.19 | True | 394.15 | +16.2% | +5.0% | +23.8% | -9.1% | 16.9 | 390.17 | 425.83 | 365.46 | -6.3% | 25 | 9754.0 | 618.0 |  |
| PG | 11 | +0.17 | True | 165.40 | +5.6% | +14.6% | +20.5% | -1.1% | 22.4 | 159.77 | 167.65 | 153.04 | -4.2% | 62 | 9906.0 | 417.0 |  |
| LIN | 12 | +0.10 | True | 515.25 | +16.7% | +5.2% | +16.1% | -5.4% | 26.4 | 506.16 | 525.79 | 487.08 | -3.8% | 19 | 9617.0 | 363.0 |  |
| AMT | 13 | -0.05 | True | 188.79 | -3.3% | +9.1% | +29.4% | -3.1% | 26.9 | 185.28 | 195.25 | 174.08 | -6.0% | 53 | 9820.0 | 594.0 |  |
| AMZN | 14 | -0.11 | True | 259.30 | +1.5% | -4.9% | +31.0% | -8.7% | 23.8 | 254.28 | 266.56 | 235.9 | -7.2% | 39 | 9917.0 | 717.0 |  |
| COST | 15 | -0.15 | True | 1053.56 | +1.8% | +4.8% | +20.2% | -3.4% | 42.1 | 1003.33 | 1067.72 | 962.82 | -4.0% | 9 | 9030.0 | 365.0 |  |

## 7. Portfolio construction

Not included: SKHY (only 85 trading days of history, needs 252); SPCX (only 103 trading days of history, needs 252).

Assets: ALAB, AMD, NVDA, MRVL, GOOG, FSLR, ETN, TSLA, AMZN, IBM, GEV, CEG, VST, JPM, XOM, UNH, COST, TLT, GLD. Covariance: Ledoit-Wolf shrinkage on the last 252 trading days.

Weights and share of risk (%):

| asset | weight: Equal weight | weight: Inverse volatility | weight: Risk parity | weight: Minimum variance | risk share: Equal weight | risk share: Inverse volatility | risk share: Risk parity | risk share: Minimum variance |
|---|---|---|---|---|---|---|---|---|
| ALAB | 5.3 | 1.9 | 1.4 | 0.0 | 16.8 | 7.8 | 5.3 | 0.0 |
| AMD | 5.3 | 2.7 | 1.6 | 0.0 | 12.6 | 8.7 | 5.3 | 0.0 |
| NVDA | 5.3 | 4.9 | 3.7 | 4.7 | 5.5 | 7.4 | 5.6 | 5.2 |
| MRVL | 5.3 | 2.3 | 1.5 | 0.0 | 13.9 | 8.0 | 5.3 | 0.0 |
| GOOG | 5.3 | 5.7 | 4.8 | 4.5 | 2.8 | 5.2 | 5.5 | 5.0 |
| FSLR | 5.3 | 3.7 | 2.9 | 0.3 | 5.9 | 6.2 | 5.4 | 0.4 |
| ETN | 5.3 | 4.4 | 2.9 | 1.9 | 7.2 | 8.6 | 5.5 | 2.1 |
| TSLA | 5.3 | 4.2 | 2.8 | 0.0 | 6.4 | 7.6 | 5.4 | 0.0 |
| AMZN | 5.3 | 5.5 | 4.3 | 3.5 | 3.1 | 5.7 | 5.5 | 3.9 |
| IBM | 5.3 | 4.0 | 5.6 | 2.4 | 1.4 | 2.0 | 5.5 | 2.6 |
| GEV | 5.3 | 3.5 | 2.7 | 0.9 | 8.0 | 7.4 | 5.5 | 1.0 |
| CEG | 5.3 | 4.0 | 3.1 | 1.5 | 6.1 | 6.7 | 5.4 | 1.7 |
| VST | 5.3 | 3.6 | 2.7 | 0.1 | 7.4 | 7.3 | 5.4 | 0.1 |
| JPM | 5.3 | 7.9 | 7.3 | 7.6 | 1.6 | 4.7 | 5.7 | 8.5 |
| XOM | 5.3 | 6.8 | 0.0 | 18.0 | -1.2 | -2.0 | -0.0 | 20.1 |
| UNH | 5.3 | 5.4 | 6.9 | 3.1 | 0.8 | 2.2 | 5.6 | 3.5 |
| COST | 5.3 | 8.7 | 22.1 | 17.9 | -1.2 | -1.6 | 6.0 | 20.0 |
| TLT | 5.3 | 14.5 | 17.8 | 30.0 | 0.4 | 2.9 | 6.3 | 21.8 |
| GLD | 5.3 | 6.4 | 5.7 | 3.6 | 2.5 | 5.3 | 5.6 | 4.0 |

| method | expected volatility | diversification ratio | effective number of bets | largest risk share | largest risk holder |
|---|---|---|---|---|---|
| Equal weight | 23.6% | 1.92 | 10.21 | 16.8% | ALAB |
| Inverse volatility | 15.8% | 2.30 | 14.07 | 8.7% | AMD |
| Risk parity | 13.0% | 2.51 | 17.97 | 6.3% | TLT |
| Minimum variance | 8.4% | 2.97 | 6.84 | 21.8% | TLT |

Concentration warnings:

- ETN and GEV have correlation 0.71: they tend to fall together
- CEG and VST have correlation 0.80: they tend to fall together

Out-of-sample comparison, monthly rebalance (2025-04-01 to 2026-11-06):

| method | CAGR | Volatility | Sharpe | Max drawdown |
|---|---|---|---|---|
| Equal weight | +43.4% | +25.7% | 1.53 | -14.6% |
| Inverse volatility | +32.2% | +18.4% | 1.61 | -10.1% |
| Risk parity | +23.7% | +14.6% | 1.53 | -8.6% |
| Minimum variance | +14.4% | +9.9% | 1.41 | -6.6% |

![Correlations](portfolio_correlation.png)

![Risk shares](portfolio_risk_shares.png)

![Walk-forward](portfolio_walk_forward.png)

## 8. Opening gaps: do pre-market moves carry into the day?

Across 15,248 stock-days (15 watchlist stocks, 2021-11-09 to 2026-11-06), each 1% of opening gap went with a -0.03% move from the open to the close (95% block-bootstrap CI [-0.09%, +0.03%]): no reliable relationship, so the size of a gap has not told you which way the session goes.

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 564 | -5.2% | +0.29% | 49% |
| down 1-3% | 2243 | -1.7% | +0.11% | 53% |
| within 1% | 9160 | +0.0% | +0.01% | 50% |
| up 1-3% | 2611 | +1.7% | +0.08% | 51% |
| gap up 3%+ | 670 | +5.3% | -0.23% | 46% |

## 9. Deciding before the open vs at the previous close

From 2022-02-03 to 2026-11-05 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +41.7% a year (worst drawdown -31.8%) against +38.5% (-30.5%) for labels set at the previous close; the two agreed on 90% of stock-weeks. Sharpe ratio difference +0.06 (95% block-bootstrap CI [-0.10, +0.22]): deciding before the open has been **not distinguishable from deciding on the previous close**.

| strategy | CAGR | Volatility | Sharpe | Max drawdown |
|---|---|---|---|---|
| Board on the previous close | +38.5% | 32.1% | 1.17 | -30.5% |
| Board on the pre-market price | +41.7% | 32.5% | 1.24 | -31.8% |
| Equal-weight watchlist | +37.6% | 33.9% | 1.11 | -40.6% |

The pre-market version uses the official opening price as a stand-in for the last pre-market trade (free pre-market history is only days long), which slightly flatters it.
