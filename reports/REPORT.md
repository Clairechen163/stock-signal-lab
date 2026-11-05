# stocklab report
Generated 2026-11-05 | data source: `yahoo` | history: 5 years | watchlist: ALAB, AMD, NVDA, MRVL, GOOG, FSLR, SKHY, ETN, TSLA, SPCX, AMZN

> Educational research code, not investment advice. Past results do not predict future returns.

## 1. Decision board

Data as of the 2026-11-04 close. `*` = provisional (under 200 trading days of history).

| ticker | action | close | 1 day | 1 month | buy rank | sell warnings | pullback entry | breakout | stop | why |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | BUY | 266.03 | +6.1% | +3.8% | 4/11 | 1/15 | 254.13 | 266.56 | 236.97 | buy rank 4/11; +9% vs 200-day average; distribution days |
| TSLA | WATCH | 385.19 | -3.3% | +1.2% | 6/11 | 4/15 | 383.21 | 408.27 | 355.03 | +0% vs 200-day average; death cross, distribution days, 20%+ off high |
| AMD | REDUCE | 488.78 | +1.0% | -24.7% | 1/11 | 6/15 |  |  |  | +18% vs 200-day average; below 50-day, MACD bearish, distribution days, 20%+ off high, below chandelier stop |
| NVDA | REDUCE | 200.13 | -3.2% | -16.3% | 3/11 | 7/15 |  |  |  | -2% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, below chandelier stop |
| SKHY | REDUCE* | 143.07 | -5.1% | -21.6% | 10/11 | 5/10 |  |  |  | -15% vs 50-day average; below 50-day, distribution days, 20%+ off high, below chandelier stop (provisional: 83 days of history) |
| FSLR | REDUCE | 194.51 | +4.6% | +8.2% | 11/11 | 6/15 |  |  |  | -10% vs 200-day average; below 200-day, death cross, distribution days, 20%+ off high |
| MRVL | SELL | 159.80 | -7.1% | -44.3% | 2/11 | 10/15 |  |  |  | -13% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, high-volume breakdown, 20%+ off high, below chandelier stop |
| ALAB | SELL | 223.27 | -4.4% | -42.7% | 5/11 | 10/15 |  |  |  | -13% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, high-volume breakdown, 20%+ off high, below chandelier stop |
| ETN | SELL | 353.08 | -9.9% | -20.7% | 7/11 | 11/15 |  |  |  | -11% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, high-volume breakdown, 20%+ off high, volatility spike, below chandelier stop |
| GOOG | SELL | 287.30 | +3.2% | -16.6% | 8/11 | 11/15 |  |  |  | -15% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| SPCX | SELL* | 135.92 | -3.8% | -20.9% | 9/11 | 6/10 |  |  |  | -9% vs 50-day average; below 50-day, MACD bearish, distribution days, 20%+ off high, below chandelier stop (provisional: 101 days of history) |

![Board label each week](board_history.png)

**Trading the labels** (2022-02-01 to 2026-11-04): buy on BUY, exit on SELL, REDUCE or AVOID, reviewed weekly with next-day execution and 5 bp costs.

| strategy | CAGR | Volatility | Sharpe | Max drawdown | Time invested | Avg holdings |
|---|---|---|---|---|---|---|
| Board strategy | +41.7% | 32.7% | 1.23 | -29.2% | 90% | 3.6 |
| Equal-weight watchlist | +34.1% | 36.7% | 0.98 | -39.8% | 100% | 8.6 |
| SPY (buy & hold) | +13.0% | 17.2% | 0.80 | -22.1% |  |  |

Sharpe difference vs equal weight: +0.24, 95% block-bootstrap CI [-0.37, +0.87].

Forward 21-day return after each label, relative to the watchlist average on the same date (sampled every 21 days, t-test across dates):

| label | observations | dates | mean 21d excess return | hit rate | p_value |
|---|---|---|---|---|---|
| BUY | 132 | 47 | -0.4% | 45% | 0.74 |
| HOLD | 71 | 36 | -1.0% | 39% | 0.63 |
| WATCH | 97 | 42 | -0.2% | 55% | 0.86 |
| AVOID | 29 | 18 | +0.6% | 61% | 0.75 |
| REDUCE | 84 | 38 | +1.2% | 63% | 0.49 |
| SELL | 63 | 26 | -0.1% | 42% | 0.94 |

![Board strategy vs holding](board_equity.png)

## 2. Sell check, stock by stock

```
ALAB  EXIT  (score 10/15, close 223.27 on 2026-11-04)
  RSI 32 | -53.8% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [volume] Down day closing below the 50-day average on 1.5x+ average volume (+2)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    Chandelier stop            329.88  (price is below, -32.3%)
    50-day SMA                 304.94  (price is below, -26.8%)
    200-day SMA                255.97  (price is below, -12.8%)
```

```
AMD  REDUCE  (score 6/15, close 488.78 on 2026-11-04)
  RSI 39 | -24.7% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    Chandelier stop            564.92  (price is below, -13.5%)
    50-day SMA                 548.90  (price is below, -11.0%)
    200-day SMA                414.23  (price is above, +18.0%)
```

```
NVDA  REDUCE  (score 7/15, close 200.13 on 2026-11-04)
  RSI 35 | -16.3% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    Chandelier stop            223.96  (price is below, -10.6%)
    50-day SMA                 221.15  (price is below, -9.5%)
    200-day SMA                204.39  (price is below, -2.1%)
```

```
MRVL  EXIT  (score 10/15, close 159.80 on 2026-11-04)
  RSI 27 | -49.5% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [volume] Down day closing below the 50-day average on 1.5x+ average volume (+2)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    Chandelier stop            247.96  (price is below, -35.6%)
    50-day SMA                 238.51  (price is below, -33.0%)
    200-day SMA                184.44  (price is below, -13.4%)
```

```
GOOG  EXIT  (score 11/15, close 287.30 on 2026-11-04)
  RSI 30 | -27.9% from 52-week high
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
    200-day SMA                337.69  (price is below, -14.9%)
    50-day SMA                 331.98  (price is below, -13.5%)
    Chandelier stop            324.22  (price is below, -11.4%)
```

```
FSLR  REDUCE  (score 6/15, close 194.51 on 2026-11-04)
  RSI 63 | -38.9% from 52-week high
  Triggered:
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
  Levels to watch:
    200-day SMA                215.09  (price is below, -9.6%)
    Chandelier stop            187.44  (price is above, +3.8%)
    50-day SMA                 187.38  (price is above, +3.8%)
```

```
SKHY  REDUCE  (score 5/10, close 143.07 on 2026-11-04)
  RSI 42 | -28.0% from high since listing
  Only 83 trading days of history; not scored yet: below_sma200, death_cross, volatility_spike
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the high since listing (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 168.16  (price is below, -14.9%)
    Chandelier stop            163.81  (price is below, -12.7%)
```

```
ETN  EXIT  (score 11/15, close 353.08 on 2026-11-04)
  RSI 37 | -23.2% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [volume] Down day closing below the 50-day average on 1.5x+ average volume (+2)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 408.61  (price is below, -13.6%)
    200-day SMA                396.19  (price is below, -10.9%)
    Chandelier stop            390.33  (price is below, -9.5%)
```

```
TSLA  WATCH  (score 4/15, close 385.19 on 2026-11-04)
  RSI 51 | -21.4% from 52-week high
  Triggered:
    - [trend] 50-day average below the 200-day average (+2)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
  Levels to watch:
    200-day SMA                384.76  (price is above, +0.1%)
    50-day SMA                 372.11  (price is above, +3.5%)
    Chandelier stop            371.96  (price is above, +3.6%)
```

```
SPCX  EXIT  (score 6/10, close 135.92 on 2026-11-04)
  RSI 40 | -35.7% from high since listing
  Only 101 trading days of history; not scored yet: below_sma200, death_cross, volatility_spike
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the high since listing (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    Chandelier stop            154.01  (price is below, -11.7%)
    50-day SMA                 149.64  (price is below, -9.2%)
```

```
AMZN  HOLD  (score 1/15, close 266.03 on 2026-11-04)
  RSI 60 | -6.3% from 52-week high
  Triggered:
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
  Levels to watch:
    50-day SMA                 253.89  (price is above, +4.8%)
    Chandelier stop            245.76  (price is above, +8.2%)
    200-day SMA                243.67  (price is above, +9.2%)
```

## 3. Which sell signals actually work? (event study)

Panel: 40 stocks, 5 years. Null hypothesis: returns after a signal look like returns on random days from the same stocks.

| rule | horizon | events | mean_after_signal | mean_random_days | difference | p_value | q_value | drop10_after_signal | drop10_base_rate | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| below_sma50 | 5d | 942 | +0.32% | +0.63% | -0.31% | 0.045 | 0.223 | 37% | 35% | weak (not significant) |
| below_sma50 | 21d | 920 | +2.55% | +2.82% | -0.27% | 0.249 | 0.484 | 37% | 35% | weak (not significant) |
| below_sma50 | 63d | 881 | +8.61% | +9.34% | -0.73% | 0.170 | 0.402 | 37% | 35% | weak (not significant) |
| below_sma200 | 5d | 454 | +0.13% | +0.55% | -0.42% | 0.048 | 0.223 | 38% | 35% | weak (not significant) |
| below_sma200 | 21d | 441 | +1.41% | +2.40% | -0.98% | 0.039 | 0.223 | 38% | 35% | weak (not significant) |
| below_sma200 | 63d | 422 | +8.28% | +8.02% | +0.26% | 0.601 | 0.901 | 38% | 35% | no edge |
| death_cross | 5d | 137 | -0.54% | +0.56% | -1.11% | 0.011 | 0.121 | 47% | 35% | weak (not significant) |
| death_cross | 21d | 132 | -0.03% | +2.53% | -2.56% | 0.006 | 0.099 | 47% | 35% | useful |
| death_cross | 63d | 126 | +9.68% | +8.57% | +1.11% | 0.715 | 0.907 | 47% | 35% | no edge |
| rsi_divergence | 5d | 434 | +0.34% | +0.73% | -0.39% | 0.071 | 0.262 | 37% | 35% | weak (not significant) |
| rsi_divergence | 21d | 431 | +2.63% | +3.30% | -0.67% | 0.117 | 0.351 | 37% | 35% | weak (not significant) |
| rsi_divergence | 63d | 425 | +8.64% | +11.09% | -2.45% | 0.017 | 0.140 | 37% | 35% | weak (not significant) |
| rsi_rollover | 5d | 553 | +1.62% | +0.71% | +0.91% | 1.000 | 1.000 | 33% | 35% | no edge |
| rsi_rollover | 21d | 541 | +3.25% | +3.23% | +0.02% | 0.526 | 0.867 | 33% | 35% | no edge |
| rsi_rollover | 63d | 533 | +8.39% | +10.98% | -2.59% | 0.004 | 0.099 | 33% | 35% | useful |
| macd_bearish | 5d | 1424 | +0.59% | +0.66% | -0.08% | 0.311 | 0.541 | 34% | 35% | weak (not significant) |
| macd_bearish | 21d | 1399 | +3.04% | +2.95% | +0.09% | 0.611 | 0.901 | 34% | 35% | no edge |
| macd_bearish | 63d | 1341 | +10.35% | +9.88% | +0.47% | 0.771 | 0.942 | 34% | 35% | no edge |
| distribution_cluster | 5d | 945 | +1.08% | +0.66% | +0.41% | 0.980 | 1.000 | 34% | 35% | no edge |
| distribution_cluster | 21d | 924 | +2.72% | +3.01% | -0.29% | 0.244 | 0.484 | 34% | 35% | weak (not significant) |
| distribution_cluster | 63d | 895 | +9.64% | +10.07% | -0.43% | 0.280 | 0.513 | 34% | 35% | weak (not significant) |
| high_volume_breakdown | 5d | 638 | +0.71% | +0.60% | +0.11% | 0.683 | 0.901 | 33% | 35% | no edge |
| high_volume_breakdown | 21d | 625 | +3.48% | +2.71% | +0.77% | 0.941 | 1.000 | 33% | 35% | no edge |
| high_volume_breakdown | 63d | 610 | +11.44% | +9.11% | +2.33% | 0.993 | 1.000 | 33% | 35% | no edge |
| drawdown_20 | 5d | 334 | +0.90% | +0.75% | +0.16% | 0.668 | 0.901 | 48% | 35% | no edge |
| drawdown_20 | 21d | 324 | +2.36% | +3.32% | -0.96% | 0.109 | 0.351 | 48% | 35% | weak (not significant) |
| drawdown_20 | 63d | 310 | +13.35% | +11.43% | +1.93% | 0.899 | 1.000 | 48% | 35% | no edge |
| volatility_spike | 5d | 279 | +0.30% | +0.68% | -0.38% | 0.139 | 0.383 | 44% | 35% | weak (not significant) |
| volatility_spike | 21d | 277 | +2.31% | +3.09% | -0.77% | 0.153 | 0.389 | 44% | 35% | weak (not significant) |
| volatility_spike | 63d | 275 | +8.12% | +10.33% | -2.21% | 0.054 | 0.223 | 44% | 35% | weak (not significant) |
| chandelier_stop | 5d | 1183 | +0.48% | +0.64% | -0.16% | 0.186 | 0.409 | 35% | 35% | weak (not significant) |
| chandelier_stop | 21d | 1161 | +3.10% | +2.94% | +0.16% | 0.673 | 0.901 | 35% | 35% | no edge |
| chandelier_stop | 63d | 1112 | +11.10% | +9.84% | +1.26% | 0.964 | 1.000 | 35% | 35% | no edge |

**2 of 33 rule-by-horizon tests** show significantly weaker returns after the signal (q < 0.10).

![Sell signal event study](sell_event_study.png)

## 4. Strategy backtests

Not included: SKHY (only 83 trading days of history, needs 452); SPCX (only 101 trading days of history, needs 452).

### ALAB (2025-01-03 to 2026-11-04)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +55.4% | +27.2% | -63.2% | +95.9% | 0.73 | 0 | 100% |  |  |  |
| 50/200 SMA cross | -65.9% | -44.4% | -67.6% | +86.2% | -0.25 | 2 | 75% | -0.98 | [-1.94, -0.28] | 0.02 |
| Close > 50-day SMA | +7.6% | +4.1% | -66.4% | +70.3% | 0.41 | 10 | 52% | -0.32 | [-1.32, +0.64] | 0.51 |
| MACD > signal | +14.8% | +7.9% | -70.4% | +65.6% | 0.44 | 21 | 50% | -0.29 | [-1.47, +0.94] | 0.64 |
| RSI 30/70 | -2.2% | -1.2% | -50.3% | +35.9% | 0.14 | 1 | 16% | -0.59 | [-2.27, +1.31] | 0.47 |
| Trailing stop 20% | -11.8% | -6.7% | -69.1% | +72.3% | 0.27 | 10 | 56% | -0.46 | [-1.41, +0.49] | 0.36 |
| Volume breakout | +91.8% | +42.8% | -55.7% | +63.5% | 0.87 | 4 | 42% | +0.14 | [-0.96, +1.19] | 0.80 |

### AMD (2022-08-23 to 2026-11-04)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +426.8% | +48.7% | -63.0% | +57.2% | 0.98 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +358.2% | +43.8% | -39.1% | +47.1% | 1.00 | 1 | 65% | +0.03 | [-0.55, +0.61] | 0.92 |
| Close > 50-day SMA | +169.2% | +26.7% | -41.8% | +43.9% | 0.75 | 37 | 54% | -0.22 | [-0.79, +0.30] | 0.45 |
| MACD > signal | +343.0% | +42.7% | -42.4% | +41.4% | 1.06 | 39 | 50% | +0.09 | [-0.49, +0.68] | 0.76 |
| RSI 30/70 | +30.3% | +6.5% | -54.7% | +31.3% | 0.36 | 3 | 33% | -0.62 | [-1.58, +0.37] | 0.22 |
| Trailing stop 20% | +217.1% | +31.7% | -58.9% | +48.6% | 0.81 | 10 | 71% | -0.17 | [-0.64, +0.29] | 0.49 |
| Volume breakout | +177.7% | +27.6% | -36.9% | +37.1% | 0.84 | 10 | 38% | -0.14 | [-0.90, +0.60] | 0.70 |

### NVDA (2022-08-23 to 2026-11-04)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +1066.0% | +79.8% | -37.3% | +49.0% | 1.44 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +672.9% | +63.0% | -28.4% | +42.7% | 1.36 | 1 | 83% | -0.08 | [-0.59, +0.44] | 0.72 |
| Close > 50-day SMA | +309.6% | +40.0% | -39.1% | +39.4% | 1.05 | 39 | 70% | -0.39 | [-0.93, +0.13] | 0.13 |
| MACD > signal | +152.9% | +24.8% | -46.7% | +34.4% | 0.81 | 40 | 51% | -0.63 | [-1.29, +0.06] | 0.07 |
| RSI 30/70 | +64.6% | +12.6% | -22.6% | +18.2% | 0.74 | 2 | 7% | -0.70 | [-1.72, +0.24] | 0.15 |
| Trailing stop 20% | +637.2% | +61.2% | -36.6% | +44.4% | 1.29 | 7 | 88% | -0.15 | [-0.49, +0.18] | 0.36 |
| Volume breakout | +211.5% | +31.2% | -19.8% | +26.3% | 1.16 | 7 | 31% | -0.28 | [-1.13, +0.48] | 0.52 |

### MRVL (2022-08-23 to 2026-11-04)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +210.3% | +31.1% | -60.8% | +66.6% | 0.73 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +55.5% | +11.1% | -65.2% | +56.5% | 0.47 | 2 | 67% | -0.27 | [-0.79, +0.18] | 0.26 |
| Close > 50-day SMA | +55.4% | +11.1% | -51.5% | +53.0% | 0.46 | 37 | 58% | -0.28 | [-0.89, +0.28] | 0.34 |
| MACD > signal | +101.6% | +18.2% | -62.5% | +50.2% | 0.58 | 44 | 51% | -0.16 | [-0.85, +0.56] | 0.66 |
| RSI 30/70 | +66.4% | +12.9% | -32.1% | +27.0% | 0.59 | 2 | 19% | -0.15 | [-1.14, +0.96] | 0.78 |
| Trailing stop 20% | +75.9% | +14.4% | -53.3% | +56.7% | 0.52 | 15 | 76% | -0.22 | [-0.73, +0.23] | 0.39 |
| Volume breakout | +76.0% | +14.5% | -46.2% | +42.0% | 0.53 | 11 | 36% | -0.21 | [-1.11, +0.62] | 0.62 |

### GOOG (2022-08-23 to 2026-11-04)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +152.7% | +24.8% | -30.2% | +31.8% | 0.86 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +151.5% | +24.6% | -29.4% | +25.9% | 0.98 | 2 | 76% | +0.12 | [-0.40, +0.59] | 0.62 |
| Close > 50-day SMA | +88.5% | +16.3% | -22.2% | +23.6% | 0.76 | 36 | 63% | -0.10 | [-0.82, +0.67] | 0.78 |
| MACD > signal | +36.1% | +7.6% | -18.1% | +21.5% | 0.45 | 42 | 50% | -0.41 | [-1.17, +0.30] | 0.27 |
| RSI 30/70 | +31.0% | +6.7% | -20.4% | +18.1% | 0.45 | 4 | 25% | -0.41 | [-1.26, +0.50] | 0.34 |
| Trailing stop 20% | +59.4% | +11.8% | -40.4% | +29.7% | 0.52 | 6 | 92% | -0.33 | [-0.76, +0.05] | 0.10 |
| Volume breakout | +105.6% | +18.8% | -17.4% | +19.4% | 0.98 | 8 | 46% | +0.13 | [-0.68, +0.91] | 0.75 |

### FSLR (2022-08-23 to 2026-11-04)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +64.1% | +12.6% | -60.0% | +55.0% | 0.49 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +18.7% | +4.2% | -51.1% | +41.8% | 0.30 | 4 | 60% | -0.18 | [-0.76, +0.38] | 0.52 |
| Close > 50-day SMA | +54.4% | +10.9% | -46.8% | +40.3% | 0.45 | 28 | 50% | -0.03 | [-0.62, +0.54] | 0.91 |
| MACD > signal | -54.0% | -16.9% | -74.1% | +40.5% | -0.26 | 48 | 49% | -0.74 | [-1.42, -0.12] | 0.02 |
| RSI 30/70 | +30.1% | +6.5% | -42.8% | +30.4% | 0.35 | 2 | 27% | -0.13 | [-1.10, +0.71] | 0.77 |
| Trailing stop 20% | +38.1% | +8.0% | -52.3% | +45.1% | 0.39 | 11 | 69% | -0.09 | [-0.59, +0.41] | 0.71 |
| Volume breakout | -16.5% | -4.2% | -53.8% | +32.1% | 0.03 | 13 | 37% | -0.46 | [-1.33, +0.35] | 0.28 |

### ETN (2022-08-23 to 2026-11-04)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +156.6% | +25.2% | -34.5% | +33.7% | 0.84 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +67.0% | +13.0% | -32.8% | +30.0% | 0.56 | 2 | 83% | -0.28 | [-0.73, +0.08] | 0.18 |
| Close > 50-day SMA | +27.9% | +6.1% | -37.5% | +24.6% | 0.36 | 46 | 66% | -0.48 | [-1.04, +0.14] | 0.12 |
| MACD > signal | +37.3% | +7.9% | -25.8% | +22.4% | 0.45 | 48 | 50% | -0.39 | [-1.08, +0.29] | 0.25 |
| RSI 30/70 | +15.7% | +3.6% | -18.6% | +11.5% | 0.36 | 1 | 5% | -0.48 | [-1.42, +0.65] | 0.35 |
| Trailing stop 20% | +169.9% | +26.8% | -23.6% | +31.0% | 0.92 | 2 | 95% | +0.08 | [-0.09, +0.29] | 0.39 |
| Volume breakout | +21.6% | +4.8% | -29.3% | +18.1% | 0.35 | 10 | 38% | -0.49 | [-1.29, +0.32] | 0.24 |

### TSLA (2022-08-23 to 2026-11-04)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +29.6% | +6.4% | -65.0% | +58.0% | 0.39 | 0 | 100% |  |  |  |
| 50/200 SMA cross | -26.4% | -7.1% | -56.8% | +40.1% | 0.01 | 4 | 47% | -0.38 | [-1.24, +0.44] | 0.37 |
| Close > 50-day SMA | +55.7% | +11.2% | -41.1% | +38.1% | 0.47 | 42 | 53% | +0.07 | [-0.65, +0.87] | 0.85 |
| MACD > signal | +434.1% | +49.2% | -39.8% | +40.4% | 1.19 | 41 | 51% | +0.79 | [+0.17, +1.44] | 0.02 |
| RSI 30/70 | +49.6% | +10.1% | -52.7% | +39.7% | 0.44 | 4 | 42% | +0.04 | [-0.69, +0.78] | 0.91 |
| Trailing stop 20% | +32.1% | +6.9% | -47.9% | +44.6% | 0.37 | 11 | 71% | -0.02 | [-0.64, +0.61] | 0.94 |
| Volume breakout | +40.5% | +8.5% | -35.4% | +25.7% | 0.44 | 9 | 18% | +0.05 | [-0.93, +1.04] | 0.91 |

### AMZN (2022-08-23 to 2026-11-04)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +98.7% | +17.8% | -40.4% | +34.1% | 0.65 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +36.8% | +7.8% | -41.4% | +27.7% | 0.41 | 2 | 73% | -0.24 | [-0.88, +0.36] | 0.46 |
| Close > 50-day SMA | +24.8% | +5.4% | -40.8% | +23.4% | 0.34 | 35 | 63% | -0.31 | [-0.94, +0.37] | 0.41 |
| MACD > signal | -2.8% | -0.7% | -28.7% | +22.7% | 0.08 | 50 | 49% | -0.57 | [-1.26, +0.16] | 0.12 |
| RSI 30/70 | +94.0% | +17.1% | -22.0% | +21.6% | 0.84 | 4 | 33% | +0.19 | [-0.47, +0.99] | 0.62 |
| Trailing stop 20% | +103.9% | +18.6% | -24.2% | +29.9% | 0.72 | 3 | 87% | +0.07 | [-0.35, +0.49] | 0.76 |
| Volume breakout | +4.1% | +1.0% | -35.5% | +18.7% | 0.14 | 11 | 45% | -0.51 | [-1.41, +0.40] | 0.27 |

![Strategy equity curves](backtest_equity.png)

## 5. Next-day forecasts

Not included: SKHY (only 83 trading days of history, needs 452); SPCX (only 101 trading days of history, needs 452).

### ALAB

Walk-forward test on 208 unseen days (2026-01-07 to 2026-11-03).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.524 | 0.524 | 0.528 | 0.454 | 0.25 | 0.858 | 0.858 |
| Logistic regression | 0.49 | 0.524 | 0.851 | 0.483 | 0.259 | 0.273 | 0.858 |
| Gradient boosting | 0.471 | 0.524 | 0.945 | 0.444 | 0.286 | 0.355 | 0.858 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 632.9 | 0.0 |  |  |
| Ridge regression | 653.0 | -0.0646 | 0.471 | 0.97 |
| Gradient boosting | 668.0 | -0.1139 | 0.447 | 0.994 |

Forecast for the next session:

```
  P(up) | Logistic regression      51.2%
  P(up) | Gradient boosting        48.7%
  P(up) | historical base rate     52.0%
  expected return (ridge)          +0.62%
  80% range low                    -6.40%
  80% range high                   +8.16%
  daily volatility                 +5.64%
```

Best out-of-sample AUC **0.483**; smallest p-value against a naive baseline 0.851, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![ALAB feature effects](forecast_ALAB.png)

### AMD

Walk-forward test on 550 unseen days (2024-08-26 to 2026-11-03).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.522 | 0.529 | 0.65 | 0.487 | 0.25 | 1.324 | 1.17 |
| Logistic regression | 0.484 | 0.529 | 0.985 | 0.486 | 0.256 | 0.355 | 1.17 |
| Gradient boosting | 0.484 | 0.529 | 0.985 | 0.483 | 0.268 | 0.499 | 1.17 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 390.2 | 0.0 |  |  |
| Ridge regression | 394.1 | -0.02 | 0.489 | 0.879 |
| Gradient boosting | 399.3 | -0.0471 | 0.485 | 0.993 |

Forecast for the next session:

```
  P(up) | Logistic regression      61.5%
  P(up) | Gradient boosting        52.7%
  P(up) | historical base rate     51.3%
  expected return (ridge)          +1.19%
  80% range low                    -4.53%
  80% range high                   +7.25%
  daily volatility                 +4.54%
```

Best out-of-sample AUC **0.486**; smallest p-value against a naive baseline 0.879, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![AMD feature effects](forecast_AMD.png)

### NVDA

Walk-forward test on 550 unseen days (2024-08-26 to 2026-11-03).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.524 | 0.524 | 0.517 | 0.499 | 0.25 | 0.699 | 0.7 |
| Logistic regression | 0.52 | 0.524 | 0.585 | 0.526 | 0.252 | 0.637 | 0.7 |
| Gradient boosting | 0.524 | 0.524 | 0.517 | 0.503 | 0.263 | 0.763 | 0.7 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 279.2 | 0.0 |  |  |
| Ridge regression | 280.5 | -0.0097 | 0.518 | 0.642 |
| Gradient boosting | 284.9 | -0.0415 | 0.531 | 0.931 |

Forecast for the next session:

```
  P(up) | Logistic regression      58.7%
  P(up) | Gradient boosting        69.9%
  P(up) | historical base rate     53.7%
  expected return (ridge)          +0.59%
  80% range low                    -2.05%
  80% range high                   +3.30%
  daily volatility                 +2.07%
```

Best out-of-sample AUC **0.526**; smallest p-value against a naive baseline 0.517, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![NVDA feature effects](forecast_NVDA.png)

### MRVL

Walk-forward test on 550 unseen days (2024-08-26 to 2026-11-03).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.536 | 0.536 | 0.517 | 0.479 | 0.249 | 0.889 | 0.89 |
| Logistic regression | 0.535 | 0.536 | 0.551 | 0.547 | 0.252 | 0.905 | 0.89 |
| Gradient boosting | 0.535 | 0.536 | 0.551 | 0.545 | 0.26 | 0.607 | 0.89 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 473.7 | 0.0 |  |  |
| Ridge regression | 475.6 | -0.0078 | 0.524 | 0.697 |
| Gradient boosting | 482.6 | -0.0377 | 0.505 | 0.972 |

Forecast for the next session:

```
  P(up) | Logistic regression      71.7%
  P(up) | Gradient boosting        65.2%
  P(up) | historical base rate     52.5%
  expected return (ridge)          +0.13%
  80% range low                    -7.06%
  80% range high                   +7.89%
  daily volatility                 +5.82%
```

Best out-of-sample AUC **0.547**; smallest p-value against a naive baseline 0.551, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![MRVL feature effects](forecast_MRVL.png)

### GOOG

Walk-forward test on 550 unseen days (2024-08-26 to 2026-11-03).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.52 | 0.52 | 0.517 | 0.484 | 0.25 | 0.941 | 0.942 |
| Logistic regression | 0.549 | 0.52 | 0.093 | 0.53 | 0.253 | 0.442 | 0.942 |
| Gradient boosting | 0.516 | 0.52 | 0.585 | 0.524 | 0.264 | 0.435 | 0.942 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 201.5 | 0.0 |  |  |
| Ridge regression | 204.5 | -0.0304 | 0.522 | 0.986 |
| Gradient boosting | 209.2 | -0.0778 | 0.513 | 0.999 |

Forecast for the next session:

```
  P(up) | Logistic regression      46.0%
  P(up) | Gradient boosting        65.6%
  P(up) | historical base rate     52.8%
  expected return (ridge)          -0.45%
  80% range low                    -4.40%
  80% range high                   +3.66%
  daily volatility                 +3.16%
```

Best out-of-sample AUC **0.530**; smallest p-value against a naive baseline 0.093, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![GOOG feature effects](forecast_GOOG.png)

### FSLR

Walk-forward test on 550 unseen days (2024-08-26 to 2026-11-03).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.509 | 0.515 | 0.618 | 0.456 | 0.25 | 0.186 | 0.144 |
| Logistic regression | 0.507 | 0.515 | 0.65 | 0.53 | 0.251 | -0.16 | 0.144 |
| Gradient boosting | 0.5 | 0.515 | 0.766 | 0.52 | 0.262 | -0.207 | 0.144 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 363.5 | 0.0 |  |  |
| Ridge regression | 364.1 | -0.0033 | 0.507 | 0.608 |
| Gradient boosting | 373.7 | -0.0572 | 0.485 | 0.998 |

Forecast for the next session:

```
  P(up) | Logistic regression      67.8%
  P(up) | Gradient boosting        63.8%
  P(up) | historical base rate     49.3%
  expected return (ridge)          +0.93%
  80% range low                    -2.19%
  80% range high                   +4.15%
  daily volatility                 +2.45%
```

Best out-of-sample AUC **0.530**; smallest p-value against a naive baseline 0.608, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![FSLR feature effects](forecast_FSLR.png)

### ETN

Walk-forward test on 550 unseen days (2024-08-26 to 2026-11-03).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.524 | 0.524 | 0.517 | 0.48 | 0.25 | 0.428 | 0.429 |
| Logistic regression | 0.511 | 0.524 | 0.739 | 0.509 | 0.255 | 0.509 | 0.429 |
| Gradient boosting | 0.54 | 0.524 | 0.234 | 0.532 | 0.259 | 0.719 | 0.429 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 244.5 | 0.0 |  |  |
| Ridge regression | 245.8 | -0.0108 | 0.52 | 0.735 |
| Gradient boosting | 250.1 | -0.0462 | 0.509 | 0.968 |

Forecast for the next session:

```
  P(up) | Logistic regression      63.1%
  P(up) | Gradient boosting        71.1%
  P(up) | historical base rate     53.9%
  expected return (ridge)          +1.33%
  80% range low                    -3.50%
  80% range high                   +6.42%
  daily volatility                 +3.82%
```

Best out-of-sample AUC **0.532**; smallest p-value against a naive baseline 0.234, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![ETN feature effects](forecast_ETN.png)

### TSLA

Walk-forward test on 550 unseen days (2024-08-26 to 2026-11-03).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.502 | 0.502 | 0.517 | 0.457 | 0.25 | 0.751 | 0.752 |
| Logistic regression | 0.496 | 0.502 | 0.617 | 0.514 | 0.253 | 0.725 | 0.752 |
| Gradient boosting | 0.524 | 0.502 | 0.163 | 0.53 | 0.261 | 0.619 | 0.752 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 366.3 | 0.0 |  |  |
| Ridge regression | 371.2 | -0.0268 | 0.496 | 0.966 |
| Gradient boosting | 373.7 | -0.041 | 0.524 | 0.938 |

Forecast for the next session:

```
  P(up) | Logistic regression      58.4%
  P(up) | Gradient boosting        52.9%
  P(up) | historical base rate     50.6%
  expected return (ridge)          +0.63%
  80% range low                    -2.39%
  80% range high                   +3.74%
  daily volatility                 +2.38%
```

Best out-of-sample AUC **0.530**; smallest p-value against a naive baseline 0.163, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![TSLA feature effects](forecast_TSLA.png)

### AMZN

Walk-forward test on 550 unseen days (2024-08-26 to 2026-11-03).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.516 | 0.516 | 0.517 | 0.463 | 0.25 | 0.728 | 0.728 |
| Logistic regression | 0.547 | 0.516 | 0.079 | 0.561 | 0.248 | 0.993 | 0.728 |
| Gradient boosting | 0.529 | 0.516 | 0.29 | 0.532 | 0.261 | 0.416 | 0.728 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 212.2 | 0.0 |  |  |
| Ridge regression | 213.9 | -0.0155 | 0.531 | 0.856 |
| Gradient boosting | 220.4 | -0.0783 | 0.515 | 0.999 |

Forecast for the next session:

```
  P(up) | Logistic regression      44.7%
  P(up) | Gradient boosting        42.5%
  P(up) | historical base rate     51.3%
  expected return (ridge)          -0.10%
  80% range low                    -3.42%
  80% range high                   +3.34%
  daily volatility                 +2.64%
```

Best out-of-sample AUC **0.561**; smallest p-value against a naive baseline 0.079, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![AMZN feature effects](forecast_AMZN.png)

## 6. Stock screen and entry plans

| ticker | rank | score | passes_filters | close | momentum_12_1 | momentum_6m | volatility | off_52w_high | forward_pe | pullback_entry | breakout_trigger | stop | stop_% | shares | position_$ | max_loss_$ | filter_notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 1 | +0.95 | True | 488.78 | +150.1% | +16.0% | +59.6% | -24.7% | 30.0 | 457.58 | 621.92 | 395.18 | -13.6% | 16 | 7321.0 | 998.0 |  |
| LLY | 2 | +0.51 | True | 1417.99 | +29.9% | +44.1% | +30.3% | +0.0% | 28.3 | 1283.46 | 1420.83 | 1194.51 | -6.9% | 7 | 8984.0 | 623.0 |  |
| V | 3 | +0.50 | True | 436.57 | +10.9% | +37.5% | +21.1% | +0.0% | 25.5 | 404.63 | 437.44 | 388.14 | -4.1% | 24 | 9711.0 | 396.0 |  |
| XOM | 4 | +0.49 | True | 169.27 | +48.8% | +15.4% | +27.2% | -9.6% | 14.1 | 168.49 | 187.62 | 159.35 | -5.4% | 59 | 9941.0 | 539.0 |  |
| MSFT | 5 | +0.47 | True | 555.80 | +3.2% | +34.8% | +25.6% | +0.0% | 23.0 | 530.96 | 556.91 | 501.29 | -5.6% | 18 | 9557.0 | 534.0 |  |
| KO | 6 | +0.44 | True | 95.80 | +30.1% | +22.4% | +17.3% | -0.0% | 27.2 | 92.5 | 96.02 | 89.1 | -3.7% | 108 | 9990.0 | 368.0 |  |
| JNJ | 7 | +0.42 | True | 276.32 | +39.9% | +24.3% | +24.5% | -0.8% | 23.8 | 265.53 | 276.87 | 251.71 | -5.2% | 37 | 9825.0 | 511.0 |  |
| AAPL | 8 | +0.38 | True | 349.51 | +24.5% | +21.8% | +21.8% | +0.0% | 32.8 | 342.91 | 350.21 | 325.86 | -5.0% | 29 | 9944.0 | 495.0 |  |
| JPM | 9 | +0.27 | True | 352.11 | +9.2% | +12.9% | +18.0% | -3.1% | 13.8 | 341.64 | 352.81 | 328.12 | -4.0% | 29 | 9908.0 | 392.0 |  |
| UNH | 10 | +0.13 | True | 409.38 | +15.7% | +12.8% | +22.9% | -5.6% | 17.6 | 402.84 | 425.83 | 378.99 | -5.9% | 24 | 9668.0 | 572.0 |  |
| LIN | 11 | +0.02 | True | 524.74 | +20.5% | +5.2% | +15.9% | -3.7% | 26.9 | 502.6 | 525.79 | 484.96 | -3.5% | 19 | 9549.0 | 335.0 |  |
| PG | 12 | +0.01 | True | 167.32 | +2.5% | +14.7% | +20.4% | +0.0% | 22.6 | 158.13 | 167.65 | 151.8 | -4.0% | 63 | 9962.0 | 399.0 |  |
| AMT | 13 | -0.16 | True | 194.86 | -2.9% | +10.4% | +29.2% | +0.0% | 27.8 | 183.59 | 195.25 | 172.19 | -6.2% | 54 | 9914.0 | 615.0 |  |
| AMZN | 14 | -0.23 | True | 266.03 | +0.9% | -3.3% | +30.9% | -6.3% | 24.4 | 254.13 | 266.56 | 236.97 | -6.7% | 39 | 9911.0 | 669.0 |  |
| COST | 15 | -0.28 | True | 1046.47 | +1.3% | +5.4% | +19.8% | -4.1% | 41.8 | 991.97 | 1048.56 | 954.13 | -3.8% | 10 | 9920.0 | 378.0 |  |

## 7. Portfolio construction

Not included: SKHY (only 83 trading days of history, needs 252); SPCX (only 101 trading days of history, needs 252).

Assets: ALAB, AMD, NVDA, MRVL, GOOG, FSLR, ETN, TSLA, AMZN, JPM, XOM, UNH, COST, TLT, GLD. Covariance: Ledoit-Wolf shrinkage on the last 252 trading days.

Weights and share of risk (%):

| asset | weight: Equal weight | weight: Inverse volatility | weight: Risk parity | weight: Minimum variance | risk share: Equal weight | risk share: Inverse volatility | risk share: Risk parity | risk share: Minimum variance |
|---|---|---|---|---|---|---|---|---|
| ALAB | 6.7 | 2.3 | 1.8 | 0.0 | 21.8 | 9.5 | 6.8 | 0.0 |
| AMD | 6.7 | 3.2 | 2.1 | 0.0 | 15.7 | 10.7 | 6.8 | 0.0 |
| NVDA | 6.7 | 5.8 | 4.9 | 5.8 | 6.6 | 8.9 | 7.2 | 6.7 |
| MRVL | 6.7 | 2.7 | 2.0 | 0.0 | 18.2 | 10.0 | 6.8 | 0.0 |
| GOOG | 6.7 | 6.5 | 5.3 | 4.2 | 4.1 | 7.7 | 7.0 | 4.8 |
| FSLR | 6.7 | 4.2 | 3.3 | 0.2 | 8.4 | 8.5 | 6.9 | 0.3 |
| ETN | 6.7 | 5.2 | 4.0 | 3.1 | 8.6 | 9.9 | 7.1 | 3.6 |
| TSLA | 6.7 | 4.9 | 3.6 | 0.6 | 8.0 | 9.5 | 6.9 | 0.7 |
| AMZN | 6.7 | 6.4 | 5.1 | 3.9 | 4.3 | 7.8 | 7.0 | 4.5 |
| JPM | 6.7 | 9.3 | 9.4 | 9.6 | 1.8 | 5.9 | 7.4 | 11.0 |
| XOM | 6.7 | 7.9 | 0.0 | 18.7 | -1.7 | -2.8 | -0.0 | 21.5 |
| UNH | 6.7 | 6.3 | 7.7 | 3.2 | 1.2 | 3.4 | 7.1 | 3.7 |
| COST | 6.7 | 10.2 | 22.1 | 17.8 | -1.2 | -0.8 | 7.7 | 20.4 |
| TLT | 6.7 | 17.5 | 22.3 | 30.0 | 0.5 | 3.9 | 8.2 | 19.5 |
| GLD | 6.7 | 7.5 | 6.3 | 2.9 | 3.7 | 7.9 | 7.1 | 3.3 |

| method | expected volatility | diversification ratio | effective number of bets | largest risk share | largest risk holder |
|---|---|---|---|---|---|
| Equal weight | 23.1% | 1.86 | 7.34 | 21.8% | ALAB |
| Inverse volatility | 14.4% | 2.30 | 11.16 | 10.7% | AMD |
| Risk parity | 12.6% | 2.35 | 13.96 | 8.2% | TLT |
| Minimum variance | 8.3% | 2.88 | 6.64 | 21.5% | XOM |

Out-of-sample comparison, monthly rebalance (2025-03-25 to 2026-11-04):

| method | CAGR | Volatility | Sharpe | Max drawdown |
|---|---|---|---|---|
| Equal weight | +43.6% | +24.9% | 1.58 | -14.1% |
| Inverse volatility | +31.7% | +17.0% | 1.71 | -10.7% |
| Risk parity | +26.3% | +13.4% | 1.80 | -8.4% |
| Minimum variance | +16.2% | +9.8% | 1.59 | -6.4% |

![Correlations](portfolio_correlation.png)

![Risk shares](portfolio_risk_shares.png)

![Walk-forward](portfolio_walk_forward.png)

## 8. Opening gaps: do pre-market moves carry into the day?

Across 10,865 stock-days (11 watchlist stocks, 2021-11-08 to 2026-11-04), each 1% of opening gap went with a -0.03% move from the open to the close (95% block-bootstrap CI [-0.08%, +0.03%]): no reliable relationship, so the size of a gap has not told you which way the session goes.

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 458 | -5.2% | +0.31% | 49% |
| down 1-3% | 1811 | -1.7% | +0.04% | 52% |
| within 1% | 6032 | +0.0% | +0.01% | 50% |
| up 1-3% | 2033 | +1.7% | +0.08% | 52% |
| gap up 3%+ | 531 | +5.4% | -0.26% | 46% |

## 9. Deciding before the open vs at the previous close

From 2022-02-02 to 2026-11-03 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +39.1% a year (worst drawdown -30.6%) against +43.1% (-30.6%) for labels set at the previous close; the two agreed on 89% of stock-weeks. Sharpe ratio difference -0.10 (95% block-bootstrap CI [-0.38, +0.14]): deciding before the open has been **not distinguishable from deciding on the previous close**.

| strategy | CAGR | Volatility | Sharpe | Max drawdown |
|---|---|---|---|---|
| Board on the previous close | +43.1% | 33.1% | 1.25 | -30.6% |
| Board on the pre-market price | +39.1% | 33.7% | 1.15 | -30.6% |
| Equal-weight watchlist | +33.7% | 37.7% | 0.96 | -42.3% |

The pre-market version uses the official opening price as a stand-in for the last pre-market trade (free pre-market history is only days long), which slightly flatters it.
