# stocklab report
Generated 2026-11-12 | data source: `yahoo` | history: 5 years | watchlist: ALAB, AMD, NVDA, MRVL, GOOG, FSLR, SKHY, ETN, TSLA, SPCX, AMZN, IBM, GEV, CEG, VST, DELL, TSM, BE

> Educational research code, not investment advice. Past results do not predict future returns.

## 1. Decision board

Data as of the 2026-11-11 close. `*` = provisional (under 200 trading days of history).

| ticker | action | close | 1 day | 1 month | buy rank | sell warnings | pullback entry | breakout | stop | why |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | BUY | 552.90 | +7.3% | -8.7% | 2/18 | 2/15 | 550.43 | 579.60 | 470.30 | buy rank 2/18; +32% vs 200-day average; distribution days, volatility spike |
| AMZN | BUY | 266.17 | -1.7% | +2.9% | 5/18 | 1/15 | 255.87 | 271.41 | 236.96 | buy rank 5/18; +9% vs 200-day average; distribution days |
| TSM | WATCH | 413.35 | +4.3% | -7.1% | 4/18 | 4/15 | 410.39 | 440.39 | 376.45 | +3% vs 200-day average; below 50-day, MACD bearish, distribution days, volatility spike |
| IBM | WATCH | 248.22 | +1.5% | +8.3% | 6/18 | 4/15 | 246.59 | 257.02 | 232.87 | +2% vs 200-day average; death cross, MACD bearish, 20%+ off high |
| TSLA | WATCH | 390.84 | +2.9% | +4.2% | 13/18 | 5/15 | 381.83 | 408.27 | 348.62 | +2% vs 200-day average; death cross, MACD bearish, distribution days, 20%+ off high |
| DELL | REDUCE | 373.68 | +11.8% | -34.6% | 1/18 | 7/15 |  |  |  | +10% vs 200-day average; below 50-day, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| ALAB | REDUCE | 230.91 | +6.8% | -29.0% | 9/18 | 8/15 |  |  |  | -10% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, below chandelier stop |
| NVDA | REDUCE | 173.73 | +2.9% | -24.0% | 10/18 | 8/15 |  |  |  | -15% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, below chandelier stop |
| CEG | REDUCE | 274.73 | +2.6% | -7.1% | 14/18 | 6/15 |  |  |  | -1% vs 200-day average; below 200-day, death cross, distribution days, 20%+ off high |
| SKHY | REDUCE* | 142.25 | +9.7% | -9.4% | 15/18 | 4/10 |  |  |  | -14% vs 50-day average; below 50-day, MACD bearish, distribution days, 20%+ off high (provisional: 88 days of history) |
| BE | REDUCE | 209.47 | +13.0% | -20.5% | 16/18 | 6/15 |  |  |  | -6% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high |
| MRVL | SELL | 168.80 | +9.3% | -37.2% | 3/18 | 9/15 |  |  |  | -9% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| SPCX | SELL* | 139.75 | -2.3% | -10.7% | 7/18 | 6/10 |  |  |  | -6% vs 50-day average; below 50-day, MACD bearish, distribution days, 20%+ off high, below chandelier stop (provisional: 106 days of history) |
| ETN | SELL | 360.62 | +1.8% | -15.5% | 8/18 | 9/15 |  |  |  | -9% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| GEV | SELL | 808.24 | +1.4% | -19.5% | 11/18 | 11/15 |  |  |  | -15% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| GOOG | SELL | 290.63 | +2.0% | -16.8% | 12/18 | 11/15 |  |  |  | -14% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| VST | SELL | 133.45 | +1.7% | -17.8% | 17/18 | 11/15 |  |  |  | -12% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, 20%+ off high, volatility spike, below chandelier stop |
| FSLR | SELL | 178.11 | -1.6% | -4.5% | 18/18 | 9/15 |  |  |  | -17% vs 200-day average; below 50-day, below 200-day, death cross, distribution days, 20%+ off high, below chandelier stop |

![Board label each week](board_history.png)

**Trading the labels** (2022-02-08 to 2026-11-11): buy on BUY, exit on SELL, REDUCE or AVOID, reviewed weekly with next-day execution and 5 bp costs.

| strategy | CAGR | Volatility | Sharpe | Max drawdown | Time invested | Avg holdings |
|---|---|---|---|---|---|---|
| Board strategy | +36.0% | 33.5% | 1.09 | -39.1% | 98% | 6.4 |
| Equal-weight watchlist | +44.3% | 34.2% | 1.24 | -36.8% | 100% | 15.0 |
| SPY (buy & hold) | +12.8% | 17.3% | 0.78 | -22.1% |  |  |

Sharpe difference vs equal weight: -0.16, 95% block-bootstrap CI [-0.60, +0.30].

Forward 21-day return after each label, relative to the watchlist average on the same date (sampled every 21 days, t-test across dates):

| label | observations | dates | mean 21d excess return | hit rate | p_value |
|---|---|---|---|---|---|
| BUY | 265 | 56 | +0.4% | 52% | 0.65 |
| HOLD | 124 | 43 | +0.9% | 47% | 0.64 |
| WATCH | 156 | 49 | +1.3% | 55% | 0.29 |
| AVOID | 48 | 23 | +0.4% | 61% | 0.85 |
| REDUCE | 165 | 51 | -0.1% | 47% | 0.93 |
| SELL | 78 | 30 | -2.3% | 30% | 0.14 |

![Board strategy vs holding](board_equity.png)

## 2. Sell check, stock by stock

```
ALAB  REDUCE  (score 8/15, close 230.91 on 2026-11-11)
  RSI 42 | -52.2% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 296.41  (price is below, -22.1%)
    200-day SMA                256.86  (price is below, -10.1%)
    Chandelier stop            253.36  (price is below, -8.9%)
```

```
AMD  HOLD  (score 2/15, close 552.90 on 2026-11-11)
  RSI 54 | -14.9% from 52-week high
  Triggered:
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
  Levels to watch:
    50-day SMA                 550.43  (price is above, +0.4%)
    Chandelier stop            486.01  (price is above, +13.8%)
    200-day SMA                420.05  (price is above, +31.6%)
```

```
NVDA  REDUCE  (score 8/15, close 173.73 on 2026-11-11)
  RSI 29 | -27.4% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 217.10  (price is below, -20.0%)
    200-day SMA                204.19  (price is below, -14.9%)
    Chandelier stop            202.55  (price is below, -14.2%)
```

```
MRVL  EXIT  (score 9/15, close 168.80 on 2026-11-11)
  RSI 38 | -46.6% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 231.06  (price is below, -26.9%)
    Chandelier stop            216.33  (price is below, -22.0%)
    200-day SMA                186.15  (price is below, -9.3%)
```

```
GOOG  EXIT  (score 11/15, close 290.63 on 2026-11-11)
  RSI 37 | -27.1% from 52-week high
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
    200-day SMA                336.56  (price is below, -13.6%)
    50-day SMA                 326.80  (price is below, -11.1%)
    Chandelier stop            324.83  (price is below, -10.5%)
```

```
FSLR  EXIT  (score 9/15, close 178.11 on 2026-11-11)
  RSI 45 | -44.0% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    200-day SMA                213.81  (price is below, -16.7%)
    50-day SMA                 185.89  (price is below, -4.2%)
    Chandelier stop            183.10  (price is below, -2.7%)
```

```
SKHY  REDUCE  (score 4/10, close 142.25 on 2026-11-11)
  RSI 46 | -28.4% from high since listing
  Only 88 trading days of history; not scored yet: below_sma200, death_cross, volatility_spike
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the high since listing (+1)
  Levels to watch:
    50-day SMA                 165.19  (price is below, -13.9%)
    Chandelier stop            134.94  (price is above, +5.4%)
```

```
ETN  EXIT  (score 9/15, close 360.62 on 2026-11-11)
  RSI 44 | -21.4% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 401.66  (price is below, -10.2%)
    200-day SMA                395.38  (price is below, -8.8%)
    Chandelier stop            372.41  (price is below, -3.2%)
```

```
TSLA  WATCH  (score 5/15, close 390.84 on 2026-11-11)
  RSI 54 | -20.2% from 52-week high
  Triggered:
    - [trend] 50-day average below the 200-day average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
  Levels to watch:
    200-day SMA                383.03  (price is above, +2.0%)
    50-day SMA                 373.65  (price is above, +4.6%)
    Chandelier stop            364.41  (price is above, +7.3%)
```

```
SPCX  EXIT  (score 6/10, close 139.75 on 2026-11-11)
  RSI 47 | -33.9% from high since listing
  Only 106 trading days of history; not scored yet: below_sma200, death_cross, volatility_spike
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the high since listing (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 149.13  (price is below, -6.3%)
    Chandelier stop            141.73  (price is below, -1.4%)
```

```
AMZN  HOLD  (score 1/15, close 266.17 on 2026-11-11)
  RSI 57 | -6.3% from 52-week high
  Triggered:
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
  Levels to watch:
    50-day SMA                 254.41  (price is above, +4.6%)
    Chandelier stop            246.98  (price is above, +7.8%)
    200-day SMA                244.35  (price is above, +8.9%)
```

```
IBM  WATCH  (score 4/15, close 248.22 on 2026-11-11)
  RSI 57 | -23.5% from 52-week high
  Triggered:
    - [trend] 50-day average below the 200-day average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [risk] 20%+ below the 52-week high (+1)
  Levels to watch:
    200-day SMA                243.67  (price is above, +1.9%)
    Chandelier stop            237.50  (price is above, +4.5%)
    50-day SMA                 235.95  (price is above, +5.2%)
```

```
GEV  EXIT  (score 11/15, close 808.24 on 2026-11-11)
  RSI 42 | -31.2% from 52-week high
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
    200-day SMA                949.99  (price is below, -14.9%)
    50-day SMA                 917.61  (price is below, -11.9%)
    Chandelier stop            832.46  (price is below, -2.9%)
```

```
CEG  REDUCE  (score 6/15, close 274.73 on 2026-11-11)
  RSI 55 | -27.1% from 52-week high
  Triggered:
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
  Levels to watch:
    200-day SMA                277.94  (price is below, -1.2%)
    50-day SMA                 269.76  (price is above, +1.8%)
    Chandelier stop            257.42  (price is above, +6.7%)
```

```
VST  EXIT  (score 11/15, close 133.45 on 2026-11-11)
  RSI 46 | -25.6% from 52-week high
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
    200-day SMA                151.87  (price is below, -12.1%)
    50-day SMA                 143.57  (price is below, -7.0%)
    Chandelier stop            139.06  (price is below, -4.0%)
```

```
DELL  REDUCE  (score 7/15, close 373.68 on 2026-11-11)
  RSI 40 | -36.4% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 498.86  (price is below, -25.1%)
    Chandelier stop            476.31  (price is below, -21.5%)
    200-day SMA                340.20  (price is above, +9.8%)
```

```
TSM  WATCH  (score 4/15, close 413.35 on 2026-11-11)
  RSI 50 | -14.9% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 21-day volatility 1.5x+ its 1-year median (+1)
  Levels to watch:
    50-day SMA                 430.47  (price is below, -4.0%)
    200-day SMA                401.03  (price is above, +3.1%)
    Chandelier stop            394.59  (price is above, +4.8%)
```

```
BE  REDUCE  (score 6/15, close 209.47 on 2026-11-11)
  RSI 48 | -39.4% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
  Levels to watch:
    50-day SMA                 245.23  (price is below, -14.6%)
    200-day SMA                223.17  (price is below, -6.1%)
    Chandelier stop            197.84  (price is above, +5.9%)
```

## 3. Which sell signals actually work? (event study)

Panel: 46 stocks, 5 years. Null hypothesis: returns after a signal look like returns on random days from the same stocks.

| rule | horizon | events | mean_after_signal | mean_random_days | difference | p_value | q_value | drop10_after_signal | drop10_base_rate | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| below_sma50 | 5d | 1071 | +0.26% | +0.68% | -0.42% | 0.013 | 0.153 | 40% | 36% | weak (not significant) |
| below_sma50 | 21d | 1048 | +2.24% | +3.08% | -0.84% | 0.018 | 0.153 | 40% | 36% | weak (not significant) |
| below_sma50 | 63d | 995 | +8.62% | +10.21% | -1.60% | 0.018 | 0.153 | 40% | 36% | weak (not significant) |
| below_sma200 | 5d | 514 | +0.25% | +0.62% | -0.37% | 0.084 | 0.317 | 39% | 36% | weak (not significant) |
| below_sma200 | 21d | 496 | +1.35% | +2.73% | -1.38% | 0.004 | 0.148 | 39% | 36% | weak (not significant) |
| below_sma200 | 63d | 472 | +9.12% | +9.17% | -0.05% | 0.489 | 0.798 | 39% | 36% | weak (not significant) |
| death_cross | 5d | 155 | +0.24% | +0.65% | -0.40% | 0.199 | 0.506 | 44% | 36% | weak (not significant) |
| death_cross | 21d | 148 | +0.84% | +2.87% | -2.02% | 0.024 | 0.162 | 44% | 36% | weak (not significant) |
| death_cross | 63d | 142 | +13.62% | +9.76% | +3.85% | 0.955 | 1.000 | 44% | 36% | no edge |
| rsi_divergence | 5d | 502 | +0.43% | +0.79% | -0.36% | 0.086 | 0.317 | 37% | 36% | weak (not significant) |
| rsi_divergence | 21d | 495 | +3.26% | +3.50% | -0.24% | 0.330 | 0.681 | 37% | 36% | weak (not significant) |
| rsi_divergence | 63d | 486 | +10.97% | +11.77% | -0.81% | 0.242 | 0.571 | 37% | 36% | weak (not significant) |
| rsi_rollover | 5d | 644 | +1.84% | +0.74% | +1.10% | 1.000 | 1.000 | 33% | 36% | no edge |
| rsi_rollover | 21d | 633 | +3.71% | +3.44% | +0.27% | 0.698 | 0.924 | 33% | 36% | no edge |
| rsi_rollover | 63d | 620 | +10.41% | +11.67% | -1.25% | 0.113 | 0.373 | 33% | 36% | weak (not significant) |
| macd_bearish | 5d | 1621 | +0.80% | +0.72% | +0.08% | 0.700 | 0.924 | 36% | 36% | no edge |
| macd_bearish | 21d | 1600 | +3.23% | +3.22% | +0.00% | 0.508 | 0.798 | 36% | 36% | no edge |
| macd_bearish | 63d | 1519 | +11.45% | +10.81% | +0.64% | 0.845 | 1.000 | 36% | 36% | no edge |
| distribution_cluster | 5d | 1078 | +0.54% | +0.72% | -0.18% | 0.171 | 0.470 | 36% | 36% | weak (not significant) |
| distribution_cluster | 21d | 1057 | +2.65% | +3.25% | -0.60% | 0.083 | 0.317 | 36% | 36% | weak (not significant) |
| distribution_cluster | 63d | 1020 | +10.01% | +10.93% | -0.92% | 0.134 | 0.402 | 36% | 36% | weak (not significant) |
| high_volume_breakdown | 5d | 763 | +0.78% | +0.68% | +0.11% | 0.678 | 0.924 | 35% | 36% | no edge |
| high_volume_breakdown | 21d | 726 | +3.82% | +3.03% | +0.78% | 0.937 | 1.000 | 35% | 36% | no edge |
| high_volume_breakdown | 63d | 704 | +12.66% | +10.19% | +2.47% | 0.993 | 1.000 | 35% | 36% | no edge |
| drawdown_20 | 5d | 406 | +1.41% | +0.82% | +0.59% | 0.952 | 1.000 | 51% | 36% | no edge |
| drawdown_20 | 21d | 395 | +2.49% | +3.77% | -1.28% | 0.049 | 0.269 | 51% | 36% | weak (not significant) |
| drawdown_20 | 63d | 373 | +13.81% | +12.78% | +1.03% | 0.743 | 0.943 | 51% | 36% | no edge |
| volatility_spike | 5d | 336 | +0.56% | +0.74% | -0.18% | 0.305 | 0.672 | 47% | 36% | weak (not significant) |
| volatility_spike | 21d | 330 | +3.17% | +3.35% | -0.17% | 0.409 | 0.750 | 47% | 36% | weak (not significant) |
| volatility_spike | 63d | 327 | +11.04% | +11.45% | -0.41% | 0.407 | 0.750 | 47% | 36% | weak (not significant) |
| chandelier_stop | 5d | 1360 | +0.70% | +0.71% | -0.02% | 0.457 | 0.793 | 37% | 36% | weak (not significant) |
| chandelier_stop | 21d | 1337 | +3.39% | +3.23% | +0.16% | 0.665 | 0.924 | 37% | 36% | no edge |
| chandelier_stop | 63d | 1275 | +12.02% | +10.84% | +1.17% | 0.940 | 1.000 | 37% | 36% | no edge |

**0 of 33 rule-by-horizon tests** show significantly weaker returns after the signal (q < 0.10).

![Sell signal event study](sell_event_study.png)

## 4. Strategy backtests

Not included: SKHY (only 88 trading days of history, needs 452); SPCX (only 106 trading days of history, needs 452).

### ALAB (2025-01-03 to 2026-11-11)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +60.7% | +29.2% | -63.2% | +97.2% | 0.75 | 0 | 100% |  |  |  |
| 50/200 SMA cross | -64.7% | -43.1% | -74.0% | +87.8% | -0.20 | 2 | 76% | -0.95 | [-1.88, -0.25] | 0.02 |
| Close > 50-day SMA | +7.6% | +4.0% | -66.4% | +70.0% | 0.41 | 10 | 52% | -0.34 | [-1.40, +0.67] | 0.51 |
| MACD > signal | +14.8% | +7.8% | -70.4% | +65.2% | 0.44 | 21 | 50% | -0.31 | [-1.52, +0.83] | 0.59 |
| RSI 30/70 | +18.4% | +9.6% | -50.3% | +37.4% | 0.43 | 1 | 16% | -0.32 | [-2.14, +1.67] | 0.73 |
| Trailing stop 20% | -11.8% | -6.6% | -69.1% | +71.9% | 0.27 | 10 | 56% | -0.48 | [-1.50, +0.52] | 0.35 |
| Volume breakout | +91.8% | +42.2% | -55.7% | +63.2% | 0.87 | 4 | 41% | +0.12 | [-1.08, +1.17] | 0.83 |

### AMD (2022-08-30 to 2026-11-11)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +551.1% | +56.4% | -63.0% | +58.3% | 1.06 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +418.3% | +48.1% | -39.1% | +48.7% | 1.05 | 1 | 65% | -0.01 | [-0.60, +0.52] | 0.98 |
| Close > 50-day SMA | +187.5% | +28.7% | -41.8% | +43.7% | 0.79 | 36 | 53% | -0.26 | [-0.83, +0.28] | 0.38 |
| MACD > signal | +343.0% | +42.7% | -42.4% | +41.4% | 1.06 | 39 | 50% | +0.01 | [-0.56, +0.53] | 0.98 |
| RSI 30/70 | +60.3% | +11.9% | -54.7% | +32.1% | 0.51 | 3 | 33% | -0.55 | [-1.60, +0.40] | 0.28 |
| Trailing stop 20% | +179.1% | +27.8% | -58.9% | +49.6% | 0.74 | 11 | 71% | -0.32 | [-0.82, +0.19] | 0.23 |
| Volume breakout | +177.7% | +27.6% | -36.9% | +37.1% | 0.84 | 10 | 38% | -0.22 | [-0.95, +0.45] | 0.52 |

### NVDA (2022-08-30 to 2026-11-11)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +1054.8% | +79.4% | -36.9% | +49.1% | 1.43 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +571.0% | +57.6% | -29.4% | +43.1% | 1.27 | 1 | 84% | -0.17 | [-0.68, +0.27] | 0.46 |
| Close > 50-day SMA | +346.8% | +43.0% | -39.1% | +39.0% | 1.11 | 38 | 69% | -0.33 | [-0.90, +0.23] | 0.27 |
| MACD > signal | +152.9% | +24.8% | -46.7% | +34.4% | 0.81 | 40 | 51% | -0.62 | [-1.33, +0.11] | 0.10 |
| RSI 30/70 | +53.1% | +10.7% | -22.6% | +18.6% | 0.64 | 2 | 8% | -0.80 | [-1.88, +0.05] | 0.10 |
| Trailing stop 20% | +613.4% | +59.9% | -36.6% | +44.8% | 1.27 | 8 | 89% | -0.16 | [-0.51, +0.17] | 0.31 |
| Volume breakout | +211.5% | +31.2% | -19.8% | +26.3% | 1.16 | 7 | 31% | -0.27 | [-1.14, +0.47] | 0.54 |

### MRVL (2022-08-30 to 2026-11-11)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +265.7% | +36.3% | -60.8% | +67.2% | 0.79 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +64.3% | +12.6% | -65.2% | +57.5% | 0.49 | 2 | 68% | -0.30 | [-0.77, +0.15] | 0.19 |
| Close > 50-day SMA | +65.8% | +12.8% | -51.5% | +52.7% | 0.49 | 36 | 58% | -0.31 | [-0.88, +0.21] | 0.31 |
| MACD > signal | +101.6% | +18.2% | -62.5% | +50.2% | 0.58 | 44 | 51% | -0.22 | [-0.93, +0.47] | 0.54 |
| RSI 30/70 | +75.7% | +14.4% | -32.1% | +29.0% | 0.61 | 2 | 19% | -0.18 | [-1.07, +0.89] | 0.71 |
| Trailing stop 20% | +72.4% | +13.9% | -53.3% | +57.0% | 0.51 | 15 | 77% | -0.28 | [-0.79, +0.21] | 0.26 |
| Volume breakout | +76.0% | +14.5% | -46.2% | +42.0% | 0.53 | 11 | 36% | -0.27 | [-1.13, +0.47] | 0.52 |

### GOOG (2022-08-30 to 2026-11-11)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +168.7% | +26.6% | -30.2% | +31.7% | 0.90 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +151.5% | +24.6% | -29.4% | +25.9% | 0.98 | 2 | 76% | +0.08 | [-0.42, +0.55] | 0.77 |
| Close > 50-day SMA | +85.6% | +15.9% | -22.2% | +23.6% | 0.74 | 34 | 63% | -0.16 | [-0.84, +0.48] | 0.61 |
| MACD > signal | +36.1% | +7.6% | -18.1% | +21.5% | 0.45 | 42 | 50% | -0.45 | [-1.14, +0.19] | 0.20 |
| RSI 30/70 | +32.5% | +7.0% | -20.4% | +18.2% | 0.46 | 4 | 25% | -0.44 | [-1.30, +0.42] | 0.32 |
| Trailing stop 20% | +44.8% | +9.2% | -40.4% | +29.7% | 0.45 | 6 | 92% | -0.46 | [-0.88, -0.08] | 0.03 |
| Volume breakout | +105.6% | +18.8% | -17.4% | +19.4% | 0.98 | 8 | 46% | +0.08 | [-0.78, +0.80] | 0.84 |

### FSLR (2022-08-30 to 2026-11-11)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +39.6% | +8.3% | -60.0% | +55.1% | 0.42 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +10.3% | +2.4% | -51.1% | +41.7% | 0.26 | 4 | 59% | -0.16 | [-0.74, +0.40] | 0.59 |
| Close > 50-day SMA | +30.3% | +6.5% | -46.8% | +40.4% | 0.35 | 28 | 50% | -0.06 | [-0.65, +0.48] | 0.82 |
| MACD > signal | -57.9% | -18.7% | -74.1% | +40.7% | -0.31 | 48 | 49% | -0.72 | [-1.38, -0.07] | 0.03 |
| RSI 30/70 | +30.1% | +6.5% | -42.8% | +30.4% | 0.35 | 2 | 27% | -0.06 | [-1.01, +0.76] | 0.89 |
| Trailing stop 20% | +16.6% | +3.7% | -52.3% | +45.2% | 0.30 | 11 | 69% | -0.11 | [-0.62, +0.36] | 0.65 |
| Volume breakout | -24.0% | -6.4% | -53.8% | +32.3% | -0.04 | 13 | 38% | -0.46 | [-1.31, +0.39] | 0.29 |

### ETN (2022-08-30 to 2026-11-11)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +180.0% | +27.9% | -34.5% | +33.9% | 0.90 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +71.0% | +13.7% | -35.7% | +30.4% | 0.58 | 2 | 83% | -0.32 | [-0.74, +0.04] | 0.11 |
| Close > 50-day SMA | +36.2% | +7.7% | -37.5% | +24.5% | 0.43 | 46 | 65% | -0.47 | [-1.07, +0.20] | 0.14 |
| MACD > signal | +37.3% | +7.9% | -25.8% | +22.4% | 0.45 | 48 | 50% | -0.44 | [-1.14, +0.18] | 0.18 |
| RSI 30/70 | +15.7% | +3.6% | -18.6% | +11.5% | 0.36 | 1 | 5% | -0.54 | [-1.50, +0.57] | 0.30 |
| Trailing stop 20% | +187.4% | +28.7% | -23.6% | +30.9% | 0.97 | 2 | 95% | +0.08 | [-0.13, +0.31] | 0.47 |
| Volume breakout | +21.6% | +4.8% | -29.3% | +18.1% | 0.35 | 10 | 38% | -0.55 | [-1.33, +0.27] | 0.19 |

### TSLA (2022-08-30 to 2026-11-11)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +41.7% | +8.7% | -65.0% | +58.3% | 0.43 | 0 | 100% |  |  |  |
| 50/200 SMA cross | -26.4% | -7.1% | -56.8% | +40.1% | 0.01 | 4 | 47% | -0.42 | [-1.27, +0.33] | 0.32 |
| Close > 50-day SMA | +60.5% | +12.0% | -41.1% | +38.5% | 0.49 | 43 | 52% | +0.05 | [-0.66, +0.79] | 0.88 |
| MACD > signal | +396.5% | +46.6% | -39.8% | +40.8% | 1.14 | 42 | 51% | +0.71 | [+0.09, +1.41] | 0.04 |
| RSI 30/70 | +51.8% | +10.5% | -52.7% | +40.2% | 0.45 | 4 | 42% | +0.01 | [-0.72, +0.75] | 0.98 |
| Trailing stop 20% | +44.5% | +9.2% | -47.9% | +45.0% | 0.42 | 11 | 71% | -0.01 | [-0.65, +0.57] | 0.97 |
| Volume breakout | +40.5% | +8.5% | -35.4% | +25.7% | 0.44 | 9 | 18% | +0.01 | [-0.89, +0.94] | 0.98 |

### AMZN (2022-08-30 to 2026-11-11)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +109.9% | +19.4% | -40.0% | +34.1% | 0.69 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +36.8% | +7.8% | -41.4% | +27.8% | 0.41 | 2 | 74% | -0.28 | [-0.93, +0.34] | 0.37 |
| Close > 50-day SMA | +34.7% | +7.4% | -41.0% | +23.3% | 0.42 | 35 | 63% | -0.27 | [-0.96, +0.49] | 0.49 |
| MACD > signal | -0.7% | -0.2% | -28.7% | +22.8% | 0.11 | 50 | 50% | -0.58 | [-1.34, +0.12] | 0.12 |
| RSI 30/70 | +94.0% | +17.1% | -22.0% | +21.6% | 0.84 | 4 | 33% | +0.15 | [-0.56, +0.86] | 0.70 |
| Trailing stop 20% | +115.4% | +20.1% | -24.2% | +29.8% | 0.76 | 3 | 87% | +0.07 | [-0.34, +0.54] | 0.75 |
| Volume breakout | +6.5% | +1.5% | -35.7% | +18.8% | 0.17 | 11 | 45% | -0.52 | [-1.43, +0.44] | 0.29 |

### IBM (2022-08-30 to 2026-11-11)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +124.0% | +21.3% | -37.5% | +31.5% | 0.77 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +63.8% | +12.5% | -28.7% | +22.8% | 0.63 | 3 | 73% | -0.14 | [-0.79, +0.52] | 0.68 |
| Close > 50-day SMA | +56.1% | +11.2% | -42.6% | +25.1% | 0.55 | 27 | 60% | -0.22 | [-0.69, +0.34] | 0.42 |
| MACD > signal | +112.3% | +19.7% | -43.1% | +23.9% | 0.88 | 30 | 50% | +0.10 | [-0.47, +0.84] | 0.76 |
| RSI 30/70 | +175.4% | +27.4% | -16.5% | +17.4% | 1.48 | 8 | 35% | +0.70 | [-0.31, +1.62] | 0.15 |
| Trailing stop 20% | +70.1% | +13.5% | -45.9% | +30.3% | 0.58 | 3 | 92% | -0.20 | [-0.44, +0.02] | 0.08 |
| Volume breakout | +68.1% | +13.2% | -25.6% | +17.0% | 0.81 | 10 | 40% | +0.04 | [-0.82, +1.00] | 0.94 |

### GEV (2025-01-13 to 2026-11-11)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +112.2% | +50.9% | -38.3% | +56.1% | 1.02 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +133.0% | +58.8% | -38.3% | +54.8% | 1.12 | 1 | 98% | +0.10 | [-0.04, +0.34] | 0.22 |
| Close > 50-day SMA | +79.1% | +37.5% | -32.7% | +43.8% | 0.95 | 15 | 63% | -0.07 | [-0.69, +0.50] | 0.83 |
| MACD > signal | +60.6% | +29.6% | -31.0% | +42.0% | 0.83 | 17 | 48% | -0.19 | [-0.98, +0.68] | 0.63 |
| RSI 30/70 | +25.8% | +13.4% | -34.4% | +34.9% | 0.54 | 1 | 31% | -0.48 | [-1.67, +0.63] | 0.42 |
| Trailing stop 20% | +44.2% | +22.1% | -45.9% | +50.1% | 0.65 | 5 | 87% | -0.36 | [-0.91, +0.09] | 0.17 |
| Volume breakout | +24.5% | +12.7% | -24.6% | +33.5% | 0.53 | 3 | 36% | -0.49 | [-1.71, +0.65] | 0.41 |

### CEG (2022-11-02 to 2026-11-11)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +199.9% | +31.5% | -50.7% | +49.3% | 0.80 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +96.8% | +18.4% | -50.7% | +43.5% | 0.60 | 3 | 72% | -0.20 | [-0.67, +0.20] | 0.35 |
| Close > 50-day SMA | +145.2% | +25.1% | -40.9% | +37.3% | 0.78 | 47 | 57% | -0.02 | [-0.60, +0.52] | 0.95 |
| MACD > signal | +28.8% | +6.5% | -41.5% | +36.9% | 0.35 | 41 | 49% | -0.45 | [-1.11, +0.15] | 0.16 |
| RSI 30/70 | +103.2% | +19.4% | -28.6% | +32.3% | 0.71 | 3 | 37% | -0.09 | [-0.91, +0.68] | 0.82 |
| Trailing stop 20% | +94.9% | +18.1% | -52.8% | +43.8% | 0.60 | 9 | 84% | -0.20 | [-0.63, +0.22] | 0.35 |
| Volume breakout | +86.0% | +16.7% | -30.0% | +30.6% | 0.66 | 9 | 39% | -0.14 | [-0.86, +0.62] | 0.70 |

### VST (2022-08-30 to 2026-11-11)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +474.0% | +51.8% | -48.8% | +52.1% | 1.07 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +424.9% | +48.6% | -48.8% | +44.0% | 1.12 | 3 | 68% | +0.06 | [-0.28, +0.45] | 0.73 |
| Close > 50-day SMA | +50.7% | +10.3% | -67.2% | +38.0% | 0.45 | 45 | 64% | -0.61 | [-1.24, -0.01] | 0.05 |
| MACD > signal | +66.6% | +13.0% | -49.0% | +37.2% | 0.52 | 47 | 51% | -0.55 | [-1.14, +0.12] | 0.09 |
| RSI 30/70 | +200.5% | +30.1% | -27.3% | +26.8% | 1.11 | 3 | 20% | +0.05 | [-0.86, +0.85] | 0.92 |
| Trailing stop 20% | +216.8% | +31.7% | -56.3% | +44.6% | 0.84 | 9 | 88% | -0.22 | [-0.65, +0.19] | 0.32 |
| Volume breakout | +278.5% | +37.4% | -31.2% | +31.4% | 1.18 | 9 | 43% | +0.11 | [-0.68, +0.95] | 0.76 |

### DELL (2022-08-30 to 2026-11-11)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +959.6% | +75.7% | -59.6% | +58.0% | 1.25 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +466.3% | +51.3% | -50.8% | +50.7% | 1.06 | 3 | 68% | -0.19 | [-0.66, +0.24] | 0.42 |
| Close > 50-day SMA | +1326.9% | +88.7% | -27.5% | +49.3% | 1.52 | 21 | 67% | +0.27 | [-0.18, +0.75] | 0.24 |
| MACD > signal | +141.4% | +23.4% | -57.7% | +43.1% | 0.69 | 45 | 52% | -0.56 | [-1.21, +0.07] | 0.08 |
| RSI 30/70 | +179.1% | +27.8% | -23.7% | +26.6% | 1.05 | 4 | 28% | -0.20 | [-1.22, +0.69] | 0.68 |
| Trailing stop 20% | +960.9% | +75.8% | -55.9% | +51.5% | 1.34 | 7 | 82% | +0.09 | [-0.28, +0.45] | 0.65 |
| Volume breakout | +378.1% | +45.3% | -37.8% | +43.2% | 1.07 | 11 | 45% | -0.18 | [-0.88, +0.44] | 0.57 |

### TSM (2022-08-30 to 2026-11-11)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +429.4% | +48.9% | -36.8% | +39.3% | 1.21 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +183.8% | +28.3% | -36.8% | +35.9% | 0.87 | 2 | 81% | -0.34 | [-0.86, +0.16] | 0.19 |
| Close > 50-day SMA | +190.3% | +29.0% | -28.8% | +31.6% | 0.96 | 37 | 68% | -0.24 | [-0.80, +0.32] | 0.40 |
| MACD > signal | +142.0% | +23.5% | -32.1% | +28.4% | 0.89 | 44 | 49% | -0.32 | [-0.92, +0.28] | 0.30 |
| RSI 30/70 | +51.4% | +10.4% | -23.0% | +16.8% | 0.67 | 3 | 12% | -0.54 | [-1.59, +0.48] | 0.32 |
| Trailing stop 20% | +213.1% | +31.3% | -30.6% | +36.7% | 0.93 | 6 | 91% | -0.28 | [-0.66, +0.09] | 0.13 |
| Volume breakout | +77.0% | +14.6% | -26.8% | +26.4% | 0.65 | 11 | 46% | -0.56 | [-1.34, +0.17] | 0.14 |

### BE (2022-08-30 to 2026-11-11)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +723.9% | +65.5% | -67.8% | +90.0% | 0.99 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +281.8% | +37.7% | -71.9% | +74.9% | 0.80 | 4 | 63% | -0.20 | [-0.77, +0.32] | 0.51 |
| Close > 50-day SMA | +359.7% | +44.0% | -53.1% | +69.7% | 0.85 | 31 | 52% | -0.14 | [-0.69, +0.35] | 0.61 |
| MACD > signal | +217.3% | +31.8% | -60.0% | +65.8% | 0.73 | 41 | 50% | -0.26 | [-1.03, +0.39] | 0.41 |
| RSI 30/70 | +147.7% | +24.2% | -61.8% | +47.0% | 0.69 | 4 | 47% | -0.30 | [-1.13, +0.58] | 0.53 |
| Trailing stop 20% | +153.4% | +24.9% | -66.7% | +73.9% | 0.65 | 19 | 61% | -0.34 | [-0.89, +0.11] | 0.17 |
| Volume breakout | +275.5% | +37.2% | -58.1% | +61.0% | 0.80 | 11 | 30% | -0.19 | [-0.97, +0.53] | 0.62 |

![Strategy equity curves](backtest_equity.png)

## 5. Next-day forecasts

Not included: SKHY (only 88 trading days of history, needs 452); SPCX (only 106 trading days of history, needs 452).

### ALAB

Walk-forward test on 213 unseen days (2026-01-07 to 2026-11-10).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.526 | 0.526 | 0.528 | 0.454 | 0.25 | 0.895 | 0.895 |
| Logistic regression | 0.498 | 0.526 | 0.814 | 0.497 | 0.257 | 0.353 | 0.895 |
| Gradient boosting | 0.474 | 0.526 | 0.943 | 0.453 | 0.283 | 0.425 | 0.895 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 652.0 | 0.0 |  |  |
| Ridge regression | 668.6 | -0.0517 | 0.474 | 0.945 |
| Gradient boosting | 686.0 | -0.107 | 0.451 | 0.993 |

Forecast for the next session:

```
  P(up) | Logistic regression      54.9%
  P(up) | Gradient boosting        43.4%
  P(up) | historical base rate     52.0%
  expected return (ridge)          +0.32%
  80% range low                    -9.60%
  80% range high                   +11.34%
  daily volatility                 +8.13%
```

Best out-of-sample AUC **0.497**; smallest p-value against a naive baseline 0.814, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![ALAB feature effects](forecast_ALAB.png)

### AMD

Walk-forward test on 550 unseen days (2024-09-03 to 2026-11-10).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.507 | 0.533 | 0.892 | 0.497 | 0.25 | 1.268 | 1.306 |
| Logistic regression | 0.487 | 0.533 | 0.985 | 0.493 | 0.255 | 0.565 | 1.306 |
| Gradient boosting | 0.484 | 0.533 | 0.991 | 0.485 | 0.269 | 0.415 | 1.306 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 403.9 | 0.0 |  |  |
| Ridge regression | 405.2 | -0.0068 | 0.491 | 0.656 |
| Gradient boosting | 413.3 | -0.0472 | 0.504 | 0.994 |

Forecast for the next session:

```
  P(up) | Logistic regression      61.6%
  P(up) | Gradient boosting        80.6%
  P(up) | historical base rate     51.5%
  expected return (ridge)          -0.08%
  80% range low                    -9.12%
  80% range high                   +9.85%
  daily volatility                 +7.39%
```

Best out-of-sample AUC **0.493**; smallest p-value against a naive baseline 0.656, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![AMD feature effects](forecast_AMD.png)

### NVDA

Walk-forward test on 550 unseen days (2024-09-03 to 2026-11-10).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.524 | 0.524 | 0.517 | 0.504 | 0.25 | 0.716 | 0.716 |
| Logistic regression | 0.507 | 0.524 | 0.791 | 0.524 | 0.252 | 0.563 | 0.716 |
| Gradient boosting | 0.5 | 0.524 | 0.875 | 0.482 | 0.268 | 0.53 | 0.716 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 279.4 | 0.0 |  |  |
| Ridge regression | 280.0 | -0.0039 | 0.507 | 0.56 |
| Gradient boosting | 288.4 | -0.0652 | 0.535 | 0.968 |

Forecast for the next session:

```
  P(up) | Logistic regression      54.8%
  P(up) | Gradient boosting        31.3%
  P(up) | historical base rate     53.7%
  expected return (ridge)          -0.68%
  80% range low                    -4.75%
  80% range high                   +3.57%
  daily volatility                 +3.27%
```

Best out-of-sample AUC **0.524**; smallest p-value against a naive baseline 0.560, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![NVDA feature effects](forecast_NVDA.png)

### MRVL

Walk-forward test on 550 unseen days (2024-09-03 to 2026-11-10).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.536 | 0.536 | 0.517 | 0.46 | 0.249 | 0.911 | 0.911 |
| Logistic regression | 0.533 | 0.536 | 0.585 | 0.545 | 0.253 | 0.691 | 0.911 |
| Gradient boosting | 0.531 | 0.536 | 0.618 | 0.547 | 0.26 | 0.686 | 0.911 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 480.5 | 0.0 |  |  |
| Ridge regression | 485.1 | -0.0191 | 0.529 | 0.855 |
| Gradient boosting | 489.5 | -0.0376 | 0.516 | 0.959 |

Forecast for the next session:

```
  P(up) | Logistic regression      42.8%
  P(up) | Gradient boosting        30.9%
  P(up) | historical base rate     52.6%
  expected return (ridge)          -1.86%
  80% range low                    -11.23%
  80% range high                   +8.49%
  daily volatility                 +7.83%
```

Best out-of-sample AUC **0.547**; smallest p-value against a naive baseline 0.585, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![MRVL feature effects](forecast_MRVL.png)

### GOOG

Walk-forward test on 550 unseen days (2024-09-03 to 2026-11-10).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.524 | 0.524 | 0.517 | 0.482 | 0.25 | 1.041 | 1.042 |
| Logistic regression | 0.551 | 0.524 | 0.108 | 0.535 | 0.253 | 0.492 | 1.042 |
| Gradient boosting | 0.515 | 0.524 | 0.681 | 0.53 | 0.262 | 0.463 | 1.042 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 201.0 | 0.0 |  |  |
| Ridge regression | 203.2 | -0.022 | 0.531 | 0.95 |
| Gradient boosting | 207.6 | -0.0666 | 0.525 | 0.996 |

Forecast for the next session:

```
  P(up) | Logistic regression      49.0%
  P(up) | Gradient boosting        53.2%
  P(up) | historical base rate     53.0%
  expected return (ridge)          +0.08%
  80% range low                    -3.95%
  80% range high                   +4.28%
  daily volatility                 +3.21%
```

Best out-of-sample AUC **0.535**; smallest p-value against a naive baseline 0.108, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![GOOG feature effects](forecast_GOOG.png)

### FSLR

Walk-forward test on 550 unseen days (2024-09-03 to 2026-11-10).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.515 | 0.515 | 0.517 | 0.463 | 0.25 |  | 0.147 |
| Logistic regression | 0.513 | 0.515 | 0.551 | 0.529 | 0.251 | 0.056 | 0.147 |
| Gradient boosting | 0.509 | 0.515 | 0.618 | 0.53 | 0.261 | -0.122 | 0.147 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 363.6 | 0.0 |  |  |
| Ridge regression | 364.3 | -0.004 | 0.513 | 0.628 |
| Gradient boosting | 373.2 | -0.0538 | 0.509 | 0.995 |

Forecast for the next session:

```
  P(up) | Logistic regression      50.6%
  P(up) | Gradient boosting        56.6%
  P(up) | historical base rate     49.1%
  expected return (ridge)          -0.80%
  80% range low                    -4.47%
  80% range high                   +3.00%
  daily volatility                 +2.94%
```

Best out-of-sample AUC **0.530**; smallest p-value against a naive baseline 0.551, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![FSLR feature effects](forecast_FSLR.png)

### ETN

Walk-forward test on 550 unseen days (2024-09-03 to 2026-11-10).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.525 | 0.525 | 0.517 | 0.471 | 0.25 | 0.485 | 0.486 |
| Logistic regression | 0.513 | 0.525 | 0.739 | 0.513 | 0.255 | 0.593 | 0.486 |
| Gradient boosting | 0.529 | 0.525 | 0.449 | 0.533 | 0.258 | 0.294 | 0.486 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 246.9 | 0.0 |  |  |
| Ridge regression | 248.5 | -0.0132 | 0.538 | 0.778 |
| Gradient boosting | 253.6 | -0.0554 | 0.522 | 0.972 |

Forecast for the next session:

```
  P(up) | Logistic regression      49.4%
  P(up) | Gradient boosting        67.0%
  P(up) | historical base rate     54.1%
  expected return (ridge)          -0.02%
  80% range low                    -5.57%
  80% range high                   +5.85%
  daily volatility                 +4.45%
```

Best out-of-sample AUC **0.533**; smallest p-value against a naive baseline 0.449, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![ETN feature effects](forecast_ETN.png)

### TSLA

Walk-forward test on 550 unseen days (2024-09-03 to 2026-11-10).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.505 | 0.505 | 0.517 | 0.462 | 0.25 | 0.771 | 0.771 |
| Logistic regression | 0.518 | 0.505 | 0.29 | 0.513 | 0.253 | 0.729 | 0.771 |
| Gradient boosting | 0.536 | 0.505 | 0.08 | 0.535 | 0.261 | 1.015 | 0.771 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 370.3 | 0.0 |  |  |
| Ridge regression | 374.7 | -0.0239 | 0.495 | 0.947 |
| Gradient boosting | 378.0 | -0.0423 | 0.518 | 0.949 |

Forecast for the next session:

```
  P(up) | Logistic regression      43.5%
  P(up) | Gradient boosting        50.6%
  P(up) | historical base rate     50.9%
  expected return (ridge)          -0.30%
  80% range low                    -5.04%
  80% range high                   +4.68%
  daily volatility                 +3.80%
```

Best out-of-sample AUC **0.535**; smallest p-value against a naive baseline 0.080, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![TSLA feature effects](forecast_TSLA.png)

### AMZN

Walk-forward test on 550 unseen days (2024-09-03 to 2026-11-10).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.516 | 0.516 | 0.517 | 0.467 | 0.25 | 0.723 | 0.723 |
| Logistic regression | 0.547 | 0.516 | 0.079 | 0.56 | 0.249 | 1.019 | 0.723 |
| Gradient boosting | 0.54 | 0.516 | 0.143 | 0.528 | 0.262 | 0.708 | 0.723 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 212.2 | 0.0 |  |  |
| Ridge regression | 214.1 | -0.0181 | 0.544 | 0.876 |
| Gradient boosting | 221.7 | -0.0921 | 0.518 | 1.0 |

Forecast for the next session:

```
  P(up) | Logistic regression      35.7%
  P(up) | Gradient boosting        43.6%
  P(up) | historical base rate     51.3%
  expected return (ridge)          -0.52%
  80% range low                    -3.83%
  80% range high                   +2.90%
  daily volatility                 +2.64%
```

Best out-of-sample AUC **0.560**; smallest p-value against a naive baseline 0.079, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![AMZN feature effects](forecast_AMZN.png)

### IBM

Walk-forward test on 550 unseen days (2024-09-03 to 2026-11-10).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.549 | 0.549 | 0.518 | 0.462 | 0.248 | 0.518 | 0.519 |
| Logistic regression | 0.535 | 0.549 | 0.767 | 0.466 | 0.255 | 0.635 | 0.519 |
| Gradient boosting | 0.502 | 0.549 | 0.988 | 0.489 | 0.266 | 0.53 | 0.519 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 253.4 | 0.0 |  |  |
| Ridge regression | 256.0 | -0.0206 | 0.531 | 0.919 |
| Gradient boosting | 258.4 | -0.0396 | 0.527 | 0.987 |

Forecast for the next session:

```
  P(up) | Logistic regression      53.3%
  P(up) | Gradient boosting        61.7%
  P(up) | historical base rate     55.2%
  expected return (ridge)          -0.05%
  80% range low                    -2.19%
  80% range high                   +2.14%
  daily volatility                 +1.69%
```

Best out-of-sample AUC **0.489**; smallest p-value against a naive baseline 0.767, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![IBM feature effects](forecast_IBM.png)

### GEV

Walk-forward test on 208 unseen days (2026-01-14 to 2026-11-10).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.534 | 0.534 | 0.528 | 0.469 | 0.249 | 0.783 | 0.784 |
| Logistic regression | 0.505 | 0.534 | 0.817 | 0.502 | 0.257 | 0.494 | 0.784 |
| Gradient boosting | 0.543 | 0.534 | 0.418 | 0.534 | 0.267 | 1.221 | 0.784 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 338.2 | 0.0 |  |  |
| Ridge regression | 344.5 | -0.0373 | 0.553 | 0.8 |
| Gradient boosting | 349.7 | -0.0689 | 0.538 | 0.886 |

Forecast for the next session:

```
  P(up) | Logistic regression      64.3%
  P(up) | Gradient boosting        73.6%
  P(up) | historical base rate     54.3%
  expected return (ridge)          +0.40%
  80% range low                    -5.80%
  80% range high                   +7.00%
  daily volatility                 +4.97%
```

Best out-of-sample AUC **0.534**; smallest p-value against a naive baseline 0.418, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![GEV feature effects](forecast_GEV.png)

### CEG

Walk-forward test on 505 unseen days (2024-11-05 to 2026-11-10).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.505 | 0.505 | 0.518 | 0.488 | 0.251 | 0.432 | 0.433 |
| Logistic regression | 0.473 | 0.505 | 0.929 | 0.501 | 0.259 | 0.038 | 0.433 |
| Gradient boosting | 0.473 | 0.505 | 0.929 | 0.463 | 0.275 | -0.092 | 0.433 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 352.2 | 0.0 |  |  |
| Ridge regression | 359.9 | -0.0442 | 0.477 | 0.981 |
| Gradient boosting | 363.0 | -0.0623 | 0.509 | 0.989 |

Forecast for the next session:

```
  P(up) | Logistic regression      58.7%
  P(up) | Gradient boosting        35.0%
  P(up) | historical base rate     52.1%
  expected return (ridge)          +0.28%
  80% range low                    -4.67%
  80% range high                   +5.49%
  daily volatility                 +3.95%
```

Best out-of-sample AUC **0.501**; smallest p-value against a naive baseline 0.929, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![CEG feature effects](forecast_CEG.png)

### VST

Walk-forward test on 550 unseen days (2024-09-03 to 2026-11-10).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.518 | 0.518 | 0.517 | 0.473 | 0.25 | 0.747 | 0.747 |
| Logistic regression | 0.485 | 0.518 | 0.943 | 0.48 | 0.261 | 1.102 | 0.747 |
| Gradient boosting | 0.507 | 0.518 | 0.711 | 0.52 | 0.268 | 0.741 | 0.747 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 392.7 | 0.0 |  |  |
| Ridge regression | 396.2 | -0.018 | 0.491 | 0.806 |
| Gradient boosting | 400.2 | -0.0387 | 0.52 | 0.951 |

Forecast for the next session:

```
  P(up) | Logistic regression      47.2%
  P(up) | Gradient boosting        62.3%
  P(up) | historical base rate     52.8%
  expected return (ridge)          -1.46%
  80% range low                    -8.25%
  80% range high                   +5.83%
  daily volatility                 +5.57%
```

Best out-of-sample AUC **0.520**; smallest p-value against a naive baseline 0.711, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![VST feature effects](forecast_VST.png)

### DELL

Walk-forward test on 550 unseen days (2024-09-03 to 2026-11-10).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.522 | 0.522 | 0.517 | 0.479 | 0.25 | 1.19 | 1.19 |
| Logistic regression | 0.511 | 0.522 | 0.711 | 0.512 | 0.255 | 0.083 | 1.19 |
| Gradient boosting | 0.496 | 0.522 | 0.892 | 0.496 | 0.268 | 0.329 | 1.19 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 407.8 | 0.0 |  |  |
| Ridge regression | 413.0 | -0.0258 | 0.493 | 0.97 |
| Gradient boosting | 421.6 | -0.0691 | 0.487 | 0.998 |

Forecast for the next session:

```
  P(up) | Logistic regression      67.7%
  P(up) | Gradient boosting        54.2%
  P(up) | historical base rate     51.7%
  expected return (ridge)          +1.55%
  80% range low                    -7.28%
  80% range high                   +11.22%
  daily volatility                 +7.10%
```

Best out-of-sample AUC **0.512**; smallest p-value against a naive baseline 0.711, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![DELL feature effects](forecast_DELL.png)

### TSM

Walk-forward test on 550 unseen days (2024-09-03 to 2026-11-10).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.513 | 0.536 | 0.876 | 0.479 | 0.25 | 1.137 | 1.278 |
| Logistic regression | 0.54 | 0.536 | 0.449 | 0.534 | 0.249 | 1.241 | 1.278 |
| Gradient boosting | 0.504 | 0.536 | 0.943 | 0.509 | 0.261 | 1.053 | 1.278 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 264.0 | 0.0 |  |  |
| Ridge regression | 262.4 | 0.0119 | 0.533 | 0.243 |
| Gradient boosting | 269.5 | -0.0417 | 0.511 | 0.98 |

Forecast for the next session:

```
  P(up) | Logistic regression      42.6%
  P(up) | Gradient boosting        61.0%
  P(up) | historical base rate     51.7%
  expected return (ridge)          -0.80%
  80% range low                    -5.69%
  80% range high                   +4.35%
  daily volatility                 +3.95%
```

Best out-of-sample AUC **0.534**; smallest p-value against a naive baseline 0.243, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![TSM feature effects](forecast_TSM.png)

### BE

Walk-forward test on 550 unseen days (2024-09-03 to 2026-11-10).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.484 | 0.516 | 0.943 | 0.476 | 0.251 |  | 1.771 |
| Logistic regression | 0.48 | 0.516 | 0.96 | 0.464 | 0.266 | 0.904 | 1.771 |
| Gradient boosting | 0.484 | 0.516 | 0.943 | 0.481 | 0.27 | 0.672 | 1.771 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 654.1 | 0.0 |  |  |
| Ridge regression | 671.1 | -0.0526 | 0.471 | 0.996 |
| Gradient boosting | 666.7 | -0.0388 | 0.495 | 0.976 |

Forecast for the next session:

```
  P(up) | Logistic regression      58.3%
  P(up) | Gradient boosting        48.0%
  P(up) | historical base rate     49.7%
  expected return (ridge)          +0.40%
  80% range low                    -9.57%
  80% range high                   +11.47%
  daily volatility                 +8.16%
```

Best out-of-sample AUC **0.481**; smallest p-value against a naive baseline 0.943, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![BE feature effects](forecast_BE.png)

## 6. Stock screen and entry plans

| ticker | rank | score | passes_filters | close | momentum_12_1 | momentum_6m | volatility | off_52w_high | forward_pe | pullback_entry | breakout_trigger | stop | stop_% | shares | position_$ | max_loss_$ | filter_notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DELL | 1 | +1.10 | True | 373.68 | +304.9% | +53.7% | +86.3% | -36.4% | 12.3 | 339.47 | 502.96 | 271.05 | -20.2% | 14 | 4753.0 | 958.0 |  |
| AMD | 2 | +1.01 | True | 552.90 | +148.2% | +24.1% | +78.9% | -14.9% | 31.3 | 550.43 | 579.6 | 470.3 | -14.6% | 12 | 6605.0 | 962.0 |  |
| V | 3 | +0.58 | True | 425.55 | +19.2% | +33.3% | +21.4% | -2.3% | 24.8 | 412.87 | 436.63 | 394.87 | -4.4% | 24 | 9909.0 | 432.0 |  |
| LLY | 4 | +0.50 | True | 1437.29 | +21.4% | +41.9% | +31.5% | +0.0% | 28.4 | 1338.14 | 1440.16 | 1245.34 | -6.9% | 7 | 9367.0 | 650.0 |  |
| MSFT | 5 | +0.49 | True | 521.13 | +8.3% | +29.1% | +27.5% | -6.2% | 21.5 | 518.2 | 556.91 | 486.48 | -6.1% | 19 | 9846.0 | 603.0 |  |
| XOM | 6 | +0.47 | True | 166.71 | +51.5% | +11.5% | +26.4% | -11.0% | 13.4 | 162.24 | 187.62 | 153.31 | -5.5% | 61 | 9897.0 | 545.0 |  |
| KO | 7 | +0.46 | True | 97.57 | +31.2% | +23.1% | +17.3% | +0.0% | 27.6 | 94.22 | 97.77 | 90.66 | -3.8% | 106 | 9987.0 | 377.0 |  |
| AAPL | 8 | +0.41 | True | 355.63 | +27.0% | +19.1% | +22.3% | +0.0% | 33.7 | 344.87 | 356.34 | 327.55 | -5.0% | 28 | 9656.0 | 485.0 |  |
| JNJ | 9 | +0.39 | True | 280.41 | +34.9% | +23.0% | +25.0% | -0.6% | 24.1 | 268.53 | 282.67 | 254.66 | -5.2% | 37 | 9936.0 | 513.0 |  |
| TSM | 10 | +0.39 | True | 413.35 | +52.3% | +3.9% | +42.5% | -14.9% | 17.7 | 410.39 | 440.39 | 376.45 | -8.3% | 24 | 9849.0 | 814.0 |  |
| JPM | 11 | +0.28 | True | 343.39 | +6.6% | +15.5% | +20.3% | -5.5% | 13.4 | 340.22 | 352.81 | 325.14 | -4.4% | 29 | 9866.0 | 437.0 |  |
| PG | 12 | +0.16 | True | 167.67 | +7.5% | +19.5% | +20.6% | -0.6% | 22.7 | 162.01 | 169.0 | 155.45 | -4.0% | 61 | 9883.0 | 400.0 |  |
| UNH | 13 | +0.11 | True | 402.94 | +20.6% | +1.6% | +23.7% | -7.1% | 17.3 | 390.85 | 425.83 | 368.03 | -5.8% | 25 | 9771.0 | 571.0 |  |
| LIN | 14 | +0.02 | True | 526.55 | +18.6% | +3.3% | +15.5% | -3.4% | 26.9 | 510.98 | 527.6 | 492.44 | -3.6% | 19 | 9709.0 | 352.0 |  |
| AMT | 15 | -0.00 | True | 190.24 | +3.9% | +11.7% | +29.2% | -2.4% | 27.1 | 186.69 | 195.25 | 176.22 | -5.6% | 53 | 9894.0 | 555.0 |  |

## 7. Portfolio construction

Not included: SKHY (only 88 trading days of history, needs 252); SPCX (only 106 trading days of history, needs 252).

Assets: ALAB, AMD, NVDA, MRVL, GOOG, FSLR, ETN, TSLA, AMZN, IBM, GEV, CEG, VST, DELL, TSM, BE, JPM, XOM, UNH, COST, TLT, GLD. Covariance: Ledoit-Wolf shrinkage on the last 252 trading days.

Weights and share of risk (%):

| asset | weight: Equal weight | weight: Inverse volatility | weight: Risk parity | weight: Minimum variance | risk share: Equal weight | risk share: Inverse volatility | risk share: Risk parity | risk share: Minimum variance |
|---|---|---|---|---|---|---|---|---|
| ALAB | 4.5 | 1.8 | 1.2 | 0.0 | 12.4 | 6.6 | 4.6 | 0.0 |
| AMD | 4.5 | 2.5 | 1.4 | 0.0 | 9.5 | 7.3 | 4.6 | 0.0 |
| NVDA | 4.5 | 4.6 | 3.4 | 4.8 | 3.9 | 6.0 | 4.8 | 5.3 |
| MRVL | 4.5 | 2.1 | 1.3 | 0.0 | 10.3 | 6.7 | 4.6 | 0.0 |
| GOOG | 4.5 | 5.3 | 4.6 | 4.3 | 1.9 | 4.0 | 4.8 | 4.8 |
| FSLR | 4.5 | 3.4 | 2.8 | 0.4 | 4.0 | 4.7 | 4.7 | 0.5 |
| ETN | 4.5 | 4.1 | 2.5 | 1.7 | 5.4 | 7.2 | 4.7 | 1.9 |
| TSLA | 4.5 | 3.9 | 2.6 | 0.0 | 4.5 | 6.1 | 4.7 | 0.0 |
| AMZN | 4.5 | 5.1 | 4.1 | 4.0 | 2.1 | 4.3 | 4.7 | 4.4 |
| IBM | 4.5 | 3.7 | 5.4 | 2.3 | 0.9 | 1.5 | 4.8 | 2.6 |
| GEV | 4.5 | 3.2 | 2.3 | 0.8 | 6.1 | 6.4 | 4.7 | 0.9 |
| CEG | 4.5 | 3.6 | 2.7 | 1.2 | 4.6 | 5.5 | 4.7 | 1.4 |
| VST | 4.5 | 3.3 | 2.4 | 0.1 | 5.5 | 6.0 | 4.7 | 0.1 |
| DELL | 4.5 | 2.2 | 1.8 | 0.0 | 7.7 | 5.4 | 4.6 | 0.0 |
| TSM | 4.5 | 4.2 | 2.3 | 0.0 | 5.5 | 7.6 | 4.7 | 0.0 |
| BE | 4.5 | 1.6 | 1.0 | 0.0 | 13.6 | 6.7 | 4.6 | 0.0 |
| JPM | 4.5 | 7.2 | 6.7 | 7.6 | 1.2 | 3.7 | 4.9 | 8.4 |
| XOM | 4.5 | 6.3 | 0.0 | 18.2 | -0.8 | -1.6 | -0.0 | 20.1 |
| UNH | 4.5 | 5.0 | 6.9 | 3.5 | 0.5 | 1.5 | 4.8 | 3.8 |
| COST | 4.5 | 8.0 | 22.4 | 17.1 | -0.9 | -1.5 | 5.1 | 18.8 |
| TLT | 4.5 | 12.9 | 16.8 | 30.0 | 0.3 | 2.1 | 5.4 | 23.0 |
| GLD | 4.5 | 5.9 | 5.4 | 3.8 | 1.8 | 4.1 | 4.8 | 4.1 |

| method | expected volatility | diversification ratio | effective number of bets | largest risk share | largest risk holder |
|---|---|---|---|---|---|
| Equal weight | 27.7% | 1.81 | 12.36 | 13.6% | BE |
| Inverse volatility | 18.2% | 2.16 | 16.55 | 7.6% | TSM |
| Risk parity | 14.0% | 2.46 | 20.97 | 5.4% | TLT |
| Minimum variance | 8.6% | 2.94 | 6.81 | 23.0% | TLT |

Concentration warnings:

- AMD and TSM have correlation 0.71: they tend to fall together
- ETN and GEV have correlation 0.72: they tend to fall together
- CEG and VST have correlation 0.81: they tend to fall together

Out-of-sample comparison, monthly rebalance (2025-04-01 to 2026-11-11):

| method | CAGR | Volatility | Sharpe | Max drawdown |
|---|---|---|---|---|
| Equal weight | +64.7% | +28.7% | 1.88 | -18.0% |
| Inverse volatility | +44.9% | +20.7% | 1.90 | -11.2% |
| Risk parity | +34.1% | +16.1% | 1.91 | -9.3% |
| Minimum variance | +14.8% | +10.1% | 1.42 | -6.8% |

![Correlations](portfolio_correlation.png)

![Risk shares](portfolio_risk_shares.png)

![Walk-forward](portfolio_walk_forward.png)

## 8. Opening gaps: do pre-market moves carry into the day?

Across 19,011 stock-days (18 watchlist stocks, 2021-11-15 to 2026-11-11), each 1% of opening gap went with a -0.02% move from the open to the close (95% block-bootstrap CI [-0.08%, +0.03%]): no reliable relationship, so the size of a gap has not told you which way the session goes.

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 770 | -5.2% | +0.30% | 50% |
| down 1-3% | 2905 | -1.7% | +0.09% | 52% |
| within 1% | 11035 | +0.0% | +0.02% | 50% |
| up 1-3% | 3370 | +1.7% | +0.09% | 52% |
| gap up 3%+ | 931 | +5.4% | -0.13% | 47% |

## 9. Deciding before the open vs at the previous close

From 2022-02-09 to 2026-11-10 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +45.4% a year (worst drawdown -33.1%) against +41.6% (-39.4%) for labels set at the previous close; the two agreed on 89% of stock-weeks. Sharpe ratio difference +0.08 (95% block-bootstrap CI [-0.10, +0.28]): deciding before the open has been **not distinguishable from deciding on the previous close**.

| strategy | CAGR | Volatility | Sharpe | Max drawdown |
|---|---|---|---|---|
| Board on the previous close | +41.6% | 33.5% | 1.21 | -39.4% |
| Board on the pre-market price | +45.4% | 33.7% | 1.28 | -33.1% |
| Equal-weight watchlist | +44.3% | 35.3% | 1.22 | -40.7% |

The pre-market version uses the official opening price as a stand-in for the last pre-market trade (free pre-market history is only days long), which slightly flatters it.
