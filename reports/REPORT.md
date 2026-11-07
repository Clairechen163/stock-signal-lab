# stocklab report
Generated 2026-11-07 | data source: `yahoo` | history: 5 years | watchlist: ALAB, AMD, NVDA, MRVL, GOOG, FSLR, SKHY, ETN, TSLA, SPCX, AMZN, IBM, GEV, CEG, VST

> Educational research code, not investment advice. Past results do not predict future returns.

## 1. Decision board

Data as of the 2026-11-06 close. `*` = provisional (under 200 trading days of history).

| ticker | action | close | 1 day | 1 month | buy rank | sell warnings | pullback entry | breakout | stop | why |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | BUY | 259.30 | -0.3% | +2.1% | 2/8 | 1/15 | 254.28 | 266.56 | 235.90 | buy rank 2/8; +6% vs 200-day average; distribution days |
| FSLR | AVOID | 201.14 | +2.7% | +12.5% | 8/8 | 5/15 |  |  |  | -6% vs 200-day average; below 200-day, death cross, 20%+ off high |
| AMD | REDUCE | 449.04 | +11.0% | -27.7% | 1/8 | 7/15 |  |  |  | +8% vs 200-day average; below 50-day, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| IBM | REDUCE | 245.00 | -0.9% | +8.1% | 4/8 | 6/15 |  |  |  | -0% vs 200-day average; below 200-day, death cross, MACD bearish, 20%+ off high |
| NVDA | REDUCE | 186.64 | +2.8% | -19.0% | 5/8 | 8/15 |  |  |  | -9% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, below chandelier stop |
| MRVL | SELL | 141.20 | +5.7% | -48.6% | 3/8 | 9/15 |  |  |  | -24% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| ALAB | SELL | 179.47 | -19.6% | -53.0% | 6/8 | 10/15 |  |  |  | -30% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, high-volume breakdown, 20%+ off high, below chandelier stop |
| GEV | SELL | 770.51 | -7.5% | -22.7% | 8/8 | 12/15 |  |  |  | -19% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, high-volume breakdown, 20%+ off high, below chandelier stop |
| GOOG | SELL | 281.74 | -1.9% | -18.9% | 9/8 | 13/15 |  |  |  | -17% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, high-volume breakdown, 20%+ off high, volatility spike, below chandelier stop |
| ETN | SELL | 341.72 | +4.5% | -19.5% | 6/8 | 9/15 |  |  |  | -14% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| SPCX | SELL* | 123.62 | -9.0% | -26.2% | 11/8 | 8/10 |  |  |  | -17% vs 50-day average; below 50-day, MACD bearish, distribution days, high-volume breakdown, 20%+ off high, below chandelier stop (provisional: 102 days of history) |
| CEG | SELL | 239.65 | -2.5% | -20.0% | 13/8 | 12/15 |  |  |  | -14% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, high-volume breakdown, 20%+ off high, below chandelier stop |
| TSLA | SELL | 358.22 | +4.2% | -4.5% | 7/8 | 10/15 |  |  |  | -7% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, 20%+ off high, below chandelier stop |
| VST | SELL | 112.89 | -6.2% | -32.3% | 14/8 | 13/15 |  |  |  | -26% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, high-volume breakdown, 20%+ off high, volatility spike, below chandelier stop |
| SKHY | SELL* | 123.90 | -13.4% | -30.5% | 15/8 | 8/10 |  |  |  | -26% vs 50-day average; below 50-day, MACD bearish, distribution days, high-volume breakdown, 20%+ off high, below chandelier stop (provisional: 84 days of history) |

![Board label each week](board_history.png)

**Trading the labels** (2022-02-02 to 2026-11-06): buy on BUY, exit on SELL, REDUCE or AVOID, reviewed weekly with next-day execution and 5 bp costs.

| strategy | CAGR | Volatility | Sharpe | Max drawdown | Time invested | Avg holdings |
|---|---|---|---|---|---|---|
| Board strategy | +37.0% | 31.4% | 1.16 | -29.5% | 97% | 5.4 |
| Equal-weight watchlist | +37.4% | 33.1% | 1.13 | -37.1% | 100% | 12.0 |
| SPY (buy & hold) | +12.6% | 17.3% | 0.77 | -22.1% |  |  |

Sharpe difference vs equal weight: +0.04, 95% block-bootstrap CI [-0.43, +0.51].

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
ALAB  EXIT  (score 10/15, close 179.47 on 2026-11-05)
  RSI 25 | -62.8% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [volume] Down day closing below the 50-day average on 1.5x+ average volume (+2)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    Chandelier stop            311.63  (price is below, -42.4%)
    50-day SMA                 302.73  (price is below, -40.7%)
    200-day SMA                255.99  (price is below, -29.9%)
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
GOOG  EXIT  (score 13/15, close 281.74 on 2026-11-05)
  RSI 28 | -29.3% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [volume] Down day closing below the 50-day average on 1.5x+ average volume (+2)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    200-day SMA                337.46  (price is below, -16.5%)
    50-day SMA                 330.83  (price is below, -14.8%)
    Chandelier stop            322.70  (price is below, -12.7%)
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
SKHY  EXIT  (score 8/10, close 123.90 on 2026-11-05)
  RSI 34 | -37.6% from high since listing
  Only 84 trading days of history; not scored yet: below_sma200, death_cross, volatility_spike
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [volume] Down day closing below the 50-day average on 1.5x+ average volume (+2)
    - [risk] 20%+ below the high since listing (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 167.47  (price is below, -26.0%)
    Chandelier stop            150.64  (price is below, -17.7%)
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
SPCX  EXIT  (score 8/10, close 123.62 on 2026-11-05)
  RSI 33 | -41.5% from high since listing
  Only 102 trading days of history; not scored yet: below_sma200, death_cross, volatility_spike
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [volume] Down day closing below the 50-day average on 1.5x+ average volume (+2)
    - [risk] 20%+ below the high since listing (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 149.31  (price is below, -17.2%)
    Chandelier stop            147.17  (price is below, -16.0%)
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
GEV  EXIT  (score 12/15, close 770.51 on 2026-11-05)
  RSI 35 | -34.4% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [volume] Down day closing below the 50-day average on 1.5x+ average volume (+2)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    200-day SMA                947.32  (price is below, -18.7%)
    50-day SMA                 926.65  (price is below, -16.8%)
    Chandelier stop            861.45  (price is below, -10.6%)
```

```
CEG  EXIT  (score 12/15, close 239.65 on 2026-11-05)
  RSI 37 | -36.4% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [volume] Down day closing below the 50-day average on 1.5x+ average volume (+2)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    200-day SMA                278.33  (price is below, -13.9%)
    50-day SMA                 270.67  (price is below, -11.5%)
    Chandelier stop            268.22  (price is below, -10.7%)
```

```
VST  EXIT  (score 13/15, close 112.89 on 2026-11-05)
  RSI 29 | -40.6% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [volume] Down day closing below the 50-day average on 1.5x+ average volume (+2)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    200-day SMA                152.46  (price is below, -26.0%)
    50-day SMA                 144.13  (price is below, -21.7%)
    Chandelier stop            144.06  (price is below, -21.6%)
```

## 3. Which sell signals actually work? (event study)

Panel: 44 stocks, 5 years. Null hypothesis: returns after a signal look like returns on random days from the same stocks.

| rule | horizon | events | mean_after_signal | mean_random_days | difference | p_value | q_value | drop10_after_signal | drop10_base_rate | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| below_sma50 | 5d | 1031 | +0.22% | +0.63% | -0.42% | 0.011 | 0.082 | 39% | 35% | useful |
| below_sma50 | 21d | 1005 | +2.41% | +2.86% | -0.46% | 0.105 | 0.348 | 39% | 35% | weak (not significant) |
| below_sma50 | 63d | 961 | +8.44% | +9.55% | -1.10% | 0.062 | 0.256 | 39% | 35% | weak (not significant) |
| below_sma200 | 5d | 486 | -0.00% | +0.54% | -0.55% | 0.011 | 0.082 | 38% | 35% | useful |
| below_sma200 | 21d | 472 | +1.15% | +2.46% | -1.31% | 0.005 | 0.082 | 38% | 35% | useful |
| below_sma200 | 63d | 448 | +8.71% | +8.19% | +0.52% | 0.697 | 0.959 | 38% | 35% | no edge |
| death_cross | 5d | 148 | -0.48% | +0.59% | -1.07% | 0.012 | 0.082 | 44% | 35% | useful |
| death_cross | 21d | 141 | +0.20% | +2.57% | -2.37% | 0.006 | 0.082 | 44% | 35% | useful |
| death_cross | 63d | 135 | +10.74% | +8.76% | +1.99% | 0.847 | 1.000 | 44% | 35% | no edge |
| rsi_divergence | 5d | 473 | +0.45% | +0.72% | -0.27% | 0.167 | 0.426 | 36% | 35% | weak (not significant) |
| rsi_divergence | 21d | 470 | +2.96% | +3.32% | -0.35% | 0.254 | 0.491 | 36% | 35% | weak (not significant) |
| rsi_divergence | 63d | 464 | +9.14% | +11.10% | -1.96% | 0.024 | 0.113 | 36% | 35% | weak (not significant) |
| rsi_rollover | 5d | 615 | +1.79% | +0.70% | +1.09% | 1.000 | 1.000 | 33% | 35% | no edge |
| rsi_rollover | 21d | 604 | +3.37% | +3.23% | +0.14% | 0.603 | 0.948 | 33% | 35% | no edge |
| rsi_rollover | 63d | 592 | +9.04% | +11.04% | -2.00% | 0.015 | 0.085 | 33% | 35% | useful |
| macd_bearish | 5d | 1547 | +0.59% | +0.66% | -0.07% | 0.327 | 0.569 | 35% | 35% | weak (not significant) |
| macd_bearish | 21d | 1519 | +3.06% | +3.01% | +0.05% | 0.570 | 0.941 | 35% | 35% | no edge |
| macd_bearish | 63d | 1451 | +10.46% | +10.04% | +0.42% | 0.748 | 0.987 | 35% | 35% | no edge |
| distribution_cluster | 5d | 1025 | +0.98% | +0.66% | +0.32% | 0.959 | 1.000 | 35% | 35% | no edge |
| distribution_cluster | 21d | 1005 | +2.70% | +3.01% | -0.32% | 0.201 | 0.474 | 35% | 35% | weak (not significant) |
| distribution_cluster | 63d | 970 | +9.57% | +10.14% | -0.57% | 0.225 | 0.491 | 35% | 35% | weak (not significant) |
| high_volume_breakdown | 5d | 720 | +0.71% | +0.61% | +0.10% | 0.677 | 0.959 | 34% | 35% | no edge |
| high_volume_breakdown | 21d | 690 | +3.51% | +2.80% | +0.71% | 0.941 | 1.000 | 34% | 35% | no edge |
| high_volume_breakdown | 63d | 671 | +11.61% | +9.34% | +2.27% | 0.991 | 1.000 | 34% | 35% | no edge |
| drawdown_20 | 5d | 375 | +0.88% | +0.73% | +0.15% | 0.686 | 0.959 | 49% | 35% | no edge |
| drawdown_20 | 21d | 365 | +2.34% | +3.40% | -1.06% | 0.072 | 0.266 | 49% | 35% | weak (not significant) |
| drawdown_20 | 63d | 346 | +13.29% | +11.60% | +1.70% | 0.869 | 1.000 | 49% | 35% | no edge |
| volatility_spike | 5d | 314 | +0.35% | +0.67% | -0.32% | 0.162 | 0.426 | 46% | 35% | weak (not significant) |
| volatility_spike | 21d | 309 | +2.66% | +3.11% | -0.46% | 0.268 | 0.491 | 46% | 35% | weak (not significant) |
| volatility_spike | 63d | 307 | +9.16% | +10.42% | -1.26% | 0.168 | 0.426 | 46% | 35% | weak (not significant) |
| chandelier_stop | 5d | 1295 | +0.53% | +0.65% | -0.12% | 0.238 | 0.491 | 36% | 35% | weak (not significant) |
| chandelier_stop | 21d | 1267 | +3.24% | +2.97% | +0.28% | 0.785 | 0.996 | 36% | 35% | no edge |
| chandelier_stop | 63d | 1213 | +11.23% | +10.00% | +1.23% | 0.961 | 1.000 | 36% | 35% | no edge |

**6 of 33 rule-by-horizon tests** show significantly weaker returns after the signal (q < 0.10).

![Sell signal event study](sell_event_study.png)

## 4. Strategy backtests

Not included: SKHY (only 84 trading days of history, needs 452); SPCX (only 102 trading days of history, needs 452).

### ALAB (2025-01-03 to 2026-11-05)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +24.9% | +12.9% | -63.2% | +96.9% | 0.61 | 0 | 100% |  |  |  |
| 50/200 SMA cross | -72.6% | -50.6% | -74.0% | +87.3% | -0.37 | 2 | 75% | -0.98 | [-1.93, -0.25] | 0.02 |
| Close > 50-day SMA | +7.6% | +4.1% | -66.4% | +70.3% | 0.41 | 10 | 52% | -0.20 | [-1.20, +0.82] | 0.70 |
| MACD > signal | +14.8% | +7.8% | -70.4% | +65.5% | 0.44 | 21 | 50% | -0.17 | [-1.38, +1.15] | 0.79 |
| RSI 30/70 | -2.2% | -1.2% | -50.3% | +35.8% | 0.14 | 1 | 16% | -0.47 | [-2.15, +1.45] | 0.57 |
| Trailing stop 20% | -11.8% | -6.6% | -69.1% | +72.2% | 0.27 | 10 | 56% | -0.34 | [-1.32, +0.72] | 0.52 |
| Volume breakout | +91.8% | +42.7% | -55.7% | +63.5% | 0.87 | 4 | 42% | +0.26 | [-0.97, +1.40] | 0.67 |

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

### GOOG (2022-08-24 to 2026-11-05)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +141.5% | +23.4% | -30.2% | +31.8% | 0.82 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +151.5% | +24.6% | -29.4% | +25.9% | 0.98 | 2 | 76% | +0.16 | [-0.38, +0.67] | 0.59 |
| Close > 50-day SMA | +83.9% | +15.7% | -22.2% | +23.6% | 0.73 | 35 | 63% | -0.09 | [-0.83, +0.64] | 0.80 |
| MACD > signal | +36.1% | +7.6% | -18.1% | +21.5% | 0.45 | 42 | 50% | -0.37 | [-1.14, +0.37] | 0.34 |
| RSI 30/70 | +28.5% | +6.2% | -20.4% | +18.1% | 0.42 | 4 | 25% | -0.40 | [-1.27, +0.57] | 0.37 |
| Trailing stop 20% | +55.3% | +11.1% | -40.4% | +29.6% | 0.50 | 6 | 92% | -0.32 | [-0.74, +0.07] | 0.11 |
| Volume breakout | +105.6% | +18.8% | -17.4% | +19.4% | 0.98 | 8 | 46% | +0.16 | [-0.73, +0.96] | 0.71 |

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

### GEV (2025-01-13 to 2026-11-05)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +102.3% | +47.5% | -38.3% | +56.1% | 0.98 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +133.0% | +59.4% | -38.3% | +55.1% | 1.12 | 1 | 98% | +0.15 | [+0.00, +0.43] | 0.43 |
| Close > 50-day SMA | +79.1% | +37.9% | -32.7% | +44.0% | 0.95 | 15 | 64% | -0.02 | [-0.70, +0.61] | 0.94 |
| MACD > signal | +60.7% | +29.9% | -31.0% | +42.2% | 0.83 | 16 | 48% | -0.14 | [-0.95, +0.72] | 0.73 |
| RSI 30/70 | +20.0% | +10.6% | -34.4% | +34.5% | 0.46 | 1 | 31% | -0.51 | [-1.72, +0.60] | 0.41 |
| Trailing stop 20% | +44.2% | +22.4% | -45.9% | +50.3% | 0.65 | 5 | 88% | -0.32 | [-0.91, +0.14] | 0.24 |
| Volume breakout | +24.5% | +12.9% | -24.6% | +33.6% | 0.53 | 3 | 36% | -0.44 | [-1.67, +0.69] | 0.48 |

### CEG (2022-11-02 to 2026-11-05)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +161.6% | +27.2% | -50.7% | +49.1% | 0.73 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +96.8% | +18.5% | -50.7% | +43.6% | 0.60 | 3 | 72% | -0.13 | [-0.60, +0.31] | 0.56 |
| Close > 50-day SMA | +139.1% | +24.4% | -40.9% | +37.4% | 0.77 | 47 | 57% | +0.03 | [-0.56, +0.61] | 0.92 |
| MACD > signal | +25.6% | +5.9% | -41.5% | +37.0% | 0.34 | 41 | 49% | -0.40 | [-1.05, +0.27] | 0.23 |
| RSI 30/70 | +77.3% | +15.4% | -28.6% | +31.8% | 0.61 | 3 | 37% | -0.13 | [-0.94, +0.69] | 0.76 |
| Trailing stop 20% | +82.3% | +16.2% | -52.8% | +43.8% | 0.56 | 8 | 84% | -0.17 | [-0.62, +0.27] | 0.40 |
| Volume breakout | +86.0% | +16.8% | -30.0% | +30.7% | 0.66 | 9 | 39% | -0.08 | [-0.78, +0.67] | 0.82 |

### VST (2022-08-24 to 2026-11-05)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +368.5% | +44.6% | -48.8% | +51.8% | 0.98 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +406.4% | +47.3% | -48.8% | +44.1% | 1.10 | 3 | 69% | +0.13 | [-0.25, +0.58] | 0.57 |
| Close > 50-day SMA | +45.4% | +9.4% | -67.2% | +38.1% | 0.43 | 45 | 64% | -0.54 | [-1.20, +0.12] | 0.09 |
| MACD > signal | +66.6% | +13.0% | -49.0% | +37.2% | 0.52 | 47 | 51% | -0.46 | [-1.13, +0.23] | 0.20 |
| RSI 30/70 | +181.1% | +28.0% | -27.3% | +26.5% | 1.06 | 3 | 20% | +0.09 | [-0.84, +0.97] | 0.84 |
| Trailing stop 20% | +205.7% | +30.6% | -56.3% | +44.7% | 0.83 | 9 | 88% | -0.15 | [-0.61, +0.29] | 0.52 |
| Volume breakout | +278.5% | +37.4% | -31.2% | +31.4% | 1.18 | 9 | 43% | +0.20 | [-0.53, +1.06] | 0.62 |

![Strategy equity curves](backtest_equity.png)

## 5. Next-day forecasts

Not included: SKHY (only 84 trading days of history, needs 452); SPCX (only 102 trading days of history, needs 452).

### ALAB

Walk-forward test on 209 unseen days (2026-01-07 to 2026-11-04).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.522 | 0.522 | 0.528 | 0.453 | 0.25 | 0.606 | 0.607 |
| Logistic regression | 0.488 | 0.522 | 0.85 | 0.484 | 0.259 | -0.017 | 0.607 |
| Gradient boosting | 0.469 | 0.522 | 0.944 | 0.444 | 0.286 | 0.062 | 0.607 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 649.2 | 0.0 |  |  |
| Ridge regression | 669.7 | -0.0641 | 0.469 | 0.975 |
| Gradient boosting | 686.0 | -0.1167 | 0.445 | 0.996 |

Forecast for the next session:

```
  P(up) | Logistic regression      77.9%
  P(up) | Gradient boosting        71.7%
  P(up) | historical base rate     51.8%
  expected return (ridge)          +4.21%
  80% range low                    -4.75%
  80% range high                   +14.01%
  daily volatility                 +7.02%
```

Best out-of-sample AUC **0.484**; smallest p-value against a naive baseline 0.850, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![ALAB feature effects](forecast_ALAB.png)

### AMD

Walk-forward test on 551 unseen days (2024-08-27 to 2026-11-05).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.508 | 0.528 | 0.837 | 0.491 | 0.25 | 1.053 | 1.095 |
| Logistic regression | 0.477 | 0.528 | 0.992 | 0.486 | 0.256 | 0.412 | 1.095 |
| Gradient boosting | 0.47 | 0.528 | 0.997 | 0.479 | 0.269 | 0.055 | 1.095 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 400.6 | 0.0 |  |  |
| Ridge regression | 403.7 | -0.0154 | 0.492 | 0.813 |
| Gradient boosting | 408.7 | -0.0406 | 0.492 | 0.98 |

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
| Gradient boosting | 0.528 | 0.523 | 0.416 | 0.485 | 0.268 | 0.853 | 0.61 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 282.1 | 0.0 |  |  |
| Ridge regression | 284.0 | -0.0131 | 0.506 | 0.692 |
| Gradient boosting | 288.8 | -0.0474 | 0.543 | 0.931 |

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

Best out-of-sample AUC **0.521**; smallest p-value against a naive baseline 0.416, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![NVDA feature effects](forecast_NVDA.png)

### MRVL

Walk-forward test on 551 unseen days (2024-08-27 to 2026-11-05).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.535 | 0.535 | 0.517 | 0.488 | 0.249 | 0.806 | 0.806 |
| Logistic regression | 0.534 | 0.535 | 0.551 | 0.549 | 0.252 | 0.641 | 0.806 |
| Gradient boosting | 0.532 | 0.535 | 0.585 | 0.547 | 0.26 | 0.431 | 0.806 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 480.0 | 0.0 |  |  |
| Ridge regression | 482.1 | -0.009 | 0.519 | 0.725 |
| Gradient boosting | 487.1 | -0.0299 | 0.495 | 0.943 |

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

Walk-forward test on 550 unseen days (2024-08-27 to 2026-11-04).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.52 | 0.52 | 0.517 | 0.483 | 0.25 | 0.926 | 0.926 |
| Logistic regression | 0.545 | 0.52 | 0.125 | 0.533 | 0.253 | 0.388 | 0.926 |
| Gradient boosting | 0.524 | 0.52 | 0.449 | 0.528 | 0.263 | 0.727 | 0.926 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 201.6 | 0.0 |  |  |
| Ridge regression | 204.4 | -0.0278 | 0.522 | 0.98 |
| Gradient boosting | 209.1 | -0.076 | 0.524 | 0.999 |

Forecast for the next session:

```
  P(up) | Logistic regression      35.8%
  P(up) | Gradient boosting        43.9%
  P(up) | historical base rate     52.8%
  expected return (ridge)          +0.62%
  80% range low                    -3.35%
  80% range high                   +4.75%
  daily volatility                 +3.14%
```

Best out-of-sample AUC **0.533**; smallest p-value against a naive baseline 0.125, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![GOOG feature effects](forecast_GOOG.png)

### FSLR

Walk-forward test on 551 unseen days (2024-08-27 to 2026-11-05).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.508 | 0.514 | 0.617 | 0.466 | 0.25 | 0.344 | 0.163 |
| Logistic regression | 0.521 | 0.514 | 0.383 | 0.533 | 0.25 | 0.017 | 0.163 |
| Gradient boosting | 0.515 | 0.514 | 0.483 | 0.526 | 0.259 | 0.189 | 0.163 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 363.3 | 0.0 |  |  |
| Ridge regression | 363.6 | -0.0017 | 0.503 | 0.557 |
| Gradient boosting | 374.2 | -0.0609 | 0.51 | 0.998 |

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
| Gradient boosting | 0.543 | 0.525 | 0.209 | 0.527 | 0.259 | 0.513 | 0.393 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 247.2 | 0.0 |  |  |
| Ridge regression | 248.7 | -0.0122 | 0.517 | 0.748 |
| Gradient boosting | 252.7 | -0.0448 | 0.51 | 0.957 |

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
| Gradient boosting | 0.51 | 0.503 | 0.383 | 0.521 | 0.263 | 0.27 | 0.708 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 369.5 | 0.0 |  |  |
| Ridge regression | 374.2 | -0.0256 | 0.495 | 0.958 |
| Gradient boosting | 375.8 | -0.0344 | 0.534 | 0.91 |

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

Best out-of-sample AUC **0.521**; smallest p-value against a naive baseline 0.383, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![TSLA feature effects](forecast_TSLA.png)

### AMZN

Walk-forward test on 551 unseen days (2024-08-27 to 2026-11-05).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.515 | 0.515 | 0.517 | 0.463 | 0.25 | 0.711 | 0.711 |
| Logistic regression | 0.55 | 0.515 | 0.057 | 0.56 | 0.248 | 1.067 | 0.711 |
| Gradient boosting | 0.519 | 0.515 | 0.449 | 0.53 | 0.261 | 0.355 | 0.711 |

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
| Gradient boosting | 259.4 | -0.0491 | 0.539 | 0.999 |

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

Walk-forward test on 204 unseen days (2026-01-14 to 2026-11-04).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.529 | 0.529 | 0.528 | 0.469 | 0.25 | 0.684 | 0.685 |
| Logistic regression | 0.5 | 0.529 | 0.819 | 0.492 | 0.259 | 0.379 | 0.685 |
| Gradient boosting | 0.529 | 0.529 | 0.528 | 0.533 | 0.268 | 1.049 | 0.685 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 336.8 | 0.0 |  |  |
| Ridge regression | 343.3 | -0.0392 | 0.549 | 0.818 |
| Gradient boosting | 347.3 | -0.0633 | 0.534 | 0.863 |

Forecast for the next session:

```
  P(up) | Logistic regression      79.3%
  P(up) | Gradient boosting        80.6%
  P(up) | historical base rate     54.2%
  expected return (ridge)          +3.65%
  80% range low                    -2.27%
  80% range high                   +9.92%
  daily volatility                 +4.59%
```

Best out-of-sample AUC **0.533**; smallest p-value against a naive baseline 0.528, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![GEV feature effects](forecast_GEV.png)

### CEG

Walk-forward test on 503 unseen days (2024-11-01 to 2026-11-04).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.503 | 0.503 | 0.518 | 0.476 | 0.251 | 0.225 | 0.225 |
| Logistic regression | 0.469 | 0.503 | 0.941 | 0.49 | 0.26 | -0.18 | 0.225 |
| Gradient boosting | 0.471 | 0.503 | 0.929 | 0.467 | 0.274 | -0.409 | 0.225 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 354.4 | 0.0 |  |  |
| Ridge regression | 362.7 | -0.0471 | 0.479 | 0.992 |
| Gradient boosting | 366.7 | -0.0703 | 0.527 | 0.997 |

Forecast for the next session:

```
  P(up) | Logistic regression      66.3%
  P(up) | Gradient boosting        52.7%
  P(up) | historical base rate     52.0%
  expected return (ridge)          +1.92%
  80% range low                    -2.18%
  80% range high                   +6.19%
  daily volatility                 +3.20%
```

Best out-of-sample AUC **0.490**; smallest p-value against a naive baseline 0.929, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![CEG feature effects](forecast_CEG.png)

### VST

Walk-forward test on 550 unseen days (2024-08-27 to 2026-11-04).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.516 | 0.516 | 0.517 | 0.496 | 0.25 | 0.539 | 0.54 |
| Logistic regression | 0.485 | 0.516 | 0.932 | 0.482 | 0.26 | 0.982 | 0.54 |
| Gradient boosting | 0.551 | 0.516 | 0.057 | 0.553 | 0.257 | 1.326 | 0.54 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 392.7 | 0.0 |  |  |
| Ridge regression | 395.7 | -0.0152 | 0.487 | 0.766 |
| Gradient boosting | 399.0 | -0.0325 | 0.505 | 0.919 |

Forecast for the next session:

```
  P(up) | Logistic regression      68.0%
  P(up) | Gradient boosting        81.2%
  P(up) | historical base rate     52.7%
  expected return (ridge)          +1.78%
  80% range low                    -4.38%
  80% range high                   +8.33%
  daily volatility                 +4.87%
```

Best out-of-sample AUC **0.553**; smallest p-value against a naive baseline 0.057, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![VST feature effects](forecast_VST.png)

## 6. Stock screen and entry plans

| ticker | rank | score | passes_filters | close | momentum_12_1 | momentum_6m | volatility | off_52w_high | forward_pe | pullback_entry | breakout_trigger | stop | stop_% | shares | position_$ | max_loss_$ | filter_notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 1 | +0.75 | True | 449.04 | +142.1% | -1.4% | +73.6% | -30.9% | 26.0 | 412.43 | 606.74 | 339.22 | -17.8% | 13 | 5362.0 | 952.0 |  |
| XOM | 2 | +0.66 | True | 165.87 | +52.5% | +16.3% | +26.3% | -11.4% | 13.4 | 161.13 | 187.62 | 151.65 | -5.9% | 62 | 9990.0 | 588.0 |  |
| V | 3 | +0.58 | True | 422.65 | +11.2% | +33.1% | +21.7% | -3.2% | 24.7 | 408.86 | 437.44 | 390.32 | -4.5% | 24 | 9813.0 | 445.0 |  |
| KO | 4 | +0.57 | True | 95.67 | +31.5% | +23.5% | +17.3% | -0.2% | 27.1 | 93.28 | 96.02 | 89.62 | -3.9% | 107 | 9981.0 | 392.0 |  |
| LLY | 5 | +0.57 | True | 1354.00 | +27.1% | +43.2% | +30.6% | -4.5% | 26.9 | 1301.95 | 1420.83 | 1207.25 | -7.3% | 7 | 9114.0 | 663.0 |  |
| JNJ | 6 | +0.56 | True | 276.22 | +41.0% | +26.1% | +24.7% | -0.8% | 23.8 | 265.79 | 276.87 | 250.96 | -5.6% | 37 | 9834.0 | 549.0 |  |
| MSFT | 7 | +0.56 | True | 530.61 | +3.9% | +28.3% | +26.7% | -4.5% | 21.9 | 516.65 | 556.91 | 485.77 | -6.0% | 19 | 9816.0 | 587.0 |  |
| AAPL | 8 | +0.49 | True | 342.37 | +26.5% | +16.9% | +21.8% | -2.0% | 32.2 | 336.01 | 350.21 | 318.47 | -5.2% | 29 | 9744.0 | 509.0 |  |
| JPM | 9 | +0.35 | True | 334.49 | +8.4% | +11.8% | +19.9% | -7.9% | 13.1 | 326.45 | 352.81 | 310.37 | -4.9% | 30 | 9794.0 | 482.0 |  |
| UNH | 10 | +0.18 | True | 394.15 | +16.2% | +5.0% | +23.8% | -9.1% | 16.9 | 390.17 | 425.83 | 365.46 | -6.3% | 25 | 9754.0 | 618.0 |  |
| PG | 11 | +0.16 | True | 165.40 | +5.6% | +14.6% | +20.5% | -1.1% | 22.4 | 159.77 | 167.65 | 153.04 | -4.2% | 62 | 9906.0 | 417.0 |  |
| LIN | 12 | +0.09 | True | 515.25 | +16.7% | +5.2% | +16.1% | -5.4% | 26.4 | 506.16 | 525.79 | 487.08 | -3.8% | 19 | 9617.0 | 363.0 |  |
| AMT | 13 | -0.05 | True | 188.79 | -3.3% | +9.1% | +29.4% | -3.1% | 26.9 | 185.28 | 195.25 | 174.08 | -6.0% | 53 | 9820.0 | 594.0 |  |
| AMZN | 14 | -0.11 | True | 259.30 | +1.5% | -4.9% | +31.0% | -8.7% | 23.8 | 254.28 | 266.56 | 235.9 | -7.2% | 39 | 9917.0 | 717.0 |  |
| COST | 15 | -0.15 | True | 1053.56 | +1.8% | +4.8% | +20.2% | -3.4% | 42.1 | 1003.33 | 1067.72 | 962.82 | -4.0% | 9 | 9030.0 | 365.0 |  |

## 7. Portfolio construction

Not included: SKHY (only 84 trading days of history, needs 252); SPCX (only 102 trading days of history, needs 252).

Assets: ALAB, AMD, NVDA, MRVL, GOOG, FSLR, ETN, TSLA, AMZN, IBM, GEV, CEG, VST, JPM, XOM, UNH, COST, TLT, GLD. Covariance: Ledoit-Wolf shrinkage on the last 252 trading days.

Weights and share of risk (%):

| asset | weight: Equal weight | weight: Inverse volatility | weight: Risk parity | weight: Minimum variance | risk share: Equal weight | risk share: Inverse volatility | risk share: Risk parity | risk share: Minimum variance |
|---|---|---|---|---|---|---|---|---|
| ALAB | 5.3 | 1.9 | 1.4 | 0.0 | 16.8 | 7.8 | 5.3 | 0.0 |
| AMD | 5.3 | 2.7 | 1.6 | 0.0 | 12.5 | 8.7 | 5.3 | 0.0 |
| NVDA | 5.3 | 4.9 | 3.8 | 4.6 | 5.4 | 7.3 | 5.6 | 5.1 |
| MRVL | 5.3 | 2.3 | 1.5 | 0.0 | 14.0 | 8.0 | 5.3 | 0.0 |
| GOOG | 5.3 | 5.6 | 4.8 | 4.5 | 2.8 | 5.2 | 5.5 | 5.1 |
| FSLR | 5.3 | 3.7 | 2.9 | 0.4 | 6.0 | 6.2 | 5.4 | 0.4 |
| ETN | 5.3 | 4.4 | 2.9 | 1.9 | 7.2 | 8.5 | 5.5 | 2.1 |
| TSLA | 5.3 | 4.2 | 2.8 | 0.0 | 6.4 | 7.6 | 5.4 | 0.0 |
| AMZN | 5.3 | 5.5 | 4.2 | 3.4 | 3.2 | 5.7 | 5.5 | 3.8 |
| IBM | 5.3 | 4.0 | 5.6 | 2.4 | 1.5 | 2.0 | 5.5 | 2.7 |
| GEV | 5.3 | 3.5 | 2.7 | 1.0 | 8.1 | 7.5 | 5.5 | 1.1 |
| CEG | 5.3 | 4.0 | 3.1 | 1.5 | 6.0 | 6.7 | 5.4 | 1.7 |
| VST | 5.3 | 3.7 | 2.8 | 0.2 | 7.2 | 7.3 | 5.4 | 0.2 |
| JPM | 5.3 | 7.9 | 7.3 | 7.6 | 1.6 | 4.7 | 5.7 | 8.5 |
| XOM | 5.3 | 6.8 | 0.0 | 17.9 | -1.2 | -2.1 | -0.0 | 20.0 |
| UNH | 5.3 | 5.4 | 6.9 | 3.1 | 0.8 | 2.2 | 5.6 | 3.5 |
| COST | 5.3 | 8.7 | 22.0 | 17.8 | -1.2 | -1.5 | 6.0 | 19.9 |
| TLT | 5.3 | 14.4 | 17.9 | 30.0 | 0.4 | 2.8 | 6.3 | 22.0 |
| GLD | 5.3 | 6.4 | 5.7 | 3.6 | 2.5 | 5.4 | 5.6 | 4.1 |

| method | expected volatility | diversification ratio | effective number of bets | largest risk share | largest risk holder |
|---|---|---|---|---|---|
| Equal weight | 23.5% | 1.92 | 10.23 | 16.8% | ALAB |
| Inverse volatility | 15.8% | 2.30 | 14.08 | 8.7% | AMD |
| Risk parity | 13.0% | 2.51 | 17.97 | 6.3% | TLT |
| Minimum variance | 8.4% | 2.97 | 6.85 | 22.0% | TLT |

Concentration warnings:

- ETN and GEV have correlation 0.72: they tend to fall together
- CEG and VST have correlation 0.80: they tend to fall together

Out-of-sample comparison, monthly rebalance (2025-04-01 to 2026-11-05):

| method | CAGR | Volatility | Sharpe | Max drawdown |
|---|---|---|---|---|
| Equal weight | +41.5% | +25.7% | 1.48 | -14.7% |
| Inverse volatility | +31.1% | +18.4% | 1.56 | -10.1% |
| Risk parity | +23.2% | +14.6% | 1.50 | -8.6% |
| Minimum variance | +14.4% | +9.9% | 1.40 | -6.6% |

![Correlations](portfolio_correlation.png)

![Risk shares](portfolio_risk_shares.png)

![Walk-forward](portfolio_walk_forward.png)

## 8. Opening gaps: do pre-market moves carry into the day?

Across 15,241 stock-days (15 watchlist stocks, 2021-11-09 to 2026-11-06), each 1% of opening gap went with a -0.03% move from the open to the close (95% block-bootstrap CI [-0.09%, +0.03%]): no reliable relationship, so the size of a gap has not told you which way the session goes.

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 564 | -5.2% | +0.29% | 49% |
| down 1-3% | 2243 | -1.7% | +0.11% | 53% |
| within 1% | 9159 | +0.0% | +0.01% | 50% |
| up 1-3% | 2610 | +1.7% | +0.08% | 51% |
| gap up 3%+ | 665 | +5.3% | -0.23% | 46% |

## 9. Deciding before the open vs at the previous close

From 2022-02-03 to 2026-11-05 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +41.7% a year (worst drawdown -31.8%) against +38.5% (-30.5%) for labels set at the previous close; the two agreed on 90% of stock-weeks. Sharpe ratio difference +0.06 (95% block-bootstrap CI [-0.10, +0.22]): deciding before the open has been **not distinguishable from deciding on the previous close**.

| strategy | CAGR | Volatility | Sharpe | Max drawdown |
|---|---|---|---|---|
| Board on the previous close | +38.5% | 32.1% | 1.17 | -30.5% |
| Board on the pre-market price | +41.7% | 32.5% | 1.24 | -31.8% |
| Equal-weight watchlist | +37.8% | 33.9% | 1.11 | -40.6% |

The pre-market version uses the official opening price as a stand-in for the last pre-market trade (free pre-market history is only days long), which slightly flatters it.
