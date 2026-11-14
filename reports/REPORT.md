# stocklab report
Generated 2026-11-14 | data source: `yahoo` | history: 5 years | watchlist: ALAB, AMD, NVDA, MRVL, GOOG, FSLR, SKHY, ETN, TSLA, SPCX, AMZN, IBM, GEV, CEG, VST, DELL, TSM, BE

> Educational research code, not investment advice. Past results do not predict future returns.

## 1. Decision board

Data as of the 2026-11-13 close. `*` = provisional (under 200 trading days of history).

| ticker | action | close | 1 day | 1 month | buy rank | sell warnings | pullback entry | breakout | stop | why |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | BUY | 266.66 | -0.3% | +4.7% | 4/9 | 1/15 | 257.33 | 271.41 | 239.17 | buy rank 4/9; +9% vs 200-day average; distribution days |
| AMD | WATCH | 534.06 | -8.8% | -5.0% | 1/9 | 5/15 | 519.02 | 586.47 | 435.15 | +26% vs 200-day average; below 50-day, distribution days, high-volume breakdown, volatility spike |
| IBM | WATCH | 247.13 | +1.0% | +6.3% | 5/9 | 4/15 | 236.52 | 257.02 | 223.65 | +2% vs 200-day average; death cross, MACD bearish, 20%+ off high |
| CEG | WATCH | 282.40 | +2.8% | +1.0% | 14/9 | 4/15 | 269.60 | 282.96 | 242.07 | +2% vs 200-day average; death cross, distribution days, 20%+ off high |
| TSLA | WATCH | 390.22 | -1.8% | +7.7% | 7/9 | 5/15 | 385.36 | 408.27 | 351.94 | +2% vs 200-day average; death cross, MACD bearish, distribution days, 20%+ off high |
| TSM | AVOID | 398.73 | -1.7% | -5.6% | 3/9 | 5/15 |  |  |  | -1% vs 200-day average; below 50-day, below 200-day, distribution days, volatility spike |
| BE | AVOID | 201.93 | -3.6% | -15.6% | 15/9 | 5/15 |  |  |  | -10% vs 200-day average; below 50-day, below 200-day, distribution days, 20%+ off high |
| SKHY | AVOID* | 137.71 | -3.2% | -6.7% | 17/9 | 3/10 |  |  |  | -16% vs 50-day average; below 50-day, distribution days, 20%+ off high (provisional: 89 days of history) |
| DELL | REDUCE | 371.17 | -0.7% | -26.8% | 1/9 | 7/15 |  |  |  | +9% vs 200-day average; below 50-day, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| SPCX | REDUCE* | 139.94 | +0.1% | -8.0% | 7/9 | 5/10 |  |  |  | -6% vs 50-day average; below 50-day, distribution days, 20%+ off high, below chandelier stop (provisional: 107 days of history) |
| ALAB | REDUCE | 227.79 | -1.4% | -24.1% | 9/9 | 8/15 |  |  |  | -11% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, below chandelier stop |
| ETN | REDUCE | 352.97 | -1.7% | -12.0% | 6/9 | 6/15 |  |  |  | -11% vs 200-day average; below 50-day, below 200-day, distribution days, 20%+ off high, volatility spike |
| MRVL | SELL | 156.76 | -4.7% | -35.0% | 2/9 | 9/15 |  |  |  | -16% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| GOOG | SELL | 295.35 | +1.6% | -14.1% | 10/9 | 10/15 |  |  |  | -12% vs 200-day average; below 50-day, below 200-day, death cross, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| GEV | SELL | 818.49 | +1.3% | -13.0% | 11/9 | 10/15 |  |  |  | -14% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, 20%+ off high, below chandelier stop |
| NVDA | SELL | 162.85 | -2.0% | -25.0% | 8/9 | 10/15 |  |  |  | -20% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, high-volume breakdown, 20%+ off high, below chandelier stop |
| VST | SELL | 134.51 | +0.8% | -11.4% | 16/9 | 11/15 |  |  |  | -11% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| FSLR | SELL | 171.39 | -0.5% | -4.1% | 9/9 | 10/15 |  |  |  | -20% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, 20%+ off high, below chandelier stop |

![Board label each week](board_history.png)

**Trading the labels** (2022-02-09 to 2026-11-13): buy on BUY, exit on SELL, REDUCE or AVOID, reviewed weekly with next-day execution and 5 bp costs.

| strategy | CAGR | Volatility | Sharpe | Max drawdown | Time invested | Avg holdings |
|---|---|---|---|---|---|---|
| Board strategy | +35.3% | 33.4% | 1.07 | -34.0% | 97% | 6.6 |
| Equal-weight watchlist | +44.2% | 34.2% | 1.24 | -36.8% | 100% | 15.0 |
| SPY (buy & hold) | +13.1% | 17.3% | 0.80 | -22.1% |  |  |

Sharpe difference vs equal weight: -0.17, 95% block-bootstrap CI [-0.72, +0.31].

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
AMD  WATCH  (score 5/15, close 534.06 on 2026-11-13)
  RSI 50 | -17.8% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [volume] Down day closing below the 50-day average on 1.5x+ average volume (+2)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
  Levels to watch:
    50-day SMA                 554.55  (price is below, -3.7%)
    Chandelier stop            468.19  (price is above, +14.1%)
    200-day SMA                423.12  (price is above, +26.2%)
```

```
NVDA  EXIT  (score 10/15, close 162.85 on 2026-11-13)
  RSI 25 | -31.9% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [volume] Down day closing below the 50-day average on 1.5x+ average volume (+2)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 214.63  (price is below, -24.1%)
    200-day SMA                203.92  (price is below, -20.1%)
    Chandelier stop            192.25  (price is below, -15.3%)
```

```
MRVL  EXIT  (score 9/15, close 156.76 on 2026-11-13)
  RSI 35 | -50.4% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 229.18  (price is below, -31.6%)
    Chandelier stop            202.15  (price is below, -22.5%)
    200-day SMA                186.93  (price is below, -16.1%)
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
FSLR  EXIT  (score 10/15, close 171.39 on 2026-11-13)
  RSI 41 | -46.1% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    200-day SMA                213.16  (price is below, -19.6%)
    Chandelier stop            184.75  (price is below, -7.2%)
    50-day SMA                 184.56  (price is below, -7.1%)
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
ETN  REDUCE  (score 6/15, close 352.97 on 2026-11-13)
  RSI 42 | -23.0% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
  Levels to watch:
    50-day SMA                 400.19  (price is below, -11.8%)
    200-day SMA                395.47  (price is below, -10.7%)
    Chandelier stop            347.01  (price is above, +1.7%)
```

```
TSLA  WATCH  (score 5/15, close 390.22 on 2026-11-13)
  RSI 54 | -20.3% from 52-week high
  Triggered:
    - [trend] 50-day average below the 200-day average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
  Levels to watch:
    200-day SMA                382.73  (price is above, +2.0%)
    50-day SMA                 374.74  (price is above, +4.1%)
    Chandelier stop            364.10  (price is above, +7.2%)
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
AMZN  HOLD  (score 1/15, close 266.66 on 2026-11-13)
  RSI 57 | -6.1% from 52-week high
  Triggered:
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
  Levels to watch:
    50-day SMA                 254.81  (price is above, +4.6%)
    Chandelier stop            248.09  (price is above, +7.5%)
    200-day SMA                244.60  (price is above, +9.0%)
```

```
IBM  WATCH  (score 4/15, close 247.13 on 2026-11-13)
  RSI 55 | -23.9% from 52-week high
  Triggered:
    - [trend] 50-day average below the 200-day average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [risk] 20%+ below the 52-week high (+1)
  Levels to watch:
    200-day SMA                243.20  (price is above, +1.6%)
    Chandelier stop            238.78  (price is above, +3.5%)
    50-day SMA                 236.52  (price is above, +4.5%)
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
TSM  WATCH  (score 5/15, close 398.73 on 2026-11-13)
  RSI 45 | -17.9% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
  Levels to watch:
    50-day SMA                 429.95  (price is below, -7.3%)
    200-day SMA                401.67  (price is below, -0.7%)
    Chandelier stop            389.56  (price is above, +2.4%)
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
| below_sma50 | 5d | 1076 | +0.36% | +0.69% | -0.34% | 0.038 | 0.181 | 40% | 36% | weak (not significant) |
| below_sma50 | 21d | 1055 | +2.12% | +3.08% | -0.96% | 0.008 | 0.140 | 40% | 36% | weak (not significant) |
| below_sma50 | 63d | 996 | +8.77% | +10.17% | -1.40% | 0.038 | 0.181 | 40% | 36% | weak (not significant) |
| below_sma200 | 5d | 521 | +0.60% | +0.63% | -0.03% | 0.467 | 0.964 | 39% | 36% | weak (not significant) |
| below_sma200 | 21d | 500 | +1.21% | +2.77% | -1.56% | 0.005 | 0.140 | 39% | 36% | weak (not significant) |
| below_sma200 | 63d | 474 | +9.50% | +9.06% | +0.44% | 0.654 | 1.000 | 39% | 36% | no edge |
| death_cross | 5d | 155 | +0.68% | +0.65% | +0.03% | 0.535 | 0.981 | 43% | 36% | no edge |
| death_cross | 21d | 149 | +0.80% | +2.89% | -2.10% | 0.019 | 0.181 | 43% | 36% | weak (not significant) |
| death_cross | 63d | 143 | +14.56% | +9.68% | +4.88% | 0.980 | 1.000 | 43% | 36% | no edge |
| rsi_divergence | 5d | 502 | +0.43% | +0.79% | -0.36% | 0.101 | 0.363 | 37% | 36% | weak (not significant) |
| rsi_divergence | 21d | 495 | +3.26% | +3.51% | -0.25% | 0.348 | 0.884 | 37% | 36% | weak (not significant) |
| rsi_divergence | 63d | 487 | +10.96% | +11.74% | -0.78% | 0.249 | 0.686 | 37% | 36% | weak (not significant) |
| rsi_rollover | 5d | 644 | +1.84% | +0.76% | +1.08% | 1.000 | 1.000 | 33% | 36% | no edge |
| rsi_rollover | 21d | 634 | +3.70% | +3.40% | +0.30% | 0.730 | 1.000 | 33% | 36% | no edge |
| rsi_rollover | 63d | 621 | +10.41% | +11.69% | -1.27% | 0.110 | 0.363 | 33% | 36% | weak (not significant) |
| macd_bearish | 5d | 1624 | +0.88% | +0.72% | +0.16% | 0.854 | 1.000 | 35% | 36% | no edge |
| macd_bearish | 21d | 1603 | +3.24% | +3.24% | +0.00% | 0.499 | 0.968 | 35% | 36% | no edge |
| macd_bearish | 63d | 1522 | +11.55% | +10.77% | +0.78% | 0.889 | 1.000 | 35% | 36% | no edge |
| distribution_cluster | 5d | 1078 | +0.53% | +0.74% | -0.21% | 0.138 | 0.414 | 37% | 36% | weak (not significant) |
| distribution_cluster | 21d | 1063 | +2.51% | +3.24% | -0.73% | 0.038 | 0.181 | 37% | 36% | weak (not significant) |
| distribution_cluster | 63d | 1022 | +9.93% | +10.93% | -1.00% | 0.101 | 0.363 | 37% | 36% | weak (not significant) |
| high_volume_breakdown | 5d | 768 | +0.86% | +0.70% | +0.16% | 0.766 | 1.000 | 35% | 36% | no edge |
| high_volume_breakdown | 21d | 734 | +3.63% | +3.04% | +0.59% | 0.895 | 1.000 | 35% | 36% | no edge |
| high_volume_breakdown | 63d | 703 | +12.66% | +10.21% | +2.45% | 0.995 | 1.000 | 35% | 36% | no edge |
| drawdown_20 | 5d | 409 | +1.53% | +0.85% | +0.69% | 0.974 | 1.000 | 51% | 36% | no edge |
| drawdown_20 | 21d | 397 | +2.32% | +3.77% | -1.45% | 0.029 | 0.181 | 51% | 36% | weak (not significant) |
| drawdown_20 | 63d | 374 | +14.11% | +12.81% | +1.30% | 0.792 | 1.000 | 51% | 36% | no edge |
| volatility_spike | 5d | 345 | +1.01% | +0.78% | +0.23% | 0.757 | 1.000 | 47% | 36% | no edge |
| volatility_spike | 21d | 330 | +3.18% | +3.37% | -0.18% | 0.419 | 0.922 | 47% | 36% | weak (not significant) |
| volatility_spike | 63d | 327 | +11.06% | +11.44% | -0.38% | 0.407 | 0.922 | 47% | 36% | weak (not significant) |
| chandelier_stop | 5d | 1364 | +0.78% | +0.73% | +0.05% | 0.622 | 1.000 | 37% | 36% | no edge |
| chandelier_stop | 21d | 1343 | +3.32% | +3.23% | +0.09% | 0.618 | 1.000 | 37% | 36% | no edge |
| chandelier_stop | 63d | 1276 | +12.16% | +10.81% | +1.34% | 0.964 | 1.000 | 37% | 36% | no edge |

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

### AMD (2022-08-31 to 2026-11-13)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +548.3% | +56.2% | -63.0% | +58.5% | 1.05 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +400.7% | +46.9% | -39.1% | +49.0% | 1.03 | 1 | 65% | -0.02 | [-0.57, +0.48] | 0.93 |
| Close > 50-day SMA | +162.1% | +25.9% | -46.9% | +43.9% | 0.74 | 36 | 53% | -0.31 | [-0.89, +0.29] | 0.30 |
| MACD > signal | +304.0% | +39.5% | -42.4% | +41.6% | 1.01 | 39 | 50% | -0.05 | [-0.59, +0.50] | 0.87 |
| RSI 30/70 | +54.9% | +11.0% | -54.7% | +32.5% | 0.48 | 3 | 33% | -0.57 | [-1.62, +0.32] | 0.25 |
| Trailing stop 20% | +156.0% | +25.1% | -58.9% | +49.8% | 0.70 | 11 | 71% | -0.35 | [-0.85, +0.15] | 0.20 |
| Volume breakout | +177.7% | +27.6% | -36.9% | +37.1% | 0.84 | 10 | 38% | -0.21 | [-0.91, +0.41] | 0.51 |

### NVDA (2022-08-31 to 2026-11-13)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +1072.4% | +79.9% | -36.9% | +49.0% | 1.44 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +529.0% | +55.1% | -31.9% | +43.2% | 1.23 | 1 | 84% | -0.21 | [-0.70, +0.18] | 0.34 |
| Close > 50-day SMA | +346.8% | +42.9% | -39.1% | +39.0% | 1.11 | 38 | 69% | -0.33 | [-0.88, +0.21] | 0.26 |
| MACD > signal | +152.9% | +24.8% | -46.7% | +34.4% | 0.81 | 40 | 51% | -0.63 | [-1.36, +0.06] | 0.09 |
| RSI 30/70 | +43.5% | +9.0% | -22.6% | +18.7% | 0.55 | 2 | 8% | -0.89 | [-1.96, -0.04] | 0.08 |
| Trailing stop 20% | +621.1% | +60.2% | -36.6% | +44.9% | 1.27 | 8 | 90% | -0.17 | [-0.57, +0.15] | 0.32 |
| Volume breakout | +211.5% | +31.1% | -19.8% | +26.3% | 1.16 | 7 | 31% | -0.28 | [-1.10, +0.51] | 0.50 |

### MRVL (2022-08-31 to 2026-11-13)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +245.9% | +34.5% | -60.8% | +67.3% | 0.77 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +52.6% | +10.6% | -65.2% | +57.6% | 0.46 | 2 | 68% | -0.31 | [-0.79, +0.14] | 0.18 |
| Close > 50-day SMA | +65.8% | +12.8% | -51.5% | +52.7% | 0.49 | 36 | 57% | -0.29 | [-0.89, +0.27] | 0.33 |
| MACD > signal | +101.6% | +18.2% | -62.5% | +50.2% | 0.58 | 44 | 51% | -0.20 | [-0.89, +0.46] | 0.57 |
| RSI 30/70 | +63.2% | +12.4% | -32.1% | +29.1% | 0.55 | 2 | 19% | -0.22 | [-1.15, +0.79] | 0.66 |
| Trailing stop 20% | +75.6% | +14.4% | -53.3% | +57.0% | 0.52 | 15 | 77% | -0.26 | [-0.76, +0.22] | 0.28 |
| Volume breakout | +76.0% | +14.4% | -46.2% | +42.0% | 0.53 | 11 | 36% | -0.25 | [-1.07, +0.50] | 0.57 |

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

### FSLR (2022-08-31 to 2026-11-13)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +34.0% | +7.2% | -60.0% | +55.1% | 0.40 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +10.0% | +2.3% | -51.1% | +41.7% | 0.26 | 4 | 59% | -0.14 | [-0.75, +0.43] | 0.60 |
| Close > 50-day SMA | +30.0% | +6.5% | -46.8% | +40.4% | 0.35 | 29 | 50% | -0.04 | [-0.60, +0.48] | 0.86 |
| MACD > signal | -59.5% | -19.4% | -74.1% | +40.7% | -0.33 | 48 | 50% | -0.72 | [-1.37, -0.02] | 0.04 |
| RSI 30/70 | +30.1% | +6.5% | -42.8% | +30.4% | 0.35 | 2 | 27% | -0.05 | [-1.05, +0.78] | 0.93 |
| Trailing stop 20% | +11.9% | +2.7% | -52.3% | +45.2% | 0.28 | 11 | 69% | -0.12 | [-0.61, +0.37] | 0.62 |
| Volume breakout | -24.3% | -6.4% | -53.8% | +32.3% | -0.04 | 14 | 38% | -0.44 | [-1.32, +0.36] | 0.32 |

### ETN (2022-08-31 to 2026-11-13)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +169.8% | +26.7% | -34.5% | +33.9% | 0.87 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +67.4% | +13.1% | -35.7% | +30.4% | 0.56 | 2 | 83% | -0.31 | [-0.72, +0.03] | 0.10 |
| Close > 50-day SMA | +34.3% | +7.3% | -37.5% | +24.5% | 0.41 | 45 | 65% | -0.46 | [-1.06, +0.20] | 0.15 |
| MACD > signal | +37.3% | +7.9% | -25.8% | +22.3% | 0.45 | 48 | 50% | -0.42 | [-1.12, +0.25] | 0.21 |
| RSI 30/70 | +15.7% | +3.5% | -18.6% | +11.5% | 0.36 | 1 | 5% | -0.51 | [-1.41, +0.69] | 0.28 |
| Trailing stop 20% | +183.0% | +28.2% | -23.6% | +30.9% | 0.96 | 2 | 94% | +0.09 | [-0.11, +0.33] | 0.39 |
| Volume breakout | +21.6% | +4.8% | -29.3% | +18.1% | 0.35 | 10 | 38% | -0.52 | [-1.29, +0.30] | 0.20 |

### TSLA (2022-08-31 to 2026-11-13)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +40.7% | +8.5% | -65.0% | +58.3% | 0.43 | 0 | 100% |  |  |  |
| 50/200 SMA cross | -26.4% | -7.1% | -56.8% | +40.1% | 0.01 | 4 | 47% | -0.41 | [-1.33, +0.41] | 0.32 |
| Close > 50-day SMA | +59.3% | +11.8% | -41.1% | +38.5% | 0.48 | 43 | 52% | +0.05 | [-0.65, +0.84] | 0.90 |
| MACD > signal | +396.5% | +46.6% | -39.8% | +40.8% | 1.14 | 42 | 51% | +0.71 | [+0.07, +1.40] | 0.04 |
| RSI 30/70 | +51.5% | +10.4% | -52.7% | +40.2% | 0.45 | 4 | 43% | +0.02 | [-0.70, +0.71] | 0.96 |
| Trailing stop 20% | +43.5% | +9.0% | -47.9% | +45.0% | 0.42 | 11 | 71% | -0.01 | [-0.63, +0.58] | 0.97 |
| Volume breakout | +40.5% | +8.4% | -35.4% | +25.7% | 0.44 | 9 | 18% | +0.01 | [-0.88, +0.93] | 0.98 |

### AMZN (2022-08-31 to 2026-11-13)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +108.5% | +19.2% | -40.0% | +34.1% | 0.68 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +37.1% | +7.8% | -41.4% | +27.8% | 0.41 | 2 | 74% | -0.28 | [-0.91, +0.33] | 0.39 |
| Close > 50-day SMA | +33.8% | +7.2% | -41.0% | +23.2% | 0.41 | 35 | 63% | -0.27 | [-0.99, +0.43] | 0.46 |
| MACD > signal | -0.5% | -0.1% | -28.7% | +22.7% | 0.11 | 50 | 50% | -0.58 | [-1.29, +0.14] | 0.12 |
| RSI 30/70 | +94.0% | +17.1% | -22.0% | +21.6% | 0.84 | 4 | 33% | +0.15 | [-0.58, +0.89] | 0.68 |
| Trailing stop 20% | +114.0% | +19.9% | -24.2% | +29.8% | 0.76 | 3 | 87% | +0.07 | [-0.35, +0.51] | 0.73 |
| Volume breakout | +6.7% | +1.5% | -35.7% | +18.8% | 0.18 | 11 | 45% | -0.51 | [-1.45, +0.44] | 0.28 |

### IBM (2022-08-31 to 2026-11-13)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +121.0% | +20.8% | -37.5% | +31.5% | 0.76 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +62.3% | +12.2% | -28.7% | +22.8% | 0.62 | 3 | 72% | -0.14 | [-0.81, +0.52] | 0.69 |
| Close > 50-day SMA | +55.4% | +11.1% | -42.6% | +25.2% | 0.55 | 27 | 60% | -0.21 | [-0.72, +0.37] | 0.43 |
| MACD > signal | +112.3% | +19.7% | -43.1% | +23.9% | 0.88 | 30 | 50% | +0.11 | [-0.47, +0.84] | 0.72 |
| RSI 30/70 | +175.4% | +27.3% | -16.5% | +17.4% | 1.48 | 8 | 35% | +0.71 | [-0.28, +1.59] | 0.14 |
| Trailing stop 20% | +67.8% | +13.1% | -45.9% | +30.3% | 0.56 | 3 | 92% | -0.20 | [-0.45, +0.01] | 0.09 |
| Volume breakout | +67.4% | +13.1% | -25.6% | +17.0% | 0.81 | 10 | 40% | +0.04 | [-0.85, +0.92] | 0.92 |

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

### TSM (2022-08-31 to 2026-11-13)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +421.4% | +48.3% | -36.8% | +39.3% | 1.20 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +173.7% | +27.2% | -36.8% | +35.9% | 0.85 | 2 | 81% | -0.35 | [-0.88, +0.13] | 0.17 |
| Close > 50-day SMA | +190.3% | +29.0% | -28.8% | +31.5% | 0.96 | 37 | 68% | -0.24 | [-0.78, +0.33] | 0.40 |
| MACD > signal | +142.0% | +23.5% | -32.1% | +28.4% | 0.88 | 44 | 49% | -0.31 | [-0.92, +0.30] | 0.32 |
| RSI 30/70 | +46.0% | +9.5% | -23.0% | +16.8% | 0.62 | 3 | 13% | -0.58 | [-1.61, +0.35] | 0.26 |
| Trailing stop 20% | +219.6% | +32.0% | -30.6% | +36.7% | 0.94 | 6 | 91% | -0.26 | [-0.60, +0.09] | 0.14 |
| Volume breakout | +77.0% | +14.6% | -26.8% | +26.4% | 0.65 | 11 | 46% | -0.55 | [-1.31, +0.15] | 0.14 |

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
  80% range low                    -9.72%
  80% range high                   +10.82%
  daily volatility                 +8.00%
```

Best out-of-sample AUC **0.498**; smallest p-value against a naive baseline 0.813, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![ALAB feature effects](forecast_ALAB.png)

### AMD

Walk-forward test on 551 unseen days (2024-09-04 to 2026-11-12).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.519 | 0.532 | 0.739 | 0.496 | 0.25 | 1.37 | 1.257 |
| Logistic regression | 0.49 | 0.532 | 0.977 | 0.492 | 0.255 | 0.43 | 1.257 |
| Gradient boosting | 0.485 | 0.532 | 0.988 | 0.493 | 0.268 | 0.656 | 1.257 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 405.9 | 0.0 |  |  |
| Ridge regression | 408.1 | -0.0108 | 0.492 | 0.738 |
| Gradient boosting | 413.8 | -0.0393 | 0.479 | 0.98 |

Forecast for the next session:

```
  P(up) | Logistic regression      45.1%
  P(up) | Gradient boosting        49.1%
  P(up) | historical base rate     51.6%
  expected return (ridge)          -0.54%
  80% range low                    -9.85%
  80% range high                   +9.73%
  daily volatility                 +7.66%
```

Best out-of-sample AUC **0.493**; smallest p-value against a naive baseline 0.738, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![AMD feature effects](forecast_AMD.png)

### NVDA

Walk-forward test on 551 unseen days (2024-09-04 to 2026-11-12).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.523 | 0.523 | 0.517 | 0.505 | 0.25 | 0.665 | 0.666 |
| Logistic regression | 0.506 | 0.523 | 0.791 | 0.521 | 0.253 | 0.499 | 0.666 |
| Gradient boosting | 0.488 | 0.523 | 0.952 | 0.478 | 0.269 | 0.476 | 0.666 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 279.9 | 0.0 |  |  |
| Ridge regression | 280.2 | -0.0027 | 0.517 | 0.544 |
| Gradient boosting | 288.1 | -0.0598 | 0.519 | 0.967 |

Forecast for the next session:

```
  P(up) | Logistic regression      57.2%
  P(up) | Gradient boosting        60.9%
  P(up) | historical base rate     53.6%
  expected return (ridge)          -0.32%
  80% range low                    -4.47%
  80% range high                   +4.01%
  daily volatility                 +3.32%
```

Best out-of-sample AUC **0.521**; smallest p-value against a naive baseline 0.544, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![NVDA feature effects](forecast_NVDA.png)

### MRVL

Walk-forward test on 551 unseen days (2024-09-04 to 2026-11-12).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.534 | 0.534 | 0.517 | 0.47 | 0.249 | 0.858 | 0.859 |
| Logistic regression | 0.537 | 0.534 | 0.449 | 0.549 | 0.252 | 0.674 | 0.859 |
| Gradient boosting | 0.517 | 0.534 | 0.791 | 0.55 | 0.258 | 0.633 | 0.859 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 480.6 | 0.0 |  |  |
| Ridge regression | 486.6 | -0.0253 | 0.53 | 0.892 |
| Gradient boosting | 488.6 | -0.0336 | 0.517 | 0.921 |

Forecast for the next session:

```
  P(up) | Logistic regression      34.9%
  P(up) | Gradient boosting        18.5%
  P(up) | historical base rate     52.5%
  expected return (ridge)          -1.48%
  80% range low                    -10.73%
  80% range high                   +8.73%
  daily volatility                 +7.69%
```

Best out-of-sample AUC **0.550**; smallest p-value against a naive baseline 0.449, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![MRVL feature effects](forecast_MRVL.png)

### GOOG

Walk-forward test on 550 unseen days (2024-09-04 to 2026-11-11).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.525 | 0.525 | 0.517 | 0.489 | 0.25 | 1.071 | 1.072 |
| Logistic regression | 0.551 | 0.525 | 0.124 | 0.535 | 0.252 | 0.527 | 1.072 |
| Gradient boosting | 0.527 | 0.525 | 0.483 | 0.533 | 0.26 | 0.722 | 1.072 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 201.1 | 0.0 |  |  |
| Ridge regression | 203.3 | -0.0216 | 0.533 | 0.948 |
| Gradient boosting | 207.5 | -0.0644 | 0.511 | 0.997 |

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

Walk-forward test on 551 unseen days (2024-09-04 to 2026-11-12).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.517 | 0.517 | 0.517 | 0.458 | 0.25 |  | 0.107 |
| Logistic regression | 0.512 | 0.517 | 0.617 | 0.525 | 0.251 | -0.122 | 0.107 |
| Gradient boosting | 0.515 | 0.517 | 0.551 | 0.527 | 0.26 | -0.269 | 0.107 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 363.5 | 0.0 |  |  |
| Ridge regression | 364.4 | -0.0052 | 0.499 | 0.669 |
| Gradient boosting | 375.1 | -0.0651 | 0.521 | 0.998 |

Forecast for the next session:

```
  P(up) | Logistic regression      51.2%
  P(up) | Gradient boosting        60.5%
  P(up) | historical base rate     49.0%
  expected return (ridge)          +0.01%
  80% range low                    -3.63%
  80% range high                   +3.78%
  daily volatility                 +2.89%
```

Best out-of-sample AUC **0.527**; smallest p-value against a naive baseline 0.551, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![FSLR feature effects](forecast_FSLR.png)

### ETN

Walk-forward test on 551 unseen days (2024-09-04 to 2026-11-12).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.525 | 0.525 | 0.517 | 0.478 | 0.25 | 0.464 | 0.464 |
| Logistic regression | 0.515 | 0.525 | 0.681 | 0.519 | 0.254 | 0.717 | 0.464 |
| Gradient boosting | 0.512 | 0.525 | 0.739 | 0.53 | 0.258 | 0.357 | 0.464 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 246.8 | 0.0 |  |  |
| Ridge regression | 248.7 | -0.0159 | 0.539 | 0.833 |
| Gradient boosting | 253.2 | -0.0532 | 0.508 | 0.97 |

Forecast for the next session:

```
  P(up) | Logistic regression      55.4%
  P(up) | Gradient boosting        55.3%
  P(up) | historical base rate     54.0%
  expected return (ridge)          +0.10%
  80% range low                    -5.35%
  80% range high                   +5.87%
  daily volatility                 +4.37%
```

Best out-of-sample AUC **0.530**; smallest p-value against a naive baseline 0.681, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![ETN feature effects](forecast_ETN.png)

### TSLA

Walk-forward test on 551 unseen days (2024-09-04 to 2026-11-12).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.505 | 0.505 | 0.517 | 0.447 | 0.25 | 0.737 | 0.738 |
| Logistic regression | 0.521 | 0.505 | 0.234 | 0.51 | 0.253 | 0.667 | 0.738 |
| Gradient boosting | 0.515 | 0.505 | 0.32 | 0.526 | 0.262 | 0.924 | 0.738 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 369.7 | 0.0 |  |  |
| Ridge regression | 374.5 | -0.0266 | 0.49 | 0.953 |
| Gradient boosting | 377.9 | -0.0452 | 0.517 | 0.954 |

Forecast for the next session:

```
  P(up) | Logistic regression      48.7%
  P(up) | Gradient boosting        46.8%
  P(up) | historical base rate     50.9%
  expected return (ridge)          -0.06%
  80% range low                    -4.80%
  80% range high                   +4.91%
  daily volatility                 +3.79%
```

Best out-of-sample AUC **0.526**; smallest p-value against a naive baseline 0.234, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![TSLA feature effects](forecast_TSLA.png)

### AMZN

Walk-forward test on 551 unseen days (2024-09-04 to 2026-11-12).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.517 | 0.517 | 0.517 | 0.457 | 0.25 | 0.747 | 0.748 |
| Logistic regression | 0.546 | 0.517 | 0.093 | 0.557 | 0.249 | 1.12 | 0.748 |
| Gradient boosting | 0.526 | 0.517 | 0.351 | 0.524 | 0.262 | 0.587 | 0.748 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 211.9 | 0.0 |  |  |
| Ridge regression | 214.0 | -0.0203 | 0.548 | 0.897 |
| Gradient boosting | 222.3 | -0.101 | 0.512 | 1.0 |

Forecast for the next session:

```
  P(up) | Logistic regression      45.8%
  P(up) | Gradient boosting        57.2%
  P(up) | historical base rate     51.4%
  expected return (ridge)          -0.12%
  80% range low                    -3.40%
  80% range high                   +3.27%
  daily volatility                 +2.61%
```

Best out-of-sample AUC **0.557**; smallest p-value against a naive baseline 0.093, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![AMZN feature effects](forecast_AMZN.png)

### IBM

Walk-forward test on 551 unseen days (2024-09-04 to 2026-11-12).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.548 | 0.548 | 0.518 | 0.461 | 0.248 | 0.496 | 0.497 |
| Logistic regression | 0.526 | 0.548 | 0.858 | 0.47 | 0.254 | 0.622 | 0.497 |
| Gradient boosting | 0.512 | 0.548 | 0.96 | 0.505 | 0.263 | 0.488 | 0.497 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 253.2 | 0.0 |  |  |
| Ridge regression | 256.0 | -0.0216 | 0.525 | 0.935 |
| Gradient boosting | 257.8 | -0.0361 | 0.514 | 0.99 |

Forecast for the next session:

```
  P(up) | Logistic regression      59.0%
  P(up) | Gradient boosting        50.9%
  P(up) | historical base rate     55.3%
  expected return (ridge)          -0.14%
  80% range low                    -2.19%
  80% range high                   +1.96%
  daily volatility                 +1.62%
```

Best out-of-sample AUC **0.505**; smallest p-value against a naive baseline 0.858, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![IBM feature effects](forecast_IBM.png)

### GEV

Walk-forward test on 209 unseen days (2026-01-14 to 2026-11-11).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.536 | 0.536 | 0.528 | 0.469 | 0.249 | 0.809 | 0.81 |
| Logistic regression | 0.507 | 0.536 | 0.816 | 0.504 | 0.256 | 0.523 | 0.81 |
| Gradient boosting | 0.536 | 0.536 | 0.528 | 0.534 | 0.267 | 1.186 | 0.81 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 337.5 | 0.0 |  |  |
| Ridge regression | 343.7 | -0.0366 | 0.555 | 0.796 |
| Gradient boosting | 349.2 | -0.0705 | 0.531 | 0.892 |

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

Best out-of-sample AUC **0.534**; smallest p-value against a naive baseline 0.528, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![GEV feature effects](forecast_GEV.png)

### CEG

Walk-forward test on 506 unseen days (2024-11-05 to 2026-11-11).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.506 | 0.506 | 0.518 | 0.486 | 0.251 | 0.457 | 0.457 |
| Logistic regression | 0.474 | 0.506 | 0.929 | 0.501 | 0.259 | 0.066 | 0.457 |
| Gradient boosting | 0.47 | 0.506 | 0.95 | 0.462 | 0.276 | -0.156 | 0.457 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 352.0 | 0.0 |  |  |
| Ridge regression | 359.7 | -0.0439 | 0.478 | 0.98 |
| Gradient boosting | 362.8 | -0.0624 | 0.502 | 0.989 |

Forecast for the next session:

```
  P(up) | Logistic regression      53.8%
  P(up) | Gradient boosting        34.0%
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
| Gradient boosting | 0.515 | 0.518 | 0.585 | 0.519 | 0.268 | 1.065 | 0.744 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 392.7 | 0.0 |  |  |
| Ridge regression | 397.7 | -0.026 | 0.496 | 0.889 |
| Gradient boosting | 403.8 | -0.0574 | 0.502 | 0.993 |

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

Best out-of-sample AUC **0.519**; smallest p-value against a naive baseline 0.585, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![VST feature effects](forecast_VST.png)

### DELL

Walk-forward test on 550 unseen days (2024-09-04 to 2026-11-11).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.522 | 0.522 | 0.517 | 0.473 | 0.25 | 1.196 | 1.196 |
| Logistic regression | 0.505 | 0.522 | 0.791 | 0.51 | 0.255 | -0.018 | 1.196 |
| Gradient boosting | 0.5 | 0.522 | 0.857 | 0.506 | 0.266 | 0.554 | 1.196 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 407.7 | 0.0 |  |  |
| Ridge regression | 414.1 | -0.0316 | 0.493 | 0.985 |
| Gradient boosting | 420.4 | -0.0631 | 0.522 | 0.995 |

Forecast for the next session:

```
  P(up) | Logistic regression      49.1%
  P(up) | Gradient boosting        80.7%
  P(up) | historical base rate     51.8%
  expected return (ridge)          +0.31%
  80% range low                    -7.98%
  80% range high                   +9.34%
  daily volatility                 +6.73%
```

Best out-of-sample AUC **0.510**; smallest p-value against a naive baseline 0.791, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![DELL feature effects](forecast_DELL.png)

### TSM

Walk-forward test on 551 unseen days (2024-09-04 to 2026-11-12).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.503 | 0.534 | 0.932 | 0.479 | 0.25 | 1.168 | 1.234 |
| Logistic regression | 0.535 | 0.534 | 0.483 | 0.536 | 0.249 | 1.13 | 1.234 |
| Gradient boosting | 0.525 | 0.534 | 0.681 | 0.517 | 0.259 | 1.412 | 1.234 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 264.0 | 0.0 |  |  |
| Ridge regression | 262.6 | 0.0102 | 0.521 | 0.266 |
| Gradient boosting | 269.9 | -0.0454 | 0.517 | 0.982 |

Forecast for the next session:

```
  P(up) | Logistic regression      45.3%
  P(up) | Gradient boosting        51.3%
  P(up) | historical base rate     51.6%
  expected return (ridge)          +0.05%
  80% range low                    -4.83%
  80% range high                   +5.18%
  daily volatility                 +3.90%
```

Best out-of-sample AUC **0.536**; smallest p-value against a naive baseline 0.266, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

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
| Gradient boosting | 667.4 | -0.0407 | 0.496 | 0.983 |

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
| DELL | 1 | +1.15 | True | 371.17 | +269.4% | +50.2% | +86.3% | -36.8% |  | 336.01 | 502.96 | 265.7 | -20.9% | 14 | 4704.0 | 984.0 |  |
| AMD | 2 | +1.13 | True | 534.06 | +117.2% | +25.9% | +80.9% | -17.8% |  | 519.02 | 586.47 | 435.15 | -16.2% | 11 | 5709.0 | 923.0 |  |
| KO | 3 | +0.67 | True | 99.25 | +32.1% | +24.3% | +17.5% | +0.0% |  | 94.76 | 99.45 | 91.29 | -3.7% | 105 | 9950.0 | 364.0 |  |
| LLY | 4 | +0.63 | True | 1443.50 | +23.8% | +44.0% | +31.2% | +0.0% |  | 1354.69 | 1446.39 | 1266.17 | -6.5% | 7 | 9483.0 | 620.0 |  |
| V | 5 | +0.63 | True | 425.76 | +18.7% | +31.2% | +21.4% | -2.3% |  | 415.13 | 436.63 | 397.24 | -4.3% | 24 | 9963.0 | 429.0 |  |
| JNJ | 6 | +0.62 | True | 285.75 | +33.2% | +27.4% | +25.0% | +0.0% |  | 271.55 | 286.32 | 257.92 | -5.0% | 36 | 9776.0 | 491.0 |  |
| AAPL | 7 | +0.60 | True | 356.27 | +25.4% | +18.9% | +22.3% | +0.0% |  | 345.91 | 356.98 | 329.49 | -4.7% | 28 | 9686.0 | 460.0 |  |
| XOM | 8 | +0.59 | True | 170.59 | +52.2% | +8.7% | +26.4% | -8.9% |  | 169.38 | 187.62 | 160.76 | -5.1% | 59 | 9993.0 | 509.0 |  |
| MSFT | 9 | +0.50 | True | 523.88 | +6.4% | +24.7% | +26.8% | -5.7% |  | 519.0 | 556.91 | 488.56 | -5.9% | 19 | 9861.0 | 578.0 |  |
| PG | 10 | +0.32 | True | 169.80 | +8.5% | +21.6% | +20.5% | +0.0% |  | 163.19 | 170.14 | 156.73 | -4.0% | 61 | 9954.0 | 394.0 |  |
| UNH | 11 | +0.31 | True | 407.46 | +23.1% | +4.7% | +23.5% | -6.0% |  | 391.19 | 425.83 | 369.54 | -5.5% | 25 | 9780.0 | 541.0 |  |
| JPM | 12 | +0.26 | True | 346.19 | +6.7% | +17.4% | +20.4% | -4.7% |  | 339.7 | 352.81 | 325.49 | -4.2% | 29 | 9851.0 | 412.0 |  |
| LIN | 13 | +0.14 | True | 526.06 | +16.5% | +4.6% | +15.1% | -3.4% |  | 513.83 | 527.6 | 495.96 | -3.5% | 19 | 9763.0 | 340.0 |  |
| AMT | 14 | +0.10 | True | 191.64 | +2.9% | +14.6% | +28.9% | -1.7% |  | 187.43 | 195.25 | 177.69 | -5.2% | 53 | 9934.0 | 516.0 |  |
| COST | 15 | +0.09 | True | 1106.21 | +7.5% | +5.8% | +20.4% | +0.0% |  | 1031.44 | 1108.42 | 992.21 | -3.8% | 9 | 9283.0 | 353.0 |  |

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

Across 19,025 stock-days (18 watchlist stocks, 2021-11-16 to 2026-11-13), each 1% of opening gap went with a -0.03% move from the open to the close (95% block-bootstrap CI [-0.08%, +0.03%]): no reliable relationship, so the size of a gap has not told you which way the session goes.

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 777 | -5.2% | +0.35% | 50% |
| down 1-3% | 2912 | -1.7% | +0.09% | 52% |
| within 1% | 11032 | +0.0% | +0.02% | 50% |
| up 1-3% | 3373 | +1.7% | +0.09% | 52% |
| gap up 3%+ | 931 | +5.4% | -0.13% | 47% |

## 9. Deciding before the open vs at the previous close

From 2022-02-10 to 2026-11-12 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +34.9% a year (worst drawdown -34.2%) against +35.3% (-34.1%) for labels set at the previous close; the two agreed on 89% of stock-weeks. Sharpe ratio difference -0.02 (95% block-bootstrap CI [-0.20, +0.17]): deciding before the open has been **not distinguishable from deciding on the previous close**.

| strategy | CAGR | Volatility | Sharpe | Max drawdown |
|---|---|---|---|---|
| Board on the previous close | +35.3% | 34.5% | 1.05 | -34.1% |
| Board on the pre-market price | +34.9% | 35.0% | 1.03 | -34.2% |
| Equal-weight watchlist | +43.7% | 35.3% | 1.20 | -40.7% |

The pre-market version uses the official opening price as a stand-in for the last pre-market trade (free pre-market history is only days long), which slightly flatters it.
