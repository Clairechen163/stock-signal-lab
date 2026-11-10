# stocklab report
Generated 2026-11-10 | data source: `yahoo` | history: 5 years | watchlist: ALAB, AMD, NVDA, MRVL, GOOG, FSLR, SKHY, ETN, TSLA, SPCX, AMZN, IBM, GEV, CEG, VST, DELL, TSM, BE

> Educational research code, not investment advice. Past results do not predict future returns.

## 1. Decision board

Data as of the 2026-11-09 close. `*` = provisional (under 200 trading days of history).

| ticker | action | close | 1 day | 1 month | buy rank | sell warnings | pullback entry | breakout | stop | why |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | BUY | 266.93 | +2.9% | +1.7% | 5/18 | 1/15 | 254.65 | 267.46 | 235.29 | buy rank 5/18; +9% vs 200-day average; distribution days |
| IBM | WATCH | 246.11 | +0.5% | +8.4% | 6/18 | 4/15 | 236.96 | 258.80 | 222.52 | +0% vs 200-day average; death cross, MACD bearish, 20%+ off high |
| DELL | REDUCE | 346.31 | +5.4% | -40.8% | 1/18 | 7/15 |  |  |  | +3% vs 200-day average; below 50-day, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| AMD | REDUCE | 508.58 | +13.3% | -16.4% | 2/18 | 7/15 |  |  |  | +22% vs 200-day average; below 50-day, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| ALAB | REDUCE | 216.87 | +13.7% | -36.6% | 7/18 | 8/15 |  |  |  | -15% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, below chandelier stop |
| SPCX | REDUCE* | 142.07 | +5.8% | -12.6% | 9/18 | 4/10 |  |  |  | -5% vs 50-day average; below 50-day, MACD bearish, distribution days, 20%+ off high (provisional: 104 days of history) |
| CEG | REDUCE | 276.09 | +10.5% | -7.4% | 13/18 | 6/15 |  |  |  | -1% vs 200-day average; below 200-day, death cross, distribution days, 20%+ off high |
| TSLA | REDUCE | 378.05 | +5.5% | -1.2% | 14/18 | 7/15 |  |  |  | -1% vs 200-day average; below 200-day, death cross, MACD bearish, distribution days, 20%+ off high |
| BE | REDUCE | 193.88 | +11.9% | -30.9% | 15/18 | 8/15 |  |  |  | -13% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, below chandelier stop |
| FSLR | REDUCE | 191.61 | -4.7% | +7.8% | 18/18 | 6/15 |  |  |  | -11% vs 200-day average; below 200-day, death cross, distribution days, 20%+ off high |
| MRVL | SELL | 154.60 | +9.5% | -43.8% | 3/18 | 9/15 |  |  |  | -17% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| TSM | SELL | 388.62 | +3.5% | -14.3% | 4/18 | 9/15 |  |  |  | -3% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| NVDA | SELL | 178.67 | -4.3% | -22.1% | 8/18 | 10/15 |  |  |  | -13% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, high-volume breakdown, 20%+ off high, below chandelier stop |
| ETN | SELL | 359.30 | +5.1% | -16.4% | 10/18 | 9/15 |  |  |  | -9% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| GEV | SELL | 829.34 | +7.1% | -17.4% | 11/18 | 11/15 |  |  |  | -13% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| GOOG | SELL | 286.01 | +0.7% | -17.8% | 12/18 | 11/15 |  |  |  | -15% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| SKHY | SELL* | 134.38 | +5.5% | -20.5% | 16/18 | 6/10 |  |  |  | -19% vs 50-day average; below 50-day, MACD bearish, distribution days, 20%+ off high, below chandelier stop (provisional: 86 days of history) |
| VST | SELL | 133.92 | +7.3% | -17.1% | 17/18 | 11/15 |  |  |  | -12% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |

![Board label each week](board_history.png)

**Trading the labels** (2022-02-04 to 2026-11-09): buy on BUY, exit on SELL, REDUCE or AVOID, reviewed weekly with next-day execution and 5 bp costs.

| strategy | CAGR | Volatility | Sharpe | Max drawdown | Time invested | Avg holdings |
|---|---|---|---|---|---|---|
| Board strategy | +36.0% | 33.9% | 1.08 | -38.0% | 100% | 6.6 |
| Equal-weight watchlist | +45.1% | 34.2% | 1.26 | -36.8% | 100% | 15.0 |
| SPY (buy & hold) | +13.1% | 17.3% | 0.80 | -22.1% |  |  |

Sharpe difference vs equal weight: -0.18, 95% block-bootstrap CI [-0.68, +0.29].

Forward 21-day return after each label, relative to the watchlist average on the same date (sampled every 21 days, t-test across dates):

| label | observations | dates | mean 21d excess return | hit rate | p_value |
|---|---|---|---|---|---|
| BUY | 264 | 55 | +0.6% | 49% | 0.49 |
| HOLD | 130 | 44 | -1.7% | 41% | 0.13 |
| WATCH | 155 | 51 | -0.1% | 51% | 0.90 |
| AVOID | 41 | 22 | -1.5% | 59% | 0.41 |
| REDUCE | 154 | 49 | +0.6% | 47% | 0.77 |
| SELL | 92 | 36 | -0.0% | 39% | 0.99 |

![Board strategy vs holding](board_equity.png)

## 2. Sell check, stock by stock

```
ALAB  REDUCE  (score 8/15, close 216.87 on 2026-11-09)
  RSI 37 | -55.1% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 299.01  (price is below, -27.5%)
    Chandelier stop            274.51  (price is below, -21.0%)
    200-day SMA                256.29  (price is below, -15.4%)
```

```
AMD  REDUCE  (score 7/15, close 508.58 on 2026-11-09)
  RSI 48 | -21.7% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 547.67  (price is below, -7.1%)
    Chandelier stop            511.22  (price is below, -0.5%)
    200-day SMA                417.22  (price is above, +21.9%)
```

```
NVDA  EXIT  (score 10/15, close 178.67 on 2026-11-09)
  RSI 27 | -25.3% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [volume] Down day closing below the 50-day average on 1.5x+ average volume (+2)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 219.00  (price is below, -18.4%)
    Chandelier stop            208.77  (price is below, -14.4%)
    200-day SMA                204.35  (price is below, -12.6%)
```

```
MRVL  EXIT  (score 9/15, close 154.60 on 2026-11-09)
  RSI 32 | -51.1% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 233.03  (price is below, -33.7%)
    Chandelier stop            230.04  (price is below, -32.8%)
    200-day SMA                185.36  (price is below, -16.6%)
```

```
GOOG  EXIT  (score 11/15, close 286.01 on 2026-11-09)
  RSI 32 | -28.2% from 52-week high
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
    200-day SMA                337.02  (price is below, -15.1%)
    50-day SMA                 328.63  (price is below, -13.0%)
    Chandelier stop            323.39  (price is below, -11.6%)
```

```
FSLR  REDUCE  (score 6/15, close 191.61 on 2026-11-09)
  RSI 57 | -39.8% from 52-week high
  Triggered:
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
  Levels to watch:
    200-day SMA                214.40  (price is below, -10.6%)
    50-day SMA                 186.74  (price is above, +2.6%)
    Chandelier stop            182.76  (price is above, +4.8%)
```

```
SKHY  EXIT  (score 6/10, close 134.38 on 2026-11-09)
  RSI 41 | -32.3% from high since listing
  Only 86 trading days of history; not scored yet: below_sma200, death_cross, volatility_spike
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the high since listing (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 166.26  (price is below, -19.2%)
    Chandelier stop            143.01  (price is below, -6.0%)
```

```
ETN  EXIT  (score 9/15, close 359.30 on 2026-11-09)
  RSI 43 | -21.9% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 404.40  (price is below, -11.2%)
    200-day SMA                396.35  (price is below, -9.3%)
    Chandelier stop            374.75  (price is below, -4.1%)
```

```
TSLA  REDUCE  (score 7/15, close 378.05 on 2026-11-09)
  RSI 50 | -22.8% from 52-week high
  Triggered:
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
  Levels to watch:
    200-day SMA                383.51  (price is below, -1.4%)
    50-day SMA                 372.72  (price is above, +1.4%)
    Chandelier stop            362.55  (price is above, +4.3%)
```

```
SPCX  REDUCE  (score 4/10, close 142.07 on 2026-11-09)
  RSI 48 | -32.8% from high since listing
  Only 104 trading days of history; not scored yet: below_sma200, death_cross, volatility_spike
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the high since listing (+1)
  Levels to watch:
    50-day SMA                 149.19  (price is below, -4.8%)
    Chandelier stop            142.01  (price is above, +0.0%)
```

```
AMZN  HOLD  (score 1/15, close 266.93 on 2026-11-09)
  RSI 59 | -6.0% from 52-week high
  Triggered:
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
  Levels to watch:
    50-day SMA                 253.96  (price is above, +5.1%)
    Chandelier stop            246.31  (price is above, +8.4%)
    200-day SMA                244.08  (price is above, +9.4%)
```

```
IBM  WATCH  (score 4/15, close 246.11 on 2026-11-09)
  RSI 53 | -24.7% from 52-week high
  Triggered:
    - [trend] 50-day average below the 200-day average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [risk] 20%+ below the 52-week high (+1)
  Levels to watch:
    200-day SMA                245.77  (price is above, +0.1%)
    Chandelier stop            238.21  (price is above, +3.3%)
    50-day SMA                 236.96  (price is above, +3.9%)
```

```
GEV  EXIT  (score 11/15, close 829.34 on 2026-11-09)
  RSI 43 | -29.4% from 52-week high
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
    200-day SMA                948.75  (price is below, -12.6%)
    50-day SMA                 921.42  (price is below, -10.0%)
    Chandelier stop            839.74  (price is below, -1.2%)
```

```
CEG  REDUCE  (score 6/15, close 276.09 on 2026-11-09)
  RSI 56 | -26.8% from 52-week high
  Triggered:
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
  Levels to watch:
    200-day SMA                278.09  (price is below, -0.7%)
    50-day SMA                 270.01  (price is above, +2.3%)
    Chandelier stop            259.17  (price is above, +6.5%)
```

```
VST  EXIT  (score 11/15, close 133.92 on 2026-11-09)
  RSI 46 | -29.5% from 52-week high
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
    200-day SMA                152.15  (price is below, -12.0%)
    50-day SMA                 143.77  (price is below, -6.9%)
    Chandelier stop            138.25  (price is below, -3.1%)
```

```
DELL  REDUCE  (score 7/15, close 346.31 on 2026-11-09)
  RSI 33 | -41.1% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 502.30  (price is below, -31.1%)
    Chandelier stop            493.60  (price is below, -29.8%)
    200-day SMA                337.81  (price is above, +2.5%)
```

```
TSM  EXIT  (score 9/15, close 388.62 on 2026-11-09)
  RSI 41 | -20.0% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 430.82  (price is below, -9.8%)
    Chandelier stop            413.84  (price is below, -6.1%)
    200-day SMA                400.31  (price is below, -2.9%)
```

```
BE  REDUCE  (score 8/15, close 193.88 on 2026-11-09)
  RSI 43 | -43.9% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 245.73  (price is below, -21.1%)
    200-day SMA                222.66  (price is below, -12.9%)
    Chandelier stop            214.82  (price is below, -9.7%)
```

## 3. Which sell signals actually work? (event study)

Panel: 46 stocks, 5 years. Null hypothesis: returns after a signal look like returns on random days from the same stocks.

| rule | horizon | events | mean_after_signal | mean_random_days | difference | p_value | q_value | drop10_after_signal | drop10_base_rate | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| below_sma50 | 5d | 1072 | +0.18% | +0.68% | -0.50% | 0.003 | 0.082 | 40% | 36% | useful |
| below_sma50 | 21d | 1043 | +2.32% | +3.07% | -0.74% | 0.033 | 0.158 | 40% | 36% | weak (not significant) |
| below_sma50 | 63d | 997 | +8.59% | +10.21% | -1.62% | 0.020 | 0.121 | 40% | 36% | weak (not significant) |
| below_sma200 | 5d | 515 | +0.08% | +0.61% | -0.53% | 0.022 | 0.121 | 39% | 36% | weak (not significant) |
| below_sma200 | 21d | 497 | +1.27% | +2.75% | -1.48% | 0.005 | 0.082 | 39% | 36% | useful |
| below_sma200 | 63d | 472 | +9.21% | +9.19% | +0.02% | 0.520 | 0.858 | 39% | 36% | no edge |
| death_cross | 5d | 155 | -0.41% | +0.64% | -1.05% | 0.012 | 0.121 | 44% | 36% | weak (not significant) |
| death_cross | 21d | 148 | +0.63% | +2.86% | -2.23% | 0.017 | 0.121 | 44% | 36% | weak (not significant) |
| death_cross | 63d | 142 | +13.61% | +9.77% | +3.84% | 0.952 | 1.000 | 44% | 36% | no edge |
| rsi_divergence | 5d | 499 | +0.44% | +0.78% | -0.35% | 0.096 | 0.352 | 37% | 36% | weak (not significant) |
| rsi_divergence | 21d | 494 | +3.26% | +3.52% | -0.26% | 0.326 | 0.707 | 37% | 36% | weak (not significant) |
| rsi_divergence | 63d | 486 | +10.97% | +11.78% | -0.82% | 0.240 | 0.660 | 37% | 36% | weak (not significant) |
| rsi_rollover | 5d | 644 | +1.84% | +0.76% | +1.08% | 1.000 | 1.000 | 33% | 36% | no edge |
| rsi_rollover | 21d | 633 | +3.71% | +3.44% | +0.26% | 0.697 | 1.000 | 33% | 36% | no edge |
| rsi_rollover | 63d | 620 | +10.41% | +11.71% | -1.29% | 0.111 | 0.366 | 33% | 36% | weak (not significant) |
| macd_bearish | 5d | 1622 | +0.71% | +0.70% | +0.00% | 0.517 | 0.858 | 36% | 36% | no edge |
| macd_bearish | 21d | 1596 | +3.29% | +3.22% | +0.07% | 0.570 | 0.895 | 36% | 36% | no edge |
| macd_bearish | 63d | 1521 | +11.47% | +10.81% | +0.67% | 0.843 | 1.000 | 36% | 36% | no edge |
| distribution_cluster | 5d | 1078 | +0.89% | +0.71% | +0.17% | 0.828 | 1.000 | 35% | 36% | no edge |
| distribution_cluster | 21d | 1055 | +3.08% | +3.24% | -0.16% | 0.347 | 0.707 | 35% | 36% | weak (not significant) |
| distribution_cluster | 63d | 1019 | +10.27% | +10.98% | -0.70% | 0.185 | 0.556 | 35% | 36% | weak (not significant) |
| high_volume_breakdown | 5d | 760 | +0.75% | +0.68% | +0.07% | 0.636 | 0.954 | 35% | 36% | no edge |
| high_volume_breakdown | 21d | 725 | +3.82% | +3.02% | +0.80% | 0.946 | 1.000 | 35% | 36% | no edge |
| high_volume_breakdown | 63d | 705 | +12.64% | +10.19% | +2.45% | 0.992 | 1.000 | 35% | 36% | no edge |
| drawdown_20 | 5d | 405 | +1.22% | +0.82% | +0.39% | 0.869 | 1.000 | 51% | 36% | no edge |
| drawdown_20 | 21d | 394 | +2.50% | +3.77% | -1.28% | 0.052 | 0.214 | 51% | 36% | weak (not significant) |
| drawdown_20 | 63d | 373 | +13.81% | +12.81% | +1.00% | 0.740 | 1.000 | 51% | 36% | no edge |
| volatility_spike | 5d | 334 | +0.51% | +0.74% | -0.22% | 0.263 | 0.669 | 47% | 36% | weak (not significant) |
| volatility_spike | 21d | 329 | +3.14% | +3.41% | -0.27% | 0.364 | 0.707 | 47% | 36% | weak (not significant) |
| volatility_spike | 63d | 327 | +11.03% | +11.46% | -0.42% | 0.401 | 0.736 | 47% | 36% | weak (not significant) |
| chandelier_stop | 5d | 1362 | +0.61% | +0.71% | -0.10% | 0.297 | 0.700 | 37% | 36% | weak (not significant) |
| chandelier_stop | 21d | 1332 | +3.49% | +3.21% | +0.28% | 0.777 | 1.000 | 37% | 36% | no edge |
| chandelier_stop | 63d | 1278 | +11.99% | +10.87% | +1.11% | 0.924 | 1.000 | 37% | 36% | no edge |

**2 of 33 rule-by-horizon tests** show significantly weaker returns after the signal (q < 0.10).

![Sell signal event study](sell_event_study.png)

## 4. Strategy backtests

Not included: SKHY (only 86 trading days of history, needs 452); SPCX (only 104 trading days of history, needs 452).

### ALAB (2025-01-03 to 2026-11-09)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +50.9% | +25.0% | -63.2% | +97.3% | 0.72 | 0 | 100% |  |  |  |
| 50/200 SMA cross | -66.9% | -45.1% | -74.0% | +87.8% | -0.24 | 2 | 75% | -0.96 | [-1.87, -0.25] | 0.02 |
| Close > 50-day SMA | +7.6% | +4.1% | -66.4% | +70.1% | 0.41 | 10 | 52% | -0.31 | [-1.39, +0.74] | 0.55 |
| MACD > signal | +14.8% | +7.8% | -70.4% | +65.3% | 0.44 | 21 | 50% | -0.28 | [-1.49, +0.91] | 0.64 |
| RSI 30/70 | +11.2% | +5.9% | -50.3% | +37.1% | 0.34 | 1 | 16% | -0.38 | [-2.10, +1.47] | 0.67 |
| Trailing stop 20% | -11.8% | -6.6% | -69.1% | +72.1% | 0.27 | 10 | 56% | -0.45 | [-1.49, +0.53] | 0.39 |
| Volume breakout | +91.8% | +42.4% | -55.7% | +63.3% | 0.87 | 4 | 41% | +0.15 | [-0.99, +1.24] | 0.78 |

### AMD (2022-08-26 to 2026-11-09)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +474.4% | +51.8% | -63.0% | +58.2% | 1.01 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +376.8% | +45.2% | -39.1% | +48.6% | 1.01 | 1 | 65% | +0.00 | [-0.56, +0.56] | 0.99 |
| Close > 50-day SMA | +182.1% | +28.1% | -41.8% | +43.7% | 0.78 | 37 | 53% | -0.22 | [-0.82, +0.31] | 0.45 |
| MACD > signal | +343.0% | +42.7% | -42.4% | +41.4% | 1.06 | 39 | 50% | +0.06 | [-0.48, +0.63] | 0.84 |
| RSI 30/70 | +47.5% | +9.7% | -54.7% | +31.9% | 0.45 | 3 | 33% | -0.56 | [-1.57, +0.45] | 0.27 |
| Trailing stop 20% | +167.7% | +26.5% | -58.9% | +49.6% | 0.72 | 11 | 71% | -0.29 | [-0.78, +0.20] | 0.24 |
| Volume breakout | +177.7% | +27.6% | -36.9% | +37.1% | 0.84 | 10 | 38% | -0.16 | [-0.93, +0.50] | 0.62 |

### NVDA (2022-08-26 to 2026-11-09)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +1034.6% | +78.6% | -36.9% | +49.0% | 1.43 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +590.1% | +58.6% | -28.4% | +43.0% | 1.29 | 1 | 84% | -0.14 | [-0.64, +0.33] | 0.53 |
| Close > 50-day SMA | +346.8% | +43.0% | -39.1% | +39.0% | 1.11 | 38 | 69% | -0.32 | [-0.88, +0.29] | 0.29 |
| MACD > signal | +152.9% | +24.8% | -46.7% | +34.4% | 0.81 | 40 | 51% | -0.61 | [-1.29, +0.10] | 0.09 |
| RSI 30/70 | +57.5% | +11.5% | -22.6% | +18.3% | 0.68 | 2 | 7% | -0.75 | [-1.80, +0.13] | 0.12 |
| Trailing stop 20% | +624.6% | +60.5% | -36.6% | +44.7% | 1.28 | 8 | 89% | -0.15 | [-0.49, +0.16] | 0.38 |
| Volume breakout | +211.5% | +31.2% | -19.8% | +26.3% | 1.16 | 7 | 31% | -0.27 | [-1.19, +0.51] | 0.54 |

### MRVL (2022-08-26 to 2026-11-09)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +220.1% | +32.0% | -60.8% | +67.1% | 0.75 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +50.5% | +10.3% | -65.2% | +57.3% | 0.45 | 2 | 68% | -0.29 | [-0.77, +0.15] | 0.20 |
| Close > 50-day SMA | +65.8% | +12.8% | -51.5% | +52.7% | 0.49 | 36 | 58% | -0.26 | [-0.87, +0.31] | 0.39 |
| MACD > signal | +101.6% | +18.2% | -62.5% | +50.2% | 0.58 | 44 | 51% | -0.17 | [-0.86, +0.55] | 0.66 |
| RSI 30/70 | +61.0% | +12.0% | -32.1% | +28.7% | 0.54 | 2 | 19% | -0.20 | [-1.08, +0.83] | 0.66 |
| Trailing stop 20% | +64.8% | +12.7% | -53.3% | +57.1% | 0.49 | 15 | 77% | -0.26 | [-0.79, +0.23] | 0.31 |
| Volume breakout | +76.0% | +14.5% | -46.2% | +42.0% | 0.53 | 11 | 36% | -0.22 | [-1.10, +0.54] | 0.58 |

### GOOG (2022-08-26 to 2026-11-09)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +161.5% | +25.8% | -30.2% | +31.7% | 0.88 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +151.5% | +24.6% | -29.4% | +25.9% | 0.98 | 2 | 76% | +0.10 | [-0.39, +0.58] | 0.69 |
| Close > 50-day SMA | +85.6% | +15.9% | -22.2% | +23.6% | 0.74 | 34 | 63% | -0.14 | [-0.80, +0.52] | 0.68 |
| MACD > signal | +36.1% | +7.6% | -18.1% | +21.5% | 0.45 | 42 | 50% | -0.43 | [-1.15, +0.24] | 0.22 |
| RSI 30/70 | +30.4% | +6.6% | -20.4% | +18.1% | 0.44 | 4 | 25% | -0.44 | [-1.36, +0.48] | 0.31 |
| Trailing stop 20% | +43.2% | +9.0% | -40.4% | +29.7% | 0.44 | 6 | 92% | -0.45 | [-0.88, -0.09] | 0.03 |
| Volume breakout | +105.6% | +18.8% | -17.4% | +19.4% | 0.98 | 8 | 46% | +0.10 | [-0.73, +0.87] | 0.81 |

### FSLR (2022-08-26 to 2026-11-09)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +57.4% | +11.4% | -60.0% | +55.1% | 0.47 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +15.6% | +3.5% | -51.1% | +41.8% | 0.29 | 4 | 59% | -0.18 | [-0.77, +0.34] | 0.51 |
| Close > 50-day SMA | +47.0% | +9.6% | -46.8% | +40.3% | 0.43 | 28 | 50% | -0.04 | [-0.61, +0.50] | 0.87 |
| MACD > signal | -54.7% | -17.2% | -74.1% | +40.6% | -0.26 | 48 | 49% | -0.73 | [-1.41, -0.09] | 0.04 |
| RSI 30/70 | +30.1% | +6.5% | -42.8% | +30.4% | 0.35 | 2 | 27% | -0.12 | [-1.13, +0.75] | 0.82 |
| Trailing stop 20% | +31.5% | +6.8% | -52.3% | +45.2% | 0.37 | 11 | 69% | -0.10 | [-0.56, +0.40] | 0.66 |
| Volume breakout | -18.3% | -4.7% | -53.8% | +32.2% | 0.01 | 13 | 38% | -0.46 | [-1.29, +0.38] | 0.28 |

### ETN (2022-08-26 to 2026-11-09)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +170.1% | +26.8% | -34.5% | +33.9% | 0.87 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +69.9% | +13.5% | -35.7% | +30.4% | 0.57 | 2 | 83% | -0.30 | [-0.75, +0.05] | 0.14 |
| Close > 50-day SMA | +32.3% | +6.9% | -37.5% | +24.5% | 0.40 | 46 | 65% | -0.47 | [-1.07, +0.14] | 0.13 |
| MACD > signal | +37.3% | +7.9% | -25.8% | +22.4% | 0.45 | 48 | 50% | -0.42 | [-1.02, +0.24] | 0.21 |
| RSI 30/70 | +15.7% | +3.6% | -18.6% | +11.5% | 0.36 | 1 | 5% | -0.51 | [-1.40, +0.59] | 0.31 |
| Trailing stop 20% | +179.1% | +27.8% | -23.6% | +30.9% | 0.95 | 2 | 95% | +0.08 | [-0.11, +0.30] | 0.42 |
| Volume breakout | +21.6% | +4.8% | -29.3% | +18.1% | 0.35 | 10 | 38% | -0.52 | [-1.30, +0.30] | 0.21 |

### TSLA (2022-08-26 to 2026-11-09)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +32.7% | +7.0% | -65.0% | +58.3% | 0.41 | 0 | 100% |  |  |  |
| 50/200 SMA cross | -26.4% | -7.1% | -56.8% | +40.1% | 0.01 | 4 | 47% | -0.39 | [-1.26, +0.41] | 0.36 |
| Close > 50-day SMA | +51.0% | +10.3% | -41.1% | +38.5% | 0.45 | 43 | 53% | +0.04 | [-0.69, +0.84] | 0.90 |
| MACD > signal | +396.5% | +46.6% | -39.8% | +40.8% | 1.14 | 42 | 51% | +0.73 | [+0.07, +1.43] | 0.04 |
| RSI 30/70 | +46.8% | +9.6% | -52.7% | +40.2% | 0.43 | 4 | 42% | +0.02 | [-0.68, +0.75] | 0.94 |
| Trailing stop 20% | +35.3% | +7.5% | -47.9% | +45.0% | 0.38 | 11 | 71% | -0.02 | [-0.64, +0.58] | 0.95 |
| Volume breakout | +40.5% | +8.5% | -35.4% | +25.7% | 0.44 | 9 | 18% | +0.04 | [-0.85, +0.99] | 0.94 |

### AMZN (2022-08-26 to 2026-11-09)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +105.6% | +18.8% | -40.0% | +34.1% | 0.67 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +37.2% | +7.9% | -41.4% | +27.8% | 0.41 | 2 | 73% | -0.26 | [-0.91, +0.34] | 0.40 |
| Close > 50-day SMA | +31.9% | +6.8% | -41.0% | +23.2% | 0.40 | 35 | 63% | -0.27 | [-0.92, +0.46] | 0.45 |
| MACD > signal | -0.4% | -0.1% | -28.7% | +22.7% | 0.11 | 50 | 49% | -0.56 | [-1.27, +0.13] | 0.12 |
| RSI 30/70 | +94.0% | +17.1% | -22.0% | +21.6% | 0.84 | 4 | 33% | +0.16 | [-0.54, +0.91] | 0.68 |
| Trailing stop 20% | +111.0% | +19.5% | -24.2% | +29.8% | 0.75 | 3 | 87% | +0.07 | [-0.35, +0.54] | 0.75 |
| Volume breakout | +6.8% | +1.6% | -35.7% | +18.7% | 0.18 | 11 | 45% | -0.50 | [-1.41, +0.46] | 0.30 |

### IBM (2022-08-26 to 2026-11-09)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +117.5% | +20.4% | -37.5% | +31.5% | 0.75 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +61.5% | +12.1% | -28.7% | +22.8% | 0.62 | 3 | 73% | -0.13 | [-0.79, +0.52] | 0.67 |
| Close > 50-day SMA | +53.7% | +10.8% | -42.6% | +25.1% | 0.54 | 27 | 59% | -0.21 | [-0.67, +0.40] | 0.43 |
| MACD > signal | +112.4% | +19.7% | -43.1% | +23.9% | 0.88 | 29 | 50% | +0.13 | [-0.48, +0.87] | 0.72 |
| RSI 30/70 | +175.4% | +27.4% | -16.5% | +17.4% | 1.48 | 8 | 35% | +0.73 | [-0.23, +1.66] | 0.12 |
| Trailing stop 20% | +65.1% | +12.7% | -45.9% | +30.3% | 0.55 | 3 | 92% | -0.20 | [-0.44, +0.02] | 0.09 |
| Volume breakout | +65.6% | +12.8% | -25.6% | +17.0% | 0.79 | 10 | 40% | +0.04 | [-0.92, +0.95] | 0.92 |

### GEV (2025-01-13 to 2026-11-09)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +117.7% | +53.3% | -38.3% | +56.2% | 1.04 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +133.0% | +59.1% | -38.3% | +54.9% | 1.12 | 1 | 98% | +0.08 | [-0.07, +0.27] | 0.24 |
| Close > 50-day SMA | +79.1% | +37.7% | -32.7% | +43.9% | 0.95 | 15 | 64% | -0.09 | [-0.72, +0.45] | 0.75 |
| MACD > signal | +60.6% | +29.7% | -31.0% | +42.1% | 0.83 | 17 | 48% | -0.21 | [-1.04, +0.58] | 0.60 |
| RSI 30/70 | +29.1% | +15.1% | -34.4% | +34.8% | 0.58 | 1 | 31% | -0.47 | [-1.69, +0.67] | 0.43 |
| Trailing stop 20% | +44.2% | +22.3% | -45.9% | +50.2% | 0.65 | 5 | 88% | -0.39 | [-0.94, +0.06] | 0.12 |
| Volume breakout | +24.5% | +12.8% | -24.6% | +33.6% | 0.53 | 3 | 36% | -0.51 | [-1.71, +0.56] | 0.39 |

### CEG (2022-11-02 to 2026-11-09)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +201.4% | +31.8% | -50.7% | +49.3% | 0.80 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +96.8% | +18.4% | -50.7% | +43.5% | 0.60 | 3 | 72% | -0.20 | [-0.64, +0.20] | 0.35 |
| Close > 50-day SMA | +139.1% | +24.4% | -40.9% | +37.3% | 0.77 | 47 | 57% | -0.04 | [-0.61, +0.48] | 0.90 |
| MACD > signal | +25.6% | +5.9% | -41.5% | +36.9% | 0.34 | 41 | 49% | -0.47 | [-1.13, +0.18] | 0.15 |
| RSI 30/70 | +104.2% | +19.5% | -28.6% | +32.2% | 0.71 | 3 | 37% | -0.09 | [-0.86, +0.72] | 0.83 |
| Trailing stop 20% | +90.0% | +17.4% | -52.8% | +43.8% | 0.58 | 9 | 84% | -0.22 | [-0.65, +0.23] | 0.32 |
| Volume breakout | +86.0% | +16.8% | -30.0% | +30.7% | 0.66 | 9 | 39% | -0.15 | [-0.86, +0.56] | 0.67 |

### VST (2022-08-26 to 2026-11-09)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +476.3% | +51.9% | -48.8% | +52.1% | 1.07 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +425.1% | +48.6% | -48.8% | +44.1% | 1.12 | 3 | 68% | +0.06 | [-0.28, +0.44] | 0.77 |
| Close > 50-day SMA | +50.8% | +10.3% | -67.2% | +38.1% | 0.45 | 45 | 64% | -0.61 | [-1.28, -0.01] | 0.06 |
| MACD > signal | +66.6% | +13.0% | -49.0% | +37.2% | 0.52 | 47 | 51% | -0.55 | [-1.19, +0.12] | 0.11 |
| RSI 30/70 | +201.5% | +30.2% | -27.3% | +26.7% | 1.12 | 3 | 20% | +0.05 | [-0.79, +0.86] | 0.91 |
| Trailing stop 20% | +216.9% | +31.7% | -56.3% | +44.7% | 0.84 | 9 | 88% | -0.22 | [-0.63, +0.21] | 0.31 |
| Volume breakout | +278.5% | +37.4% | -31.2% | +31.4% | 1.18 | 9 | 43% | +0.11 | [-0.67, +0.93] | 0.77 |

### DELL (2022-08-26 to 2026-11-09)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +826.3% | +70.2% | -59.6% | +57.8% | 1.20 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +424.8% | +48.6% | -50.8% | +50.4% | 1.03 | 3 | 68% | -0.17 | [-0.65, +0.27] | 0.47 |
| Close > 50-day SMA | +1326.9% | +88.7% | -27.5% | +49.3% | 1.52 | 21 | 67% | +0.32 | [-0.16, +0.84] | 0.19 |
| MACD > signal | +141.4% | +23.4% | -57.7% | +43.1% | 0.69 | 45 | 52% | -0.51 | [-1.17, +0.17] | 0.15 |
| RSI 30/70 | +158.7% | +25.5% | -23.7% | +25.9% | 1.00 | 4 | 28% | -0.20 | [-1.25, +0.78] | 0.71 |
| Trailing stop 20% | +900.8% | +73.4% | -55.9% | +51.6% | 1.31 | 7 | 82% | +0.11 | [-0.27, +0.49] | 0.57 |
| Volume breakout | +378.1% | +45.3% | -37.8% | +43.2% | 1.07 | 11 | 45% | -0.13 | [-0.83, +0.54] | 0.68 |

### TSM (2022-08-26 to 2026-11-09)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +400.7% | +46.9% | -36.8% | +39.3% | 1.18 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +166.8% | +26.4% | -36.8% | +35.9% | 0.83 | 2 | 81% | -0.34 | [-0.88, +0.18] | 0.19 |
| Close > 50-day SMA | +190.3% | +29.0% | -28.8% | +31.6% | 0.96 | 37 | 68% | -0.21 | [-0.79, +0.40] | 0.47 |
| MACD > signal | +142.0% | +23.5% | -32.1% | +28.4% | 0.89 | 44 | 49% | -0.29 | [-0.90, +0.29] | 0.37 |
| RSI 30/70 | +42.3% | +8.8% | -23.0% | +16.6% | 0.59 | 3 | 12% | -0.59 | [-1.58, +0.39] | 0.25 |
| Trailing stop 20% | +215.0% | +31.5% | -30.6% | +36.7% | 0.93 | 6 | 91% | -0.25 | [-0.63, +0.10] | 0.18 |
| Volume breakout | +77.0% | +14.6% | -26.8% | +26.4% | 0.65 | 11 | 46% | -0.53 | [-1.34, +0.22] | 0.17 |

### BE (2022-08-26 to 2026-11-09)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +652.8% | +62.0% | -67.8% | +89.8% | 0.97 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +248.8% | +34.8% | -71.9% | +74.6% | 0.77 | 4 | 63% | -0.20 | [-0.84, +0.34] | 0.50 |
| Close > 50-day SMA | +353.8% | +43.5% | -53.1% | +69.7% | 0.85 | 31 | 52% | -0.12 | [-0.69, +0.38] | 0.67 |
| MACD > signal | +217.3% | +31.8% | -60.0% | +65.8% | 0.73 | 41 | 50% | -0.24 | [-0.97, +0.39] | 0.47 |
| RSI 30/70 | +147.7% | +24.2% | -61.8% | +47.0% | 0.69 | 4 | 47% | -0.28 | [-1.14, +0.69] | 0.55 |
| Trailing stop 20% | +150.2% | +24.5% | -66.7% | +73.9% | 0.65 | 19 | 61% | -0.32 | [-0.87, +0.12] | 0.21 |
| Volume breakout | +275.5% | +37.2% | -58.1% | +61.0% | 0.80 | 11 | 30% | -0.17 | [-0.96, +0.54] | 0.66 |

![Strategy equity curves](backtest_equity.png)

## 5. Next-day forecasts

Not included: SKHY (only 86 trading days of history, needs 452); SPCX (only 104 trading days of history, needs 452).

### ALAB

Walk-forward test on 211 unseen days (2026-01-07 to 2026-11-06).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.526 | 0.526 | 0.528 | 0.454 | 0.25 | 0.826 | 0.827 |
| Logistic regression | 0.493 | 0.526 | 0.849 | 0.491 | 0.258 | 0.262 | 0.827 |
| Gradient boosting | 0.474 | 0.526 | 0.943 | 0.453 | 0.284 | 0.338 | 0.827 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 653.5 | 0.0 |  |  |
| Ridge regression | 671.1 | -0.0545 | 0.474 | 0.953 |
| Gradient boosting | 688.0 | -0.1085 | 0.45 | 0.994 |

Forecast for the next session:

```
  P(up) | Logistic regression      47.7%
  P(up) | Gradient boosting        60.4%
  P(up) | historical base rate     52.1%
  expected return (ridge)          +1.00%
  80% range low                    -8.79%
  80% range high                   +11.84%
  daily volatility                 +7.95%
```

Best out-of-sample AUC **0.491**; smallest p-value against a naive baseline 0.849, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![ALAB feature effects](forecast_ALAB.png)

### AMD

Walk-forward test on 550 unseen days (2024-08-29 to 2026-11-06).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.507 | 0.531 | 0.876 | 0.488 | 0.25 | 1.149 | 1.203 |
| Logistic regression | 0.489 | 0.531 | 0.978 | 0.488 | 0.256 | 0.626 | 1.203 |
| Gradient boosting | 0.491 | 0.531 | 0.973 | 0.488 | 0.268 | 0.328 | 1.203 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 404.3 | 0.0 |  |  |
| Ridge regression | 407.5 | -0.0161 | 0.495 | 0.826 |
| Gradient boosting | 410.9 | -0.0329 | 0.478 | 0.953 |

Forecast for the next session:

```
  P(up) | Logistic regression      56.8%
  P(up) | Gradient boosting        68.3%
  P(up) | historical base rate     51.3%
  expected return (ridge)          -0.48%
  80% range low                    -9.26%
  80% range high                   +9.15%
  daily volatility                 +7.21%
```

Best out-of-sample AUC **0.488**; smallest p-value against a naive baseline 0.826, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![AMD feature effects](forecast_AMD.png)

### NVDA

Walk-forward test on 550 unseen days (2024-08-29 to 2026-11-06).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.524 | 0.524 | 0.517 | 0.504 | 0.25 | 0.656 | 0.656 |
| Logistic regression | 0.518 | 0.524 | 0.618 | 0.521 | 0.252 | 0.626 | 0.656 |
| Gradient boosting | 0.505 | 0.524 | 0.815 | 0.479 | 0.268 | 0.657 | 0.656 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 281.5 | 0.0 |  |  |
| Ridge regression | 282.2 | -0.0055 | 0.513 | 0.584 |
| Gradient boosting | 289.1 | -0.055 | 0.531 | 0.957 |

Forecast for the next session:

```
  P(up) | Logistic regression      68.0%
  P(up) | Gradient boosting        58.5%
  P(up) | historical base rate     53.6%
  expected return (ridge)          +1.18%
  80% range low                    -2.67%
  80% range high                   +5.17%
  daily volatility                 +3.02%
```

Best out-of-sample AUC **0.521**; smallest p-value against a naive baseline 0.584, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![NVDA feature effects](forecast_NVDA.png)

### MRVL

Walk-forward test on 550 unseen days (2024-08-29 to 2026-11-06).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.536 | 0.536 | 0.517 | 0.482 | 0.249 | 0.859 | 0.86 |
| Logistic regression | 0.538 | 0.536 | 0.483 | 0.54 | 0.254 | 0.956 | 0.86 |
| Gradient boosting | 0.516 | 0.536 | 0.837 | 0.542 | 0.263 | -0.092 | 0.86 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 481.8 | 0.0 |  |  |
| Ridge regression | 488.1 | -0.0261 | 0.525 | 0.942 |
| Gradient boosting | 493.2 | -0.0478 | 0.476 | 0.984 |

Forecast for the next session:

```
  P(up) | Logistic regression      47.5%
  P(up) | Gradient boosting        60.0%
  P(up) | historical base rate     52.5%
  expected return (ridge)          -1.28%
  80% range low                    -10.25%
  80% range high                   +8.58%
  daily volatility                 +7.43%
```

Best out-of-sample AUC **0.542**; smallest p-value against a naive baseline 0.483, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![MRVL feature effects](forecast_MRVL.png)

### GOOG

Walk-forward test on 550 unseen days (2024-08-29 to 2026-11-06).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.524 | 0.524 | 0.517 | 0.483 | 0.25 | 0.973 | 0.974 |
| Logistic regression | 0.562 | 0.524 | 0.04 | 0.535 | 0.253 | 0.627 | 0.974 |
| Gradient boosting | 0.535 | 0.524 | 0.32 | 0.53 | 0.262 | 0.7 | 0.974 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 201.6 | 0.0 |  |  |
| Ridge regression | 203.9 | -0.0231 | 0.529 | 0.957 |
| Gradient boosting | 208.2 | -0.0668 | 0.515 | 0.996 |

Forecast for the next session:

```
  P(up) | Logistic regression      49.9%
  P(up) | Gradient boosting        49.0%
  P(up) | historical base rate     52.9%
  expected return (ridge)          +0.00%
  80% range low                    -3.97%
  80% range high                   +4.13%
  daily volatility                 +3.16%
```

Best out-of-sample AUC **0.535**; smallest p-value against a naive baseline 0.040, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![GOOG feature effects](forecast_GOOG.png)

### FSLR

Walk-forward test on 550 unseen days (2024-08-29 to 2026-11-06).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.513 | 0.513 | 0.517 | 0.467 | 0.25 |  | 0.168 |
| Logistic regression | 0.513 | 0.513 | 0.517 | 0.529 | 0.251 | -0.203 | 0.168 |
| Gradient boosting | 0.516 | 0.513 | 0.449 | 0.527 | 0.259 | 0.089 | 0.168 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 363.9 | 0.0 |  |  |
| Ridge regression | 364.9 | -0.0059 | 0.515 | 0.687 |
| Gradient boosting | 376.2 | -0.0687 | 0.5 | 0.999 |

Forecast for the next session:

```
  P(up) | Logistic regression      63.4%
  P(up) | Gradient boosting        59.8%
  P(up) | historical base rate     49.2%
  expected return (ridge)          +0.16%
  80% range low                    -3.30%
  80% range high                   +3.75%
  daily volatility                 +2.75%
```

Best out-of-sample AUC **0.529**; smallest p-value against a naive baseline 0.449, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![FSLR feature effects](forecast_FSLR.png)

### ETN

Walk-forward test on 550 unseen days (2024-08-29 to 2026-11-06).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.525 | 0.525 | 0.517 | 0.467 | 0.25 | 0.432 | 0.433 |
| Logistic regression | 0.518 | 0.525 | 0.65 | 0.506 | 0.256 | 0.572 | 0.433 |
| Gradient boosting | 0.525 | 0.525 | 0.517 | 0.528 | 0.259 | 0.367 | 0.433 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 248.1 | 0.0 |  |  |
| Ridge regression | 249.8 | -0.0144 | 0.527 | 0.785 |
| Gradient boosting | 254.5 | -0.0526 | 0.515 | 0.971 |

Forecast for the next session:

```
  P(up) | Logistic regression      57.2%
  P(up) | Gradient boosting        81.9%
  P(up) | historical base rate     54.0%
  expected return (ridge)          +0.31%
  80% range low                    -5.22%
  80% range high                   +6.16%
  daily volatility                 +4.42%
```

Best out-of-sample AUC **0.528**; smallest p-value against a naive baseline 0.517, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![ETN feature effects](forecast_ETN.png)

### TSLA

Walk-forward test on 550 unseen days (2024-08-29 to 2026-11-06).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.504 | 0.504 | 0.517 | 0.45 | 0.25 | 0.761 | 0.761 |
| Logistic regression | 0.527 | 0.504 | 0.143 | 0.512 | 0.253 | 0.878 | 0.761 |
| Gradient boosting | 0.536 | 0.504 | 0.068 | 0.535 | 0.261 | 0.853 | 0.761 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 370.5 | 0.0 |  |  |
| Ridge regression | 375.0 | -0.0244 | 0.495 | 0.95 |
| Gradient boosting | 378.2 | -0.0421 | 0.498 | 0.937 |

Forecast for the next session:

```
  P(up) | Logistic regression      50.4%
  P(up) | Gradient boosting        48.2%
  P(up) | historical base rate     50.7%
  expected return (ridge)          +0.14%
  80% range low                    -4.58%
  80% range high                   +5.10%
  daily volatility                 +3.77%
```

Best out-of-sample AUC **0.535**; smallest p-value against a naive baseline 0.068, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![TSLA feature effects](forecast_TSLA.png)

### AMZN

Walk-forward test on 550 unseen days (2024-08-29 to 2026-11-06).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.516 | 0.516 | 0.517 | 0.467 | 0.25 | 0.758 | 0.759 |
| Logistic regression | 0.549 | 0.516 | 0.068 | 0.563 | 0.248 | 1.058 | 0.759 |
| Gradient boosting | 0.505 | 0.516 | 0.711 | 0.51 | 0.265 | -0.083 | 0.759 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 212.6 | 0.0 |  |  |
| Ridge regression | 214.3 | -0.0159 | 0.547 | 0.862 |
| Gradient boosting | 221.8 | -0.0884 | 0.518 | 1.0 |

Forecast for the next session:

```
  P(up) | Logistic regression      44.0%
  P(up) | Gradient boosting        37.6%
  P(up) | historical base rate     51.2%
  expected return (ridge)          +0.15%
  80% range low                    -3.14%
  80% range high                   +3.56%
  daily volatility                 +2.61%
```

Best out-of-sample AUC **0.563**; smallest p-value against a naive baseline 0.068, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![AMZN feature effects](forecast_AMZN.png)

### IBM

Walk-forward test on 550 unseen days (2024-08-29 to 2026-11-06).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.547 | 0.547 | 0.518 | 0.471 | 0.248 | 0.514 | 0.515 |
| Logistic regression | 0.527 | 0.547 | 0.838 | 0.474 | 0.255 | 0.632 | 0.515 |
| Gradient boosting | 0.509 | 0.547 | 0.967 | 0.497 | 0.266 | 0.549 | 0.515 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 253.5 | 0.0 |  |  |
| Ridge regression | 256.9 | -0.0273 | 0.531 | 0.964 |
| Gradient boosting | 257.3 | -0.0309 | 0.509 | 0.968 |

Forecast for the next session:

```
  P(up) | Logistic regression      53.3%
  P(up) | Gradient boosting        63.1%
  P(up) | historical base rate     55.0%
  expected return (ridge)          -0.03%
  80% range low                    -2.18%
  80% range high                   +2.17%
  daily volatility                 +1.70%
```

Best out-of-sample AUC **0.497**; smallest p-value against a naive baseline 0.838, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![IBM feature effects](forecast_IBM.png)

### GEV

Walk-forward test on 206 unseen days (2026-01-14 to 2026-11-06).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.534 | 0.534 | 0.528 | 0.469 | 0.249 | 0.846 | 0.847 |
| Logistic regression | 0.505 | 0.534 | 0.818 | 0.5 | 0.257 | 0.56 | 0.847 |
| Gradient boosting | 0.534 | 0.534 | 0.528 | 0.536 | 0.267 | 1.235 | 0.847 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 338.6 | 0.0 |  |  |
| Ridge regression | 343.9 | -0.0314 | 0.553 | 0.762 |
| Gradient boosting | 348.9 | -0.0619 | 0.534 | 0.862 |

Forecast for the next session:

```
  P(up) | Logistic regression      55.2%
  P(up) | Gradient boosting        83.2%
  P(up) | historical base rate     54.4%
  expected return (ridge)          +1.08%
  80% range low                    -5.08%
  80% range high                   +7.65%
  daily volatility                 +4.91%
```

Best out-of-sample AUC **0.536**; smallest p-value against a naive baseline 0.528, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![GEV feature effects](forecast_GEV.png)

### CEG

Walk-forward test on 504 unseen days (2024-11-04 to 2026-11-06).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.506 | 0.506 | 0.518 | 0.482 | 0.251 | 0.468 | 0.468 |
| Logistic regression | 0.48 | 0.506 | 0.885 | 0.491 | 0.26 | 0.088 | 0.468 |
| Gradient boosting | 0.484 | 0.506 | 0.847 | 0.472 | 0.274 | -0.08 | 0.468 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 352.4 | 0.0 |  |  |
| Ridge regression | 361.0 | -0.0498 | 0.482 | 0.99 |
| Gradient boosting | 364.4 | -0.0696 | 0.506 | 0.997 |

Forecast for the next session:

```
  P(up) | Logistic regression      40.6%
  P(up) | Gradient boosting        35.2%
  P(up) | historical base rate     52.1%
  expected return (ridge)          +0.14%
  80% range low                    -4.70%
  80% range high                   +5.22%
  daily volatility                 +3.86%
```

Best out-of-sample AUC **0.491**; smallest p-value against a naive baseline 0.847, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![CEG feature effects](forecast_CEG.png)

### VST

Walk-forward test on 550 unseen days (2024-08-29 to 2026-11-06).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.518 | 0.518 | 0.517 | 0.482 | 0.25 | 0.666 | 0.666 |
| Logistic regression | 0.489 | 0.518 | 0.92 | 0.479 | 0.261 | 1.184 | 0.666 |
| Gradient boosting | 0.535 | 0.518 | 0.234 | 0.534 | 0.263 | 1.283 | 0.666 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 395.9 | 0.0 |  |  |
| Ridge regression | 400.2 | -0.0221 | 0.496 | 0.841 |
| Gradient boosting | 402.3 | -0.0329 | 0.505 | 0.908 |

Forecast for the next session:

```
  P(up) | Logistic regression      41.6%
  P(up) | Gradient boosting        38.8%
  P(up) | historical base rate     52.8%
  expected return (ridge)          +0.92%
  80% range low                    -6.07%
  80% range high                   +8.42%
  daily volatility                 +5.60%
```

Best out-of-sample AUC **0.534**; smallest p-value against a naive baseline 0.234, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![VST feature effects](forecast_VST.png)

### DELL

Walk-forward test on 550 unseen days (2024-08-29 to 2026-11-06).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.522 | 0.522 | 0.517 | 0.482 | 0.25 | 1.14 | 1.14 |
| Logistic regression | 0.515 | 0.522 | 0.65 | 0.508 | 0.255 | 0.159 | 1.14 |
| Gradient boosting | 0.504 | 0.522 | 0.815 | 0.498 | 0.268 | 0.478 | 1.14 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 405.5 | 0.0 |  |  |
| Ridge regression | 411.7 | -0.0306 | 0.491 | 0.986 |
| Gradient boosting | 418.3 | -0.0638 | 0.513 | 0.997 |

Forecast for the next session:

```
  P(up) | Logistic regression      61.1%
  P(up) | Gradient boosting        53.3%
  P(up) | historical base rate     51.7%
  expected return (ridge)          +0.42%
  80% range low                    -7.54%
  80% range high                   +9.07%
  daily volatility                 +6.44%
```

Best out-of-sample AUC **0.508**; smallest p-value against a naive baseline 0.650, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![DELL feature effects](forecast_DELL.png)

### TSM

Walk-forward test on 550 unseen days (2024-08-29 to 2026-11-06).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.498 | 0.535 | 0.96 | 0.47 | 0.25 | 0.917 | 1.15 |
| Logistic regression | 0.531 | 0.535 | 0.585 | 0.522 | 0.251 | 0.999 | 1.15 |
| Gradient boosting | 0.511 | 0.535 | 0.876 | 0.502 | 0.263 | 1.075 | 1.15 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 264.9 | 0.0 |  |  |
| Ridge regression | 263.4 | 0.0117 | 0.525 | 0.247 |
| Gradient boosting | 271.0 | -0.0465 | 0.525 | 0.983 |

Forecast for the next session:

```
  P(up) | Logistic regression      59.5%
  P(up) | Gradient boosting        61.9%
  P(up) | historical base rate     51.5%
  expected return (ridge)          +0.04%
  80% range low                    -4.69%
  80% range high                   +5.01%
  daily volatility                 +3.78%
```

Best out-of-sample AUC **0.522**; smallest p-value against a naive baseline 0.247, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![TSM feature effects](forecast_TSM.png)

### BE

Walk-forward test on 550 unseen days (2024-08-29 to 2026-11-06).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.484 | 0.516 | 0.943 | 0.479 | 0.251 |  | 1.706 |
| Logistic regression | 0.471 | 0.516 | 0.985 | 0.463 | 0.266 | 0.578 | 1.706 |
| Gradient boosting | 0.5 | 0.516 | 0.791 | 0.477 | 0.269 | 0.975 | 1.706 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 652.6 | 0.0 |  |  |
| Ridge regression | 670.6 | -0.0558 | 0.465 | 0.997 |
| Gradient boosting | 665.6 | -0.0403 | 0.495 | 0.987 |

Forecast for the next session:

```
  P(up) | Logistic regression      53.2%
  P(up) | Gradient boosting        47.1%
  P(up) | historical base rate     49.6%
  expected return (ridge)          +0.69%
  80% range low                    -8.70%
  80% range high                   +11.06%
  daily volatility                 +7.64%
```

Best out-of-sample AUC **0.477**; smallest p-value against a naive baseline 0.791, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![BE feature effects](forecast_BE.png)

## 6. Stock screen and entry plans

| ticker | rank | score | passes_filters | close | momentum_12_1 | momentum_6m | volatility | off_52w_high | forward_pe | pullback_entry | breakout_trigger | stop | stop_% | shares | position_$ | max_loss_$ | filter_notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DELL | 1 | +1.07 | True | 346.31 | +296.4% | +40.6% | +85.3% | -41.1% | 11.4 | 312.77 | 572.82 | 245.68 | -21.5% | 14 | 4379.0 | 939.0 |  |
| AMD | 2 | +0.88 | True | 508.58 | +155.8% | +10.9% | +77.7% | -21.7% | 28.8 | 469.86 | 606.74 | 392.43 | -16.5% | 12 | 5638.0 | 929.0 |  |
| MSFT | 3 | +0.53 | True | 545.18 | +8.5% | +32.6% | +27.2% | -1.9% | 22.5 | 531.61 | 556.91 | 500.41 | -5.9% | 18 | 9569.0 | 562.0 |  |
| V | 4 | +0.51 | True | 422.16 | +15.3% | +30.9% | +21.7% | -3.3% | 24.6 | 410.51 | 437.44 | 392.04 | -4.5% | 24 | 9852.0 | 443.0 |  |
| LLY | 5 | +0.49 | True | 1411.95 | +26.6% | +46.5% | +31.5% | -0.4% | 27.9 | 1313.42 | 1420.83 | 1216.1 | -7.4% | 7 | 9194.0 | 681.0 |  |
| JNJ | 6 | +0.46 | True | 282.11 | +43.0% | +28.8% | +25.0% | +0.0% | 24.3 | 266.07 | 282.67 | 251.37 | -5.5% | 37 | 9845.0 | 544.0 |  |
| XOM | 7 | +0.45 | True | 164.73 | +51.8% | +11.5% | +26.3% | -12.0% | 13.2 | 160.11 | 187.62 | 150.88 | -5.8% | 62 | 9927.0 | 573.0 |  |
| KO | 8 | +0.44 | True | 96.03 | +30.9% | +23.6% | +17.3% | +0.0% | 27.2 | 93.59 | 96.22 | 90.0 | -3.8% | 106 | 9921.0 | 381.0 |  |
| AAPL | 9 | +0.39 | True | 350.69 | +25.2% | +19.9% | +22.1% | +0.0% | 33.2 | 343.87 | 351.39 | 326.16 | -5.2% | 29 | 9972.0 | 514.0 |  |
| JPM | 10 | +0.28 | True | 342.08 | +8.3% | +15.1% | +20.4% | -5.9% | 13.4 | 340.66 | 352.81 | 324.42 | -4.8% | 29 | 9879.0 | 471.0 |  |
| PG | 11 | +0.14 | True | 168.32 | +5.8% | +19.1% | +20.6% | +0.0% | 22.7 | 160.57 | 168.66 | 153.83 | -4.2% | 62 | 9956.0 | 418.0 |  |
| UNH | 12 | +0.12 | True | 397.62 | +21.1% | +4.7% | +23.7% | -8.3% | 17.0 | 390.31 | 425.83 | 366.65 | -6.1% | 25 | 9758.0 | 591.0 |  |
| LIN | 13 | +0.01 | True | 520.33 | +18.1% | +3.8% | +16.2% | -4.5% | 26.6 | 507.81 | 525.79 | 488.53 | -3.8% | 19 | 9648.0 | 366.0 |  |
| AMT | 14 | -0.02 | True | 189.00 | +6.5% | +8.7% | +29.4% | -3.0% | 27.0 | 185.6 | 195.25 | 174.76 | -5.8% | 53 | 9837.0 | 574.0 |  |
| AMZN | 15 | -0.08 | True | 266.93 | +8.0% | -0.8% | +31.3% | -6.0% | 24.5 | 254.65 | 267.46 | 235.29 | -7.6% | 39 | 9931.0 | 755.0 |  |

## 7. Portfolio construction

Not included: SKHY (only 86 trading days of history, needs 252); SPCX (only 104 trading days of history, needs 252).

Assets: ALAB, AMD, NVDA, MRVL, GOOG, FSLR, ETN, TSLA, AMZN, IBM, GEV, CEG, VST, DELL, TSM, BE, JPM, XOM, UNH, COST, TLT, GLD. Covariance: Ledoit-Wolf shrinkage on the last 252 trading days.

Weights and share of risk (%):

| asset | weight: Equal weight | weight: Inverse volatility | weight: Risk parity | weight: Minimum variance | risk share: Equal weight | risk share: Inverse volatility | risk share: Risk parity | risk share: Minimum variance |
|---|---|---|---|---|---|---|---|---|
| ALAB | 4.5 | 1.8 | 1.2 | 0.0 | 12.4 | 6.6 | 4.6 | 0.0 |
| AMD | 4.5 | 2.5 | 1.4 | 0.0 | 9.5 | 7.4 | 4.6 | 0.0 |
| NVDA | 4.5 | 4.6 | 3.4 | 5.1 | 3.9 | 6.0 | 4.8 | 5.6 |
| MRVL | 4.5 | 2.1 | 1.3 | 0.0 | 10.3 | 6.7 | 4.6 | 0.0 |
| GOOG | 4.5 | 5.2 | 4.6 | 4.5 | 1.9 | 4.0 | 4.8 | 4.9 |
| FSLR | 4.5 | 3.4 | 2.8 | 0.6 | 4.1 | 4.7 | 4.7 | 0.6 |
| ETN | 4.5 | 4.1 | 2.5 | 1.7 | 5.5 | 7.2 | 4.7 | 1.9 |
| TSLA | 4.5 | 3.9 | 2.5 | 0.0 | 4.6 | 6.1 | 4.7 | 0.0 |
| AMZN | 4.5 | 5.1 | 4.0 | 3.5 | 2.2 | 4.4 | 4.7 | 3.8 |
| IBM | 4.5 | 3.7 | 5.4 | 2.4 | 0.9 | 1.5 | 4.8 | 2.6 |
| GEV | 4.5 | 3.2 | 2.3 | 0.9 | 6.2 | 6.3 | 4.7 | 0.9 |
| CEG | 4.5 | 3.6 | 2.7 | 1.3 | 4.5 | 5.4 | 4.7 | 1.5 |
| VST | 4.5 | 3.3 | 2.4 | 0.1 | 5.4 | 6.0 | 4.7 | 0.2 |
| DELL | 4.5 | 2.3 | 1.8 | 0.0 | 7.5 | 5.3 | 4.7 | 0.0 |
| TSM | 4.5 | 4.2 | 2.3 | 0.0 | 5.5 | 7.6 | 4.7 | 0.0 |
| BE | 4.5 | 1.6 | 1.0 | 0.0 | 13.6 | 6.7 | 4.6 | 0.0 |
| JPM | 4.5 | 7.2 | 6.6 | 7.5 | 1.2 | 3.7 | 4.9 | 8.3 |
| XOM | 4.5 | 6.3 | 0.0 | 18.0 | -0.8 | -1.7 | -0.0 | 19.8 |
| UNH | 4.5 | 5.0 | 6.8 | 3.3 | 0.5 | 1.5 | 4.8 | 3.6 |
| COST | 4.5 | 8.0 | 22.8 | 17.7 | -0.9 | -1.6 | 5.1 | 19.5 |
| TLT | 4.5 | 12.9 | 16.8 | 30.0 | 0.3 | 2.1 | 5.4 | 23.0 |
| GLD | 4.5 | 5.9 | 5.3 | 3.6 | 1.8 | 4.2 | 4.8 | 3.9 |

| method | expected volatility | diversification ratio | effective number of bets | largest risk share | largest risk holder |
|---|---|---|---|---|---|
| Equal weight | 27.5% | 1.82 | 12.39 | 13.6% | BE |
| Inverse volatility | 18.2% | 2.16 | 16.50 | 7.6% | TSM |
| Risk parity | 13.9% | 2.48 | 20.97 | 5.4% | TLT |
| Minimum variance | 8.6% | 2.96 | 6.77 | 23.0% | TLT |

Concentration warnings:

- AMD and TSM have correlation 0.70: they tend to fall together
- ETN and GEV have correlation 0.72: they tend to fall together
- CEG and VST have correlation 0.80: they tend to fall together

Out-of-sample comparison, monthly rebalance (2025-04-01 to 2026-11-09):

| method | CAGR | Volatility | Sharpe | Max drawdown |
|---|---|---|---|---|
| Equal weight | +63.4% | +28.7% | 1.86 | -18.0% |
| Inverse volatility | +44.4% | +20.7% | 1.88 | -11.2% |
| Risk parity | +33.6% | +16.0% | 1.89 | -9.3% |
| Minimum variance | +14.7% | +10.0% | 1.42 | -6.8% |

![Correlations](portfolio_correlation.png)

![Risk shares](portfolio_risk_shares.png)

![Walk-forward](portfolio_walk_forward.png)

## 8. Opening gaps: do pre-market moves carry into the day?

Across 19,001 stock-days (18 watchlist stocks, 2021-11-11 to 2026-11-09), each 1% of opening gap went with a -0.02% move from the open to the close (95% block-bootstrap CI [-0.08%, +0.03%]): no reliable relationship, so the size of a gap has not told you which way the session goes.

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 768 | -5.2% | +0.30% | 50% |
| down 1-3% | 2896 | -1.7% | +0.09% | 52% |
| within 1% | 11046 | +0.0% | +0.02% | 50% |
| up 1-3% | 3367 | +1.7% | +0.09% | 52% |
| gap up 3%+ | 924 | +5.4% | -0.14% | 47% |

## 9. Deciding before the open vs at the previous close

From 2022-02-07 to 2026-11-06 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +33.1% a year (worst drawdown -41.1%) against +32.2% (-42.1%) for labels set at the previous close; the two agreed on 89% of stock-weeks. Sharpe ratio difference +0.03 (95% block-bootstrap CI [-0.12, +0.18]): deciding before the open has been **not distinguishable from deciding on the previous close**.

| strategy | CAGR | Volatility | Sharpe | Max drawdown |
|---|---|---|---|---|
| Board on the previous close | +32.2% | 35.0% | 0.97 | -42.1% |
| Board on the pre-market price | +33.1% | 34.3% | 1.01 | -41.1% |
| Equal-weight watchlist | +43.6% | 35.3% | 1.20 | -40.7% |

The pre-market version uses the official opening price as a stand-in for the last pre-market trade (free pre-market history is only days long), which slightly flatters it.
