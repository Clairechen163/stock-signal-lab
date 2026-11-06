# stocklab report
Generated 2026-11-06 | data source: `yahoo` | history: 5 years | watchlist: ALAB, AMD, NVDA, MRVL, GOOG, FSLR, SKHY, ETN, TSLA, SPCX, AMZN, IBM

> Educational research code, not investment advice. Past results do not predict future returns.

## 1. Decision board

Data as of the 2026-11-05 close. `*` = provisional (under 200 trading days of history).

| ticker | action | close | 1 day | 1 month | buy rank | sell warnings | pullback entry | breakout | stop | why |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | BUY | 260.21 | -2.2% | +0.1% | 3/12 | 1/15 | 254.43 | 266.56 | 235.51 | buy rank 3/12; +7% vs 200-day average; distribution days |
| IBM | WATCH | 247.11 | -2.8% | +12.1% | 4/12 | 4/15 | 244.57 | 258.80 | 229.50 | +0% vs 200-day average; death cross, RSI rollover, 20%+ off high |
| FSLR | AVOID | 195.76 | +0.6% | +8.7% | 11/12 | 5/15 |  |  |  | -9% vs 200-day average; below 200-day, death cross, 20%+ off high |
| AMD | SELL | 404.40 | -17.3% | -37.4% | 1/12 | 11/15 |  |  |  | -3% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, high-volume breakdown, 20%+ off high, volatility spike, below chandelier stop |
| MRVL | SELL | 133.55 | -16.4% | -53.1% | 2/12 | 11/15 |  |  |  | -28% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, high-volume breakdown, 20%+ off high, volatility spike, below chandelier stop |
| NVDA | SELL | 181.60 | -9.3% | -23.5% | 5/12 | 10/15 |  |  |  | -11% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, high-volume breakdown, 20%+ off high, below chandelier stop |
| ALAB | SELL | 179.47 | -19.6% | -53.0% | 6/12 | 10/15 |  |  |  | -30% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, high-volume breakdown, 20%+ off high, below chandelier stop |
| ETN | SELL | 327.02 | -7.4% | -24.2% | 7/12 | 11/15 |  |  |  | -17% vs 200-day average; below 50-day, below 200-day, MACD bearish, distribution days, high-volume breakdown, 20%+ off high, volatility spike, below chandelier stop |
| GOOG | SELL | 281.74 | -1.9% | -18.9% | 8/12 | 13/15 |  |  |  | -17% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, high-volume breakdown, 20%+ off high, volatility spike, below chandelier stop |
| SPCX | SELL* | 123.62 | -9.0% | -26.2% | 9/12 | 8/10 |  |  |  | -17% vs 50-day average; below 50-day, MACD bearish, distribution days, high-volume breakdown, 20%+ off high, below chandelier stop (provisional: 102 days of history) |
| TSLA | SELL | 343.69 | -10.8% | -9.0% | 10/12 | 12/15 |  |  |  | -11% vs 200-day average; below 50-day, below 200-day, death cross, MACD bearish, distribution days, high-volume breakdown, 20%+ off high, below chandelier stop |
| SKHY | SELL* | 123.90 | -13.4% | -30.5% | 12/12 | 8/10 |  |  |  | -26% vs 50-day average; below 50-day, MACD bearish, distribution days, high-volume breakdown, 20%+ off high, below chandelier stop (provisional: 84 days of history) |

![Board label each week](board_history.png)

**Trading the labels** (2022-02-02 to 2026-11-05): buy on BUY, exit on SELL, REDUCE or AVOID, reviewed weekly with next-day execution and 5 bp costs.

| strategy | CAGR | Volatility | Sharpe | Max drawdown | Time invested | Avg holdings |
|---|---|---|---|---|---|---|
| Board strategy | +31.9% | 31.7% | 1.03 | -28.2% | 95% | 4.1 |
| Equal-weight watchlist | +31.5% | 33.9% | 0.98 | -36.5% | 100% | 9.6 |
| SPY (buy & hold) | +12.5% | 17.3% | 0.77 | -22.1% |  |  |

Sharpe difference vs equal weight: +0.06, 95% block-bootstrap CI [-0.52, +0.61].

Forward 21-day return after each label, relative to the watchlist average on the same date (sampled every 21 days, t-test across dates):

| label | observations | dates | mean 21d excess return | hit rate | p_value |
|---|---|---|---|---|---|
| BUY | 157 | 53 | +0.1% | 49% | 0.93 |
| HOLD | 78 | 34 | -2.1% | 41% | 0.14 |
| WATCH | 103 | 46 | +1.1% | 52% | 0.53 |
| AVOID | 34 | 18 | +3.3% | 67% | 0.02 |
| REDUCE | 100 | 43 | -1.1% | 53% | 0.48 |
| SELL | 60 | 29 | +0.3% | 52% | 0.86 |

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
AMD  EXIT  (score 11/15, close 404.40 on 2026-11-05)
  RSI 30 | -37.7% from 52-week high
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
    50-day SMA                 547.37  (price is below, -26.1%)
    Chandelier stop            542.99  (price is below, -25.5%)
    200-day SMA                415.00  (price is below, -2.6%)
```

```
NVDA  EXIT  (score 10/15, close 181.60 on 2026-11-05)
  RSI 25 | -24.1% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [volume] Down day closing below the 50-day average on 1.5x+ average volume (+2)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 220.59  (price is below, -17.7%)
    Chandelier stop            217.05  (price is below, -16.3%)
    200-day SMA                204.38  (price is below, -11.1%)
```

```
MRVL  EXIT  (score 11/15, close 133.55 on 2026-11-05)
  RSI 23 | -57.8% from 52-week high
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
    50-day SMA                 236.28  (price is below, -43.5%)
    Chandelier stop            231.68  (price is below, -42.4%)
    200-day SMA                184.69  (price is below, -27.7%)
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
FSLR  WATCH  (score 5/15, close 195.76 on 2026-11-05)
  RSI 64 | -38.5% from 52-week high
  Triggered:
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [risk] 20%+ below the 52-week high (+1)
  Levels to watch:
    200-day SMA                214.85  (price is below, -8.9%)
    50-day SMA                 187.17  (price is above, +4.6%)
    Chandelier stop            184.50  (price is above, +6.1%)
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
ETN  EXIT  (score 11/15, close 327.02 on 2026-11-05)
  RSI 32 | -28.9% from 52-week high
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
    50-day SMA                 406.76  (price is below, -19.6%)
    200-day SMA                396.15  (price is below, -17.4%)
    Chandelier stop            380.96  (price is below, -14.2%)
```

```
TSLA  EXIT  (score 12/15, close 343.69 on 2026-11-05)
  RSI 36 | -29.8% from 52-week high
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
    200-day SMA                384.32  (price is below, -10.6%)
    50-day SMA                 372.07  (price is below, -7.6%)
    Chandelier stop            364.90  (price is below, -5.8%)
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
AMZN  HOLD  (score 1/15, close 260.21 on 2026-11-05)
  RSI 55 | -8.4% from 52-week high
  Triggered:
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
  Levels to watch:
    50-day SMA                 253.89  (price is above, +2.5%)
    Chandelier stop            244.85  (price is above, +6.3%)
    200-day SMA                243.82  (price is above, +6.7%)
```

```
IBM  WATCH  (score 4/15, close 247.11 on 2026-11-05)
  RSI 54 | -24.4% from 52-week high
  Triggered:
    - [trend] 50-day average below the 200-day average (+2)
    - [momentum] RSI was overbought (>70) in the last 5 days and has dropped below 65 (+1)
    - [risk] 20%+ below the 52-week high (+1)
  Levels to watch:
    200-day SMA                246.19  (price is above, +0.4%)
    Chandelier stop            237.25  (price is above, +4.2%)
    50-day SMA                 236.63  (price is above, +4.4%)
```

## 3. Which sell signals actually work? (event study)

Panel: 41 stocks, 5 years. Null hypothesis: returns after a signal look like returns on random days from the same stocks.

| rule | horizon | events | mean_after_signal | mean_random_days | difference | p_value | q_value | drop10_after_signal | drop10_base_rate | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| below_sma50 | 5d | 963 | +0.26% | +0.62% | -0.36% | 0.024 | 0.134 | 37% | 35% | weak (not significant) |
| below_sma50 | 21d | 940 | +2.43% | +2.79% | -0.36% | 0.192 | 0.373 | 37% | 35% | weak (not significant) |
| below_sma50 | 63d | 901 | +8.43% | +9.24% | -0.81% | 0.150 | 0.371 | 37% | 35% | weak (not significant) |
| below_sma200 | 5d | 462 | +0.05% | +0.54% | -0.49% | 0.032 | 0.134 | 37% | 35% | weak (not significant) |
| below_sma200 | 21d | 450 | +1.31% | +2.39% | -1.09% | 0.027 | 0.134 | 37% | 35% | weak (not significant) |
| below_sma200 | 63d | 430 | +8.39% | +7.92% | +0.48% | 0.676 | 0.902 | 37% | 35% | no edge |
| death_cross | 5d | 141 | -0.74% | +0.56% | -1.30% | 0.003 | 0.058 | 46% | 35% | useful |
| death_cross | 21d | 135 | -0.39% | +2.49% | -2.88% | 0.001 | 0.033 | 46% | 35% | useful |
| death_cross | 63d | 129 | +10.18% | +8.46% | +1.72% | 0.814 | 0.995 | 46% | 35% | no edge |
| rsi_divergence | 5d | 446 | +0.33% | +0.71% | -0.39% | 0.075 | 0.247 | 37% | 35% | weak (not significant) |
| rsi_divergence | 21d | 443 | +2.57% | +3.25% | -0.68% | 0.108 | 0.312 | 37% | 35% | weak (not significant) |
| rsi_divergence | 63d | 436 | +8.42% | +10.91% | -2.49% | 0.010 | 0.087 | 37% | 35% | useful |
| rsi_rollover | 5d | 573 | +1.61% | +0.68% | +0.93% | 1.000 | 1.000 | 33% | 35% | no edge |
| rsi_rollover | 21d | 563 | +3.15% | +3.17% | -0.02% | 0.487 | 0.766 | 33% | 35% | weak (not significant) |
| rsi_rollover | 63d | 552 | +8.25% | +10.76% | -2.52% | 0.007 | 0.077 | 33% | 35% | useful |
| macd_bearish | 5d | 1453 | +0.54% | +0.65% | -0.11% | 0.240 | 0.418 | 34% | 35% | weak (not significant) |
| macd_bearish | 21d | 1429 | +2.91% | +2.93% | -0.02% | 0.457 | 0.754 | 34% | 35% | weak (not significant) |
| macd_bearish | 63d | 1368 | +10.22% | +9.76% | +0.45% | 0.765 | 0.970 | 34% | 35% | no edge |
| distribution_cluster | 5d | 971 | +1.00% | +0.65% | +0.35% | 0.975 | 1.000 | 35% | 35% | no edge |
| distribution_cluster | 21d | 948 | +2.65% | +3.00% | -0.36% | 0.183 | 0.373 | 35% | 35% | weak (not significant) |
| distribution_cluster | 63d | 918 | +9.40% | +9.93% | -0.54% | 0.241 | 0.418 | 35% | 35% | weak (not significant) |
| high_volume_breakdown | 5d | 658 | +0.64% | +0.60% | +0.05% | 0.590 | 0.846 | 33% | 35% | no edge |
| high_volume_breakdown | 21d | 641 | +3.47% | +2.71% | +0.77% | 0.950 | 1.000 | 33% | 35% | no edge |
| high_volume_breakdown | 63d | 625 | +11.34% | +9.01% | +2.33% | 0.992 | 1.000 | 33% | 35% | no edge |
| drawdown_20 | 5d | 340 | +0.74% | +0.73% | +0.01% | 0.521 | 0.782 | 48% | 35% | no edge |
| drawdown_20 | 21d | 332 | +1.96% | +3.36% | -1.40% | 0.032 | 0.134 | 48% | 35% | weak (not significant) |
| drawdown_20 | 63d | 315 | +13.29% | +11.26% | +2.03% | 0.909 | 1.000 | 48% | 35% | no edge |
| volatility_spike | 5d | 292 | +0.32% | +0.66% | -0.33% | 0.168 | 0.371 | 45% | 35% | weak (not significant) |
| volatility_spike | 21d | 288 | +2.32% | +3.03% | -0.71% | 0.166 | 0.371 | 45% | 35% | weak (not significant) |
| volatility_spike | 63d | 286 | +7.86% | +10.10% | -2.24% | 0.053 | 0.196 | 45% | 35% | weak (not significant) |
| chandelier_stop | 5d | 1215 | +0.43% | +0.64% | -0.21% | 0.113 | 0.312 | 35% | 35% | weak (not significant) |
| chandelier_stop | 21d | 1190 | +3.07% | +2.90% | +0.17% | 0.684 | 0.902 | 35% | 35% | no edge |
| chandelier_stop | 63d | 1141 | +10.92% | +9.70% | +1.22% | 0.964 | 1.000 | 35% | 35% | no edge |

**4 of 33 rule-by-horizon tests** show significantly weaker returns after the signal (q < 0.10).

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

### AMD (2022-08-24 to 2026-11-05)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +315.9% | +40.6% | -63.0% | +57.8% | 0.88 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +279.1% | +37.5% | -39.1% | +47.9% | 0.90 | 1 | 65% | +0.03 | [-0.56, +0.59] | 0.94 |
| Close > 50-day SMA | +156.9% | +25.3% | -41.8% | +43.8% | 0.73 | 37 | 54% | -0.15 | [-0.70, +0.39] | 0.61 |
| MACD > signal | +343.0% | +42.7% | -42.4% | +41.4% | 1.06 | 39 | 50% | +0.19 | [-0.43, +0.88] | 0.58 |
| RSI 30/70 | +30.3% | +6.5% | -54.7% | +31.3% | 0.36 | 3 | 33% | -0.52 | [-1.60, +0.53] | 0.33 |
| Trailing stop 20% | +150.3% | +24.5% | -58.9% | +49.3% | 0.69 | 10 | 71% | -0.19 | [-0.66, +0.30] | 0.45 |
| Volume breakout | +177.7% | +27.6% | -36.9% | +37.1% | 0.84 | 10 | 38% | -0.03 | [-0.88, +0.75] | 0.93 |

### NVDA (2022-08-24 to 2026-11-05)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +917.2% | +74.0% | -37.3% | +49.2% | 1.37 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +601.4% | +59.2% | -28.4% | +42.9% | 1.30 | 1 | 84% | -0.07 | [-0.62, +0.45] | 0.78 |
| Close > 50-day SMA | +293.7% | +38.7% | -39.1% | +39.3% | 1.03 | 39 | 69% | -0.34 | [-0.92, +0.20] | 0.23 |
| MACD > signal | +152.9% | +24.8% | -46.7% | +34.4% | 0.81 | 40 | 51% | -0.56 | [-1.24, +0.23] | 0.16 |
| RSI 30/70 | +64.6% | +12.6% | -22.6% | +18.2% | 0.74 | 2 | 7% | -0.63 | [-1.64, +0.35] | 0.21 |
| Trailing stop 20% | +543.1% | +56.0% | -36.6% | +44.6% | 1.22 | 7 | 88% | -0.15 | [-0.50, +0.18] | 0.38 |
| Volume breakout | +211.5% | +31.2% | -19.8% | +26.3% | 1.16 | 7 | 31% | -0.21 | [-1.08, +0.64] | 0.65 |

### MRVL (2022-08-24 to 2026-11-05)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +145.9% | +24.0% | -60.8% | +67.1% | 0.65 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +30.0% | +6.5% | -65.2% | +57.1% | 0.39 | 2 | 67% | -0.26 | [-0.77, +0.20] | 0.27 |
| Close > 50-day SMA | +47.3% | +9.7% | -51.5% | +52.9% | 0.43 | 37 | 58% | -0.22 | [-0.82, +0.36] | 0.47 |
| MACD > signal | +101.6% | +18.2% | -62.5% | +50.2% | 0.58 | 44 | 51% | -0.07 | [-0.80, +0.75] | 0.86 |
| RSI 30/70 | +39.0% | +8.2% | -32.1% | +28.2% | 0.42 | 2 | 19% | -0.23 | [-1.18, +0.79] | 0.64 |
| Trailing stop 20% | +66.8% | +13.0% | -53.3% | +56.7% | 0.49 | 15 | 76% | -0.16 | [-0.67, +0.31] | 0.53 |
| Volume breakout | +76.0% | +14.5% | -46.2% | +42.0% | 0.53 | 11 | 36% | -0.12 | [-1.07, +0.73] | 0.78 |

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

### FSLR (2022-08-24 to 2026-11-05)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +60.8% | +12.0% | -60.0% | +55.0% | 0.48 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +15.6% | +3.5% | -51.1% | +41.8% | 0.29 | 4 | 59% | -0.19 | [-0.77, +0.34] | 0.50 |
| Close > 50-day SMA | +50.2% | +10.2% | -46.8% | +40.2% | 0.44 | 28 | 50% | -0.04 | [-0.62, +0.54] | 0.89 |
| MACD > signal | -53.7% | -16.8% | -74.1% | +40.5% | -0.25 | 48 | 49% | -0.73 | [-1.41, -0.11] | 0.03 |
| RSI 30/70 | +30.1% | +6.5% | -42.8% | +30.4% | 0.35 | 2 | 27% | -0.12 | [-1.16, +0.74] | 0.78 |
| Trailing stop 20% | +34.4% | +7.3% | -52.3% | +45.1% | 0.38 | 11 | 69% | -0.10 | [-0.57, +0.39] | 0.69 |
| Volume breakout | -16.5% | -4.2% | -53.8% | +32.1% | 0.03 | 13 | 37% | -0.45 | [-1.29, +0.34] | 0.30 |

### ETN (2022-08-24 to 2026-11-05)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +133.6% | +22.5% | -34.5% | +33.8% | 0.77 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +54.6% | +11.0% | -35.7% | +30.2% | 0.50 | 2 | 83% | -0.27 | [-0.72, +0.08] | 0.19 |
| Close > 50-day SMA | +25.7% | +5.6% | -37.5% | +24.6% | 0.35 | 46 | 66% | -0.42 | [-0.99, +0.19] | 0.17 |
| MACD > signal | +37.3% | +7.9% | -25.8% | +22.4% | 0.45 | 48 | 50% | -0.32 | [-1.05, +0.41] | 0.38 |
| RSI 30/70 | +15.7% | +3.6% | -18.6% | +11.5% | 0.36 | 1 | 5% | -0.41 | [-1.41, +0.79] | 0.43 |
| Trailing stop 20% | +165.3% | +26.2% | -23.6% | +31.0% | 0.91 | 2 | 95% | +0.14 | [-0.09, +0.39] | 0.28 |
| Volume breakout | +21.6% | +4.8% | -29.3% | +18.1% | 0.35 | 10 | 38% | -0.42 | [-1.24, +0.45] | 0.32 |

### TSLA (2022-08-24 to 2026-11-05)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +16.0% | +3.6% | -65.0% | +58.2% | 0.35 | 0 | 100% |  |  |  |
| 50/200 SMA cross | -26.4% | -7.1% | -56.8% | +40.1% | 0.01 | 4 | 47% | -0.34 | [-1.23, +0.49] | 0.43 |
| Close > 50-day SMA | +39.4% | +8.3% | -41.1% | +38.4% | 0.40 | 42 | 53% | +0.05 | [-0.66, +0.84] | 0.90 |
| MACD > signal | +376.6% | +45.2% | -39.8% | +40.8% | 1.11 | 41 | 51% | +0.76 | [+0.15, +1.40] | 0.02 |
| RSI 30/70 | +33.5% | +7.1% | -52.7% | +40.1% | 0.37 | 4 | 42% | +0.02 | [-0.72, +0.78] | 0.96 |
| Trailing stop 20% | +18.3% | +4.1% | -47.9% | +44.9% | 0.31 | 11 | 71% | -0.04 | [-0.62, +0.59] | 0.91 |
| Volume breakout | +40.5% | +8.5% | -35.4% | +25.7% | 0.44 | 9 | 18% | +0.09 | [-0.88, +1.05] | 0.83 |

### AMZN (2022-08-24 to 2026-11-05)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +89.4% | +16.5% | -40.4% | +34.1% | 0.62 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +33.8% | +7.2% | -41.4% | +27.8% | 0.39 | 2 | 73% | -0.23 | [-0.89, +0.39] | 0.48 |
| Close > 50-day SMA | +21.7% | +4.8% | -40.8% | +23.3% | 0.32 | 35 | 63% | -0.30 | [-0.92, +0.38] | 0.41 |
| MACD > signal | -2.8% | -0.7% | -28.7% | +22.7% | 0.08 | 50 | 49% | -0.53 | [-1.23, +0.20] | 0.15 |
| RSI 30/70 | +94.0% | +17.1% | -22.0% | +21.6% | 0.84 | 4 | 33% | +0.22 | [-0.45, +1.03] | 0.55 |
| Trailing stop 20% | +94.4% | +17.2% | -24.2% | +29.9% | 0.68 | 3 | 87% | +0.06 | [-0.38, +0.51] | 0.78 |
| Volume breakout | +4.1% | +1.0% | -35.5% | +18.7% | 0.14 | 11 | 45% | -0.47 | [-1.33, +0.48] | 0.31 |

### IBM (2022-08-24 to 2026-11-05)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +112.4% | +19.7% | -37.5% | +31.5% | 0.73 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +57.1% | +11.4% | -28.7% | +22.9% | 0.59 | 3 | 73% | -0.15 | [-0.79, +0.51] | 0.65 |
| Close > 50-day SMA | +54.3% | +10.9% | -42.6% | +25.1% | 0.54 | 27 | 59% | -0.19 | [-0.65, +0.40] | 0.48 |
| MACD > signal | +107.2% | +19.0% | -43.1% | +24.0% | 0.85 | 30 | 50% | +0.12 | [-0.47, +0.86] | 0.72 |
| RSI 30/70 | +175.4% | +27.4% | -16.5% | +17.4% | 1.48 | 8 | 35% | +0.74 | [-0.23, +1.63] | 0.12 |
| Trailing stop 20% | +61.2% | +12.1% | -45.9% | +30.3% | 0.53 | 3 | 92% | -0.20 | [-0.45, +0.03] | 0.09 |
| Volume breakout | +66.2% | +12.9% | -25.0% | +17.0% | 0.80 | 10 | 40% | +0.07 | [-0.85, +0.97] | 0.90 |

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
  80% range high                   +14.02%
  daily volatility                 +7.02%
```

Best out-of-sample AUC **0.484**; smallest p-value against a naive baseline 0.850, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![ALAB feature effects](forecast_ALAB.png)

### AMD

Walk-forward test on 550 unseen days (2024-08-27 to 2026-11-04).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.507 | 0.527 | 0.837 | 0.49 | 0.25 | 0.97 | 1.024 |
| Logistic regression | 0.476 | 0.527 | 0.992 | 0.485 | 0.256 | 0.317 | 1.024 |
| Gradient boosting | 0.469 | 0.527 | 0.997 | 0.478 | 0.269 | -0.058 | 1.024 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 398.5 | 0.0 |  |  |
| Ridge regression | 402.6 | -0.0207 | 0.491 | 0.891 |
| Gradient boosting | 407.6 | -0.0461 | 0.495 | 0.992 |

Forecast for the next session:

```
  P(up) | Logistic regression      64.3%
  P(up) | Gradient boosting        59.6%
  P(up) | historical base rate     51.2%
  expected return (ridge)          +1.79%
  80% range low                    -5.67%
  80% range high                   +9.84%
  daily volatility                 +5.94%
```

Best out-of-sample AUC **0.485**; smallest p-value against a naive baseline 0.891, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![AMD feature effects](forecast_AMD.png)

### NVDA

Walk-forward test on 550 unseen days (2024-08-27 to 2026-11-04).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.522 | 0.522 | 0.517 | 0.497 | 0.25 | 0.583 | 0.583 |
| Logistic regression | 0.52 | 0.522 | 0.551 | 0.523 | 0.252 | 0.594 | 0.583 |
| Gradient boosting | 0.525 | 0.522 | 0.449 | 0.486 | 0.268 | 0.763 | 0.583 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 282.2 | 0.0 |  |  |
| Ridge regression | 284.0 | -0.0131 | 0.507 | 0.692 |
| Gradient boosting | 289.2 | -0.0508 | 0.54 | 0.944 |

Forecast for the next session:

```
  P(up) | Logistic regression      43.4%
  P(up) | Gradient boosting        58.2%
  P(up) | historical base rate     53.6%
  expected return (ridge)          -0.12%
  80% range low                    -3.68%
  80% range high                   +3.58%
  daily volatility                 +2.84%
```

Best out-of-sample AUC **0.523**; smallest p-value against a naive baseline 0.449, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![NVDA feature effects](forecast_NVDA.png)

### MRVL

Walk-forward test on 550 unseen days (2024-08-27 to 2026-11-04).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.535 | 0.535 | 0.517 | 0.487 | 0.249 | 0.773 | 0.773 |
| Logistic regression | 0.533 | 0.535 | 0.551 | 0.547 | 0.252 | 0.595 | 0.773 |
| Gradient boosting | 0.522 | 0.535 | 0.739 | 0.545 | 0.26 | 0.596 | 0.773 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 479.8 | 0.0 |  |  |
| Ridge regression | 482.3 | -0.0103 | 0.518 | 0.754 |
| Gradient boosting | 488.0 | -0.0344 | 0.495 | 0.965 |

Forecast for the next session:

```
  P(up) | Logistic regression      76.3%
  P(up) | Gradient boosting        76.7%
  P(up) | historical base rate     52.4%
  expected return (ridge)          -0.99%
  80% range low                    -9.10%
  80% range high                   +7.84%
  daily volatility                 +6.67%
```

Best out-of-sample AUC **0.547**; smallest p-value against a naive baseline 0.551, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![MRVL feature effects](forecast_MRVL.png)

### GOOG

Walk-forward test on 550 unseen days (2024-08-27 to 2026-11-04).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.52 | 0.52 | 0.517 | 0.483 | 0.25 | 0.926 | 0.926 |
| Logistic regression | 0.545 | 0.52 | 0.125 | 0.533 | 0.253 | 0.388 | 0.926 |
| Gradient boosting | 0.522 | 0.52 | 0.483 | 0.528 | 0.263 | 0.706 | 0.926 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 201.6 | 0.0 |  |  |
| Ridge regression | 204.4 | -0.0278 | 0.522 | 0.98 |
| Gradient boosting | 209.1 | -0.076 | 0.522 | 0.999 |

Forecast for the next session:

```
  P(up) | Logistic regression      35.8%
  P(up) | Gradient boosting        44.5%
  P(up) | historical base rate     52.8%
  expected return (ridge)          +0.62%
  80% range low                    -3.35%
  80% range high                   +4.75%
  daily volatility                 +3.14%
```

Best out-of-sample AUC **0.533**; smallest p-value against a naive baseline 0.125, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![GOOG feature effects](forecast_GOOG.png)

### FSLR

Walk-forward test on 550 unseen days (2024-08-27 to 2026-11-04).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.509 | 0.515 | 0.618 | 0.464 | 0.25 | 0.345 | 0.142 |
| Logistic regression | 0.52 | 0.515 | 0.416 | 0.531 | 0.251 | -0.011 | 0.142 |
| Gradient boosting | 0.52 | 0.515 | 0.416 | 0.527 | 0.259 | 0.248 | 0.142 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 363.5 | 0.0 |  |  |
| Ridge regression | 363.9 | -0.0025 | 0.502 | 0.582 |
| Gradient boosting | 374.5 | -0.0615 | 0.509 | 0.998 |

Forecast for the next session:

```
  P(up) | Logistic regression      62.8%
  P(up) | Gradient boosting        46.6%
  P(up) | historical base rate     49.3%
  expected return (ridge)          +1.41%
  80% range low                    -1.72%
  80% range high                   +4.65%
  daily volatility                 +2.45%
```

Best out-of-sample AUC **0.531**; smallest p-value against a naive baseline 0.416, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![FSLR feature effects](forecast_FSLR.png)

### ETN

Walk-forward test on 550 unseen days (2024-08-27 to 2026-11-04).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.524 | 0.524 | 0.517 | 0.483 | 0.25 | 0.341 | 0.342 |
| Logistic regression | 0.515 | 0.524 | 0.681 | 0.508 | 0.256 | 0.482 | 0.342 |
| Gradient boosting | 0.547 | 0.524 | 0.143 | 0.525 | 0.26 | 0.537 | 0.342 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 246.7 | 0.0 |  |  |
| Ridge regression | 248.7 | -0.0167 | 0.516 | 0.825 |
| Gradient boosting | 252.6 | -0.0486 | 0.513 | 0.968 |

Forecast for the next session:

```
  P(up) | Logistic regression      84.4%
  P(up) | Gradient boosting        72.3%
  P(up) | historical base rate     53.9%
  expected return (ridge)          +2.11%
  80% range low                    -3.06%
  80% range high                   +7.57%
  daily volatility                 +4.06%
```

Best out-of-sample AUC **0.525**; smallest p-value against a naive baseline 0.143, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![ETN feature effects](forecast_ETN.png)

### TSLA

Walk-forward test on 550 unseen days (2024-08-27 to 2026-11-04).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.502 | 0.502 | 0.517 | 0.459 | 0.25 | 0.677 | 0.677 |
| Logistic regression | 0.505 | 0.502 | 0.449 | 0.511 | 0.253 | 0.784 | 0.677 |
| Gradient boosting | 0.505 | 0.502 | 0.449 | 0.519 | 0.264 | 0.169 | 0.677 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 369.4 | 0.0 |  |  |
| Ridge regression | 374.3 | -0.0266 | 0.495 | 0.964 |
| Gradient boosting | 375.9 | -0.0356 | 0.533 | 0.917 |

Forecast for the next session:

```
  P(up) | Logistic regression      57.9%
  P(up) | Gradient boosting        60.2%
  P(up) | historical base rate     50.5%
  expected return (ridge)          +0.97%
  80% range low                    -3.40%
  80% range high                   +5.53%
  daily volatility                 +3.45%
```

Best out-of-sample AUC **0.519**; smallest p-value against a naive baseline 0.449, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![TSLA feature effects](forecast_TSLA.png)

### AMZN

Walk-forward test on 550 unseen days (2024-08-27 to 2026-11-04).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.516 | 0.516 | 0.517 | 0.462 | 0.25 | 0.716 | 0.717 |
| Logistic regression | 0.551 | 0.516 | 0.057 | 0.561 | 0.248 | 1.075 | 0.717 |
| Gradient boosting | 0.52 | 0.516 | 0.449 | 0.53 | 0.261 | 0.363 | 0.717 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 212.3 | 0.0 |  |  |
| Ridge regression | 214.0 | -0.0153 | 0.538 | 0.853 |
| Gradient boosting | 221.3 | -0.0858 | 0.527 | 1.0 |

Forecast for the next session:

```
  P(up) | Logistic regression      57.1%
  P(up) | Gradient boosting        51.7%
  P(up) | historical base rate     51.2%
  expected return (ridge)          +0.85%
  80% range low                    -2.55%
  80% range high                   +4.37%
  daily volatility                 +2.68%
```

Best out-of-sample AUC **0.561**; smallest p-value against a naive baseline 0.057, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![AMZN feature effects](forecast_AMZN.png)

### IBM

Walk-forward test on 550 unseen days (2024-08-27 to 2026-11-04).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.547 | 0.547 | 0.518 | 0.473 | 0.248 | 0.52 | 0.52 |
| Logistic regression | 0.54 | 0.547 | 0.65 | 0.476 | 0.254 | 0.735 | 0.52 |
| Gradient boosting | 0.515 | 0.547 | 0.943 | 0.494 | 0.265 | 0.59 | 0.52 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 253.4 | 0.0 |  |  |
| Ridge regression | 258.7 | -0.0424 | 0.529 | 0.996 |
| Gradient boosting | 259.5 | -0.0488 | 0.54 | 0.999 |

Forecast for the next session:

```
  P(up) | Logistic regression      41.1%
  P(up) | Gradient boosting        46.0%
  P(up) | historical base rate     55.0%
  expected return (ridge)          -0.29%
  80% range low                    -2.50%
  80% range high                   +1.97%
  daily volatility                 +1.75%
```

Best out-of-sample AUC **0.494**; smallest p-value against a naive baseline 0.650, before correcting for the four models tested here and the other stocks (the corrected count is in the summary).

![IBM feature effects](forecast_IBM.png)

## 6. Stock screen and entry plans

| ticker | rank | score | passes_filters | close | momentum_12_1 | momentum_6m | volatility | off_52w_high | forward_pe | pullback_entry | breakout_trigger | stop | stop_% | shares | position_$ | max_loss_$ | filter_notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| XOM | 1 | +0.51 | True | 165.30 | +47.9% | +14.3% | +27.6% | -11.7% | 13.4 | 160.45 | 187.62 | 150.74 | -6.0% | 62 | 9948.0 | 602.0 |  |
| LLY | 2 | +0.51 | True | 1364.73 | +31.9% | +40.4% | +31.4% | -3.8% | 27.2 | 1293.22 | 1420.83 | 1198.01 | -7.4% | 7 | 9053.0 | 666.0 |  |
| V | 3 | +0.49 | True | 422.59 | +10.2% | +32.1% | +21.8% | -3.2% | 24.7 | 407.0 | 437.44 | 388.79 | -4.5% | 24 | 9768.0 | 437.0 |  |
| KO | 4 | +0.47 | True | 95.73 | +28.3% | +23.6% | +17.4% | -0.1% | 27.1 | 92.9 | 96.02 | 89.46 | -3.7% | 107 | 9940.0 | 367.0 |  |
| MSFT | 5 | +0.47 | True | 535.93 | +3.8% | +27.9% | +26.7% | -3.6% | 22.2 | 531.63 | 556.91 | 500.51 | -5.9% | 18 | 9569.0 | 560.0 |  |
| JNJ | 6 | +0.46 | True | 272.32 | +41.4% | +23.7% | +24.6% | -2.2% | 23.4 | 265.58 | 276.87 | 251.28 | -5.4% | 37 | 9826.0 | 529.0 |  |
| AAPL | 7 | +0.42 | True | 344.17 | +25.1% | +19.9% | +22.1% | -1.5% | 32.3 | 343.1 | 350.21 | 325.36 | -5.2% | 29 | 9950.0 | 514.0 |  |
| JPM | 8 | +0.28 | True | 337.34 | +8.6% | +11.2% | +19.9% | -7.2% | 13.2 | 336.96 | 352.81 | 320.99 | -4.7% | 29 | 9772.0 | 463.0 |  |
| UNH | 9 | +0.14 | True | 395.72 | +16.7% | +8.3% | +23.8% | -8.8% | 17.0 | 390.14 | 425.83 | 364.9 | -6.5% | 25 | 9753.0 | 631.0 |  |
| PG | 10 | +0.08 | True | 167.10 | +2.7% | +16.0% | +20.3% | -0.1% | 22.6 | 159.01 | 167.65 | 152.53 | -4.1% | 62 | 9859.0 | 402.0 |  |
| LIN | 11 | +0.04 | True | 521.23 | +17.4% | +6.2% | +16.0% | -4.3% | 26.7 | 504.58 | 525.79 | 485.88 | -3.7% | 19 | 9587.0 | 355.0 |  |
| AMT | 12 | -0.10 | True | 193.99 | -4.1% | +10.1% | +29.2% | -0.4% | 27.7 | 184.95 | 195.25 | 173.81 | -6.0% | 54 | 9987.0 | 601.0 |  |
| AMZN | 13 | -0.15 | True | 260.21 | +4.3% | -4.0% | +31.1% | -8.4% | 23.9 | 254.43 | 266.56 | 235.51 | -7.4% | 39 | 9923.0 | 738.0 |  |
| COST | 14 | -0.21 | True | 1065.59 | +0.6% | +5.6% | +20.1% | -2.3% | 42.6 | 997.93 | 1067.72 | 957.78 | -4.0% | 10 | 9979.0 | 401.0 |  |
| NEE | 15 | -0.21 | True | 88.25 | -3.0% | -4.0% | +20.5% | -8.5% | 20.2 | 81.4 | 88.63 | 77.76 | -4.5% | 122 | 9930.0 | 443.0 |  |

## 7. Portfolio construction

Not included: SKHY (only 84 trading days of history, needs 252); SPCX (only 102 trading days of history, needs 252).

Assets: ALAB, AMD, NVDA, MRVL, GOOG, FSLR, ETN, TSLA, AMZN, IBM, JPM, XOM, UNH, COST, TLT, GLD. Covariance: Ledoit-Wolf shrinkage on the last 252 trading days.

Weights and share of risk (%):

| asset | weight: Equal weight | weight: Inverse volatility | weight: Risk parity | weight: Minimum variance | risk share: Equal weight | risk share: Inverse volatility | risk share: Risk parity | risk share: Minimum variance |
|---|---|---|---|---|---|---|---|---|
| ALAB | 6.2 | 2.2 | 1.7 | 0.0 | 21.2 | 9.2 | 6.4 | 0.0 |
| AMD | 6.2 | 3.0 | 2.0 | 0.0 | 15.4 | 10.3 | 6.4 | 0.0 |
| NVDA | 6.2 | 5.5 | 4.6 | 5.1 | 6.6 | 8.7 | 6.7 | 5.8 |
| MRVL | 6.2 | 2.6 | 1.8 | 0.0 | 17.7 | 9.7 | 6.3 | 0.0 |
| GOOG | 6.2 | 6.3 | 5.2 | 4.5 | 3.9 | 7.2 | 6.6 | 5.1 |
| FSLR | 6.2 | 4.1 | 3.3 | 0.5 | 7.6 | 7.8 | 6.4 | 0.5 |
| ETN | 6.2 | 5.0 | 3.9 | 3.3 | 8.2 | 9.3 | 6.6 | 3.7 |
| TSLA | 6.2 | 4.7 | 3.2 | 0.0 | 8.1 | 9.5 | 6.5 | 0.0 |
| AMZN | 6.2 | 6.2 | 4.8 | 3.5 | 4.2 | 7.6 | 6.6 | 3.9 |
| IBM | 6.2 | 4.4 | 5.8 | 2.4 | 2.5 | 3.3 | 6.6 | 2.7 |
| JPM | 6.2 | 8.9 | 8.2 | 8.0 | 2.1 | 6.2 | 6.8 | 9.1 |
| XOM | 6.2 | 7.6 | 0.0 | 17.9 | -1.4 | -2.2 | -0.0 | 20.3 |
| UNH | 6.2 | 6.1 | 7.2 | 2.9 | 1.4 | 3.6 | 6.6 | 3.3 |
| COST | 6.2 | 9.8 | 21.5 | 18.0 | -1.2 | -0.9 | 7.2 | 20.4 |
| TLT | 6.2 | 16.3 | 20.4 | 30.0 | 0.5 | 3.7 | 7.6 | 20.8 |
| GLD | 6.2 | 7.2 | 6.4 | 3.8 | 3.3 | 7.1 | 6.7 | 4.3 |

| method | expected volatility | diversification ratio | effective number of bets | largest risk share | largest risk holder |
|---|---|---|---|---|---|
| Equal weight | 22.6% | 1.94 | 7.73 | 21.2% | ALAB |
| Inverse volatility | 14.5% | 2.38 | 11.93 | 10.3% | AMD |
| Risk parity | 12.7% | 2.46 | 14.96 | 7.6% | TLT |
| Minimum variance | 8.4% | 2.91 | 6.80 | 20.8% | TLT |

Out-of-sample comparison, monthly rebalance (2025-03-25 to 2026-11-05):

| method | CAGR | Volatility | Sharpe | Max drawdown |
|---|---|---|---|---|
| Equal weight | +36.3% | +24.2% | 1.40 | -14.7% |
| Inverse volatility | +27.0% | +16.8% | 1.51 | -10.7% |
| Risk parity | +22.6% | +13.6% | 1.56 | -8.6% |
| Minimum variance | +14.8% | +9.8% | 1.46 | -6.5% |

![Correlations](portfolio_correlation.png)

![Risk shares](portfolio_risk_shares.png)

![Walk-forward](portfolio_walk_forward.png)

## 8. Opening gaps: do pre-market moves carry into the day?

Across 12,121 stock-days (12 watchlist stocks, 2021-11-09 to 2026-11-05), each 1% of opening gap went with a -0.02% move from the open to the close (95% block-bootstrap CI [-0.07%, +0.03%]): no reliable relationship, so the size of a gap has not told you which way the session goes.

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 479 | -5.2% | +0.19% | 48% |
| down 1-3% | 1890 | -1.7% | +0.05% | 53% |
| within 1% | 7105 | +0.0% | +0.02% | 51% |
| up 1-3% | 2101 | +1.7% | +0.07% | 52% |
| gap up 3%+ | 546 | +5.4% | -0.24% | 46% |

## 9. Deciding before the open vs at the previous close

From 2022-02-03 to 2026-11-04 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +34.2% a year (worst drawdown -28.3%) against +33.2% (-24.7%) for labels set at the previous close; the two agreed on 89% of stock-weeks. Sharpe ratio difference +0.04 (95% block-bootstrap CI [-0.12, +0.19]): deciding before the open has been **not distinguishable from deciding on the previous close**.

| strategy | CAGR | Volatility | Sharpe | Max drawdown |
|---|---|---|---|---|
| Board on the previous close | +33.2% | 32.2% | 1.05 | -24.7% |
| Board on the pre-market price | +34.2% | 31.6% | 1.09 | -28.3% |
| Equal-weight watchlist | +33.1% | 34.7% | 1.00 | -38.9% |

The pre-market version uses the official opening price as a stand-in for the last pre-market trade (free pre-market history is only days long), which slightly flatters it.
