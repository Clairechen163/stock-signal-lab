# stocklab report
Generated 2026-11-13 | data source: `yahoo` | history: 5 years | watchlist: ALAB, AMD, NVDA, MRVL, GOOG, FSLR, SKHY, ETN, TSLA, SPCX, AMZN, IBM, GEV, CEG, VST, DELL, TSM, BE

> Educational research code, not investment advice. Past results do not predict future returns.

## 1. Decision board

Data as of the 2026-11-12 close. `*` = provisional (under 200 trading days of history).

| ticker | action | close | 1 day | 1 month | buy rank | sell warnings | pullback entry | breakout | stop | why |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | BUY | 585.30 | +5.9% | +2.5% | 2/18 | 2/15 | 552.99 | 586.47 | 472.72 | buy rank 2/18; +39% vs 200-day average; distribution days, volatility spike |
| AMZN | BUY | 267.44 | +0.5% | +5.3% | 5/18 | 1/15 | 256.50 | 271.41 | 237.89 | buy rank 5/18; +9% vs 200-day average; distribution days |
| TSM | WATCH | 405.49 | -1.9% | -5.7% | 4/18 | 3/15 | 388.35 | 440.39 | 354.06 | +1% vs 200-day average; below 50-day, distribution days, volatility spike |
| IBM | WATCH | 244.67 | -1.4% | +8.1% | 6/18 | 4/15 | 236.24 | 257.02 | 222.87 | +0% vs 200-day average; death cross, MACD bearish, 20%+ off high |
| TSLA | WATCH | 397.45 | +1.7% | +8.2% | 13/18 | 4/15 | 383.59 | 408.27 | 350.45 | +4% vs 200-day average; death cross, MACD bearish, distribution days |
| CEG | WATCH | 282.40 | +2.8% | +1.0% | 14/18 | 4/15 | 269.60 | 282.96 | 242.07 | +2% vs 200-day average; death cross, distribution days, 20%+ off high |
| BE | AVOID | 201.93 | -3.6% | -15.6% | 15/18 | 5/15 |  |  |  | -10% vs 200-day average; below 50-day, below 200-day, distribution days, 20%+ off high |
| SKHY | AVOID* | 137.71 | -3.2% | -6.7% | 17/18 | 3/10 |  |  |  | -16% vs 50-day average; below 50-day, distribution days, 20%+ off high (provisional: 89 days of history) |
| DELL | REDUCE | 371.17 | -0.7% | -26.8% | 1/18 | 7/15 |  |  |  | +9% vs 200-day average; below 50-day, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| SPCX | REDUCE* | 139.94 | +0.1% | -8.0% | 7/18 | 5/10 |  |  |  | -6% vs 50-day average; below 50-day, distribution days, 20%+ off high, below chandelier stop (provisional: 107 days of history) |
| ALAB | REDUCE | 227.79 | -1.4% | -24.1% | 9/18 | 8/15 |  |  |  | -11% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, below chandelier stop |
| MRVL | SELL | 164.45 | -2.6% | -33.0% | 3/18 | 9/15 |  |  |  | -12% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| ETN | SELL | 359.04 | -0.4% | -11.9% | 8/18 | 9/15 |  |  |  | -9% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| GOOG | SELL | 295.35 | +1.6% | -14.1% | 10/18 | 10/15 |  |  |  | -12% vs 200-day average; below 50-day, below 200-day, death cross, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| GEV | SELL | 818.49 | +1.3% | -13.0% | 11/18 | 10/15 |  |  |  | -14% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, 20%+ off high, below chandelier stop |
| NVDA | SELL | 166.19 | -4.3% | -24.9% | 12/18 | 10/15 |  |  |  | -19% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, high-volume breakdown, 20%+ off high, below chandelier stop |
| VST | SELL | 134.51 | +0.8% | -11.4% | 16/18 | 11/15 |  |  |  | -11% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| FSLR | SELL | 172.30 | -3.3% | -3.8% | 18/18 | 9/15 |  |  |  | -19% vs 200-day average; below 50-day, below 200-day, death cross, distribution days, 20%+ off high, below chandelier stop |

![Board label each week](board_history.png)

**Trading the labels** (2022-02-09 to 2026-11-12): buy on BUY, exit on SELL, REDUCE or AVOID, reviewed weekly with next-day execution and 5 bp costs.

| strategy | CAGR | Volatility | Sharpe | Max drawdown | Time invested | Avg holdings |
|---|---|---|---|---|---|---|
| Board strategy | +35.5% | 33.4% | 1.08 | -34.0% | 97% | 6.6 |
| Equal-weight watchlist | +44.5% | 34.2% | 1.25 | -36.8% | 100% | 15.0 |
| SPY (buy & hold) | +13.2% | 17.3% | 0.80 | -22.1% |  |  |

Sharpe difference vs equal weight: -0.17, 95% block-bootstrap CI [-0.73, +0.32].

Forward 21-day return after each label, relative to the watchlist average on the same date (sampled every 21 days, t-test across dates):

| label | observations | dates | mean 21d excess return | hit rate | p_value |
|---|---|---|---|---|---|
| BUY | 270 | 55 | +1.1% | 56% | 0.22 |
| HOLD | 124 | 43 | +0.6% | 47% | 0.76 |
| WATCH | 158 | 50 | +1.3% | 58% | 0.23 |
| AVOID | 41 | 17 | -3.3% | 41% | 0.12 |
| REDUCE | 160 | 51 | -0.8% | 43% | 0.59 |
| SELL | 84 | 32 | -2.1% | 44% | 0.18 |

![Board strategy vs holding](board_equity.png)

## 2. Sell check, stock by stock

```
ALAB  REDUCE  (score 8/15, close 227.79 on 2026-11-12)
  RSI 41 | -52.8% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 295.49  (price is below, -22.9%)
    200-day SMA                257.16  (price is below, -11.4%)
    Chandelier stop            246.67  (price is below, -7.7%)
```

```
AMD  HOLD  (score 2/15, close 585.30 on 2026-11-12)
  RSI 57 | -9.9% from 52-week high
  Triggered:
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
  Levels to watch:
    50-day SMA                 552.99  (price is above, +5.8%)
    Chandelier stop            473.58  (price is above, +23.6%)
    200-day SMA                421.71  (price is above, +38.8%)
```

```
NVDA  EXIT  (score 10/15, close 166.19 on 2026-11-12)
  RSI 26 | -30.5% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [volume] Down day closing below the 50-day average on 1.5x+ average volume (+2)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 215.94  (price is below, -23.0%)
    200-day SMA                204.07  (price is below, -18.6%)
    Chandelier stop            196.44  (price is below, -15.4%)
```

```
MRVL  EXIT  (score 9/15, close 164.45 on 2026-11-12)
  RSI 37 | -48.0% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 230.22  (price is below, -28.6%)
    Chandelier stop            212.35  (price is below, -22.6%)
    200-day SMA                186.55  (price is below, -11.8%)
```

```
GOOG  EXIT  (score 10/15, close 295.35 on 2026-11-12)
  RSI 41 | -25.9% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    200-day SMA                336.36  (price is below, -12.2%)
    50-day SMA                 326.04  (price is below, -9.4%)
    Chandelier stop            325.13  (price is below, -9.2%)
```

```
FSLR  EXIT  (score 9/15, close 172.30 on 2026-11-12)
  RSI 41 | -45.9% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    200-day SMA                213.42  (price is below, -19.3%)
    50-day SMA                 185.28  (price is below, -7.0%)
    Chandelier stop            183.77  (price is below, -6.2%)
```

```
SKHY  WATCH  (score 3/10, close 137.71 on 2026-11-12)
  RSI 44 | -30.7% from high since listing
  Only 89 trading days of history; not scored yet: below_sma200, death_cross, volatility_spike
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the high since listing (+1)
  Levels to watch:
    50-day SMA                 164.64  (price is below, -16.4%)
    Chandelier stop            135.40  (price is above, +1.7%)
```

```
ETN  EXIT  (score 9/15, close 359.04 on 2026-11-12)
  RSI 44 | -21.7% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 401.05  (price is below, -10.5%)
    200-day SMA                395.46  (price is below, -9.2%)
    Chandelier stop            367.57  (price is below, -2.3%)
```

```
TSLA  WATCH  (score 4/15, close 397.45 on 2026-11-12)
  RSI 57 | -18.9% from 52-week high
  Triggered:
    - [trend] 50-day average below the 200-day average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
  Levels to watch:
    200-day SMA                382.86  (price is above, +3.8%)
    50-day SMA                 374.46  (price is above, +6.1%)
    Chandelier stop            364.53  (price is above, +9.0%)
```

```
SPCX  REDUCE  (score 5/10, close 139.94 on 2026-11-12)
  RSI 47 | -33.8% from high since listing
  Only 107 trading days of history; not scored yet: below_sma200, death_cross, volatility_spike
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the high since listing (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 149.12  (price is below, -6.2%)
    Chandelier stop            141.37  (price is below, -1.0%)
```

```
AMZN  HOLD  (score 1/15, close 267.44 on 2026-11-12)
  RSI 58 | -5.8% from 52-week high
  Triggered:
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
  Levels to watch:
    50-day SMA                 254.66  (price is above, +5.0%)
    Chandelier stop            247.42  (price is above, +8.1%)
    200-day SMA                244.47  (price is above, +9.4%)
```

```
IBM  WATCH  (score 4/15, close 244.67 on 2026-11-12)
  RSI 52 | -24.6% from 52-week high
  Triggered:
    - [trend] 50-day average below the 200-day average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [risk] 20%+ below the 52-week high (+1)
  Levels to watch:
    200-day SMA                243.47  (price is above, +0.5%)
    Chandelier stop            238.03  (price is above, +2.8%)
    50-day SMA                 236.24  (price is above, +3.6%)
```

```
GEV  EXIT  (score 10/15, close 818.49 on 2026-11-12)
  RSI 43 | -30.3% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    200-day SMA                950.53  (price is below, -13.9%)
    50-day SMA                 915.55  (price is below, -10.6%)
    Chandelier stop            823.97  (price is below, -0.7%)
```

```
CEG  WATCH  (score 4/15, close 282.40 on 2026-11-12)
  RSI 58 | -25.1% from 52-week high
  Triggered:
    - [trend] 50-day average below the 200-day average (+2)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
  Levels to watch:
    200-day SMA                277.92  (price is above, +1.6%)
    50-day SMA                 269.60  (price is above, +4.7%)
    Chandelier stop            253.20  (price is above, +11.5%)
```

```
VST  EXIT  (score 11/15, close 134.51 on 2026-11-12)
  RSI 47 | -25.0% from 52-week high
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
    200-day SMA                151.72  (price is below, -11.3%)
    50-day SMA                 143.39  (price is below, -6.2%)
    Chandelier stop            136.85  (price is below, -1.7%)
```

```
DELL  REDUCE  (score 7/15, close 371.17 on 2026-11-12)
  RSI 39 | -36.8% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 496.46  (price is below, -25.2%)
    Chandelier stop            442.16  (price is below, -16.1%)
    200-day SMA                341.48  (price is above, +8.7%)
```

```
TSM  WATCH  (score 3/15, close 405.49 on 2026-11-12)
  RSI 47 | -16.5% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
  Levels to watch:
    50-day SMA                 430.29  (price is below, -5.8%)
    200-day SMA                401.36  (price is above, +1.0%)
    Chandelier stop            389.45  (price is above, +4.1%)
```

```
BE  WATCH  (score 5/15, close 201.93 on 2026-11-12)
  RSI 46 | -41.6% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
  Levels to watch:
    50-day SMA                 244.92  (price is below, -17.6%)
    200-day SMA                223.35  (price is below, -9.6%)
    Chandelier stop            193.52  (price is above, +4.3%)
```

## 3. Which sell signals actually work? (event study)

Panel: 46 stocks, 5 years. Null hypothesis: returns after a signal look like returns on random days from the same stocks.

| rule | horizon | events | mean_after_signal | mean_random_days | difference | p_value | q_value | drop10_after_signal | drop10_base_rate | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| below_sma50 | 5d | 1075 | +0.35% | +0.70% | -0.35% | 0.030 | 0.192 | 40% | 36% | weak (not significant) |
| below_sma50 | 21d | 1055 | +2.12% | +3.09% | -0.97% | 0.006 | 0.115 | 40% | 36% | weak (not significant) |
| below_sma50 | 63d | 995 | +8.77% | +10.19% | -1.43% | 0.035 | 0.192 | 40% | 36% | weak (not significant) |
| below_sma200 | 5d | 520 | +0.60% | +0.63% | -0.03% | 0.476 | 0.952 | 39% | 36% | weak (not significant) |
| below_sma200 | 21d | 498 | +1.28% | +2.75% | -1.46% | 0.007 | 0.115 | 39% | 36% | weak (not significant) |
| below_sma200 | 63d | 472 | +9.48% | +9.17% | +0.31% | 0.613 | 1.000 | 39% | 36% | no edge |
| death_cross | 5d | 155 | +0.68% | +0.66% | +0.02% | 0.519 | 0.952 | 43% | 36% | no edge |
| death_cross | 21d | 148 | +0.80% | +2.86% | -2.07% | 0.025 | 0.192 | 43% | 36% | weak (not significant) |
| death_cross | 63d | 142 | +14.81% | +9.76% | +5.06% | 0.986 | 1.000 | 43% | 36% | no edge |
| rsi_divergence | 5d | 502 | +0.43% | +0.78% | -0.35% | 0.110 | 0.390 | 37% | 36% | weak (not significant) |
| rsi_divergence | 21d | 495 | +3.26% | +3.52% | -0.26% | 0.329 | 0.835 | 37% | 36% | weak (not significant) |
| rsi_divergence | 63d | 487 | +10.96% | +11.79% | -0.83% | 0.244 | 0.672 | 37% | 36% | weak (not significant) |
| rsi_rollover | 5d | 644 | +1.84% | +0.76% | +1.08% | 1.000 | 1.000 | 33% | 36% | no edge |
| rsi_rollover | 21d | 634 | +3.70% | +3.44% | +0.26% | 0.689 | 1.000 | 33% | 36% | no edge |
| rsi_rollover | 63d | 620 | +10.41% | +11.63% | -1.22% | 0.118 | 0.390 | 33% | 36% | weak (not significant) |
| macd_bearish | 5d | 1623 | +0.88% | +0.72% | +0.15% | 0.842 | 1.000 | 35% | 36% | no edge |
| macd_bearish | 21d | 1602 | +3.24% | +3.24% | +0.00% | 0.515 | 0.952 | 35% | 36% | no edge |
| macd_bearish | 63d | 1520 | +11.57% | +10.79% | +0.78% | 0.876 | 1.000 | 35% | 36% | no edge |
| distribution_cluster | 5d | 1078 | +0.53% | +0.73% | -0.20% | 0.130 | 0.390 | 37% | 36% | weak (not significant) |
| distribution_cluster | 21d | 1062 | +2.53% | +3.25% | -0.72% | 0.042 | 0.198 | 37% | 36% | weak (not significant) |
| distribution_cluster | 63d | 1021 | +9.93% | +10.85% | -0.92% | 0.124 | 0.390 | 37% | 36% | weak (not significant) |
| high_volume_breakdown | 5d | 768 | +0.86% | +0.69% | +0.17% | 0.790 | 1.000 | 35% | 36% | no edge |
| high_volume_breakdown | 21d | 732 | +3.69% | +3.04% | +0.65% | 0.907 | 1.000 | 35% | 36% | no edge |
| high_volume_breakdown | 63d | 703 | +12.66% | +10.19% | +2.46% | 0.996 | 1.000 | 35% | 36% | no edge |
| drawdown_20 | 5d | 409 | +1.53% | +0.85% | +0.69% | 0.967 | 1.000 | 51% | 36% | no edge |
| drawdown_20 | 21d | 397 | +2.32% | +3.76% | -1.44% | 0.032 | 0.192 | 51% | 36% | weak (not significant) |
| drawdown_20 | 63d | 374 | +14.11% | +12.86% | +1.25% | 0.781 | 1.000 | 51% | 36% | no edge |
| volatility_spike | 5d | 342 | +0.93% | +0.75% | +0.18% | 0.698 | 1.000 | 47% | 36% | no edge |
| volatility_spike | 21d | 330 | +3.18% | +3.38% | -0.20% | 0.397 | 0.928 | 47% | 36% | weak (not significant) |
| volatility_spike | 63d | 327 | +11.06% | +11.42% | -0.36% | 0.422 | 0.928 | 47% | 36% | weak (not significant) |
| chandelier_stop | 5d | 1363 | +0.78% | +0.72% | +0.06% | 0.652 | 1.000 | 37% | 36% | no edge |
| chandelier_stop | 21d | 1342 | +3.34% | +3.24% | +0.10% | 0.601 | 1.000 | 37% | 36% | no edge |
| chandelier_stop | 63d | 1276 | +12.16% | +10.82% | +1.34% | 0.968 | 1.000 | 37% | 36% | no edge |

**0 of 33 rule-by-horizon tests** show significantly weaker returns after the signal (q < 0.10).

![Sell signal event study](sell_event_study.png)

## 4. Strategy backtests

Not included: SKHY (only 89 trading days of history, needs 452); SPCX (only 107 trading days of history, needs 452).

### ALAB (2025-01-03 to 2026-11-12)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +58.5% | +28.2% | -63.2% | +97.1% | 0.74 | 0 | 100% |  |  |  |
| 50/200 SMA cross | -65.2% | -43.4% | -74.0% | +87.7% | -0.21 | 2 | 76% | -0.95 | [-1.88, -0.25] | 0.02 |
| Close > 50-day SMA | +7.6% | +4.0% | -66.4% | +69.9% | 0.41 | 10 | 52% | -0.33 | [-1.35, +0.67] | 0.49 |
| MACD > signal | +14.8% | +7.7% | -70.4% | +65.1% | 0.44 | 21 | 50% | -0.31 | [-1.44, +0.86] | 0.59 |
| RSI 30/70 | +16.8% | +8.7% | -50.3% | +37.4% | 0.41 | 1 | 16% | -0.34 | [-2.16, +1.59] | 0.71 |
| Trailing stop 20% | -11.8% | -6.6% | -69.1% | +71.8% | 0.27 | 10 | 56% | -0.47 | [-1.48, +0.50] | 0.35 |
| Volume breakout | +91.8% | +42.1% | -55.7% | +63.1% | 0.87 | 4 | 41% | +0.13 | [-0.98, +1.21] | 0.82 |

### AMD (2022-08-31 to 2026-11-12)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +610.6% | +59.7% | -63.0% | +58.4% | 1.09 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +448.7% | +50.2% | -39.1% | +48.8% | 1.08 | 1 | 65% | -0.02 | [-0.58, +0.50] | 0.96 |
| Close > 50-day SMA | +187.5% | +28.7% | -41.8% | +43.7% | 0.79 | 36 | 53% | -0.30 | [-0.87, +0.27] | 0.33 |
| MACD > signal | +343.0% | +42.7% | -42.4% | +41.4% | 1.06 | 39 | 50% | -0.03 | [-0.58, +0.53] | 0.93 |
| RSI 30/70 | +69.7% | +13.5% | -54.7% | +32.2% | 0.55 | 3 | 33% | -0.54 | [-1.64, +0.41] | 0.28 |
| Trailing stop 20% | +180.7% | +28.0% | -58.9% | +49.6% | 0.74 | 11 | 71% | -0.35 | [-0.86, +0.16] | 0.20 |
| Volume breakout | +177.7% | +27.6% | -36.9% | +37.1% | 0.84 | 10 | 38% | -0.25 | [-0.93, +0.39] | 0.47 |

### NVDA (2022-08-31 to 2026-11-12)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +1096.5% | +80.9% | -36.9% | +49.0% | 1.45 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +541.9% | +55.9% | -30.5% | +43.2% | 1.24 | 1 | 84% | -0.21 | [-0.69, +0.17] | 0.33 |
| Close > 50-day SMA | +346.8% | +43.0% | -39.1% | +39.0% | 1.11 | 38 | 69% | -0.34 | [-0.89, +0.20] | 0.24 |
| MACD > signal | +152.9% | +24.8% | -46.7% | +34.4% | 0.81 | 40 | 51% | -0.64 | [-1.36, +0.07] | 0.08 |
| RSI 30/70 | +46.5% | +9.5% | -22.6% | +18.7% | 0.58 | 2 | 8% | -0.87 | [-2.00, -0.04] | 0.08 |
| Trailing stop 20% | +621.1% | +60.3% | -36.6% | +45.0% | 1.27 | 8 | 90% | -0.18 | [-0.57, +0.14] | 0.27 |
| Volume breakout | +211.5% | +31.2% | -19.8% | +26.3% | 1.16 | 7 | 31% | -0.29 | [-1.15, +0.48] | 0.49 |

### MRVL (2022-08-31 to 2026-11-12)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +262.9% | +36.1% | -60.8% | +67.3% | 0.79 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +60.0% | +11.9% | -65.2% | +57.5% | 0.48 | 2 | 68% | -0.31 | [-0.78, +0.14] | 0.18 |
| Close > 50-day SMA | +65.8% | +12.8% | -51.5% | +52.7% | 0.49 | 36 | 58% | -0.30 | [-0.92, +0.25] | 0.31 |
| MACD > signal | +101.6% | +18.2% | -62.5% | +50.2% | 0.58 | 44 | 51% | -0.21 | [-0.89, +0.48] | 0.53 |
| RSI 30/70 | +71.2% | +13.7% | -32.1% | +29.1% | 0.59 | 2 | 19% | -0.20 | [-1.12, +0.86] | 0.70 |
| Trailing stop 20% | +75.6% | +14.4% | -53.3% | +57.0% | 0.52 | 15 | 77% | -0.27 | [-0.79, +0.20] | 0.25 |
| Volume breakout | +76.0% | +14.5% | -46.2% | +42.0% | 0.53 | 11 | 36% | -0.26 | [-1.12, +0.47] | 0.54 |

### GOOG (2022-08-31 to 2026-11-12)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +169.6% | +26.7% | -30.2% | +31.7% | 0.91 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +151.5% | +24.6% | -29.4% | +25.9% | 0.98 | 2 | 76% | +0.07 | [-0.41, +0.53] | 0.78 |
| Close > 50-day SMA | +85.6% | +15.9% | -22.2% | +23.6% | 0.74 | 34 | 63% | -0.16 | [-0.82, +0.48] | 0.63 |
| MACD > signal | +36.1% | +7.6% | -18.1% | +21.5% | 0.45 | 42 | 50% | -0.46 | [-1.12, +0.19] | 0.20 |
| RSI 30/70 | +34.7% | +7.4% | -20.4% | +18.2% | 0.48 | 4 | 25% | -0.42 | [-1.30, +0.46] | 0.33 |
| Trailing stop 20% | +42.9% | +8.9% | -40.4% | +29.7% | 0.44 | 6 | 92% | -0.47 | [-0.90, -0.09] | 0.03 |
| Volume breakout | +105.6% | +18.8% | -17.4% | +19.4% | 0.98 | 8 | 46% | +0.08 | [-0.79, +0.84] | 0.82 |

### FSLR (2022-08-31 to 2026-11-12)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +34.7% | +7.4% | -60.0% | +55.1% | 0.40 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +10.0% | +2.3% | -51.1% | +41.7% | 0.26 | 4 | 59% | -0.14 | [-0.74, +0.43] | 0.62 |
| Close > 50-day SMA | +30.0% | +6.5% | -46.8% | +40.4% | 0.35 | 29 | 50% | -0.05 | [-0.62, +0.49] | 0.86 |
| MACD > signal | -59.2% | -19.3% | -74.1% | +40.7% | -0.32 | 48 | 49% | -0.72 | [-1.39, -0.04] | 0.03 |
| RSI 30/70 | +30.1% | +6.5% | -42.8% | +30.4% | 0.35 | 2 | 27% | -0.05 | [-1.05, +0.80] | 0.92 |
| Trailing stop 20% | +12.5% | +2.9% | -52.3% | +45.3% | 0.28 | 11 | 69% | -0.11 | [-0.61, +0.37] | 0.64 |
| Volume breakout | -24.3% | -6.4% | -53.8% | +32.3% | -0.04 | 14 | 38% | -0.44 | [-1.35, +0.40] | 0.31 |

### ETN (2022-08-31 to 2026-11-12)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +174.5% | +27.3% | -34.5% | +33.9% | 0.88 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +70.3% | +13.6% | -35.7% | +30.4% | 0.57 | 2 | 83% | -0.31 | [-0.72, +0.04] | 0.11 |
| Close > 50-day SMA | +34.3% | +7.3% | -37.5% | +24.5% | 0.41 | 45 | 65% | -0.47 | [-1.06, +0.21] | 0.13 |
| MACD > signal | +37.3% | +7.9% | -25.8% | +22.4% | 0.45 | 48 | 50% | -0.43 | [-1.10, +0.22] | 0.19 |
| RSI 30/70 | +15.7% | +3.6% | -18.6% | +11.5% | 0.36 | 1 | 5% | -0.52 | [-1.47, +0.54] | 0.29 |
| Trailing stop 20% | +183.0% | +28.2% | -23.6% | +30.9% | 0.96 | 2 | 95% | +0.08 | [-0.13, +0.31] | 0.46 |
| Volume breakout | +21.6% | +4.8% | -29.3% | +18.1% | 0.35 | 10 | 38% | -0.53 | [-1.33, +0.31] | 0.20 |

### TSLA (2022-08-31 to 2026-11-12)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +43.3% | +9.0% | -65.0% | +58.3% | 0.44 | 0 | 100% |  |  |  |
| 50/200 SMA cross | -26.4% | -7.1% | -56.8% | +40.1% | 0.01 | 4 | 47% | -0.42 | [-1.32, +0.37] | 0.31 |
| Close > 50-day SMA | +62.3% | +12.3% | -41.1% | +38.5% | 0.49 | 43 | 52% | +0.06 | [-0.64, +0.87] | 0.90 |
| MACD > signal | +396.5% | +46.6% | -39.8% | +40.8% | 1.14 | 42 | 51% | +0.70 | [+0.09, +1.40] | 0.04 |
| RSI 30/70 | +54.3% | +10.9% | -52.7% | +40.3% | 0.46 | 4 | 43% | +0.02 | [-0.66, +0.73] | 0.95 |
| Trailing stop 20% | +46.1% | +9.5% | -47.9% | +45.0% | 0.43 | 11 | 71% | -0.01 | [-0.63, +0.60] | 0.97 |
| Volume breakout | +40.5% | +8.5% | -35.4% | +25.7% | 0.44 | 9 | 18% | +0.01 | [-0.91, +0.96] | 0.99 |

### AMZN (2022-08-31 to 2026-11-12)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +109.1% | +19.3% | -40.0% | +34.1% | 0.69 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +37.5% | +7.9% | -41.4% | +27.8% | 0.41 | 2 | 74% | -0.27 | [-0.90, +0.34] | 0.39 |
| Close > 50-day SMA | +34.2% | +7.3% | -41.0% | +23.3% | 0.42 | 35 | 63% | -0.27 | [-0.96, +0.44] | 0.47 |
| MACD > signal | -0.2% | -0.0% | -28.7% | +22.8% | 0.11 | 50 | 50% | -0.57 | [-1.32, +0.13] | 0.12 |
| RSI 30/70 | +94.0% | +17.1% | -22.0% | +21.6% | 0.84 | 4 | 33% | +0.15 | [-0.61, +0.87] | 0.69 |
| Trailing stop 20% | +114.6% | +20.0% | -24.2% | +29.8% | 0.76 | 3 | 87% | +0.07 | [-0.36, +0.52] | 0.73 |
| Volume breakout | +7.0% | +1.6% | -35.7% | +18.8% | 0.18 | 11 | 45% | -0.51 | [-1.45, +0.45] | 0.29 |

### IBM (2022-08-31 to 2026-11-12)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +118.8% | +20.6% | -37.5% | +31.5% | 0.76 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +62.3% | +12.3% | -28.7% | +22.8% | 0.62 | 3 | 73% | -0.13 | [-0.78, +0.54] | 0.70 |
| Close > 50-day SMA | +53.8% | +10.8% | -42.6% | +25.2% | 0.54 | 27 | 60% | -0.22 | [-0.72, +0.34] | 0.42 |
| MACD > signal | +112.3% | +19.7% | -43.1% | +23.9% | 0.88 | 30 | 50% | +0.12 | [-0.45, +0.84] | 0.72 |
| RSI 30/70 | +175.4% | +27.4% | -16.5% | +17.4% | 1.48 | 8 | 35% | +0.72 | [-0.28, +1.64] | 0.14 |
| Trailing stop 20% | +66.1% | +12.9% | -45.9% | +30.3% | 0.56 | 3 | 92% | -0.20 | [-0.45, +0.01] | 0.08 |
| Volume breakout | +65.7% | +12.8% | -25.6% | +17.0% | 0.79 | 10 | 40% | +0.04 | [-0.87, +0.95] | 0.94 |

### GEV (2025-01-13 to 2026-11-12)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +114.9% | +51.8% | -38.3% | +56.1% | 1.03 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +133.0% | +58.6% | -38.3% | +54.8% | 1.12 | 1 | 97% | +0.09 | [-0.05, +0.32] | 0.25 |
| Close > 50-day SMA | +79.1% | +37.4% | -32.7% | +43.8% | 0.95 | 15 | 63% | -0.08 | [-0.68, +0.49] | 0.79 |
| MACD > signal | +60.6% | +29.5% | -31.0% | +42.0% | 0.83 | 17 | 48% | -0.20 | [-0.98, +0.65] | 0.60 |
| RSI 30/70 | +27.4% | +14.1% | -34.4% | +34.9% | 0.55 | 1 | 31% | -0.47 | [-1.72, +0.60] | 0.43 |
| Trailing stop 20% | +44.2% | +22.1% | -45.9% | +50.0% | 0.65 | 5 | 87% | -0.38 | [-0.91, +0.09] | 0.15 |
| Volume breakout | +24.5% | +12.7% | -24.6% | +33.5% | 0.53 | 3 | 35% | -0.50 | [-1.72, +0.67] | 0.40 |

### CEG (2022-11-02 to 2026-11-12)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +208.3% | +32.4% | -50.7% | +49.3% | 0.81 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +96.8% | +18.4% | -50.7% | +43.5% | 0.60 | 3 | 72% | -0.21 | [-0.68, +0.21] | 0.33 |
| Close > 50-day SMA | +145.1% | +25.0% | -40.9% | +37.3% | 0.78 | 48 | 57% | -0.03 | [-0.62, +0.50] | 0.92 |
| MACD > signal | +32.4% | +7.3% | -41.5% | +36.9% | 0.37 | 41 | 49% | -0.44 | [-1.07, +0.16] | 0.19 |
| RSI 30/70 | +108.9% | +20.2% | -28.6% | +32.3% | 0.73 | 3 | 37% | -0.09 | [-0.90, +0.71] | 0.82 |
| Trailing stop 20% | +100.3% | +18.9% | -52.8% | +43.8% | 0.61 | 9 | 84% | -0.20 | [-0.64, +0.24] | 0.37 |
| Volume breakout | +86.0% | +16.7% | -30.0% | +30.6% | 0.66 | 9 | 39% | -0.16 | [-0.88, +0.57] | 0.66 |

### VST (2022-08-31 to 2026-11-12)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +473.7% | +51.8% | -48.8% | +52.1% | 1.07 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +420.5% | +48.3% | -48.8% | +44.0% | 1.12 | 3 | 68% | +0.05 | [-0.28, +0.43] | 0.76 |
| Close > 50-day SMA | +49.5% | +10.1% | -67.2% | +38.0% | 0.45 | 45 | 64% | -0.62 | [-1.25, -0.02] | 0.05 |
| MACD > signal | +66.6% | +13.0% | -49.0% | +37.2% | 0.52 | 47 | 51% | -0.55 | [-1.20, +0.11] | 0.10 |
| RSI 30/70 | +202.8% | +30.3% | -27.3% | +26.8% | 1.12 | 3 | 20% | +0.05 | [-0.83, +0.85] | 0.90 |
| Trailing stop 20% | +214.1% | +31.4% | -56.3% | +44.6% | 0.84 | 9 | 88% | -0.23 | [-0.66, +0.21] | 0.30 |
| Volume breakout | +278.5% | +37.4% | -31.2% | +31.4% | 1.18 | 9 | 43% | +0.11 | [-0.62, +0.96] | 0.78 |

### DELL (2022-08-31 to 2026-11-12)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +970.3% | +76.2% | -59.6% | +58.0% | 1.26 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +462.5% | +51.1% | -50.8% | +50.7% | 1.06 | 3 | 69% | -0.20 | [-0.70, +0.21] | 0.37 |
| Close > 50-day SMA | +1326.9% | +88.7% | -27.5% | +49.3% | 1.52 | 21 | 67% | +0.27 | [-0.18, +0.75] | 0.27 |
| MACD > signal | +141.4% | +23.4% | -57.7% | +43.1% | 0.69 | 45 | 52% | -0.57 | [-1.16, +0.07] | 0.08 |
| RSI 30/70 | +177.3% | +27.6% | -23.7% | +26.6% | 1.05 | 4 | 28% | -0.21 | [-1.23, +0.67] | 0.67 |
| Trailing stop 20% | +979.0% | +76.5% | -55.9% | +51.5% | 1.35 | 7 | 82% | +0.09 | [-0.28, +0.48] | 0.64 |
| Volume breakout | +378.1% | +45.3% | -37.8% | +43.2% | 1.07 | 11 | 45% | -0.19 | [-0.85, +0.42] | 0.55 |

### TSM (2022-08-31 to 2026-11-12)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +430.2% | +49.0% | -36.8% | +39.3% | 1.21 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +178.4% | +27.7% | -36.8% | +35.9% | 0.86 | 2 | 81% | -0.35 | [-0.87, +0.13] | 0.17 |
| Close > 50-day SMA | +190.3% | +29.0% | -28.8% | +31.6% | 0.96 | 37 | 68% | -0.25 | [-0.78, +0.31] | 0.38 |
| MACD > signal | +142.0% | +23.5% | -32.1% | +28.4% | 0.89 | 44 | 49% | -0.32 | [-0.92, +0.24] | 0.29 |
| RSI 30/70 | +48.5% | +9.9% | -23.0% | +16.8% | 0.64 | 3 | 13% | -0.57 | [-1.62, +0.42] | 0.27 |
| Trailing stop 20% | +219.6% | +32.0% | -30.6% | +36.7% | 0.94 | 6 | 91% | -0.27 | [-0.62, +0.09] | 0.13 |
| Volume breakout | +77.0% | +14.6% | -26.8% | +26.4% | 0.65 | 11 | 46% | -0.56 | [-1.34, +0.14] | 0.12 |

### BE (2022-08-31 to 2026-11-12)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +718.4% | +65.2% | -67.8% | +90.0% | 0.99 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +279.2% | +37.5% | -71.9% | +74.9% | 0.79 | 4 | 63% | -0.20 | [-0.79, +0.33] | 0.53 |
| Close > 50-day SMA | +373.7% | +45.0% | -53.1% | +69.7% | 0.86 | 31 | 52% | -0.13 | [-0.71, +0.38] | 0.63 |
| MACD > signal | +217.3% | +31.8% | -60.0% | +65.8% | 0.73 | 41 | 50% | -0.26 | [-1.04, +0.39] | 0.44 |
| RSI 30/70 | +147.7% | +24.2% | -61.8% | +47.0% | 0.69 | 4 | 47% | -0.30 | [-1.14, +0.55] | 0.54 |
| Trailing stop 20% | +161.1% | +25.8% | -66.7% | +73.8% | 0.66 | 19 | 60% | -0.33 | [-0.82, +0.14] | 0.17 |
| Volume breakout | +275.5% | +37.2% | -58.1% | +61.0% | 0.80 | 11 | 30% | -0.19 | [-0.95, +0.54] | 0.63 |

![Strategy equity curves](backtest_equity.png)

## 5. Next-day forecasts

Not included: SKHY (only 89 trading days of history, needs 452); SPCX (only 107 trading days of history, needs 452).

### ALAB

Walk-forward test on 214 unseen days (2026-01-07 to 2026-11-11).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.523 | 0.523 | 0.528 | 0.456 | 0.25 | 0.877 | 0.877 |
| Logistic regression | 0.495 | 0.523 | 0.813 | 0.498 | 0.257 | 0.333 | 0.877 |
| Gradient boosting | 0.477 | 0.523 | 0.925 | 0.456 | 0.283 | 0.423 | 0.877 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 650.5 | 0.0 |  |  |
| Ridge regression | 667.1 | -0.0516 | 0.477 | 0.944 |
| Gradient boosting | 684.4 | -0.1068 | 0.453 | 0.993 |

Forecast for the next session:

```
  P(up) | Logistic regression      47.4%
  P(up) | Gradient boosting        30.4%
  P(up) | historical base rate     51.9%
  expected return (ridge)          +0.03%
  80% range low                    -9.71%
  80% range high                   +10.82%
  daily volatility                 +8.00%
```

Best out-of-sample AUC **0.498**; smallest p-value against a naive baseline 0.813, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![ALAB feature effects](forecast_ALAB.png)

### AMD

Walk-forward test on 550 unseen days (2024-09-04 to 2026-11-11).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.52 | 0.533 | 0.739 | 0.498 | 0.25 | 1.45 | 1.325 |
| Logistic regression | 0.489 | 0.533 | 0.982 | 0.49 | 0.255 | 0.431 | 1.325 |
| Gradient boosting | 0.485 | 0.533 | 0.988 | 0.493 | 0.268 | 0.728 | 1.325 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 404.4 | 0.0 |  |  |
| Ridge regression | 407.3 | -0.0141 | 0.491 | 0.799 |
| Gradient boosting | 412.4 | -0.0398 | 0.485 | 0.982 |

Forecast for the next session:

```
  P(up) | Logistic regression      44.0%
  P(up) | Gradient boosting        56.2%
  P(up) | historical base rate     51.6%
  expected return (ridge)          -1.51%
  80% range low                    -10.41%
  80% range high                   +8.29%
  daily volatility                 +7.40%
```

Best out-of-sample AUC **0.493**; smallest p-value against a naive baseline 0.799, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![AMD feature effects](forecast_AMD.png)

### NVDA

Walk-forward test on 550 unseen days (2024-09-04 to 2026-11-11).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.524 | 0.524 | 0.517 | 0.504 | 0.25 | 0.687 | 0.687 |
| Logistic regression | 0.507 | 0.524 | 0.791 | 0.523 | 0.253 | 0.521 | 0.687 |
| Gradient boosting | 0.495 | 0.524 | 0.92 | 0.48 | 0.268 | 0.592 | 0.687 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 280.0 | 0.0 |  |  |
| Ridge regression | 280.2 | -0.0016 | 0.518 | 0.526 |
| Gradient boosting | 287.5 | -0.0543 | 0.516 | 0.954 |

Forecast for the next session:

```
  P(up) | Logistic regression      69.2%
  P(up) | Gradient boosting        73.9%
  P(up) | historical base rate     53.7%
  expected return (ridge)          +0.85%
  80% range low                    -3.35%
  80% range high                   +5.22%
  daily volatility                 +3.31%
```

Best out-of-sample AUC **0.523**; smallest p-value against a naive baseline 0.526, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![NVDA feature effects](forecast_NVDA.png)

### MRVL

Walk-forward test on 550 unseen days (2024-09-04 to 2026-11-11).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.535 | 0.535 | 0.517 | 0.471 | 0.249 | 0.888 | 0.888 |
| Logistic regression | 0.536 | 0.535 | 0.483 | 0.547 | 0.253 | 0.674 | 0.888 |
| Gradient boosting | 0.515 | 0.535 | 0.837 | 0.55 | 0.259 | 0.591 | 0.888 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 480.6 | 0.0 |  |  |
| Ridge regression | 487.0 | -0.0267 | 0.529 | 0.905 |
| Gradient boosting | 488.6 | -0.0335 | 0.518 | 0.92 |

Forecast for the next session:

```
  P(up) | Logistic regression      32.0%
  P(up) | Gradient boosting        46.8%
  P(up) | historical base rate     52.6%
  expected return (ridge)          -1.92%
  80% range low                    -11.10%
  80% range high                   +8.20%
  daily volatility                 +7.67%
```

Best out-of-sample AUC **0.550**; smallest p-value against a naive baseline 0.483, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![MRVL feature effects](forecast_MRVL.png)

### GOOG

Walk-forward test on 550 unseen days (2024-09-04 to 2026-11-11).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.525 | 0.525 | 0.517 | 0.489 | 0.25 | 1.071 | 1.072 |
| Logistic regression | 0.551 | 0.525 | 0.124 | 0.535 | 0.252 | 0.527 | 1.072 |
| Gradient boosting | 0.536 | 0.525 | 0.32 | 0.532 | 0.261 | 0.795 | 1.072 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 201.1 | 0.0 |  |  |
| Ridge regression | 203.3 | -0.0216 | 0.533 | 0.948 |
| Gradient boosting | 207.5 | -0.0648 | 0.513 | 0.997 |

Forecast for the next session:

```
  P(up) | Logistic regression      50.6%
  P(up) | Gradient boosting        60.4%
  P(up) | historical base rate     53.1%
  expected return (ridge)          +0.12%
  80% range low                    -3.96%
  80% range high                   +4.37%
  daily volatility                 +3.25%
```

Best out-of-sample AUC **0.535**; smallest p-value against a naive baseline 0.124, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![GOOG feature effects](forecast_GOOG.png)

### FSLR

Walk-forward test on 550 unseen days (2024-09-04 to 2026-11-11).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.516 | 0.516 | 0.517 | 0.459 | 0.25 |  | 0.112 |
| Logistic regression | 0.511 | 0.516 | 0.618 | 0.524 | 0.251 | -0.122 | 0.112 |
| Gradient boosting | 0.515 | 0.516 | 0.551 | 0.526 | 0.26 | -0.269 | 0.112 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 363.8 | 0.0 |  |  |
| Ridge regression | 364.7 | -0.0052 | 0.5 | 0.668 |
| Gradient boosting | 375.4 | -0.0649 | 0.516 | 0.998 |

Forecast for the next session:

```
  P(up) | Logistic regression      45.6%
  P(up) | Gradient boosting        35.3%
  P(up) | historical base rate     49.1%
  expected return (ridge)          +0.09%
  80% range low                    -3.55%
  80% range high                   +3.86%
  daily volatility                 +2.89%
```

Best out-of-sample AUC **0.526**; smallest p-value against a naive baseline 0.551, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![FSLR feature effects](forecast_FSLR.png)

### ETN

Walk-forward test on 550 unseen days (2024-09-04 to 2026-11-11).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.525 | 0.525 | 0.517 | 0.477 | 0.25 | 0.484 | 0.485 |
| Logistic regression | 0.515 | 0.525 | 0.711 | 0.517 | 0.254 | 0.718 | 0.485 |
| Gradient boosting | 0.515 | 0.525 | 0.711 | 0.532 | 0.257 | 0.376 | 0.485 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 246.9 | 0.0 |  |  |
| Ridge regression | 248.9 | -0.0164 | 0.538 | 0.841 |
| Gradient boosting | 253.3 | -0.0529 | 0.507 | 0.97 |

Forecast for the next session:

```
  P(up) | Logistic regression      40.0%
  P(up) | Gradient boosting        53.8%
  P(up) | historical base rate     54.1%
  expected return (ridge)          -0.55%
  80% range low                    -5.97%
  80% range high                   +5.17%
  daily volatility                 +4.37%
```

Best out-of-sample AUC **0.532**; smallest p-value against a naive baseline 0.711, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![ETN feature effects](forecast_ETN.png)

### TSLA

Walk-forward test on 550 unseen days (2024-09-04 to 2026-11-11).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.505 | 0.505 | 0.517 | 0.446 | 0.25 | 0.752 | 0.753 |
| Logistic regression | 0.52 | 0.505 | 0.261 | 0.509 | 0.253 | 0.668 | 0.753 |
| Gradient boosting | 0.515 | 0.505 | 0.351 | 0.525 | 0.263 | 0.926 | 0.753 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 369.9 | 0.0 |  |  |
| Ridge regression | 374.8 | -0.0266 | 0.489 | 0.953 |
| Gradient boosting | 378.2 | -0.0453 | 0.518 | 0.954 |

Forecast for the next session:

```
  P(up) | Logistic regression      46.1%
  P(up) | Gradient boosting        41.4%
  P(up) | historical base rate     50.9%
  expected return (ridge)          -0.16%
  80% range low                    -4.88%
  80% range high                   +4.79%
  daily volatility                 +3.78%
```

Best out-of-sample AUC **0.525**; smallest p-value against a naive baseline 0.261, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![TSLA feature effects](forecast_TSLA.png)

### AMZN

Walk-forward test on 550 unseen days (2024-09-04 to 2026-11-11).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.518 | 0.518 | 0.517 | 0.456 | 0.25 | 0.752 | 0.753 |
| Logistic regression | 0.545 | 0.518 | 0.108 | 0.555 | 0.249 | 1.121 | 0.753 |
| Gradient boosting | 0.527 | 0.518 | 0.351 | 0.524 | 0.262 | 0.592 | 0.753 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 212.1 | 0.0 |  |  |
| Ridge regression | 214.2 | -0.0204 | 0.547 | 0.898 |
| Gradient boosting | 222.5 | -0.1009 | 0.511 | 1.0 |

Forecast for the next session:

```
  P(up) | Logistic regression      43.2%
  P(up) | Gradient boosting        51.6%
  P(up) | historical base rate     51.4%
  expected return (ridge)          -0.22%
  80% range low                    -3.49%
  80% range high                   +3.17%
  daily volatility                 +2.61%
```

Best out-of-sample AUC **0.555**; smallest p-value against a naive baseline 0.108, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![AMZN feature effects](forecast_AMZN.png)

### IBM

Walk-forward test on 550 unseen days (2024-09-04 to 2026-11-11).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.547 | 0.547 | 0.518 | 0.463 | 0.248 | 0.485 | 0.485 |
| Logistic regression | 0.525 | 0.547 | 0.858 | 0.471 | 0.255 | 0.608 | 0.485 |
| Gradient boosting | 0.515 | 0.547 | 0.943 | 0.509 | 0.262 | 0.517 | 0.485 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 253.4 | 0.0 |  |  |
| Ridge regression | 256.1 | -0.0215 | 0.525 | 0.933 |
| Gradient boosting | 257.9 | -0.0358 | 0.516 | 0.99 |

Forecast for the next session:

```
  P(up) | Logistic regression      55.7%
  P(up) | Gradient boosting        54.7%
  P(up) | historical base rate     55.2%
  expected return (ridge)          -0.21%
  80% range low                    -2.36%
  80% range high                   +1.99%
  daily volatility                 +1.70%
```

Best out-of-sample AUC **0.509**; smallest p-value against a naive baseline 0.858, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![IBM feature effects](forecast_IBM.png)

### GEV

Walk-forward test on 209 unseen days (2026-01-14 to 2026-11-11).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.536 | 0.536 | 0.528 | 0.469 | 0.249 | 0.809 | 0.81 |
| Logistic regression | 0.507 | 0.536 | 0.816 | 0.504 | 0.256 | 0.523 | 0.81 |
| Gradient boosting | 0.536 | 0.536 | 0.528 | 0.535 | 0.267 | 1.186 | 0.81 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 337.5 | 0.0 |  |  |
| Ridge regression | 343.7 | -0.0366 | 0.555 | 0.796 |
| Gradient boosting | 349.1 | -0.0698 | 0.536 | 0.89 |

Forecast for the next session:

```
  P(up) | Logistic regression      54.1%
  P(up) | Gradient boosting        57.3%
  P(up) | historical base rate     54.4%
  expected return (ridge)          +0.24%
  80% range low                    -5.78%
  80% range high                   +6.65%
  daily volatility                 +4.84%
```

Best out-of-sample AUC **0.535**; smallest p-value against a naive baseline 0.528, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![GEV feature effects](forecast_GEV.png)

### CEG

Walk-forward test on 506 unseen days (2024-11-05 to 2026-11-11).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.506 | 0.506 | 0.518 | 0.486 | 0.251 | 0.457 | 0.457 |
| Logistic regression | 0.474 | 0.506 | 0.929 | 0.501 | 0.259 | 0.066 | 0.457 |
| Gradient boosting | 0.472 | 0.506 | 0.94 | 0.462 | 0.276 | -0.093 | 0.457 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 352.0 | 0.0 |  |  |
| Ridge regression | 359.7 | -0.0439 | 0.478 | 0.98 |
| Gradient boosting | 362.9 | -0.063 | 0.508 | 0.99 |

Forecast for the next session:

```
  P(up) | Logistic regression      53.8%
  P(up) | Gradient boosting        33.0%
  P(up) | historical base rate     52.2%
  expected return (ridge)          +0.02%
  80% range low                    -4.74%
  80% range high                   +5.02%
  daily volatility                 +3.81%
```

Best out-of-sample AUC **0.501**; smallest p-value against a naive baseline 0.929, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![CEG feature effects](forecast_CEG.png)

### VST

Walk-forward test on 550 unseen days (2024-09-04 to 2026-11-11).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.518 | 0.518 | 0.517 | 0.47 | 0.25 | 0.744 | 0.744 |
| Logistic regression | 0.473 | 0.518 | 0.985 | 0.476 | 0.262 | 0.95 | 0.744 |
| Gradient boosting | 0.515 | 0.518 | 0.585 | 0.52 | 0.268 | 1.101 | 0.744 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 392.7 | 0.0 |  |  |
| Ridge regression | 397.7 | -0.026 | 0.496 | 0.889 |
| Gradient boosting | 403.6 | -0.0567 | 0.502 | 0.993 |

Forecast for the next session:

```
  P(up) | Logistic regression      40.4%
  P(up) | Gradient boosting        39.5%
  P(up) | historical base rate     52.8%
  expected return (ridge)          -0.46%
  80% range low                    -7.13%
  80% range high                   +6.70%
  daily volatility                 +5.42%
```

Best out-of-sample AUC **0.520**; smallest p-value against a naive baseline 0.585, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![VST feature effects](forecast_VST.png)

### DELL

Walk-forward test on 550 unseen days (2024-09-04 to 2026-11-11).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.522 | 0.522 | 0.517 | 0.472 | 0.25 | 1.196 | 1.196 |
| Logistic regression | 0.504 | 0.522 | 0.815 | 0.509 | 0.255 | 0.057 | 1.196 |
| Gradient boosting | 0.496 | 0.522 | 0.892 | 0.501 | 0.267 | 0.411 | 1.196 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 407.7 | 0.0 |  |  |
| Ridge regression | 414.1 | -0.0316 | 0.493 | 0.985 |
| Gradient boosting | 420.4 | -0.0631 | 0.522 | 0.995 |

Forecast for the next session:

```
  P(up) | Logistic regression      49.5%
  P(up) | Gradient boosting        80.3%
  P(up) | historical base rate     51.7%
  expected return (ridge)          +0.31%
  80% range low                    -7.98%
  80% range high                   +9.34%
  daily volatility                 +6.73%
```

Best out-of-sample AUC **0.509**; smallest p-value against a naive baseline 0.815, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![DELL feature effects](forecast_DELL.png)

### TSM

Walk-forward test on 550 unseen days (2024-09-04 to 2026-11-11).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.504 | 0.535 | 0.933 | 0.481 | 0.25 | 1.192 | 1.254 |
| Logistic regression | 0.535 | 0.535 | 0.517 | 0.534 | 0.249 | 1.131 | 1.254 |
| Gradient boosting | 0.524 | 0.535 | 0.711 | 0.519 | 0.258 | 1.36 | 1.254 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 264.1 | 0.0 |  |  |
| Ridge regression | 262.8 | 0.0099 | 0.52 | 0.272 |
| Gradient boosting | 270.0 | -0.0451 | 0.522 | 0.982 |

Forecast for the next session:

```
  P(up) | Logistic regression      42.2%
  P(up) | Gradient boosting        56.8%
  P(up) | historical base rate     51.6%
  expected return (ridge)          -0.34%
  80% range low                    -5.20%
  80% range high                   +4.77%
  daily volatility                 +3.90%
```

Best out-of-sample AUC **0.534**; smallest p-value against a naive baseline 0.272, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![TSM feature effects](forecast_TSM.png)

### BE

Walk-forward test on 550 unseen days (2024-09-04 to 2026-11-11).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.485 | 0.515 | 0.92 | 0.478 | 0.251 |  | 1.749 |
| Logistic regression | 0.484 | 0.515 | 0.932 | 0.471 | 0.265 | 1.045 | 1.749 |
| Gradient boosting | 0.505 | 0.515 | 0.681 | 0.485 | 0.268 | 1.31 | 1.749 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 654.3 | 0.0 |  |  |
| Ridge regression | 671.2 | -0.0523 | 0.471 | 0.996 |
| Gradient boosting | 667.1 | -0.0396 | 0.496 | 0.981 |

Forecast for the next session:

```
  P(up) | Logistic regression      46.2%
  P(up) | Gradient boosting        57.5%
  P(up) | historical base rate     49.6%
  expected return (ridge)          +0.18%
  80% range low                    -9.52%
  80% range high                   +10.93%
  daily volatility                 +7.95%
```

Best out-of-sample AUC **0.485**; smallest p-value against a naive baseline 0.681, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![BE feature effects](forecast_BE.png)

## 6. Stock screen and entry plans

| ticker | rank | score | passes_filters | close | momentum_12_1 | momentum_6m | volatility | off_52w_high | forward_pe | pullback_entry | breakout_trigger | stop | stop_% | shares | position_$ | max_loss_$ | filter_notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DELL | 1 | +1.07 | True | 371.17 | +269.4% | +50.2% | +86.3% | -36.8% | 12.2 | 336.01 | 502.96 | 265.7 | -20.9% | 14 | 4704.0 | 984.0 |  |
| AMD | 2 | +1.07 | True | 585.30 | +140.3% | +30.2% | +78.8% | -9.9% | 33.1 | 552.99 | 586.47 | 472.72 | -14.5% | 12 | 6636.0 | 963.0 |  |
| V | 3 | +0.55 | True | 420.31 | +16.4% | +30.8% | +21.6% | -3.5% | 24.5 | 413.94 | 436.63 | 395.77 | -4.4% | 24 | 9934.0 | 436.0 |  |
| XOM | 4 | +0.52 | True | 169.78 | +52.1% | +12.6% | +26.6% | -9.3% | 13.5 | 169.21 | 187.62 | 160.31 | -5.3% | 59 | 9983.0 | 525.0 |  |
| LLY | 5 | +0.51 | True | 1427.28 | +23.0% | +42.2% | +31.1% | -0.7% | 28.2 | 1346.92 | 1440.16 | 1256.08 | -6.7% | 7 | 9428.0 | 636.0 |  |
| MSFT | 6 | +0.48 | True | 523.00 | +5.8% | +28.3% | +27.5% | -5.9% | 21.6 | 518.72 | 556.91 | 487.88 | -5.9% | 19 | 9856.0 | 586.0 |  |
| KO | 7 | +0.48 | True | 97.44 | +31.6% | +22.6% | +17.4% | -0.1% | 27.6 | 94.49 | 97.77 | 91.04 | -3.6% | 105 | 9922.0 | 362.0 |  |
| AAPL | 8 | +0.41 | True | 354.88 | +24.9% | +19.2% | +22.3% | -0.1% | 33.7 | 345.26 | 356.07 | 328.49 | -4.9% | 28 | 9667.0 | 470.0 |  |
| JNJ | 9 | +0.41 | True | 283.52 | +33.9% | +24.2% | +25.0% | +0.0% | 24.4 | 270.04 | 284.09 | 256.35 | -5.1% | 37 | 9991.0 | 506.0 |  |
| TSM | 10 | +0.35 | True | 405.49 | +49.2% | -2.4% | +42.7% | -16.5% | 17.3 | 388.35 | 440.39 | 354.06 | -8.8% | 25 | 9709.0 | 857.0 |  |
| JPM | 11 | +0.30 | True | 342.82 | +8.3% | +15.4% | +20.3% | -5.7% | 13.4 | 339.99 | 352.81 | 325.29 | -4.3% | 29 | 9860.0 | 426.0 |  |
| PG | 12 | +0.18 | True | 168.03 | +7.7% | +19.4% | +20.6% | -0.4% | 22.7 | 162.61 | 169.0 | 156.2 | -3.9% | 61 | 9919.0 | 391.0 |  |
| UNH | 13 | +0.16 | True | 405.13 | +24.0% | +2.7% | +23.7% | -6.6% | 17.4 | 391.01 | 425.83 | 368.93 | -5.6% | 25 | 9775.0 | 552.0 |  |
| LIN | 14 | +0.02 | True | 522.49 | +17.0% | +2.8% | +15.5% | -4.1% | 26.7 | 512.45 | 527.6 | 494.04 | -3.6% | 19 | 9736.0 | 350.0 |  |
| AMT | 15 | +0.00 | True | 189.79 | +1.0% | +13.6% | +29.2% | -2.6% | 27.1 | 187.11 | 195.25 | 177.02 | -5.4% | 53 | 9917.0 | 535.0 |  |

## 7. Portfolio construction

Not included: SKHY (only 89 trading days of history, needs 252); SPCX (only 107 trading days of history, needs 252).

Assets: ALAB, AMD, NVDA, MRVL, GOOG, FSLR, ETN, TSLA, AMZN, IBM, GEV, CEG, VST, DELL, TSM, BE, JPM, XOM, UNH, COST, TLT, GLD. Covariance: Ledoit-Wolf shrinkage on the last 252 trading days.

Weights and share of risk (%):

| asset | weight: Equal weight | weight: Inverse volatility | weight: Risk parity | weight: Minimum variance | risk share: Equal weight | risk share: Inverse volatility | risk share: Risk parity | risk share: Minimum variance |
|---|---|---|---|---|---|---|---|---|
| ALAB | 4.5 | 1.8 | 1.2 | 0.0 | 12.4 | 6.6 | 4.6 | 0.0 |
| AMD | 4.5 | 2.5 | 1.4 | 0.0 | 9.4 | 7.3 | 4.6 | 0.0 |
| NVDA | 4.5 | 4.5 | 3.4 | 4.7 | 3.9 | 5.9 | 4.8 | 5.2 |
| MRVL | 4.5 | 2.1 | 1.3 | 0.0 | 10.3 | 6.7 | 4.6 | 0.0 |
| GOOG | 4.5 | 5.3 | 4.6 | 4.4 | 1.9 | 4.0 | 4.8 | 4.9 |
| FSLR | 4.5 | 3.4 | 2.8 | 0.4 | 4.0 | 4.7 | 4.7 | 0.4 |
| ETN | 4.5 | 4.1 | 2.6 | 1.7 | 5.4 | 7.2 | 4.7 | 1.9 |
| TSLA | 4.5 | 3.9 | 2.6 | 0.0 | 4.5 | 6.1 | 4.7 | 0.0 |
| AMZN | 4.5 | 5.1 | 4.1 | 4.0 | 2.1 | 4.3 | 4.7 | 4.4 |
| IBM | 4.5 | 3.7 | 5.4 | 2.3 | 0.9 | 1.5 | 4.8 | 2.6 |
| GEV | 4.5 | 3.2 | 2.3 | 0.9 | 6.2 | 6.4 | 4.7 | 1.0 |
| CEG | 4.5 | 3.6 | 2.7 | 1.3 | 4.5 | 5.5 | 4.7 | 1.5 |
| VST | 4.5 | 3.4 | 2.4 | 0.1 | 5.4 | 6.0 | 4.7 | 0.1 |
| DELL | 4.5 | 2.2 | 1.8 | 0.0 | 7.7 | 5.4 | 4.6 | 0.0 |
| TSM | 4.5 | 4.2 | 2.3 | 0.0 | 5.5 | 7.6 | 4.7 | 0.0 |
| BE | 4.5 | 1.6 | 1.0 | 0.0 | 13.6 | 6.7 | 4.6 | 0.0 |
| JPM | 4.5 | 7.2 | 6.7 | 7.6 | 1.2 | 3.7 | 4.9 | 8.3 |
| XOM | 4.5 | 6.3 | 0.0 | 18.3 | -0.8 | -1.6 | -0.0 | 20.1 |
| UNH | 4.5 | 5.0 | 6.9 | 3.5 | 0.5 | 1.5 | 4.8 | 3.9 |
| COST | 4.5 | 8.0 | 22.5 | 17.0 | -0.9 | -1.5 | 5.1 | 18.7 |
| TLT | 4.5 | 12.9 | 16.6 | 30.0 | 0.3 | 2.1 | 5.4 | 23.1 |
| GLD | 4.5 | 5.9 | 5.4 | 3.7 | 1.8 | 4.1 | 4.8 | 4.1 |

| method | expected volatility | diversification ratio | effective number of bets | largest risk share | largest risk holder |
|---|---|---|---|---|---|
| Equal weight | 27.6% | 1.81 | 12.37 | 13.6% | BE |
| Inverse volatility | 18.2% | 2.16 | 16.57 | 7.6% | TSM |
| Risk parity | 14.0% | 2.46 | 20.97 | 5.4% | TLT |
| Minimum variance | 8.6% | 2.95 | 6.79 | 23.1% | TLT |

Concentration warnings:

- ETN and GEV have correlation 0.72: they tend to fall together
- CEG and VST have correlation 0.80: they tend to fall together

Out-of-sample comparison, monthly rebalance (2025-04-01 to 2026-11-12):

| method | CAGR | Volatility | Sharpe | Max drawdown |
|---|---|---|---|---|
| Equal weight | +64.3% | +28.7% | 1.88 | -18.0% |
| Inverse volatility | +44.5% | +20.6% | 1.89 | -11.2% |
| Risk parity | +33.7% | +16.0% | 1.89 | -9.3% |
| Minimum variance | +14.6% | +10.0% | 1.41 | -6.8% |

![Correlations](portfolio_correlation.png)

![Risk shares](portfolio_risk_shares.png)

![Walk-forward](portfolio_walk_forward.png)

## 8. Opening gaps: do pre-market moves carry into the day?

Across 19,016 stock-days (18 watchlist stocks, 2021-11-16 to 2026-11-12), each 1% of opening gap went with a -0.03% move from the open to the close (95% block-bootstrap CI [-0.08%, +0.03%]): no reliable relationship, so the size of a gap has not told you which way the session goes.

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 776 | -5.2% | +0.36% | 50% |
| down 1-3% | 2911 | -1.7% | +0.09% | 52% |
| within 1% | 11027 | +0.0% | +0.02% | 50% |
| up 1-3% | 3371 | +1.7% | +0.09% | 52% |
| gap up 3%+ | 931 | +5.4% | -0.13% | 47% |

## 9. Deciding before the open vs at the previous close

From 2022-02-10 to 2026-11-11 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +34.8% a year (worst drawdown -34.2%) against +35.1% (-34.1%) for labels set at the previous close; the two agreed on 89% of stock-weeks. Sharpe ratio difference -0.02 (95% block-bootstrap CI [-0.20, +0.18]): deciding before the open has been **not distinguishable from deciding on the previous close**.

| strategy | CAGR | Volatility | Sharpe | Max drawdown |
|---|---|---|---|---|
| Board on the previous close | +35.1% | 34.6% | 1.05 | -34.1% |
| Board on the pre-market price | +34.8% | 35.0% | 1.03 | -34.2% |
| Equal-weight watchlist | +43.3% | 35.3% | 1.20 | -40.7% |

The pre-market version uses the official opening price as a stand-in for the last pre-market trade (free pre-market history is only days long), which slightly flatters it.
