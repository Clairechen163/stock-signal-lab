# stocklab report
Generated 2026-11-20 | data source: `yahoo` | history: 5 years | watchlist: ALAB, AMD, NVDA, MRVL, GOOG, FSLR, SKHY, ETN, TSLA, SPCX, AMZN, IBM, GEV, CEG, VST, DELL, TSM, BE

> Educational research code, not investment advice. Past results do not predict future returns.

## 1. Decision board

Data as of the 2026-11-19 close. `*` = provisional (under 200 trading days of history).

| ticker | action | close | 1 day | 1 month | buy rank | sell warnings | pullback entry | breakout | stop | why |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | BUY | 257.37 | -3.9% | -1.9% | 2/9 | 2/15 | 255.23 | 271.41 | 236.01 | buy rank 2/9; +5% vs 200-day average; distribution days, volatility spike |
| AMD | WATCH | 489.19 | -7.7% | -11.5% | 1/9 | 5/15 | 445.71 | 586.47 | 358.74 | +14% vs 200-day average; below 50-day, high-volume breakdown, 20%+ off high, volatility spike |
| SPCX | REDUCE* | 143.50 | +1.3% | -2.9% | 6/9 | 5/10 |  |  |  | -3% vs 50-day average; below 50-day, distribution days, 20%+ off high, below chandelier stop (provisional: 111 days of history) |
| TSLA | REDUCE | 374.41 | -2.4% | -3.1% | 7/9 | 8/15 |  |  |  | -2% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, 20%+ off high |
| ALAB | REDUCE | 216.75 | +2.4% | -23.9% | 13/9 | 7/15 |  |  |  | -16% vs 200-day average; below 50-day, below 200-day, distribution days, 20%+ off high, below chandelier stop |
| CEG | REDUCE | 262.74 | -2.0% | +1.7% | 14/9 | 7/15 |  |  |  | -5% vs 200-day average; below 50-day, below 200-day, death cross, distribution days, 20%+ off high |
| BE | REDUCE | 170.98 | -1.4% | -23.2% | 15/9 | 8/15 |  |  |  | -24% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, below chandelier stop |
| DELL | SELL | 313.11 | -3.0% | -32.2% | 1/9 | 9/15 |  |  |  | -9% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| MRVL | SELL | 138.47 | -4.9% | -43.4% | 3/9 | 9/15 |  |  |  | -26% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| TSM | SELL | 352.09 | -2.9% | -18.5% | 4/9 | 9/15 |  |  |  | -12% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| IBM | SELL | 223.88 | -2.0% | -10.4% | 5/9 | 9/15 |  |  |  | -7% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, 20%+ off high, below chandelier stop |
| ETN | SELL | 330.57 | -2.3% | -15.8% | 6/9 | 11/15 |  |  |  | -16% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| GOOG | SELL | 279.20 | +0.6% | -17.0% | 10/9 | 10/15 |  |  |  | -17% vs 200-day average; below 50-day, below 200-day, death cross, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| GEV | SELL | 772.22 | -1.0% | -13.2% | 11/9 | 11/15 |  |  |  | -19% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| NVDA | SELL | 145.98 | -3.3% | -34.2% | 8/9 | 10/15 |  |  |  | -28% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, high-volume breakdown, 20%+ off high, below chandelier stop |
| VST | SELL | 125.58 | -1.2% | -16.5% | 16/9 | 11/15 |  |  |  | -17% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| SKHY | SELL* | 122.47 | -0.1% | -12.4% | 17/9 | 6/10 |  |  |  | -24% vs 50-day average; below 50-day, MACD bearish, distribution days, 20%+ off high, below chandelier stop (provisional: 93 days of history) |
| FSLR | SELL | 151.95 | +0.6% | -13.1% | 9/9 | 10/15 |  |  |  | -28% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, 20%+ off high, below chandelier stop |

![Board label each week](board_history.png)

**Trading the labels** (2022-02-16 to 2026-11-19): buy on BUY, exit on SELL, REDUCE or AVOID, reviewed weekly with next-day execution and 5 bp costs.

| strategy | CAGR | Volatility | Sharpe | Max drawdown | Time invested | Avg holdings |
|---|---|---|---|---|---|---|
| Board strategy | +35.6% | 33.5% | 1.08 | -32.2% | 97% | 6.6 |
| Equal-weight watchlist | +42.4% | 34.2% | 1.21 | -36.8% | 100% | 15.1 |
| SPY (buy & hold) | +12.5% | 17.3% | 0.77 | -22.1% |  |  |

Sharpe difference vs equal weight: -0.13, 95% block-bootstrap CI [-0.67, +0.37].

Forward 21-day return after each label, relative to the watchlist average on the same date (sampled every 21 days, t-test across dates):

| label | observations | dates | mean 21d excess return | hit rate | p_value |
|---|---|---|---|---|---|
| BUY | 235 | 52 | +0.5% | 58% | 0.58 |
| HOLD | 120 | 42 | -0.2% | 52% | 0.90 |
| WATCH | 190 | 50 | +0.1% | 44% | 0.92 |
| AVOID | 43 | 23 | +0.3% | 39% | 0.91 |
| REDUCE | 168 | 52 | -1.0% | 37% | 0.44 |
| SELL | 83 | 35 | +2.1% | 51% | 0.60 |

![Board strategy vs holding](board_equity.png)

## 2. Sell check, stock by stock

```
ALAB  REDUCE  (score 7/15, close 216.75 on 2026-11-18)
  RSI 41 | -55.1% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 288.88  (price is below, -25.0%)
    200-day SMA                258.31  (price is below, -16.1%)
    Chandelier stop            232.09  (price is below, -6.6%)
```

```
AMD  WATCH  (score 5/15, close 489.19 on 2026-11-19)
  RSI 45 | -24.7% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [volume] Down day closing below the 50-day average on 1.5x+ average volume (+2)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
  Levels to watch:
    50-day SMA                 554.93  (price is below, -11.8%)
    Chandelier stop            463.55  (price is above, +5.5%)
    200-day SMA                428.63  (price is above, +14.1%)
```

```
NVDA  EXIT  (score 10/15, close 145.98 on 2026-11-19)
  RSI 20 | -39.0% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [volume] Down day closing below the 50-day average on 1.5x+ average volume (+2)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 208.86  (price is below, -30.1%)
    200-day SMA                203.32  (price is below, -28.2%)
    Chandelier stop            192.56  (price is below, -24.2%)
```

```
MRVL  EXIT  (score 9/15, close 138.47 on 2026-11-19)
  RSI 32 | -56.2% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 222.53  (price is below, -37.8%)
    Chandelier stop            205.92  (price is below, -32.8%)
    200-day SMA                188.29  (price is below, -26.5%)
```

```
GOOG  EXIT  (score 10/15, close 279.20 on 2026-11-18)
  RSI 33 | -29.9% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    200-day SMA                335.21  (price is below, -16.7%)
    50-day SMA                 321.89  (price is below, -13.3%)
    Chandelier stop            312.16  (price is below, -10.6%)
```

```
FSLR  EXIT  (score 10/15, close 151.95 on 2026-11-19)
  RSI 31 | -52.3% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    200-day SMA                211.58  (price is below, -28.2%)
    Chandelier stop            185.76  (price is below, -18.2%)
    50-day SMA                 180.37  (price is below, -15.8%)
```

```
SKHY  EXIT  (score 6/10, close 122.47 on 2026-11-18)
  RSI 38 | -38.3% from high since listing
  Only 93 trading days of history; not scored yet: below_sma200, death_cross, volatility_spike
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the high since listing (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 160.13  (price is below, -23.5%)
    Chandelier stop            137.28  (price is below, -10.8%)
```

```
ETN  EXIT  (score 11/15, close 330.57 on 2026-11-19)
  RSI 36 | -27.9% from 52-week high
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
    200-day SMA                395.08  (price is below, -16.3%)
    50-day SMA                 394.00  (price is below, -16.1%)
    Chandelier stop            345.71  (price is below, -4.4%)
```

```
TSLA  REDUCE  (score 8/15, close 374.41 on 2026-11-19)
  RSI 47 | -23.6% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
  Levels to watch:
    200-day SMA                381.92  (price is below, -2.0%)
    50-day SMA                 376.03  (price is below, -0.4%)
    Chandelier stop            365.79  (price is above, +2.4%)
```

```
SPCX  REDUCE  (score 5/10, close 143.50 on 2026-11-18)
  RSI 51 | -32.1% from high since listing
  Only 111 trading days of history; not scored yet: below_sma200, death_cross, volatility_spike
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the high since listing (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 148.38  (price is below, -3.3%)
    Chandelier stop            143.82  (price is below, -0.2%)
```

```
AMZN  HOLD  (score 2/15, close 257.37 on 2026-11-19)
  RSI 49 | -9.4% from 52-week high
  Triggered:
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
  Levels to watch:
    50-day SMA                 255.23  (price is above, +0.8%)
    Chandelier stop            246.52  (price is above, +4.4%)
    200-day SMA                245.03  (price is above, +5.0%)
```

```
IBM  EXIT  (score 9/15, close 223.88 on 2026-11-19)
  RSI 33 | -31.0% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    200-day SMA                241.96  (price is below, -7.5%)
    Chandelier stop            237.51  (price is below, -5.7%)
    50-day SMA                 236.35  (price is below, -5.3%)
```

```
GEV  EXIT  (score 11/15, close 772.22 on 2026-11-18)
  RSI 39 | -34.2% from 52-week high
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
    200-day SMA                951.26  (price is below, -18.8%)
    50-day SMA                 901.85  (price is below, -14.4%)
    Chandelier stop            773.63  (price is below, -0.2%)
```

```
CEG  REDUCE  (score 7/15, close 262.74 on 2026-11-18)
  RSI 48 | -30.2% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
  Levels to watch:
    200-day SMA                277.43  (price is below, -5.3%)
    50-day SMA                 267.46  (price is below, -1.8%)
    Chandelier stop            246.70  (price is above, +6.5%)
```

```
VST  EXIT  (score 11/15, close 125.58 on 2026-11-18)
  RSI 41 | -30.0% from 52-week high
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
    200-day SMA                151.17  (price is below, -16.9%)
    50-day SMA                 141.80  (price is below, -11.4%)
    Chandelier stop            136.58  (price is below, -8.1%)
```

```
DELL  EXIT  (score 9/15, close 313.11 on 2026-11-18)
  RSI 33 | -46.7% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 480.34  (price is below, -34.8%)
    Chandelier stop            407.46  (price is below, -23.2%)
    200-day SMA                345.65  (price is below, -9.4%)
```

```
TSM  EXIT  (score 9/15, close 352.09 on 2026-11-19)
  RSI 34 | -27.5% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 424.37  (price is below, -17.0%)
    200-day SMA                402.29  (price is below, -12.5%)
    Chandelier stop            387.07  (price is below, -9.0%)
```

```
BE  REDUCE  (score 8/15, close 170.98 on 2026-11-18)
  RSI 39 | -50.6% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 238.50  (price is below, -28.3%)
    200-day SMA                223.76  (price is below, -23.6%)
    Chandelier stop            179.49  (price is below, -4.7%)
```

## 3. Which sell signals actually work? (event study)

Panel: 46 stocks, 5 years. Null hypothesis: returns after a signal look like returns on random days from the same stocks.

| rule | horizon | events | mean_after_signal | mean_random_days | difference | p_value | q_value | drop10_after_signal | drop10_base_rate | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| below_sma50 | 5d | 1076 | +0.22% | +0.68% | -0.46% | 0.008 | 0.088 | 40% | 36% | useful |
| below_sma50 | 21d | 1059 | +2.07% | +3.07% | -1.00% | 0.006 | 0.088 | 40% | 36% | useful |
| below_sma50 | 63d | 1003 | +8.50% | +10.15% | -1.65% | 0.019 | 0.161 | 40% | 36% | weak (not significant) |
| below_sma200 | 5d | 521 | +0.39% | +0.60% | -0.21% | 0.219 | 0.724 | 39% | 36% | weak (not significant) |
| below_sma200 | 21d | 504 | +1.14% | +2.75% | -1.61% | 0.001 | 0.049 | 39% | 36% | useful |
| below_sma200 | 63d | 475 | +9.24% | +9.05% | +0.18% | 0.569 | 0.988 | 39% | 36% | no edge |
| death_cross | 5d | 156 | +0.01% | +0.63% | -0.62% | 0.102 | 0.464 | 44% | 36% | weak (not significant) |
| death_cross | 21d | 149 | +0.95% | +2.91% | -1.96% | 0.033 | 0.206 | 44% | 36% | weak (not significant) |
| death_cross | 63d | 142 | +13.59% | +9.65% | +3.94% | 0.956 | 1.000 | 44% | 36% | no edge |
| rsi_divergence | 5d | 503 | +0.43% | +0.76% | -0.33% | 0.112 | 0.464 | 37% | 36% | weak (not significant) |
| rsi_divergence | 21d | 494 | +3.26% | +3.50% | -0.24% | 0.344 | 0.861 | 37% | 36% | weak (not significant) |
| rsi_divergence | 63d | 486 | +10.97% | +11.64% | -0.66% | 0.287 | 0.861 | 37% | 36% | weak (not significant) |
| rsi_rollover | 5d | 645 | +1.83% | +0.74% | +1.09% | 1.000 | 1.000 | 33% | 36% | no edge |
| rsi_rollover | 21d | 635 | +3.70% | +3.41% | +0.29% | 0.716 | 0.988 | 33% | 36% | no edge |
| rsi_rollover | 63d | 621 | +10.41% | +11.55% | -1.14% | 0.129 | 0.475 | 33% | 36% | weak (not significant) |
| macd_bearish | 5d | 1620 | +0.81% | +0.70% | +0.11% | 0.778 | 0.988 | 36% | 36% | no edge |
| macd_bearish | 21d | 1603 | +3.23% | +3.22% | +0.01% | 0.506 | 0.928 | 36% | 36% | no edge |
| macd_bearish | 63d | 1530 | +11.20% | +10.76% | +0.44% | 0.745 | 0.988 | 36% | 36% | no edge |
| distribution_cluster | 5d | 1079 | +0.92% | +0.70% | +0.22% | 0.872 | 1.000 | 35% | 36% | no edge |
| distribution_cluster | 21d | 1066 | +3.20% | +3.25% | -0.05% | 0.453 | 0.928 | 35% | 36% | weak (not significant) |
| distribution_cluster | 63d | 1022 | +10.50% | +10.82% | -0.33% | 0.355 | 0.861 | 35% | 36% | weak (not significant) |
| high_volume_breakdown | 5d | 766 | +0.82% | +0.67% | +0.15% | 0.755 | 0.988 | 34% | 36% | no edge |
| high_volume_breakdown | 21d | 734 | +3.64% | +3.01% | +0.63% | 0.905 | 1.000 | 34% | 36% | no edge |
| high_volume_breakdown | 63d | 702 | +12.61% | +10.05% | +2.56% | 0.993 | 1.000 | 34% | 36% | no edge |
| drawdown_20 | 5d | 405 | +1.33% | +0.81% | +0.52% | 0.925 | 1.000 | 52% | 36% | no edge |
| drawdown_20 | 21d | 395 | +2.32% | +3.74% | -1.42% | 0.037 | 0.206 | 52% | 36% | weak (not significant) |
| drawdown_20 | 63d | 374 | +13.53% | +12.76% | +0.77% | 0.690 | 0.988 | 52% | 36% | no edge |
| volatility_spike | 5d | 350 | +0.93% | +0.75% | +0.18% | 0.712 | 0.988 | 47% | 36% | no edge |
| volatility_spike | 21d | 331 | +3.16% | +3.35% | -0.19% | 0.406 | 0.893 | 47% | 36% | weak (not significant) |
| volatility_spike | 63d | 329 | +10.78% | +11.33% | -0.55% | 0.365 | 0.861 | 47% | 36% | weak (not significant) |
| chandelier_stop | 5d | 1356 | +0.69% | +0.70% | -0.00% | 0.501 | 0.928 | 37% | 36% | weak (not significant) |
| chandelier_stop | 21d | 1338 | +3.34% | +3.22% | +0.12% | 0.637 | 0.988 | 37% | 36% | no edge |
| chandelier_stop | 63d | 1272 | +11.98% | +10.74% | +1.24% | 0.951 | 1.000 | 37% | 36% | no edge |

**3 of 33 rule-by-horizon tests** show significantly weaker returns after the signal (q < 0.10).

![Sell signal event study](sell_event_study.png)

## 4. Strategy backtests

Not included: SKHY (only 93 trading days of history, needs 452); SPCX (only 111 trading days of history, needs 452).

### ALAB (2025-01-03 to 2026-11-18)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +50.8% | +24.6% | -63.2% | +97.0% | 0.71 | 0 | 100% |  |  |  |
| 50/200 SMA cross | -66.9% | -44.6% | -74.0% | +87.7% | -0.23 | 2 | 76% | -0.94 | [-1.87, -0.21] | 0.02 |
| Close > 50-day SMA | +7.6% | +4.0% | -66.4% | +69.6% | 0.41 | 10 | 51% | -0.31 | [-1.34, +0.65] | 0.55 |
| MACD > signal | +20.0% | +10.2% | -70.4% | +64.9% | 0.47 | 22 | 49% | -0.24 | [-1.38, +0.94] | 0.69 |
| RSI 30/70 | +11.1% | +5.8% | -50.3% | +38.0% | 0.34 | 1 | 17% | -0.38 | [-2.13, +1.43] | 0.66 |
| Trailing stop 20% | -11.8% | -6.5% | -69.1% | +71.5% | 0.27 | 10 | 55% | -0.45 | [-1.46, +0.52] | 0.39 |
| Volume breakout | +91.8% | +41.7% | -55.7% | +62.9% | 0.86 | 4 | 41% | +0.15 | [-1.01, +1.29] | 0.79 |

### AMD (2022-09-08 to 2026-11-19)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +472.2% | +51.7% | -63.0% | +58.7% | 1.00 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +358.6% | +43.9% | -39.1% | +49.3% | 0.98 | 1 | 66% | -0.02 | [-0.57, +0.54] | 0.96 |
| Close > 50-day SMA | +147.4% | +24.2% | -49.9% | +44.0% | 0.71 | 37 | 54% | -0.29 | [-0.89, +0.29] | 0.36 |
| MACD > signal | +270.1% | +36.7% | -42.4% | +42.0% | 0.95 | 39 | 51% | -0.05 | [-0.57, +0.46] | 0.85 |
| RSI 30/70 | +41.8% | +8.7% | -54.7% | +33.0% | 0.42 | 3 | 34% | -0.58 | [-1.60, +0.30] | 0.24 |
| Trailing stop 20% | +125.9% | +21.5% | -58.9% | +50.0% | 0.64 | 11 | 71% | -0.36 | [-0.90, +0.12] | 0.17 |
| Volume breakout | +161.9% | +25.9% | -36.9% | +37.2% | 0.80 | 11 | 38% | -0.20 | [-0.87, +0.45] | 0.58 |

### NVDA (2022-09-08 to 2026-11-19)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +917.8% | +74.1% | -39.0% | +49.1% | 1.37 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +463.8% | +51.2% | -39.0% | +43.3% | 1.17 | 1 | 84% | -0.20 | [-0.65, +0.21] | 0.35 |
| Close > 50-day SMA | +346.8% | +43.0% | -39.1% | +39.0% | 1.11 | 38 | 69% | -0.26 | [-0.90, +0.43] | 0.43 |
| MACD > signal | +152.9% | +24.8% | -46.7% | +34.4% | 0.81 | 40 | 51% | -0.56 | [-1.39, +0.22] | 0.17 |
| RSI 30/70 | +41.4% | +8.6% | -22.2% | +17.9% | 0.55 | 2 | 7% | -0.83 | [-2.03, +0.08] | 0.12 |
| Trailing stop 20% | +593.2% | +58.8% | -36.6% | +44.9% | 1.25 | 8 | 90% | -0.12 | [-0.52, +0.24] | 0.52 |
| Volume breakout | +211.5% | +31.2% | -19.8% | +26.3% | 1.16 | 7 | 31% | -0.21 | [-1.14, +0.67] | 0.64 |

### MRVL (2022-09-08 to 2026-11-19)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +182.4% | +28.1% | -60.8% | +67.4% | 0.70 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +34.8% | +7.4% | -65.2% | +57.8% | 0.41 | 2 | 68% | -0.29 | [-0.76, +0.17] | 0.21 |
| Close > 50-day SMA | +65.8% | +12.8% | -51.5% | +52.7% | 0.49 | 36 | 58% | -0.21 | [-0.86, +0.34] | 0.48 |
| MACD > signal | +101.6% | +18.2% | -62.5% | +50.2% | 0.58 | 44 | 51% | -0.12 | [-0.85, +0.56] | 0.74 |
| RSI 30/70 | +44.2% | +9.1% | -32.1% | +29.5% | 0.45 | 2 | 20% | -0.26 | [-1.18, +0.77] | 0.59 |
| Trailing stop 20% | +62.3% | +12.3% | -53.3% | +57.0% | 0.48 | 15 | 76% | -0.22 | [-0.73, +0.24] | 0.38 |
| Volume breakout | +76.0% | +14.5% | -46.2% | +42.0% | 0.53 | 11 | 36% | -0.17 | [-1.04, +0.66] | 0.67 |

### GOOG (2022-09-08 to 2026-11-18)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +152.0% | +24.7% | -30.3% | +31.7% | 0.86 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +151.5% | +24.7% | -29.4% | +25.9% | 0.98 | 2 | 76% | +0.12 | [-0.37, +0.61] | 0.63 |
| Close > 50-day SMA | +85.6% | +15.9% | -22.2% | +23.6% | 0.74 | 34 | 63% | -0.11 | [-0.83, +0.58] | 0.77 |
| MACD > signal | +29.9% | +6.4% | -21.6% | +21.6% | 0.40 | 42 | 50% | -0.46 | [-1.17, +0.23] | 0.20 |
| RSI 30/70 | +27.3% | +5.9% | -20.4% | +18.3% | 0.41 | 4 | 26% | -0.45 | [-1.27, +0.43] | 0.31 |
| Trailing stop 20% | +41.4% | +8.6% | -40.4% | +29.7% | 0.43 | 6 | 92% | -0.43 | [-0.88, -0.03] | 0.05 |
| Volume breakout | +105.6% | +18.8% | -17.4% | +19.4% | 0.98 | 8 | 46% | +0.13 | [-0.68, +0.94] | 0.74 |

### FSLR (2022-09-08 to 2026-11-19)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +11.8% | +2.7% | -60.0% | +55.2% | 0.32 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +3.5% | +0.8% | -51.1% | +41.6% | 0.22 | 4 | 58% | -0.10 | [-0.72, +0.47] | 0.73 |
| Close > 50-day SMA | +22.3% | +4.9% | -46.8% | +40.3% | 0.32 | 29 | 49% | -0.00 | [-0.62, +0.54] | 1.00 |
| MACD > signal | -61.6% | -20.4% | -74.1% | +40.8% | -0.36 | 49 | 50% | -0.68 | [-1.35, +0.01] | 0.05 |
| RSI 30/70 | +30.1% | +6.5% | -42.8% | +30.4% | 0.35 | 2 | 27% | +0.03 | [-0.97, +0.87] | 0.95 |
| Trailing stop 20% | -7.2% | -1.8% | -57.9% | +45.3% | 0.18 | 12 | 69% | -0.14 | [-0.67, +0.32] | 0.58 |
| Volume breakout | -28.7% | -7.8% | -53.8% | +32.2% | -0.09 | 14 | 37% | -0.41 | [-1.27, +0.36] | 0.35 |

### ETN (2022-09-08 to 2026-11-19)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +140.7% | +23.3% | -34.5% | +34.0% | 0.79 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +56.8% | +11.3% | -35.7% | +30.5% | 0.51 | 2 | 84% | -0.28 | [-0.69, +0.09] | 0.15 |
| Close > 50-day SMA | +31.0% | +6.7% | -37.5% | +24.5% | 0.39 | 44 | 65% | -0.40 | [-0.99, +0.27] | 0.22 |
| MACD > signal | +37.2% | +7.9% | -25.8% | +22.4% | 0.45 | 49 | 50% | -0.34 | [-1.06, +0.43] | 0.35 |
| RSI 30/70 | +15.7% | +3.6% | -18.6% | +11.5% | 0.36 | 1 | 5% | -0.43 | [-1.39, +0.69] | 0.40 |
| Trailing stop 20% | +169.5% | +26.7% | -23.6% | +30.8% | 0.92 | 2 | 94% | +0.14 | [-0.08, +0.42] | 0.28 |
| Volume breakout | +21.6% | +4.8% | -29.3% | +18.1% | 0.35 | 10 | 38% | -0.44 | [-1.24, +0.47] | 0.31 |

### TSLA (2022-09-08 to 2026-11-19)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +24.9% | +5.4% | -65.0% | +58.2% | 0.38 | 0 | 100% |  |  |  |
| 50/200 SMA cross | -26.4% | -7.1% | -56.8% | +40.1% | 0.01 | 4 | 47% | -0.37 | [-1.27, +0.49] | 0.39 |
| Close > 50-day SMA | +46.3% | +9.5% | -41.1% | +38.5% | 0.43 | 42 | 53% | +0.05 | [-0.72, +0.79] | 0.91 |
| MACD > signal | +396.5% | +46.6% | -39.8% | +40.8% | 1.14 | 42 | 51% | +0.76 | [+0.12, +1.47] | 0.04 |
| RSI 30/70 | +45.4% | +9.4% | -52.7% | +40.3% | 0.42 | 4 | 43% | +0.04 | [-0.73, +0.81] | 0.92 |
| Trailing stop 20% | +27.3% | +5.9% | -47.9% | +45.0% | 0.35 | 11 | 71% | -0.03 | [-0.67, +0.60] | 0.94 |
| Volume breakout | +40.5% | +8.5% | -35.4% | +25.7% | 0.44 | 9 | 18% | +0.06 | [-0.86, +0.97] | 0.90 |

### AMZN (2022-09-08 to 2026-11-19)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +93.0% | +17.0% | -40.0% | +34.2% | 0.63 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +32.3% | +6.9% | -41.4% | +28.0% | 0.38 | 2 | 74% | -0.25 | [-0.93, +0.40] | 0.41 |
| Close > 50-day SMA | +24.3% | +5.3% | -41.5% | +23.4% | 0.34 | 34 | 63% | -0.29 | [-0.98, +0.39] | 0.41 |
| MACD > signal | -3.9% | -1.0% | -28.7% | +23.0% | 0.07 | 50 | 50% | -0.56 | [-1.27, +0.14] | 0.13 |
| RSI 30/70 | +94.0% | +17.1% | -22.0% | +21.6% | 0.84 | 4 | 33% | +0.21 | [-0.54, +0.97] | 0.57 |
| Trailing stop 20% | +98.1% | +17.7% | -24.2% | +29.9% | 0.69 | 3 | 87% | +0.07 | [-0.34, +0.50] | 0.76 |
| Volume breakout | +2.9% | +0.7% | -36.2% | +19.0% | 0.13 | 11 | 46% | -0.50 | [-1.44, +0.40] | 0.29 |

### IBM (2022-09-08 to 2026-11-19)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +100.9% | +18.1% | -37.5% | +31.6% | 0.69 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +62.9% | +12.4% | -28.7% | +22.8% | 0.63 | 3 | 72% | -0.06 | [-0.80, +0.64] | 0.87 |
| Close > 50-day SMA | +43.6% | +9.0% | -43.2% | +25.3% | 0.47 | 28 | 60% | -0.22 | [-0.68, +0.33] | 0.42 |
| MACD > signal | +112.3% | +19.7% | -43.1% | +23.9% | 0.88 | 30 | 50% | +0.19 | [-0.39, +1.03] | 0.59 |
| RSI 30/70 | +175.4% | +27.4% | -16.5% | +17.4% | 1.48 | 8 | 35% | +0.79 | [-0.24, +1.65] | 0.10 |
| Trailing stop 20% | +52.5% | +10.6% | -45.9% | +30.4% | 0.49 | 3 | 92% | -0.20 | [-0.45, +0.02] | 0.10 |
| Volume breakout | +54.7% | +11.0% | -30.2% | +17.2% | 0.69 | 11 | 40% | +0.00 | [-0.87, +0.91] | 1.00 |

### GEV (2025-01-13 to 2026-11-18)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +102.7% | +46.5% | -38.3% | +56.0% | 0.96 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +133.0% | +58.0% | -38.3% | +54.5% | 1.11 | 1 | 97% | +0.15 | [-0.00, +0.44] | 0.17 |
| Close > 50-day SMA | +79.1% | +37.0% | -32.7% | +43.6% | 0.94 | 15 | 63% | -0.02 | [-0.64, +0.58] | 0.95 |
| MACD > signal | +60.6% | +29.2% | -31.0% | +41.8% | 0.82 | 17 | 47% | -0.14 | [-0.88, +0.67] | 0.72 |
| RSI 30/70 | +20.2% | +10.5% | -35.0% | +35.0% | 0.46 | 1 | 32% | -0.50 | [-1.68, +0.66] | 0.41 |
| Trailing stop 20% | +44.2% | +21.9% | -45.9% | +49.8% | 0.65 | 5 | 86% | -0.32 | [-0.88, +0.21] | 0.25 |
| Volume breakout | +24.5% | +12.6% | -24.6% | +33.3% | 0.53 | 3 | 35% | -0.44 | [-1.66, +0.73] | 0.47 |

### CEG (2022-11-02 to 2026-11-18)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +187.2% | +29.9% | -50.7% | +49.3% | 0.78 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +96.8% | +18.3% | -50.7% | +43.4% | 0.60 | 3 | 72% | -0.17 | [-0.65, +0.21] | 0.45 |
| Close > 50-day SMA | +128.3% | +22.7% | -43.6% | +37.3% | 0.73 | 48 | 57% | -0.04 | [-0.59, +0.52] | 0.88 |
| MACD > signal | +23.4% | +5.4% | -42.6% | +36.9% | 0.32 | 41 | 49% | -0.45 | [-1.10, +0.16] | 0.15 |
| RSI 30/70 | +94.6% | +18.0% | -28.6% | +32.3% | 0.67 | 3 | 37% | -0.11 | [-0.94, +0.65] | 0.78 |
| Trailing stop 20% | +86.7% | +16.8% | -52.8% | +43.8% | 0.57 | 9 | 84% | -0.21 | [-0.66, +0.23] | 0.34 |
| Volume breakout | +86.0% | +16.7% | -30.0% | +30.6% | 0.66 | 9 | 39% | -0.12 | [-0.84, +0.60] | 0.73 |

### VST (2022-09-08 to 2026-11-18)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +429.5% | +49.0% | -48.8% | +52.2% | 1.03 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +414.5% | +47.9% | -48.8% | +44.0% | 1.11 | 3 | 68% | +0.09 | [-0.26, +0.49] | 0.63 |
| Close > 50-day SMA | +47.8% | +9.8% | -67.2% | +38.0% | 0.44 | 45 | 63% | -0.59 | [-1.18, +0.02] | 0.06 |
| MACD > signal | +64.4% | +12.6% | -49.0% | +37.2% | 0.51 | 47 | 51% | -0.52 | [-1.14, +0.17] | 0.12 |
| RSI 30/70 | +182.7% | +28.2% | -27.3% | +26.9% | 1.06 | 3 | 21% | +0.03 | [-0.89, +0.85] | 0.93 |
| Trailing stop 20% | +210.5% | +31.1% | -56.3% | +44.6% | 0.83 | 9 | 87% | -0.19 | [-0.64, +0.27] | 0.38 |
| Volume breakout | +278.5% | +37.5% | -31.2% | +31.4% | 1.18 | 9 | 43% | +0.15 | [-0.66, +1.04] | 0.72 |

### DELL (2022-09-08 to 2026-11-18)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +754.4% | +67.0% | -59.6% | +58.3% | 1.16 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +374.5% | +45.1% | -50.8% | +51.0% | 0.98 | 3 | 69% | -0.19 | [-0.68, +0.24] | 0.41 |
| Close > 50-day SMA | +1326.9% | +88.8% | -27.5% | +49.3% | 1.52 | 21 | 67% | +0.36 | [-0.13, +0.92] | 0.19 |
| MACD > signal | +141.4% | +23.5% | -57.7% | +43.1% | 0.69 | 45 | 52% | -0.47 | [-1.13, +0.27] | 0.17 |
| RSI 30/70 | +153.8% | +24.9% | -23.7% | +26.8% | 0.96 | 4 | 27% | -0.20 | [-1.17, +0.70] | 0.69 |
| Trailing stop 20% | +921.0% | +74.3% | -55.9% | +51.5% | 1.33 | 7 | 81% | +0.16 | [-0.26, +0.59] | 0.46 |
| Volume breakout | +378.1% | +45.4% | -37.8% | +43.2% | 1.07 | 11 | 45% | -0.09 | [-0.81, +0.56] | 0.78 |

### TSM (2022-09-08 to 2026-11-19)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +361.0% | +44.1% | -36.8% | +39.5% | 1.12 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +141.7% | +23.5% | -36.8% | +36.2% | 0.76 | 2 | 82% | -0.36 | [-0.85, +0.14] | 0.16 |
| Close > 50-day SMA | +190.3% | +29.0% | -28.8% | +31.6% | 0.96 | 37 | 68% | -0.16 | [-0.73, +0.47] | 0.61 |
| MACD > signal | +118.0% | +20.5% | -32.1% | +28.6% | 0.79 | 45 | 49% | -0.33 | [-0.93, +0.25] | 0.29 |
| RSI 30/70 | +28.9% | +6.3% | -23.0% | +17.3% | 0.44 | 3 | 13% | -0.68 | [-1.70, +0.20] | 0.16 |
| Trailing stop 20% | +220.1% | +32.0% | -30.6% | +36.7% | 0.94 | 6 | 90% | -0.18 | [-0.57, +0.18] | 0.31 |
| Volume breakout | +77.0% | +14.6% | -26.8% | +26.4% | 0.65 | 11 | 46% | -0.47 | [-1.30, +0.30] | 0.23 |

### BE (2022-09-08 to 2026-11-18)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +553.8% | +56.7% | -67.8% | +90.1% | 0.93 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +202.9% | +30.3% | -71.9% | +75.0% | 0.72 | 4 | 63% | -0.21 | [-0.76, +0.36] | 0.48 |
| Close > 50-day SMA | +346.9% | +43.0% | -53.1% | +69.7% | 0.84 | 31 | 51% | -0.09 | [-0.63, +0.44] | 0.72 |
| MACD > signal | +182.4% | +28.2% | -60.0% | +65.9% | 0.69 | 41 | 51% | -0.25 | [-0.95, +0.40] | 0.49 |
| RSI 30/70 | +147.7% | +24.2% | -61.8% | +47.1% | 0.69 | 4 | 48% | -0.24 | [-1.09, +0.63] | 0.60 |
| Trailing stop 20% | +146.3% | +24.1% | -66.7% | +73.8% | 0.64 | 19 | 60% | -0.29 | [-0.80, +0.19] | 0.24 |
| Volume breakout | +275.5% | +37.2% | -58.1% | +61.0% | 0.80 | 11 | 30% | -0.13 | [-0.97, +0.61] | 0.74 |

![Strategy equity curves](backtest_equity.png)

## 5. Next-day forecasts

Not included: SKHY (only 93 trading days of history, needs 452); SPCX (only 111 trading days of history, needs 452).

### ALAB

Walk-forward test on 218 unseen days (2026-01-07 to 2026-11-17).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.523 | 0.523 | 0.527 | 0.457 | 0.25 | 0.814 | 0.815 |
| Logistic regression | 0.5 | 0.523 | 0.772 | 0.503 | 0.257 | 0.302 | 0.815 |
| Gradient boosting | 0.477 | 0.523 | 0.923 | 0.458 | 0.282 | 0.358 | 0.815 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 648.7 | 0.0 |  |  |
| Ridge regression | 664.6 | -0.0497 | 0.477 | 0.94 |
| Gradient boosting | 682.0 | -0.1053 | 0.454 | 0.993 |

Forecast for the next session:

```
  P(up) | Logistic regression      53.9%
  P(up) | Gradient boosting        26.9%
  P(up) | historical base rate     51.9%
  expected return (ridge)          +1.78%
  80% range low                    -8.45%
  80% range high                   +13.15%
  daily volatility                 +8.26%
```

Best out-of-sample AUC **0.503**; smallest p-value against a naive baseline 0.772, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![ALAB feature effects](forecast_ALAB.png)

### AMD

Walk-forward test on 550 unseen days (2024-09-11 to 2026-11-18).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.504 | 0.529 | 0.892 | 0.488 | 0.25 | 0.97 | 1.151 |
| Logistic regression | 0.489 | 0.529 | 0.973 | 0.491 | 0.256 | 0.689 | 1.151 |
| Gradient boosting | 0.495 | 0.529 | 0.952 | 0.504 | 0.265 | 1.173 | 1.151 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 407.8 | 0.0 |  |  |
| Ridge regression | 409.7 | -0.0094 | 0.505 | 0.698 |
| Gradient boosting | 416.0 | -0.0406 | 0.505 | 0.973 |

Forecast for the next session:

```
  P(up) | Logistic regression      70.4%
  P(up) | Gradient boosting        70.7%
  P(up) | historical base rate     51.5%
  expected return (ridge)          +2.17%
  80% range low                    -7.64%
  80% range high                   +13.03%
  daily volatility                 +7.88%
```

Best out-of-sample AUC **0.504**; smallest p-value against a naive baseline 0.698, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![AMD feature effects](forecast_AMD.png)

### NVDA

Walk-forward test on 550 unseen days (2024-09-11 to 2026-11-18).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.516 | 0.516 | 0.517 | 0.512 | 0.251 | 0.454 | 0.454 |
| Logistic regression | 0.509 | 0.516 | 0.65 | 0.523 | 0.254 | 0.411 | 0.454 |
| Gradient boosting | 0.504 | 0.516 | 0.739 | 0.475 | 0.272 | 0.611 | 0.454 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 278.3 | 0.0 |  |  |
| Ridge regression | 279.9 | -0.012 | 0.516 | 0.658 |
| Gradient boosting | 289.1 | -0.0794 | 0.511 | 0.983 |

Forecast for the next session:

```
  P(up) | Logistic regression      56.7%
  P(up) | Gradient boosting        79.6%
  P(up) | historical base rate     53.5%
  expected return (ridge)          +0.87%
  80% range low                    -3.17%
  80% range high                   +5.07%
  daily volatility                 +3.19%
```

Best out-of-sample AUC **0.523**; smallest p-value against a naive baseline 0.650, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![NVDA feature effects](forecast_NVDA.png)

### MRVL

Walk-forward test on 550 unseen days (2024-09-11 to 2026-11-18).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.531 | 0.531 | 0.517 | 0.467 | 0.249 | 0.752 | 0.752 |
| Logistic regression | 0.538 | 0.531 | 0.383 | 0.555 | 0.25 | 0.873 | 0.752 |
| Gradient boosting | 0.544 | 0.531 | 0.29 | 0.563 | 0.255 | 0.702 | 0.752 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 481.2 | 0.0 |  |  |
| Ridge regression | 486.1 | -0.0205 | 0.535 | 0.874 |
| Gradient boosting | 492.5 | -0.0472 | 0.509 | 0.972 |

Forecast for the next session:

```
  P(up) | Logistic regression      65.3%
  P(up) | Gradient boosting        46.2%
  P(up) | historical base rate     52.5%
  expected return (ridge)          +1.45%
  80% range low                    -7.97%
  80% range high                   +11.82%
  daily volatility                 +7.60%
```

Best out-of-sample AUC **0.563**; smallest p-value against a naive baseline 0.290, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![MRVL feature effects](forecast_MRVL.png)

### GOOG

Walk-forward test on 549 unseen days (2024-09-11 to 2026-11-17).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.523 | 0.523 | 0.517 | 0.484 | 0.25 | 1.043 | 1.043 |
| Logistic regression | 0.534 | 0.523 | 0.319 | 0.529 | 0.253 | 0.283 | 1.043 |
| Gradient boosting | 0.514 | 0.523 | 0.681 | 0.534 | 0.262 | 0.467 | 1.043 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 201.1 | 0.0 |  |  |
| Ridge regression | 203.1 | -0.0198 | 0.525 | 0.937 |
| Gradient boosting | 207.6 | -0.0658 | 0.536 | 0.997 |

Forecast for the next session:

```
  P(up) | Logistic regression      57.3%
  P(up) | Gradient boosting        55.2%
  P(up) | historical base rate     53.1%
  expected return (ridge)          +0.35%
  80% range low                    -3.78%
  80% range high                   +4.66%
  daily volatility                 +3.28%
```

Best out-of-sample AUC **0.534**; smallest p-value against a naive baseline 0.319, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![GOOG feature effects](forecast_GOOG.png)

### FSLR

Walk-forward test on 550 unseen days (2024-09-11 to 2026-11-18).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.518 | 0.518 | 0.517 | 0.467 | 0.25 |  | -0.08 |
| Logistic regression | 0.513 | 0.518 | 0.618 | 0.526 | 0.252 | -0.221 | -0.08 |
| Gradient boosting | 0.496 | 0.518 | 0.857 | 0.509 | 0.266 | -0.119 | -0.08 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 360.1 | 0.0 |  |  |
| Ridge regression | 362.5 | -0.0131 | 0.495 | 0.838 |
| Gradient boosting | 369.5 | -0.0528 | 0.516 | 0.991 |

Forecast for the next session:

```
  P(up) | Logistic regression      58.4%
  P(up) | Gradient boosting        31.1%
  P(up) | historical base rate     48.8%
  expected return (ridge)          +0.99%
  80% range low                    -3.12%
  80% range high                   +5.28%
  daily volatility                 +3.24%
```

Best out-of-sample AUC **0.526**; smallest p-value against a naive baseline 0.618, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![FSLR feature effects](forecast_FSLR.png)

### ETN

Walk-forward test on 550 unseen days (2024-09-11 to 2026-11-18).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.525 | 0.525 | 0.517 | 0.481 | 0.25 | 0.353 | 0.354 |
| Logistic regression | 0.518 | 0.525 | 0.65 | 0.518 | 0.254 | 0.524 | 0.354 |
| Gradient boosting | 0.533 | 0.525 | 0.383 | 0.531 | 0.26 | 0.13 | 0.354 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 247.5 | 0.0 |  |  |
| Ridge regression | 248.9 | -0.0111 | 0.536 | 0.734 |
| Gradient boosting | 255.8 | -0.0683 | 0.5 | 0.993 |

Forecast for the next session:

```
  P(up) | Logistic regression      60.2%
  P(up) | Gradient boosting        74.6%
  P(up) | historical base rate     53.9%
  expected return (ridge)          +0.94%
  80% range low                    -4.53%
  80% range high                   +6.73%
  daily volatility                 +4.35%
```

Best out-of-sample AUC **0.531**; smallest p-value against a naive baseline 0.383, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![ETN feature effects](forecast_ETN.png)

### TSLA

Walk-forward test on 550 unseen days (2024-09-11 to 2026-11-18).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.489 | 0.502 | 0.739 | 0.471 | 0.25 | 0.422 | 0.677 |
| Logistic regression | 0.515 | 0.502 | 0.29 | 0.512 | 0.253 | 1.049 | 0.677 |
| Gradient boosting | 0.525 | 0.502 | 0.143 | 0.531 | 0.262 | 0.555 | 0.677 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 367.2 | 0.0 |  |  |
| Ridge regression | 371.6 | -0.0239 | 0.498 | 0.946 |
| Gradient boosting | 374.5 | -0.0401 | 0.536 | 0.954 |

Forecast for the next session:

```
  P(up) | Logistic regression      49.1%
  P(up) | Gradient boosting        53.9%
  P(up) | historical base rate     50.8%
  expected return (ridge)          +0.36%
  80% range low                    -4.27%
  80% range high                   +5.22%
  daily volatility                 +3.69%
```

Best out-of-sample AUC **0.531**; smallest p-value against a naive baseline 0.143, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![TSLA feature effects](forecast_TSLA.png)

### AMZN

Walk-forward test on 550 unseen days (2024-09-11 to 2026-11-18).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.515 | 0.515 | 0.517 | 0.453 | 0.25 | 0.616 | 0.616 |
| Logistic regression | 0.54 | 0.515 | 0.125 | 0.552 | 0.25 | 0.882 | 0.616 |
| Gradient boosting | 0.52 | 0.515 | 0.416 | 0.525 | 0.262 | 0.295 | 0.616 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 212.2 | 0.0 |  |  |
| Ridge regression | 214.3 | -0.0205 | 0.535 | 0.916 |
| Gradient boosting | 221.9 | -0.0941 | 0.533 | 1.0 |

Forecast for the next session:

```
  P(up) | Logistic regression      48.8%
  P(up) | Gradient boosting        49.1%
  P(up) | historical base rate     51.3%
  expected return (ridge)          +0.16%
  80% range low                    -3.31%
  80% range high                   +3.74%
  daily volatility                 +2.75%
```

Best out-of-sample AUC **0.552**; smallest p-value against a naive baseline 0.125, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![AMZN feature effects](forecast_AMZN.png)

### IBM

Walk-forward test on 550 unseen days (2024-09-11 to 2026-11-18).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.544 | 0.544 | 0.518 | 0.478 | 0.249 | 0.348 | 0.349 |
| Logistic regression | 0.535 | 0.544 | 0.681 | 0.478 | 0.253 | 0.678 | 0.349 |
| Gradient boosting | 0.496 | 0.544 | 0.988 | 0.499 | 0.267 | 0.382 | 0.349 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 254.3 | 0.0 |  |  |
| Ridge regression | 256.6 | -0.0181 | 0.529 | 0.891 |
| Gradient boosting | 257.4 | -0.0242 | 0.513 | 0.901 |

Forecast for the next session:

```
  P(up) | Logistic regression      45.3%
  P(up) | Gradient boosting        45.9%
  P(up) | historical base rate     55.0%
  expected return (ridge)          +0.05%
  80% range low                    -2.08%
  80% range high                   +2.23%
  daily volatility                 +1.68%
```

Best out-of-sample AUC **0.499**; smallest p-value against a naive baseline 0.681, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![IBM feature effects](forecast_IBM.png)

### GEV

Walk-forward test on 213 unseen days (2026-01-14 to 2026-11-17).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.531 | 0.531 | 0.528 | 0.471 | 0.25 | 0.671 | 0.672 |
| Logistic regression | 0.502 | 0.531 | 0.814 | 0.508 | 0.257 | 0.378 | 0.672 |
| Gradient boosting | 0.531 | 0.531 | 0.528 | 0.526 | 0.27 | 1.015 | 0.672 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 336.8 | 0.0 |  |  |
| Ridge regression | 343.5 | -0.0405 | 0.549 | 0.822 |
| Gradient boosting | 350.6 | -0.084 | 0.521 | 0.93 |

Forecast for the next session:

```
  P(up) | Logistic regression      65.7%
  P(up) | Gradient boosting        57.9%
  P(up) | historical base rate     54.2%
  expected return (ridge)          +1.00%
  80% range low                    -5.22%
  80% range high                   +7.64%
  daily volatility                 +4.96%
```

Best out-of-sample AUC **0.526**; smallest p-value against a naive baseline 0.528, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![GEV feature effects](forecast_GEV.png)

### CEG

Walk-forward test on 510 unseen days (2024-11-05 to 2026-11-17).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.502 | 0.502 | 0.518 | 0.494 | 0.251 | 0.392 | 0.393 |
| Logistic regression | 0.471 | 0.502 | 0.928 | 0.5 | 0.259 | -0.003 | 0.393 |
| Gradient boosting | 0.476 | 0.502 | 0.884 | 0.467 | 0.275 | -0.092 | 0.393 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 351.1 | 0.0 |  |  |
| Ridge regression | 359.0 | -0.0451 | 0.475 | 0.983 |
| Gradient boosting | 361.8 | -0.0618 | 0.51 | 0.989 |

Forecast for the next session:

```
  P(up) | Logistic regression      61.2%
  P(up) | Gradient boosting        48.4%
  P(up) | historical base rate     52.0%
  expected return (ridge)          +0.51%
  80% range low                    -4.28%
  80% range high                   +5.55%
  daily volatility                 +3.82%
```

Best out-of-sample AUC **0.500**; smallest p-value against a naive baseline 0.884, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![CEG feature effects](forecast_CEG.png)

### VST

Walk-forward test on 549 unseen days (2024-09-11 to 2026-11-17).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.514 | 0.514 | 0.517 | 0.493 | 0.25 | 0.66 | 0.661 |
| Logistic regression | 0.483 | 0.514 | 0.932 | 0.483 | 0.26 | 0.949 | 0.661 |
| Gradient boosting | 0.53 | 0.514 | 0.234 | 0.542 | 0.263 | 1.548 | 0.661 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 392.4 | 0.0 |  |  |
| Ridge regression | 394.4 | -0.0102 | 0.51 | 0.692 |
| Gradient boosting | 401.2 | -0.0453 | 0.492 | 0.978 |

Forecast for the next session:

```
  P(up) | Logistic regression      52.9%
  P(up) | Gradient boosting        50.0%
  P(up) | historical base rate     52.6%
  expected return (ridge)          +0.61%
  80% range low                    -6.12%
  80% range high                   +7.83%
  daily volatility                 +5.41%
```

Best out-of-sample AUC **0.542**; smallest p-value against a naive baseline 0.234, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![VST feature effects](forecast_VST.png)

### DELL

Walk-forward test on 549 unseen days (2024-09-11 to 2026-11-17).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.519 | 0.519 | 0.517 | 0.46 | 0.25 | 1.078 | 1.079 |
| Logistic regression | 0.501 | 0.519 | 0.815 | 0.505 | 0.255 | -0.188 | 1.079 |
| Gradient boosting | 0.506 | 0.519 | 0.739 | 0.505 | 0.267 | 0.53 | 1.079 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 409.7 | 0.0 |  |  |
| Ridge regression | 415.9 | -0.0304 | 0.494 | 0.982 |
| Gradient boosting | 423.7 | -0.0697 | 0.517 | 0.997 |

Forecast for the next session:

```
  P(up) | Logistic regression      50.3%
  P(up) | Gradient boosting        67.2%
  P(up) | historical base rate     51.7%
  expected return (ridge)          +0.11%
  80% range low                    -8.23%
  80% range high                   +9.22%
  daily volatility                 +6.79%
```

Best out-of-sample AUC **0.505**; smallest p-value against a naive baseline 0.739, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![DELL feature effects](forecast_DELL.png)

### TSM

Walk-forward test on 550 unseen days (2024-09-11 to 2026-11-18).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.522 | 0.531 | 0.681 | 0.472 | 0.25 | 0.942 | 1.036 |
| Logistic regression | 0.533 | 0.531 | 0.483 | 0.529 | 0.25 | 0.936 | 1.036 |
| Gradient boosting | 0.516 | 0.531 | 0.766 | 0.512 | 0.261 | 1.06 | 1.036 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 264.5 | 0.0 |  |  |
| Ridge regression | 263.7 | 0.0063 | 0.525 | 0.364 |
| Gradient boosting | 270.1 | -0.0422 | 0.52 | 0.977 |

Forecast for the next session:

```
  P(up) | Logistic regression      71.9%
  P(up) | Gradient boosting        68.3%
  P(up) | historical base rate     51.6%
  expected return (ridge)          +1.66%
  80% range low                    -3.57%
  80% range high                   +7.18%
  daily volatility                 +4.12%
```

Best out-of-sample AUC **0.529**; smallest p-value against a naive baseline 0.364, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![TSM feature effects](forecast_TSM.png)

### BE

Walk-forward test on 549 unseen days (2024-09-11 to 2026-11-17).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.488 | 0.512 | 0.875 | 0.483 | 0.251 |  | 1.7 |
| Logistic regression | 0.474 | 0.512 | 0.967 | 0.467 | 0.265 | 0.708 | 1.7 |
| Gradient boosting | 0.515 | 0.512 | 0.449 | 0.498 | 0.264 | 1.616 | 1.7 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 654.1 | 0.0 |  |  |
| Ridge regression | 671.9 | -0.0551 | 0.474 | 0.998 |
| Gradient boosting | 668.1 | -0.0431 | 0.479 | 0.991 |

Forecast for the next session:

```
  P(up) | Logistic regression      54.9%
  P(up) | Gradient boosting        65.9%
  P(up) | historical base rate     49.4%
  expected return (ridge)          +0.69%
  80% range low                    -9.16%
  80% range high                   +11.60%
  daily volatility                 +8.03%
```

Best out-of-sample AUC **0.498**; smallest p-value against a naive baseline 0.449, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![BE feature effects](forecast_BE.png)

## 6. Stock screen and entry plans

| ticker | rank | score | passes_filters | close | momentum_12_1 | momentum_6m | volatility | off_52w_high | forward_pe | pullback_entry | breakout_trigger | stop | stop_% | shares | position_$ | max_loss_$ | filter_notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AMD | 1 | +0.81 | True | 489.19 | +140.0% | +8.8% | +83.1% | -24.7% | 27.7 | 445.71 | 586.47 | 358.74 | -19.5% | 11 | 4903.0 | 957.0 |  |
| V | 2 | +0.63 | True | 402.25 | +27.7% | +21.9% | +22.8% | -7.7% | 23.5 | 393.41 | 436.63 | 375.33 | -4.6% | 25 | 9835.0 | 452.0 |  |
| KO | 3 | +0.55 | True | 96.09 | +33.6% | +19.9% | +17.5% | -3.4% | 27.2 | 95.64 | 99.68 | 92.05 | -3.8% | 104 | 9946.0 | 373.0 |  |
| LLY | 4 | +0.54 | True | 1351.12 | +24.0% | +30.1% | +29.7% | -6.4% | 26.6 | 1260.93 | 1446.39 | 1174.29 | -6.9% | 7 | 8827.0 | 607.0 |  |
| MSFT | 5 | +0.51 | True | 498.30 | +8.8% | +19.4% | +27.5% | -10.2% | 20.6 | 482.41 | 555.84 | 450.63 | -6.6% | 20 | 9648.0 | 636.0 |  |
| XOM | 6 | +0.49 | True | 158.93 | +52.6% | +3.7% | +27.4% | -14.6% | 12.7 | 154.64 | 186.45 | 146.06 | -5.5% | 64 | 9897.0 | 549.0 |  |
| AAPL | 7 | +0.48 | True | 349.21 | +29.0% | +14.7% | +21.7% | -2.0% | 33.0 | 347.55 | 356.98 | 332.06 | -4.5% | 28 | 9731.0 | 434.0 |  |
| JNJ | 8 | +0.38 | True | 267.14 | +31.8% | +16.5% | +24.7% | -6.5% | 23.0 | 260.33 | 286.32 | 246.72 | -5.2% | 38 | 9893.0 | 517.0 |  |
| PG | 9 | +0.26 | True | 167.85 | +9.1% | +18.7% | +21.0% | -3.0% | 22.6 | 165.57 | 173.37 | 159.25 | -3.8% | 60 | 9934.0 | 379.0 |  |
| LIN | 10 | +0.11 | True | 510.21 | +22.3% | -0.2% | +15.4% | -6.4% | 26.1 | 493.94 | 527.6 | 476.5 | -3.5% | 20 | 9879.0 | 349.0 |  |
| AMZN | 11 | +0.02 | True | 257.37 | +17.9% | -4.1% | +33.2% | -9.4% | 23.6 | 255.23 | 271.41 | 236.01 | -7.5% | 39 | 9954.0 | 749.0 |  |
| COST | 12 | +0.01 | True | 1093.83 | +12.0% | +4.4% | +19.7% | -1.8% | 43.7 | 1052.12 | 1115.97 | 1015.43 | -3.5% | 9 | 9469.0 | 330.0 |  |
| AMT | 13 | -0.03 | True | 181.15 | +1.8% | +0.6% | +30.4% | -7.0% | 26.0 | 179.05 | 195.25 | 168.86 | -5.7% | 55 | 9847.0 | 560.0 |  |
| DELL | 14 | +1.01 | False | 313.11 | +280.8% | +29.3% | +87.5% | -46.7% | 10.2 | 279.8 | 502.96 | 213.18 | -23.8% | 15 | 4197.0 | 999.0 | below 200-day SMA |
| MRVL | 15 | +0.49 | False | 138.47 | +211.6% | -27.4% | +87.7% | -56.2% | 18.8 | 122.56 | 252.15 | 90.73 | -26.0% | 31 | 3799.0 | 987.0 | below 200-day SMA; down >50% from high |

## 7. Portfolio construction

Not included: SKHY (only 93 trading days of history, needs 252); SPCX (only 111 trading days of history, needs 252).

Assets: ALAB, AMD, NVDA, MRVL, GOOG, FSLR, ETN, TSLA, AMZN, IBM, GEV, CEG, VST, DELL, TSM, BE, JPM, XOM, UNH, COST, TLT, GLD. Covariance: Ledoit-Wolf shrinkage on the last 252 trading days.

Weights and share of risk (%):

| asset | weight: Equal weight | weight: Inverse volatility | weight: Risk parity | weight: Minimum variance | risk share: Equal weight | risk share: Inverse volatility | risk share: Risk parity | risk share: Minimum variance |
|---|---|---|---|---|---|---|---|---|
| ALAB | 4.5 | 1.8 | 1.2 | 0.0 | 12.4 | 6.5 | 4.6 | 0.0 |
| AMD | 4.5 | 2.5 | 1.4 | 0.0 | 9.5 | 7.3 | 4.6 | 0.0 |
| NVDA | 4.5 | 4.6 | 3.4 | 4.6 | 4.0 | 6.0 | 4.8 | 5.1 |
| MRVL | 4.5 | 2.1 | 1.3 | 0.0 | 10.4 | 6.8 | 4.6 | 0.0 |
| GOOG | 4.5 | 5.3 | 4.5 | 4.0 | 2.0 | 4.1 | 4.8 | 4.5 |
| FSLR | 4.5 | 3.4 | 2.7 | 0.1 | 4.1 | 4.7 | 4.7 | 0.1 |
| ETN | 4.5 | 4.1 | 2.6 | 2.2 | 5.4 | 7.2 | 4.7 | 2.5 |
| TSLA | 4.5 | 3.9 | 2.6 | 0.0 | 4.5 | 6.0 | 4.7 | 0.0 |
| AMZN | 4.5 | 5.1 | 4.2 | 4.8 | 2.1 | 4.2 | 4.8 | 5.4 |
| IBM | 4.5 | 3.7 | 5.4 | 2.4 | 0.9 | 1.5 | 4.8 | 2.7 |
| GEV | 4.5 | 3.2 | 2.3 | 0.6 | 6.2 | 6.4 | 4.7 | 0.7 |
| CEG | 4.5 | 3.6 | 2.7 | 1.4 | 4.5 | 5.4 | 4.7 | 1.5 |
| VST | 4.5 | 3.4 | 2.4 | 0.0 | 5.4 | 6.0 | 4.7 | 0.0 |
| DELL | 4.5 | 2.2 | 1.8 | 0.0 | 7.7 | 5.4 | 4.6 | 0.0 |
| TSM | 4.5 | 4.2 | 2.3 | 0.0 | 5.6 | 7.6 | 4.7 | 0.0 |
| BE | 4.5 | 1.6 | 1.0 | 0.0 | 13.4 | 6.7 | 4.6 | 0.0 |
| JPM | 4.5 | 7.3 | 6.8 | 7.9 | 1.2 | 3.6 | 4.9 | 8.8 |
| XOM | 4.5 | 6.2 | 0.0 | 18.0 | -0.7 | -1.4 | -0.0 | 20.0 |
| UNH | 4.5 | 4.9 | 6.6 | 2.7 | 0.5 | 1.5 | 4.8 | 3.1 |
| COST | 4.5 | 8.0 | 22.3 | 17.5 | -0.9 | -1.5 | 5.1 | 19.5 |
| TLT | 4.5 | 12.9 | 17.2 | 30.0 | 0.3 | 2.0 | 5.4 | 21.9 |
| GLD | 4.5 | 5.9 | 5.3 | 3.8 | 1.8 | 4.1 | 4.8 | 4.2 |

| method | expected volatility | diversification ratio | effective number of bets | largest risk share | largest risk holder |
|---|---|---|---|---|---|
| Equal weight | 27.6% | 1.82 | 12.42 | 13.4% | BE |
| Inverse volatility | 18.3% | 2.16 | 16.62 | 7.6% | TSM |
| Risk parity | 14.0% | 2.47 | 20.97 | 5.4% | TLT |
| Minimum variance | 8.7% | 2.91 | 6.86 | 21.9% | TLT |

Concentration warnings:

- AMD and TSM have correlation 0.70: they tend to fall together
- ETN and GEV have correlation 0.73: they tend to fall together
- CEG and VST have correlation 0.80: they tend to fall together

Out-of-sample comparison, monthly rebalance (2025-04-01 to 2026-11-18):

| method | CAGR | Volatility | Sharpe | Max drawdown |
|---|---|---|---|---|
| Equal weight | +56.4% | +28.7% | 1.70 | -18.0% |
| Inverse volatility | +39.2% | +20.7% | 1.70 | -11.2% |
| Risk parity | +29.9% | +16.1% | 1.71 | -9.3% |
| Minimum variance | +12.5% | +10.1% | 1.22 | -6.8% |

![Correlations](portfolio_correlation.png)

![Risk shares](portfolio_risk_shares.png)

![Walk-forward](portfolio_walk_forward.png)

## 8. Opening gaps: do pre-market moves carry into the day?

Across 19,032 stock-days (18 watchlist stocks, 2021-11-23 to 2026-11-19), each 1% of opening gap went with a -0.03% move from the open to the close (95% block-bootstrap CI [-0.08%, +0.03%]): no reliable relationship, so the size of a gap has not told you which way the session goes.

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 785 | -5.2% | +0.33% | 50% |
| down 1-3% | 2919 | -1.7% | +0.08% | 52% |
| within 1% | 11006 | +0.0% | +0.01% | 50% |
| up 1-3% | 3391 | +1.7% | +0.07% | 52% |
| gap up 3%+ | 931 | +5.4% | -0.13% | 47% |

## 9. Deciding before the open vs at the previous close

From 2022-02-17 to 2026-11-18 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +38.3% a year (worst drawdown -35.5%) against +36.5% (-34.9%) for labels set at the previous close; the two agreed on 89% of stock-weeks. Sharpe ratio difference +0.03 (95% block-bootstrap CI [-0.12, +0.20]): deciding before the open has been **not distinguishable from deciding on the previous close**.

| strategy | CAGR | Volatility | Sharpe | Max drawdown |
|---|---|---|---|---|
| Board on the previous close | +36.5% | 34.6% | 1.07 | -34.9% |
| Board on the pre-market price | +38.3% | 35.2% | 1.10 | -35.5% |
| Equal-weight watchlist | +42.6% | 35.4% | 1.18 | -40.7% |

The pre-market version uses the official opening price as a stand-in for the last pre-market trade (free pre-market history is only days long), which slightly flatters it.
