# stocklab report
Generated 2026-11-04 | data source: `yahoo` | history: 5 years | watchlist: ALAB, AMD, NVDA, MRVL, GOOG, FSLR, SKHY, ETN, TSLA, SPCX

> Educational research code, not investment advice. Past results do not predict future returns.

## 1. Decision board

Data as of the 2026-11-03 close. `*` = provisional (under 200 trading days of history).

| ticker | action | close | 1 day | 1 month | buy rank | sell warnings | pullback entry | breakout | stop | why |
|---|---|---|---|---|---|---|---|---|---|---|
| NVDA | WATCH | 206.69 | +2.3% | -13.5% | 3/10 | 5/15 | 200.27 | 237.94 | 187.42 | +1% vs 200-day average; below 50-day, MACD bearish, distribution days, below chandelier stop |
| TSLA | WATCH | 398.50 | -1.3% | +5.2% | 6/10 | 3/15 | 382.84 | 408.27 | 356.04 | +4% vs 200-day average; death cross, distribution days |
| AMD | REDUCE | 483.90 | +3.7% | -23.4% | 1/10 | 6/15 |  |  |  | +17% vs 200-day average; below 50-day, MACD bearish, distribution days, 20%+ off high, below chandelier stop |
| MRVL | REDUCE | 171.97 | +0.3% | -36.6% | 2/10 | 8/15 |  |  |  | -7% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, below chandelier stop |
| ETN | REDUCE | 391.70 | +7.0% | -9.5% | 4/10 | 7/15 |  |  |  | -1% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, below chandelier stop |
| ALAB | REDUCE | 233.62 | +1.7% | -35.5% | 5/10 | 8/15 |  |  |  | -9% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, below chandelier stop |
| SKHY | REDUCE* | 150.79 | +2.1% | -22.7% | 8/10 | 5/10 |  |  |  | -11% vs 50-day average; below 50-day, distribution days, 20%+ off high, below chandelier stop (provisional: 82 days of history) |
| SPCX | REDUCE* | 141.31 | +3.6% | -17.4% | 9/10 | 5/10 |  |  |  | -6% vs 50-day average; below 50-day, MACD bearish, 20%+ off high, below chandelier stop (provisional: 100 days of history) |
| FSLR | REDUCE | 185.90 | +2.1% | +5.5% | 10/10 | 7/15 |  |  |  | -14% vs 200-day average; below 50-day, below 200-day, death cross, distribution days, 20%+ off high |
| GOOG | SELL | 278.27 | +0.1% | -19.1% | 7/10 | 11/15 |  |  |  | -18% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |

![Board label each week](board_history.png)

**Trading the labels** (2022-01-31 to 2026-11-03): buy on BUY, exit on SELL, REDUCE or AVOID, reviewed weekly with next-day execution and 5 bp costs.

| strategy | CAGR | Volatility | Sharpe | Max drawdown | Time invested | Avg holdings |
|---|---|---|---|---|---|---|
| Board strategy | +32.5% | 35.2% | 0.98 | -36.8% | 89% | 3.2 |
| Equal-weight watchlist | +37.9% | 38.4% | 1.03 | -41.5% | 100% | 7.6 |
| SPY (buy & hold) | +12.9% | 17.2% | 0.79 | -22.1% |  |  |

Sharpe difference vs equal weight: -0.05, 95% block-bootstrap CI [-0.68, +0.56].

Forward 21-day return after each label, relative to the watchlist average on the same date (sampled every 21 days, t-test across dates):

| label | observations | dates | mean 21d excess return | hit rate | p_value |
|---|---|---|---|---|---|
| BUY | 114 | 46 | +0.5% | 61% | 0.62 |
| HOLD | 56 | 34 | -0.8% | 47% | 0.71 |
| WATCH | 82 | 40 | +1.2% | 40% | 0.54 |
| AVOID | 26 | 15 | -0.4% | 67% | 0.85 |
| REDUCE | 84 | 37 | -1.1% | 38% | 0.32 |
| SELL | 58 | 24 | -2.5% | 42% | 0.24 |

![Board strategy vs holding](board_equity.png)

## 2. Sell check, stock by stock

```
ALAB  REDUCE  (score 8/15, close 233.62 on 2026-11-03)
  RSI 33 | -51.6% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    Chandelier stop            330.17  (price is below, -29.2%)
    50-day SMA                 306.13  (price is below, -23.7%)
    200-day SMA                255.77  (price is below, -8.7%)
```

```
AMD  REDUCE  (score 6/15, close 483.90 on 2026-11-03)
  RSI 38 | -25.5% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    Chandelier stop            566.52  (price is below, -14.6%)
    50-day SMA                 548.70  (price is below, -11.8%)
    200-day SMA                412.94  (price is above, +17.2%)
```

```
NVDA  WATCH  (score 5/15, close 206.69 on 2026-11-03)
  RSI 39 | -13.6% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    Chandelier stop            224.10  (price is below, -7.8%)
    50-day SMA                 221.41  (price is below, -6.6%)
    200-day SMA                204.27  (price is above, +1.2%)
```

```
MRVL  REDUCE  (score 8/15, close 171.97 on 2026-11-03)
  RSI 29 | -45.6% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    Chandelier stop            247.83  (price is below, -30.6%)
    50-day SMA                 240.12  (price is below, -28.4%)
    200-day SMA                184.04  (price is below, -6.6%)
```

```
GOOG  EXIT  (score 11/15, close 278.27 on 2026-11-03)
  RSI 21 | -30.2% from 52-week high
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
    200-day SMA                337.86  (price is below, -17.6%)
    50-day SMA                 333.09  (price is below, -16.5%)
    Chandelier stop            325.56  (price is below, -14.5%)
```

```
FSLR  REDUCE  (score 7/15, close 185.90 on 2026-11-03)
  RSI 56 | -41.6% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
  Levels to watch:
    200-day SMA                215.32  (price is below, -13.7%)
    50-day SMA                 187.62  (price is below, -0.9%)
    Chandelier stop            165.83  (price is above, +12.1%)
```

```
SKHY  REDUCE  (score 5/10, close 150.79 on 2026-11-03)
  RSI 46 | -24.1% from high since listing
  Only 82 trading days of history; not scored yet: below_sma200, death_cross, volatility_spike
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the high since listing (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 168.49  (price is below, -10.5%)
    Chandelier stop            168.24  (price is below, -10.4%)
```

```
ETN  REDUCE  (score 7/15, close 391.70 on 2026-11-03)
  RSI 48 | -14.8% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 409.73  (price is below, -4.4%)
    200-day SMA                396.09  (price is below, -1.1%)
    Chandelier stop            395.60  (price is below, -1.0%)
```

```
TSLA  WATCH  (score 3/15, close 398.50 on 2026-11-03)
  RSI 59 | -18.7% from 52-week high
  Triggered:
    - [trend] 50-day average below the 200-day average (+2)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
  Levels to watch:
    200-day SMA                384.93  (price is above, +3.5%)
    Chandelier stop            374.02  (price is above, +6.5%)
    50-day SMA                 371.41  (price is above, +7.3%)
```

```
SPCX  REDUCE  (score 5/10, close 141.31 on 2026-11-03)
  RSI 44 | -33.2% from high since listing
  Only 100 trading days of history; not scored yet: below_sma200, death_cross, volatility_spike
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [momentum] MACD line below its signal line (+1)
    - [risk] 20%+ below the high since listing (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    Chandelier stop            154.17  (price is below, -8.3%)
    50-day SMA                 149.68  (price is below, -5.6%)
```

## 3. Which sell signals actually work? (event study)

Panel: 40 stocks, 5 years. Null hypothesis: returns after a signal look like returns on random days from the same stocks.

| rule | horizon | events | mean_after_signal | mean_random_days | difference | p_value | q_value | drop10_after_signal | drop10_base_rate | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| below_sma50 | 5d | 942 | +0.32% | +0.64% | -0.31% | 0.044 | 0.304 | 37% | 35% | weak (not significant) |
| below_sma50 | 21d | 920 | +2.56% | +2.82% | -0.27% | 0.251 | 0.517 | 37% | 35% | weak (not significant) |
| below_sma50 | 63d | 881 | +8.62% | +9.34% | -0.73% | 0.177 | 0.393 | 37% | 35% | weak (not significant) |
| below_sma200 | 5d | 454 | +0.21% | +0.55% | -0.34% | 0.091 | 0.335 | 38% | 35% | weak (not significant) |
| below_sma200 | 21d | 441 | +1.52% | +2.40% | -0.88% | 0.064 | 0.304 | 38% | 35% | weak (not significant) |
| below_sma200 | 63d | 422 | +8.37% | +8.02% | +0.35% | 0.625 | 0.952 | 38% | 35% | no edge |
| death_cross | 5d | 137 | -0.20% | +0.57% | -0.77% | 0.057 | 0.304 | 48% | 35% | weak (not significant) |
| death_cross | 21d | 132 | +0.43% | +2.52% | -2.08% | 0.020 | 0.225 | 48% | 35% | weak (not significant) |
| death_cross | 63d | 126 | +10.06% | +8.57% | +1.48% | 0.774 | 0.971 | 48% | 35% | no edge |
| rsi_divergence | 5d | 434 | +0.34% | +0.73% | -0.39% | 0.077 | 0.317 | 37% | 35% | weak (not significant) |
| rsi_divergence | 21d | 431 | +2.63% | +3.30% | -0.67% | 0.116 | 0.383 | 37% | 35% | weak (not significant) |
| rsi_divergence | 63d | 425 | +8.64% | +11.10% | -2.47% | 0.016 | 0.225 | 37% | 35% | weak (not significant) |
| rsi_rollover | 5d | 553 | +1.62% | +0.72% | +0.90% | 1.000 | 1.000 | 33% | 35% | no edge |
| rsi_rollover | 21d | 541 | +3.25% | +3.23% | +0.02% | 0.524 | 0.865 | 33% | 35% | no edge |
| rsi_rollover | 63d | 533 | +8.39% | +10.99% | -2.60% | 0.003 | 0.115 | 33% | 35% | weak (not significant) |
| macd_bearish | 5d | 1424 | +0.61% | +0.66% | -0.05% | 0.360 | 0.625 | 35% | 35% | weak (not significant) |
| macd_bearish | 21d | 1398 | +3.10% | +2.94% | +0.16% | 0.692 | 0.952 | 35% | 35% | no edge |
| macd_bearish | 63d | 1340 | +10.38% | +9.88% | +0.49% | 0.795 | 0.971 | 35% | 35% | no edge |
| distribution_cluster | 5d | 942 | +0.97% | +0.66% | +0.31% | 0.941 | 1.000 | 34% | 35% | no edge |
| distribution_cluster | 21d | 923 | +2.78% | +3.00% | -0.22% | 0.303 | 0.588 | 34% | 35% | weak (not significant) |
| distribution_cluster | 63d | 894 | +9.70% | +10.07% | -0.37% | 0.329 | 0.603 | 34% | 35% | weak (not significant) |
| high_volume_breakdown | 5d | 638 | +0.71% | +0.61% | +0.09% | 0.673 | 0.952 | 33% | 35% | no edge |
| high_volume_breakdown | 21d | 625 | +3.48% | +2.72% | +0.76% | 0.946 | 1.000 | 33% | 35% | no edge |
| high_volume_breakdown | 63d | 609 | +11.45% | +9.10% | +2.35% | 0.996 | 1.000 | 33% | 35% | no edge |
| drawdown_20 | 5d | 334 | +0.99% | +0.74% | +0.25% | 0.768 | 0.971 | 48% | 35% | no edge |
| drawdown_20 | 21d | 323 | +2.65% | +3.38% | -0.72% | 0.178 | 0.393 | 48% | 35% | weak (not significant) |
| drawdown_20 | 63d | 310 | +13.47% | +11.48% | +1.99% | 0.894 | 1.000 | 48% | 35% | no edge |
| volatility_spike | 5d | 280 | +0.31% | +0.68% | -0.38% | 0.136 | 0.393 | 44% | 35% | weak (not significant) |
| volatility_spike | 21d | 278 | +2.34% | +3.09% | -0.76% | 0.173 | 0.393 | 44% | 35% | weak (not significant) |
| volatility_spike | 63d | 276 | +8.14% | +10.28% | -2.14% | 0.064 | 0.304 | 44% | 35% | weak (not significant) |
| chandelier_stop | 5d | 1183 | +0.50% | +0.66% | -0.16% | 0.163 | 0.393 | 35% | 35% | weak (not significant) |
| chandelier_stop | 21d | 1162 | +3.10% | +2.94% | +0.17% | 0.679 | 0.952 | 35% | 35% | no edge |
| chandelier_stop | 63d | 1111 | +11.15% | +9.83% | +1.32% | 0.969 | 1.000 | 35% | 35% | no edge |

**0 of 33 rule-by-horizon tests** show significantly weaker returns after the signal (q < 0.10).

![Sell signal event study](sell_event_study.png)

## 4. Strategy backtests

Not included: SKHY (only 82 trading days of history, needs 452); SPCX (only 100 trading days of history, needs 452).

### ALAB (2025-01-03 to 2026-11-03)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +62.6% | +30.5% | -63.2% | +95.9% | 0.76 | 0 | 100% |  |  |  |
| 50/200 SMA cross | -64.3% | -43.1% | -66.7% | +86.2% | -0.22 | 2 | 75% | -0.98 | [-1.97, -0.26] | 0.03 |
| Close > 50-day SMA | +7.6% | +4.1% | -66.4% | +70.4% | 0.41 | 10 | 52% | -0.35 | [-1.34, +0.62] | 0.48 |
| MACD > signal | +14.8% | +7.9% | -70.4% | +65.6% | 0.44 | 21 | 50% | -0.32 | [-1.49, +0.89] | 0.59 |
| RSI 30/70 | -2.2% | -1.2% | -50.3% | +35.9% | 0.14 | 1 | 16% | -0.61 | [-2.21, +1.31] | 0.44 |
| Trailing stop 20% | -11.8% | -6.7% | -69.1% | +72.4% | 0.27 | 10 | 57% | -0.49 | [-1.49, +0.45] | 0.31 |
| Volume breakout | +91.8% | +42.9% | -55.7% | +63.6% | 0.88 | 4 | 42% | +0.12 | [-1.03, +1.15] | 0.84 |

### AMD (2022-08-22 to 2026-11-03)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +422.9% | +48.5% | -63.0% | +57.2% | 0.97 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +353.7% | +43.5% | -39.1% | +47.1% | 1.00 | 1 | 65% | +0.03 | [-0.56, +0.61] | 0.93 |
| Close > 50-day SMA | +169.9% | +26.8% | -41.8% | +43.9% | 0.76 | 37 | 54% | -0.22 | [-0.80, +0.37] | 0.45 |
| MACD > signal | +343.0% | +42.7% | -42.4% | +41.4% | 1.06 | 39 | 50% | +0.09 | [-0.50, +0.66] | 0.75 |
| RSI 30/70 | +30.3% | +6.5% | -54.7% | +31.3% | 0.36 | 3 | 33% | -0.62 | [-1.64, +0.39] | 0.23 |
| Trailing stop 20% | +214.7% | +31.5% | -58.9% | +48.6% | 0.80 | 10 | 71% | -0.17 | [-0.65, +0.31] | 0.50 |
| Volume breakout | +177.7% | +27.6% | -36.9% | +37.1% | 0.84 | 10 | 38% | -0.13 | [-0.91, +0.58] | 0.73 |

### NVDA (2022-08-22 to 2026-11-03)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +1107.1% | +81.3% | -37.3% | +49.0% | 1.46 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +698.3% | +64.2% | -28.4% | +42.7% | 1.37 | 1 | 83% | -0.08 | [-0.59, +0.48] | 0.74 |
| Close > 50-day SMA | +310.5% | +40.1% | -39.1% | +39.4% | 1.05 | 39 | 70% | -0.41 | [-0.92, +0.08] | 0.12 |
| MACD > signal | +152.9% | +24.8% | -46.7% | +34.4% | 0.81 | 40 | 51% | -0.64 | [-1.30, +0.05] | 0.06 |
| RSI 30/70 | +64.6% | +12.6% | -22.6% | +18.2% | 0.74 | 2 | 7% | -0.72 | [-1.74, +0.20] | 0.15 |
| Trailing stop 20% | +663.2% | +62.5% | -36.6% | +44.4% | 1.31 | 7 | 88% | -0.14 | [-0.48, +0.20] | 0.38 |
| Volume breakout | +211.5% | +31.2% | -19.8% | +26.3% | 1.16 | 7 | 31% | -0.30 | [-1.13, +0.48] | 0.47 |

### MRVL (2022-08-22 to 2026-11-03)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +238.2% | +33.8% | -60.8% | +66.5% | 0.77 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +67.4% | +13.1% | -65.2% | +56.4% | 0.50 | 2 | 67% | -0.27 | [-0.80, +0.17] | 0.27 |
| Close > 50-day SMA | +57.3% | +11.4% | -51.5% | +53.0% | 0.46 | 37 | 58% | -0.30 | [-0.89, +0.26] | 0.29 |
| MACD > signal | +101.6% | +18.2% | -62.5% | +50.2% | 0.58 | 44 | 51% | -0.19 | [-0.86, +0.51] | 0.59 |
| RSI 30/70 | +79.1% | +14.9% | -32.1% | +26.8% | 0.65 | 2 | 19% | -0.11 | [-1.11, +0.99] | 0.84 |
| Trailing stop 20% | +78.2% | +14.8% | -53.3% | +56.7% | 0.52 | 15 | 76% | -0.24 | [-0.73, +0.23] | 0.32 |
| Volume breakout | +76.0% | +14.5% | -46.2% | +42.0% | 0.53 | 11 | 36% | -0.24 | [-1.16, +0.55] | 0.57 |

### GOOG (2022-08-22 to 2026-11-03)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +144.6% | +23.8% | -30.2% | +31.8% | 0.83 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +151.5% | +24.6% | -29.4% | +25.9% | 0.98 | 2 | 76% | +0.15 | [-0.38, +0.64] | 0.59 |
| Close > 50-day SMA | +88.4% | +16.3% | -22.2% | +23.6% | 0.76 | 36 | 63% | -0.07 | [-0.78, +0.66] | 0.85 |
| MACD > signal | +36.1% | +7.6% | -18.1% | +21.5% | 0.45 | 42 | 50% | -0.38 | [-1.15, +0.37] | 0.31 |
| RSI 30/70 | +26.9% | +5.9% | -20.4% | +18.0% | 0.41 | 4 | 25% | -0.43 | [-1.29, +0.52] | 0.31 |
| Trailing stop 20% | +59.3% | +11.8% | -40.4% | +29.7% | 0.52 | 6 | 92% | -0.31 | [-0.73, +0.04] | 0.13 |
| Volume breakout | +105.6% | +18.8% | -17.4% | +19.4% | 0.98 | 8 | 46% | +0.15 | [-0.70, +0.96] | 0.70 |

### FSLR (2022-08-22 to 2026-11-03)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +62.4% | +12.3% | -60.0% | +55.0% | 0.48 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +22.9% | +5.1% | -51.1% | +41.8% | 0.32 | 4 | 60% | -0.16 | [-0.76, +0.38] | 0.57 |
| Close > 50-day SMA | +59.8% | +11.8% | -46.8% | +40.3% | 0.48 | 28 | 50% | -0.01 | [-0.57, +0.54] | 0.99 |
| MACD > signal | -56.0% | -17.8% | -74.1% | +40.4% | -0.29 | 48 | 49% | -0.77 | [-1.46, -0.17] | 0.02 |
| RSI 30/70 | +30.1% | +6.5% | -42.8% | +30.4% | 0.35 | 2 | 27% | -0.13 | [-1.17, +0.72] | 0.78 |
| Trailing stop 20% | +42.9% | +8.9% | -52.3% | +45.2% | 0.41 | 11 | 69% | -0.07 | [-0.57, +0.41] | 0.78 |
| Volume breakout | -16.5% | -4.2% | -53.8% | +32.1% | 0.03 | 13 | 37% | -0.45 | [-1.34, +0.33] | 0.28 |

### ETN (2022-08-22 to 2026-11-03)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +183.1% | +28.2% | -34.5% | +33.3% | 0.91 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +85.2% | +15.9% | -32.8% | +29.6% | 0.65 | 2 | 82% | -0.27 | [-0.73, +0.11] | 0.21 |
| Close > 50-day SMA | +27.2% | +5.9% | -37.5% | +24.6% | 0.36 | 46 | 66% | -0.56 | [-1.15, +0.03] | 0.06 |
| MACD > signal | +37.3% | +7.9% | -25.8% | +22.4% | 0.45 | 48 | 50% | -0.46 | [-1.11, +0.18] | 0.16 |
| RSI 30/70 | +15.7% | +3.6% | -18.6% | +11.5% | 0.36 | 1 | 5% | -0.55 | [-1.46, +0.58] | 0.27 |
| Trailing stop 20% | +168.4% | +26.6% | -23.6% | +31.0% | 0.92 | 2 | 95% | +0.00 | [-0.18, +0.24] | 0.98 |
| Volume breakout | +21.6% | +4.8% | -29.3% | +18.1% | 0.35 | 10 | 38% | -0.56 | [-1.36, +0.18] | 0.15 |

### TSLA (2022-08-22 to 2026-11-03)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +34.4% | +7.3% | -65.0% | +57.9% | 0.41 | 0 | 100% |  |  |  |
| 50/200 SMA cross | -26.4% | -7.1% | -56.8% | +40.1% | 0.01 | 4 | 47% | -0.39 | [-1.26, +0.41] | 0.36 |
| Close > 50-day SMA | +61.4% | +12.1% | -41.1% | +38.0% | 0.49 | 42 | 53% | +0.08 | [-0.67, +0.88] | 0.82 |
| MACD > signal | +452.6% | +50.4% | -39.8% | +40.4% | 1.21 | 41 | 50% | +0.80 | [+0.17, +1.46] | 0.02 |
| RSI 30/70 | +54.7% | +11.0% | -52.7% | +39.7% | 0.46 | 4 | 42% | +0.05 | [-0.70, +0.79] | 0.90 |
| Trailing stop 20% | +37.0% | +7.8% | -47.9% | +44.5% | 0.39 | 11 | 71% | -0.02 | [-0.61, +0.66] | 0.96 |
| Volume breakout | +40.5% | +8.5% | -35.4% | +25.7% | 0.44 | 9 | 18% | +0.03 | [-0.97, +0.96] | 0.94 |

![Strategy equity curves](backtest_equity.png)

## 5. Next-day forecasts

Not included: SKHY (only 82 trading days of history, needs 452); SPCX (only 100 trading days of history, needs 452).

### ALAB

Walk-forward test on 207 unseen days (2026-01-07 to 2026-11-02).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.527 | 0.527 | 0.528 | 0.456 | 0.25 | 0.914 | 0.915 |
| Logistic regression | 0.493 | 0.527 | 0.852 | 0.482 | 0.259 | 0.34 | 0.915 |
| Gradient boosting | 0.469 | 0.527 | 0.959 | 0.439 | 0.287 | 0.356 | 0.915 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 633.6 | 0.0 |  |  |
| Ridge regression | 653.4 | -0.0634 | 0.473 | 0.967 |
| Gradient boosting | 668.2 | -0.1122 | 0.449 | 0.993 |

Forecast for the next session:

```
  P(up) | Logistic regression      56.2%
  P(up) | Gradient boosting        37.1%
  P(up) | historical base rate     52.1%
  expected return (ridge)          +1.21%
  80% range low                    -6.30%
  80% range high                   +9.33%
  daily volatility                 +6.02%
```

Best out-of-sample AUC **0.482**: no reliable edge: treat the forecast as close to a coin flip.

![ALAB feature effects](forecast_ALAB.png)

### AMD

Walk-forward test on 550 unseen days (2024-08-23 to 2026-11-02).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.507 | 0.527 | 0.837 | 0.489 | 0.25 | 1.13 | 1.139 |
| Logistic regression | 0.478 | 0.527 | 0.991 | 0.484 | 0.256 | 0.496 | 1.139 |
| Gradient boosting | 0.473 | 0.527 | 0.995 | 0.48 | 0.269 | 0.078 | 1.139 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 390.4 | 0.0 |  |  |
| Ridge regression | 394.7 | -0.0219 | 0.485 | 0.902 |
| Gradient boosting | 399.9 | -0.0488 | 0.473 | 0.994 |

Forecast for the next session:

```
  P(up) | Logistic regression      58.3%
  P(up) | Gradient boosting        67.2%
  P(up) | historical base rate     51.2%
  expected return (ridge)          +0.95%
  80% range low                    -4.83%
  80% range high                   +7.09%
  daily volatility                 +4.60%
```

Best out-of-sample AUC **0.484**: no reliable edge: treat the forecast as close to a coin flip.

![AMD feature effects](forecast_AMD.png)

### NVDA

Walk-forward test on 550 unseen days (2024-08-23 to 2026-11-02).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.524 | 0.524 | 0.517 | 0.499 | 0.25 | 0.709 | 0.71 |
| Logistic regression | 0.522 | 0.524 | 0.551 | 0.527 | 0.252 | 0.644 | 0.71 |
| Gradient boosting | 0.516 | 0.524 | 0.65 | 0.494 | 0.266 | 0.528 | 0.71 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 279.0 | 0.0 |  |  |
| Ridge regression | 280.5 | -0.011 | 0.518 | 0.661 |
| Gradient boosting | 284.8 | -0.0419 | 0.533 | 0.928 |

Forecast for the next session:

```
  P(up) | Logistic regression      57.4%
  P(up) | Gradient boosting        68.8%
  P(up) | historical base rate     53.8%
  expected return (ridge)          +0.10%
  80% range low                    -2.45%
  80% range high                   +2.71%
  daily volatility                 +2.01%
```

Best out-of-sample AUC **0.527**: no reliable edge: treat the forecast as close to a coin flip.

![NVDA feature effects](forecast_NVDA.png)

### MRVL

Walk-forward test on 550 unseen days (2024-08-23 to 2026-11-02).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.536 | 0.536 | 0.517 | 0.485 | 0.249 | 0.908 | 0.908 |
| Logistic regression | 0.542 | 0.536 | 0.416 | 0.551 | 0.251 | 1.275 | 0.908 |
| Gradient boosting | 0.527 | 0.536 | 0.681 | 0.544 | 0.262 | 0.888 | 0.908 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 473.0 | 0.0 |  |  |
| Ridge regression | 474.3 | -0.0051 | 0.524 | 0.632 |
| Gradient boosting | 481.1 | -0.0342 | 0.491 | 0.96 |

Forecast for the next session:

```
  P(up) | Logistic regression      65.2%
  P(up) | Gradient boosting        61.3%
  P(up) | historical base rate     52.6%
  expected return (ridge)          +1.08%
  80% range low                    -6.40%
  80% range high                   +9.15%
  daily volatility                 +6.00%
```

Best out-of-sample AUC **0.551**: a small edge out of sample; still check the p-values before trusting it.

![MRVL feature effects](forecast_MRVL.png)

### GOOG

Walk-forward test on 550 unseen days (2024-08-23 to 2026-11-02).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.52 | 0.52 | 0.517 | 0.492 | 0.25 | 0.901 | 0.901 |
| Logistic regression | 0.553 | 0.52 | 0.068 | 0.534 | 0.253 | 0.432 | 0.901 |
| Gradient boosting | 0.542 | 0.52 | 0.163 | 0.536 | 0.261 | 0.599 | 0.901 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 201.0 | 0.0 |  |  |
| Ridge regression | 204.1 | -0.0304 | 0.522 | 0.988 |
| Gradient boosting | 209.0 | -0.0807 | 0.513 | 0.999 |

Forecast for the next session:

```
  P(up) | Logistic regression      59.2%
  P(up) | Gradient boosting        62.7%
  P(up) | historical base rate     52.8%
  expected return (ridge)          +0.20%
  80% range low                    -3.62%
  80% range high                   +4.16%
  daily volatility                 +3.03%
```

Best out-of-sample AUC **0.536**: a small edge out of sample; still check the p-values before trusting it.

![GOOG feature effects](forecast_GOOG.png)

### FSLR

Walk-forward test on 550 unseen days (2024-08-23 to 2026-11-02).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.515 | 0.515 | 0.517 | 0.449 | 0.25 |  | 0.115 |
| Logistic regression | 0.507 | 0.515 | 0.65 | 0.527 | 0.251 | -0.114 | 0.115 |
| Gradient boosting | 0.507 | 0.515 | 0.65 | 0.523 | 0.26 | 0.207 | 0.115 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 363.0 | 0.0 |  |  |
| Ridge regression | 363.6 | -0.0034 | 0.504 | 0.613 |
| Gradient boosting | 372.2 | -0.0515 | 0.504 | 0.993 |

Forecast for the next session:

```
  P(up) | Logistic regression      59.2%
  P(up) | Gradient boosting        64.5%
  P(up) | historical base rate     49.2%
  expected return (ridge)          +0.87%
  80% range low                    -2.05%
  80% range high                   +3.88%
  daily volatility                 +2.30%
```

Best out-of-sample AUC **0.527**: no reliable edge: treat the forecast as close to a coin flip.

![FSLR feature effects](forecast_FSLR.png)

### ETN

Walk-forward test on 550 unseen days (2024-08-23 to 2026-11-02).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.524 | 0.524 | 0.517 | 0.477 | 0.25 | 0.542 | 0.542 |
| Logistic regression | 0.509 | 0.524 | 0.766 | 0.504 | 0.255 | 0.622 | 0.542 |
| Gradient boosting | 0.529 | 0.524 | 0.416 | 0.53 | 0.258 | 0.654 | 0.542 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 240.5 | 0.0 |  |  |
| Ridge regression | 241.5 | -0.008 | 0.505 | 0.676 |
| Gradient boosting | 245.7 | -0.0433 | 0.502 | 0.961 |

Forecast for the next session:

```
  P(up) | Logistic regression      52.2%
  P(up) | Gradient boosting        45.1%
  P(up) | historical base rate     53.9%
  expected return (ridge)          +0.29%
  80% range low                    -3.82%
  80% range high                   +4.57%
  daily volatility                 +3.26%
```

Best out-of-sample AUC **0.530**: a small edge out of sample; still check the p-values before trusting it.

![ETN feature effects](forecast_ETN.png)

### TSLA

Walk-forward test on 550 unseen days (2024-08-23 to 2026-11-02).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.502 | 0.502 | 0.517 | 0.453 | 0.25 | 0.752 | 0.753 |
| Logistic regression | 0.509 | 0.502 | 0.383 | 0.514 | 0.252 | 1.069 | 0.753 |
| Gradient boosting | 0.515 | 0.502 | 0.29 | 0.515 | 0.266 | 0.804 | 0.753 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 366.3 | 0.0 |  |  |
| Ridge regression | 370.8 | -0.025 | 0.502 | 0.956 |
| Gradient boosting | 374.1 | -0.0435 | 0.525 | 0.942 |

Forecast for the next session:

```
  P(up) | Logistic regression      51.2%
  P(up) | Gradient boosting        33.5%
  P(up) | historical base rate     50.7%
  expected return (ridge)          +0.44%
  80% range low                    -2.40%
  80% range high                   +3.37%
  daily volatility                 +2.24%
```

Best out-of-sample AUC **0.515**: no reliable edge: treat the forecast as close to a coin flip.

![TSLA feature effects](forecast_TSLA.png)

## 6. Stock screen and entry plans

| ticker | rank | score | passes_filters | close | momentum_12_1 | momentum_6m | volatility | off_52w_high | forward_pe | pullback_entry | breakout_trigger | stop | stop_% | shares | position_$ | max_loss_$ | filter_notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 1 | +1.07 | True | 483.90 | +146.7% | +36.2% | +59.7% | -25.5% | 29.7 | 453.23 | 647.15 | 391.9 | -13.5% | 16 | 7252.0 | 981.0 |  |
| XOM | 2 | +0.53 | True | 177.46 | +47.6% | +16.1% | +25.7% | -5.2% | 14.8 | 177.41 | 187.62 | 169.12 | -4.7% | 56 | 9935.0 | 464.0 |  |
| LLY | 3 | +0.52 | True | 1409.38 | +33.3% | +43.0% | +30.5% | -0.6% | 28.1 | 1272.0 | 1420.38 | 1183.03 | -7.0% | 7 | 8904.0 | 623.0 |  |
| V | 4 | +0.47 | True | 420.42 | +9.4% | +31.1% | +19.9% | -1.2% | 24.5 | 401.4 | 426.36 | 386.16 | -3.8% | 24 | 9634.0 | 366.0 |  |
| KO | 5 | +0.45 | True | 94.80 | +28.9% | +22.3% | +17.3% | -1.1% | 26.9 | 92.0 | 96.02 | 88.68 | -3.6% | 108 | 9936.0 | 359.0 |  |
| MSFT | 6 | +0.42 | True | 520.99 | +2.3% | +27.2% | +22.7% | -4.1% | 21.5 | 514.06 | 544.54 | 487.97 | -5.1% | 19 | 9767.0 | 496.0 |  |
| JNJ | 7 | +0.37 | True | 266.17 | +36.9% | +19.3% | +23.4% | -4.4% | 22.9 | 265.47 | 275.75 | 252.31 | -5.0% | 37 | 9822.0 | 487.0 |  |
| AAPL | 8 | +0.35 | True | 331.90 | +23.6% | +17.0% | +19.3% | -4.9% | 31.2 | 324.46 | 349.61 | 309.57 | -4.6% | 30 | 9734.0 | 447.0 |  |
| NVDA | 9 | +0.32 | True | 206.69 | +18.3% | +5.4% | +34.7% | -13.6% | 13.0 | 200.27 | 237.94 | 187.42 | -6.4% | 49 | 9813.0 | 629.0 |  |
| JPM | 10 | +0.25 | True | 337.98 | +8.4% | +10.3% | +16.0% | -7.0% | 13.2 | 335.53 | 344.27 | 323.18 | -3.7% | 29 | 9730.0 | 358.0 |  |
| UNH | 11 | +0.11 | True | 404.44 | +13.8% | +12.5% | +23.2% | -6.7% | 17.4 | 401.17 | 425.83 | 379.11 | -5.5% | 24 | 9628.0 | 529.0 |  |
| PG | 12 | -0.02 | True | 162.06 | -0.8% | +13.4% | +19.5% | -1.5% | 21.9 | 157.11 | 164.83 | 151.23 | -3.7% | 63 | 9898.0 | 370.0 |  |
| LIN | 13 | -0.02 | True | 511.55 | +16.9% | +2.9% | +15.1% | -6.1% | 26.2 | 500.57 | 520.76 | 483.87 | -3.3% | 19 | 9511.0 | 317.0 |  |
| AMT | 14 | -0.20 | True | 187.29 | -5.7% | +7.3% | +28.4% | -1.5% | 26.7 | 182.15 | 189.35 | 171.22 | -6.0% | 54 | 9836.0 | 590.0 |  |
| AMZN | 15 | -0.26 | True | 250.69 | +2.9% | -8.4% | +28.4% | -11.7% | 23.0 | 243.05 | 263.16 | 227.78 | -6.3% | 41 | 9965.0 | 626.0 |  |

## 7. Portfolio construction

Not included: SKHY (only 82 trading days of history, needs 252); SPCX (only 100 trading days of history, needs 252).

Assets: ALAB, AMD, NVDA, MRVL, GOOG, FSLR, ETN, TSLA, JPM, XOM, UNH, COST, TLT, GLD. Covariance: Ledoit-Wolf shrinkage on the last 252 trading days.

Weights and share of risk (%):

| asset | weight: Equal weight | weight: Inverse volatility | weight: Risk parity | weight: Minimum variance | risk share: Equal weight | risk share: Inverse volatility | risk share: Risk parity | risk share: Minimum variance |
|---|---|---|---|---|---|---|---|---|
| ALAB | 7.1 | 2.4 | 1.6 | 0.0 | 23.0 | 10.3 | 7.1 | 0.0 |
| AMD | 7.1 | 3.4 | 2.0 | 0.0 | 16.6 | 11.6 | 7.1 | 0.0 |
| NVDA | 7.1 | 6.2 | 4.5 | 6.1 | 6.9 | 9.6 | 7.1 | 7.0 |
| MRVL | 7.1 | 2.9 | 1.7 | 0.0 | 19.2 | 11.0 | 7.1 | 0.0 |
| GOOG | 7.1 | 7.0 | 5.9 | 6.2 | 3.9 | 7.3 | 7.1 | 7.1 |
| FSLR | 7.1 | 4.5 | 3.1 | 0.4 | 8.7 | 9.1 | 7.1 | 0.5 |
| ETN | 7.1 | 5.7 | 3.5 | 3.4 | 8.9 | 11.0 | 7.1 | 3.9 |
| TSLA | 7.1 | 5.2 | 3.4 | 0.7 | 8.2 | 10.1 | 7.1 | 0.9 |
| JPM | 7.1 | 10.1 | 8.3 | 10.1 | 1.9 | 6.4 | 7.1 | 11.7 |
| XOM | 7.1 | 8.5 | 17.0 | 18.3 | -1.6 | -2.4 | 7.1 | 21.1 |
| UNH | 7.1 | 6.7 | 6.7 | 3.3 | 1.2 | 3.8 | 7.1 | 3.8 |
| COST | 7.1 | 10.9 | 16.8 | 18.5 | -1.3 | -0.9 | 7.1 | 21.3 |
| TLT | 7.1 | 18.6 | 20.3 | 30.0 | 0.5 | 4.3 | 7.1 | 19.4 |
| GLD | 7.1 | 8.0 | 5.3 | 3.0 | 3.9 | 8.7 | 7.1 | 3.4 |

| method | expected volatility | diversification ratio | effective number of bets | largest risk share | largest risk holder |
|---|---|---|---|---|---|
| Equal weight | 23.8% | 1.82 | 6.75 | 23.0% | ALAB |
| Inverse volatility | 14.3% | 2.30 | 10.30 | 11.6% | AMD |
| Risk parity | 10.3% | 2.83 | 14.00 | 7.1% | TLT |
| Minimum variance | 8.3% | 2.82 | 6.45 | 21.3% | COST |

Out-of-sample comparison, monthly rebalance (2025-03-25 to 2026-11-03):

| method | CAGR | Volatility | Sharpe | Max drawdown |
|---|---|---|---|---|
| Equal weight | +46.0% | +25.3% | 1.63 | -14.2% |
| Inverse volatility | +32.7% | +16.8% | 1.77 | -10.2% |
| Risk parity | +26.9% | +13.4% | 1.85 | -8.2% |
| Minimum variance | +16.2% | +9.8% | 1.59 | -6.2% |

![Correlations](portfolio_correlation.png)

![Risk shares](portfolio_risk_shares.png)

![Walk-forward](portfolio_walk_forward.png)

## 8. Opening gaps: do pre-market moves carry into the day?

Across 9,609 stock-days (10 watchlist stocks, 2021-11-05 to 2026-11-03), each 1% of opening gap went with a -0.02% move from the open to the close (95% block-bootstrap CI [-0.08%, +0.04%]): no reliable relationship, so the size of a gap has not told you which way the session goes.

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 426 | -5.2% | +0.28% | 49% |
| down 1-3% | 1650 | -1.7% | +0.04% | 53% |
| within 1% | 5173 | +0.0% | +0.02% | 50% |
| up 1-3% | 1858 | +1.7% | +0.08% | 52% |
| gap up 3%+ | 502 | +5.3% | -0.24% | 46% |
