# stocklab report
Generated 2026-10-15 | data source: `yahoo` | history: 5 years

> Educational research code, not investment advice. Past results do not predict future returns.

**Holdings at a glance**

| ticker | status | score | P&L | close |
|---|---|---|---|---|
| KLAC | EXIT | 8/15 | -17.4% | 171.76 |
| VRT | EXIT | 10/15 | -20.0% | 209.58 |
| ALAB | REDUCE | 6/15 | -12.8% | 290.45 |

## 1. Sell check on current holdings

```
KLAC  EXIT  (score 8/15, close 171.76 on 2026-10-15)
  Entry 208.00 -> P&L -17.4%
  RSI 35 | -43.0% from 52-week high
  Triggered:
    - [position] Price is below your 15% stop-loss at 176.80 (overrides score)
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    50-day SMA                 187.37  (price is below, -8.3%)
    Chandelier stop            184.51  (price is below, -6.9%)
    200-day SMA                180.51  (price is below, -4.8%)
    Your 15% stop-loss         176.80  (price is below, -2.8%)
```

```
VRT  EXIT  (score 10/15, close 209.58 on 2026-10-15)
  Entry 262.00 -> P&L -20.0%
  RSI 28 | -44.3% from 52-week high
  Triggered:
    - [position] Price is below your 15% stop-loss at 222.70 (overrides score)
    - [trend] Close below the 50-day moving average (+1)
    - [trend] Close below the 200-day moving average (+2)
    - [trend] 50-day average below the 200-day average (+2)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    200-day SMA                267.97  (price is below, -21.8%)
    50-day SMA                 256.70  (price is below, -18.4%)
    Chandelier stop            222.94  (price is below, -6.0%)
    Your 15% stop-loss         222.70  (price is below, -5.9%)
```

```
ALAB  REDUCE  (score 6/15, close 290.45 on 2026-10-15)
  Entry 333.00 -> P&L -12.8%
  RSI 38 | -39.9% from 52-week high
  Triggered:
    - [trend] Close below the 50-day moving average (+1)
    - [momentum] MACD line below its signal line (+1)
    - [volume] 5+ distribution days in the last 25 sessions (institutional selling) (+1)
    - [risk] 20%+ below the 52-week high (+1)
    - [risk] Close below the chandelier stop (22-day high minus 3x ATR) (+2)
  Levels to watch:
    Chandelier stop            328.93  (price is below, -11.7%)
    50-day SMA                 316.01  (price is below, -8.1%)
    Your 15% stop-loss         283.05  (price is above, +2.6%)
    200-day SMA                249.18  (price is above, +16.6%)
```

## 2. Which sell signals actually work? (event study)

Panel: 36 stocks, 5 years. Null hypothesis: returns after a signal look like returns on random days from the same stocks.

| rule | horizon | events | mean_after_signal | mean_random_days | difference | p_value | q_value | drop10_after_signal | drop10_base_rate | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| below_sma50 | 5d | 837 | +0.47% | +0.64% | -0.18% | 0.178 | 0.424 | 37% | 34% | weak (not significant) |
| below_sma50 | 21d | 826 | +2.40% | +2.82% | -0.42% | 0.160 | 0.424 | 37% | 34% | weak (not significant) |
| below_sma50 | 63d | 789 | +8.71% | +9.50% | -0.80% | 0.168 | 0.424 | 37% | 34% | weak (not significant) |
| below_sma200 | 5d | 397 | +0.30% | +0.54% | -0.24% | 0.183 | 0.424 | 37% | 34% | weak (not significant) |
| below_sma200 | 21d | 390 | +1.74% | +2.35% | -0.62% | 0.142 | 0.424 | 37% | 34% | weak (not significant) |
| below_sma200 | 63d | 368 | +8.00% | +7.97% | +0.03% | 0.529 | 0.850 | 37% | 34% | no edge |
| death_cross | 5d | 119 | +0.14% | +0.56% | -0.42% | 0.193 | 0.424 | 47% | 34% | weak (not significant) |
| death_cross | 21d | 115 | +0.68% | +2.44% | -1.76% | 0.051 | 0.424 | 47% | 34% | weak (not significant) |
| death_cross | 63d | 112 | +7.66% | +8.56% | -0.89% | 0.338 | 0.605 | 47% | 34% | weak (not significant) |
| rsi_divergence | 5d | 398 | +0.32% | +0.76% | -0.44% | 0.060 | 0.424 | 36% | 34% | weak (not significant) |
| rsi_divergence | 21d | 397 | +2.56% | +3.34% | -0.78% | 0.100 | 0.424 | 36% | 34% | weak (not significant) |
| rsi_divergence | 63d | 388 | +9.40% | +11.37% | -1.97% | 0.051 | 0.424 | 36% | 34% | weak (not significant) |
| rsi_rollover | 5d | 500 | +1.70% | +0.75% | +0.95% | 1.000 | 1.000 | 33% | 34% | no edge |
| rsi_rollover | 21d | 493 | +3.37% | +3.31% | +0.06% | 0.541 | 0.850 | 33% | 34% | no edge |
| rsi_rollover | 63d | 484 | +8.45% | +11.33% | -2.88% | 0.002 | 0.066 | 33% | 34% | useful |
| macd_bearish | 5d | 1262 | +0.71% | +0.68% | +0.03% | 0.573 | 0.860 | 34% | 34% | no edge |
| macd_bearish | 21d | 1252 | +3.15% | +2.98% | +0.17% | 0.681 | 0.925 | 34% | 34% | no edge |
| macd_bearish | 63d | 1199 | +10.53% | +10.12% | +0.41% | 0.726 | 0.925 | 34% | 34% | no edge |
| distribution_cluster | 5d | 832 | +0.91% | +0.69% | +0.22% | 0.860 | 1.000 | 35% | 34% | no edge |
| distribution_cluster | 21d | 818 | +2.47% | +3.02% | -0.55% | 0.093 | 0.424 | 35% | 34% | weak (not significant) |
| distribution_cluster | 63d | 793 | +9.48% | +10.32% | -0.84% | 0.161 | 0.424 | 35% | 34% | weak (not significant) |
| high_volume_breakdown | 5d | 566 | +0.81% | +0.62% | +0.20% | 0.803 | 0.981 | 31% | 34% | no edge |
| high_volume_breakdown | 21d | 562 | +3.43% | +2.71% | +0.73% | 0.917 | 1.000 | 31% | 34% | no edge |
| high_volume_breakdown | 63d | 542 | +11.62% | +9.19% | +2.43% | 0.989 | 1.000 | 31% | 34% | no edge |
| drawdown_20 | 5d | 290 | +1.04% | +0.80% | +0.24% | 0.729 | 0.925 | 46% | 34% | no edge |
| drawdown_20 | 21d | 282 | +3.14% | +3.50% | -0.36% | 0.335 | 0.605 | 46% | 34% | weak (not significant) |
| drawdown_20 | 63d | 265 | +14.72% | +12.00% | +2.72% | 0.937 | 1.000 | 46% | 34% | no edge |
| volatility_spike | 5d | 253 | +0.40% | +0.73% | -0.33% | 0.181 | 0.424 | 42% | 34% | weak (not significant) |
| volatility_spike | 21d | 253 | +2.62% | +3.12% | -0.50% | 0.269 | 0.555 | 42% | 34% | weak (not significant) |
| volatility_spike | 63d | 242 | +8.68% | +10.50% | -1.82% | 0.116 | 0.424 | 42% | 34% | weak (not significant) |
| chandelier_stop | 5d | 1046 | +0.61% | +0.68% | -0.07% | 0.348 | 0.605 | 34% | 34% | weak (not significant) |
| chandelier_stop | 21d | 1035 | +3.20% | +2.97% | +0.23% | 0.714 | 0.925 | 34% | 34% | no edge |
| chandelier_stop | 63d | 986 | +11.32% | +10.00% | +1.32% | 0.962 | 1.000 | 34% | 34% | no edge |

**1 of 33 rule-by-horizon tests** show significantly weaker returns after the signal (q < 0.10).

![Sell signal event study](sell_event_study.png)

## 3. Strategy backtests

### KLAC (2022-08-02 to 2026-10-15)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +352.2% | +43.3% | -44.5% | +46.3% | 1.01 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +247.2% | +34.6% | -44.5% | +41.2% | 0.93 | 2 | 78% | -0.08 | [-0.54, +0.38] | 0.70 |
| Close > 50-day SMA | +103.1% | +18.4% | -37.5% | +37.4% | 0.64 | 41 | 67% | -0.37 | [-0.88, +0.14] | 0.14 |
| MACD > signal | -4.4% | -1.1% | -39.9% | +33.5% | 0.14 | 43 | 49% | -0.87 | [-1.52, -0.36] | 0.00 |
| RSI 30/70 | +97.4% | +17.6% | -20.0% | +15.9% | 1.10 | 3 | 9% | +0.09 | [-0.83, +0.98] | 0.85 |
| Trailing stop 20% | +185.8% | +28.5% | -46.5% | +42.4% | 0.81 | 7 | 86% | -0.21 | [-0.53, +0.10] | 0.21 |
| Volume breakout | +13.0% | +3.0% | -31.2% | +27.6% | 0.24 | 9 | 35% | -0.77 | [-1.52, -0.03] | 0.04 |

### VRT (2022-08-02 to 2026-10-15)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +1657.3% | +98.2% | -61.3% | +62.5% | 1.41 | 0 | 100% |  |  |  |
| 50/200 SMA cross | +985.4% | +76.7% | -52.9% | +56.8% | 1.29 | 2 | 86% | -0.12 | [-0.56, +0.22] | 0.57 |
| Close > 50-day SMA | +730.4% | +65.7% | -42.2% | +48.9% | 1.28 | 27 | 69% | -0.13 | [-0.76, +0.44] | 0.67 |
| MACD > signal | +283.6% | +37.8% | -49.2% | +44.5% | 0.95 | 42 | 52% | -0.46 | [-1.00, +0.14] | 0.11 |
| RSI 30/70 | +58.0% | +11.5% | -28.6% | +18.4% | 0.68 | 1 | 8% | -0.73 | [-2.07, +0.48] | 0.25 |
| Trailing stop 20% | +699.1% | +64.2% | -60.3% | +54.8% | 1.18 | 8 | 84% | -0.23 | [-0.69, +0.22] | 0.32 |
| Volume breakout | +279.8% | +37.5% | -51.3% | +43.4% | 0.95 | 10 | 49% | -0.46 | [-1.24, +0.23] | 0.21 |

### ALAB (2025-01-03 to 2026-10-15)

| strategy | Total return | CAGR | Max drawdown | Volatility | Sharpe | Round trips | Time in market | Sharpe vs B&H | 95% CI | p-value |
|---|---|---|---|---|---|---|---|---|---|---|
| Buy & Hold | +102.4% | +48.8% | -63.2% | +95.7% | 0.89 | 0 | 100% |  |  |  |
| 50/200 SMA cross | -55.5% | -36.7% | -63.8% | +85.8% | -0.10 | 2 | 74% | -1.00 | [-1.96, -0.24] | 0.03 |
| Close > 50-day SMA | +3.7% | +2.1% | -66.4% | +71.5% | 0.39 | 9 | 54% | -0.50 | [-1.57, +0.47] | 0.32 |
| MACD > signal | +14.8% | +8.1% | -70.4% | +66.6% | 0.45 | 21 | 52% | -0.45 | [-1.53, +0.74] | 0.42 |
| RSI 30/70 | -2.2% | -1.2% | -50.3% | +36.4% | 0.15 | 1 | 16% | -0.75 | [-2.33, +1.18] | 0.36 |
| Trailing stop 20% | -15.0% | -8.8% | -69.1% | +73.5% | 0.25 | 9 | 58% | -0.65 | [-1.71, +0.29] | 0.20 |
| Volume breakout | +84.9% | +41.4% | -55.7% | +64.6% | 0.86 | 3 | 43% | -0.04 | [-1.24, +1.04] | 0.94 |

![Strategy equity curves](backtest_equity.png)

## 4. Next-day forecasts

### KLAC

Walk-forward test on 551 unseen days (2024-08-05 to 2026-10-14).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.561 | 0.561 | 0.518 | 0.48 | 0.248 | 1.059 | 1.06 |
| Logistic regression | 0.548 | 0.561 | 0.74 | 0.513 | 0.251 | 0.522 | 1.06 |
| Gradient boosting | 0.528 | 0.561 | 0.944 | 0.52 | 0.256 | 1.193 | 1.06 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 331.6 | 0.0 |  |  |
| Ridge regression | 334.6 | -0.018 | 0.515 | 0.876 |
| Gradient boosting | 331.6 | 0.0 | 0.515 | 0.499 |

Forecast for the next session:

```
  P(up) | Logistic regression      55.8%
  P(up) | Gradient boosting        52.4%
  P(up) | historical base rate     53.8%
  expected return (ridge)          +0.40%
  80% range low                    -2.94%
  80% range high                   +3.86%
  daily volatility                 +2.64%
```

Best out-of-sample AUC **0.520**: no reliable edge: treat the forecast as close to a coin flip.

![KLAC feature effects](forecast_KLAC.png)

### VRT

Walk-forward test on 551 unseen days (2024-08-05 to 2026-10-14).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.543 | 0.543 | 0.518 | 0.481 | 0.248 | 1.122 | 1.122 |
| Logistic regression | 0.506 | 0.543 | 0.96 | 0.473 | 0.254 | 0.632 | 1.122 |
| Gradient boosting | 0.523 | 0.543 | 0.837 | 0.518 | 0.257 | 1.281 | 1.122 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 423.6 | 0.0 |  |  |
| Ridge regression | 428.8 | -0.0247 | 0.53 | 0.972 |
| Gradient boosting | 431.0 | -0.0352 | 0.477 | 0.966 |

Forecast for the next session:

```
  P(up) | Logistic regression      60.1%
  P(up) | Gradient boosting        68.3%
  P(up) | historical base rate     54.3%
  expected return (ridge)          +0.54%
  80% range low                    -2.84%
  80% range high                   +4.03%
  daily volatility                 +2.66%
```

Best out-of-sample AUC **0.518**: no reliable edge: treat the forecast as close to a coin flip.

![VRT feature effects](forecast_VRT.png)

### ALAB

Walk-forward test on 194 unseen days (2026-01-07 to 2026-10-14).

| model | accuracy | always-majority accuracy | p (beats majority) | AUC | Brier | strategy Sharpe | buy & hold Sharpe |
|---|---|---|---|---|---|---|---|
| Majority class (baseline) | 0.526 | 0.526 | 0.529 | 0.454 | 0.25 | 1.224 | 1.224 |
| Logistic regression | 0.495 | 0.526 | 0.825 | 0.484 | 0.259 | 0.686 | 1.224 |
| Gradient boosting | 0.469 | 0.526 | 0.951 | 0.438 | 0.288 | 0.531 | 1.224 |

| model | RMSE (bps) | R2 out-of-sample vs zero | direction hit rate | DM p (beats zero) |
|---|---|---|---|---|
| Zero / random walk (baseline) | 632.1 | 0.0 |  |  |
| Ridge regression | 652.9 | -0.0668 | 0.469 | 0.965 |
| Gradient boosting | 671.1 | -0.1271 | 0.438 | 0.996 |

Forecast for the next session:

```
  P(up) | Logistic regression      50.1%
  P(up) | Gradient boosting        76.9%
  P(up) | historical base rate     52.0%
  expected return (ridge)          +0.83%
  80% range low                    -5.73%
  80% range high                   +7.85%
  daily volatility                 +5.25%
```

Best out-of-sample AUC **0.484**: no reliable edge: treat the forecast as close to a coin flip.

![ALAB feature effects](forecast_ALAB.png)

## 5. Stock screen and entry plans

| ticker | rank | score | passes_filters | close | momentum_12_1 | momentum_6m | volatility | off_52w_high | forward_pe | pullback_entry | breakout_trigger | stop | stop_% | shares | position_$ | max_loss_$ | filter_notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LLY | 1 | +0.73 | True | 1263.19 | +40.9% | +40.2% | +30.9% | -1.3% | 26.6 | 1179.07 | 1265.72 | 1106.87 | -6.1% | 8 | 9433.0 | 578.0 |  |
| XOM | 2 | +0.70 | True | 175.13 | +49.7% | +16.8% | +23.7% | -1.1% | 15.1 | 165.37 | 177.36 | 158.41 | -4.2% | 60 | 9922.0 | 417.0 |  |
| KO | 3 | +0.58 | True | 93.11 | +33.6% | +25.4% | +17.7% | +0.0% | 26.4 | 88.04 | 93.3 | 85.24 | -3.2% | 113 | 9948.0 | 316.0 |  |
| AAPL | 4 | +0.56 | True | 344.73 | +34.7% | +31.1% | +25.8% | +0.0% | 36.0 | 337.19 | 345.41 | 324.09 | -3.9% | 29 | 9779.0 | 380.0 |  |
| ALAB | 5 | +0.56 | True | 290.90 | +66.6% | +70.3% | +92.1% | -39.8% | 45.4 | 266.63 | 390.58 | 218.09 | -18.2% | 20 | 5333.0 | 971.0 |  |
| JNJ | 6 | +0.45 | True | 259.24 | +43.2% | +11.7% | +23.5% | -6.9% | 22.1 | 252.99 | 272.49 | 240.48 | -4.9% | 39 | 9866.0 | 488.0 |  |
| NVDA | 7 | +0.34 | True | 216.84 | +19.1% | +9.6% | +36.4% | -9.4% | 13.6 | 210.83 | 239.72 | 198.81 | -5.7% | 47 | 9909.0 | 565.0 |  |
| V | 8 | +0.32 | True | 396.11 | +7.3% | +26.2% | +18.4% | +0.0% | 26.4 | 372.82 | 396.9 | 359.25 | -3.6% | 26 | 9693.0 | 353.0 |  |
| JPM | 9 | +0.27 | True | 335.25 | +17.1% | +9.2% | +17.1% | -7.7% | 13.2 | 335.13 | 350.99 | 322.46 | -3.8% | 29 | 9719.0 | 368.0 |  |
| GOOGL | 10 | +0.16 | True | 349.71 | +40.1% | +4.2% | +31.9% | -13.0% | 22.9 | 346.89 | 355.68 | 329.49 | -5.0% | 28 | 9713.0 | 487.0 |  |
| MSFT | 11 | +0.13 | True | 535.98 | -3.7% | +28.1% | +37.3% | -1.4% | 22.6 | 518.28 | 544.54 | 495.66 | -4.4% | 19 | 9847.0 | 430.0 |  |
| UNH | 12 | +0.11 | True | 407.83 | +7.0% | +30.4% | +24.1% | -6.0% | 17.6 | 386.11 | 408.65 | 363.22 | -5.9% | 25 | 9653.0 | 572.0 |  |
| PG | 13 | -0.23 | True | 158.40 | +1.5% | +12.4% | +16.4% | -3.8% | 21.4 | 148.83 | 158.72 | 143.69 | -3.5% | 67 | 9972.0 | 344.0 |  |
| AMZN | 14 | -0.31 | True | 252.49 | +13.7% | +1.1% | +39.9% | -11.1% | 24.2 | 246.73 | 262.95 | 235.2 | -4.7% | 40 | 9869.0 | 461.0 |  |
| LIN | 15 | -0.45 | True | 496.58 | +2.0% | +0.1% | +18.9% | -8.9% | 25.4 | 478.03 | 497.57 | 462.57 | -3.2% | 20 | 9561.0 | 309.0 |  |

## 6. Portfolio construction

Assets: KLAC, VRT, ALAB, JPM, XOM, UNH, COST, TLT, GLD. Covariance: Ledoit-Wolf shrinkage on the last 252 trading days.

Weights and share of risk (%):

| asset | weight: Equal weight | weight: Inverse volatility | weight: Risk parity | weight: Minimum variance | risk share: Equal weight | risk share: Inverse volatility | risk share: Risk parity | risk share: Minimum variance |
|---|---|---|---|---|---|---|---|---|
| KLAC | 11.1 | 5.4 | 3.8 | 1.0 | 24.5 | 17.4 | 11.1 | 1.2 |
| VRT | 11.1 | 5.0 | 3.8 | 1.4 | 24.8 | 15.9 | 11.1 | 1.7 |
| ALAB | 11.1 | 3.4 | 3.1 | 1.6 | 37.6 | 13.2 | 11.1 | 1.9 |
| JPM | 11.1 | 13.8 | 11.2 | 15.0 | 4.2 | 13.5 | 11.1 | 18.0 |
| XOM | 11.1 | 12.0 | 17.1 | 18.5 | -1.0 | 1.7 | 11.1 | 22.2 |
| UNH | 11.1 | 9.2 | 8.5 | 4.1 | 3.3 | 10.0 | 11.1 | 5.0 |
| COST | 11.1 | 15.1 | 17.6 | 21.5 | -0.9 | 4.8 | 11.1 | 25.8 |
| TLT | 11.1 | 25.2 | 26.5 | 30.0 | 0.9 | 9.2 | 11.1 | 16.0 |
| GLD | 11.1 | 10.7 | 8.3 | 6.9 | 6.7 | 14.4 | 11.1 | 8.2 |

| method | expected volatility | diversification ratio | effective number of bets | largest risk share | largest risk holder |
|---|---|---|---|---|---|
| Equal weight | 21.5% | 1.91 | 3.70 | 37.6% | ALAB |
| Inverse volatility | 11.9% | 2.47 | 7.53 | 17.4% | KLAC |
| Risk parity | 10.4% | 2.66 | 9.00 | 11.1% | TLT |
| Minimum variance | 9.2% | 2.56 | 5.43 | 25.8% | COST |

Out-of-sample comparison, monthly rebalance (2025-03-25 to 2026-10-15; limited by the asset with the shortest history):

| method | CAGR | Volatility | Sharpe | Max drawdown |
|---|---|---|---|---|
| Equal weight | +45.6% | +22.3% | 1.80 | -13.7% |
| Inverse volatility | +27.9% | +13.5% | 1.89 | -7.2% |
| Risk parity | +24.3% | +12.1% | 1.86 | -6.7% |
| Minimum variance | +15.2% | +10.1% | 1.45 | -6.0% |

![Correlations](portfolio_correlation.png)

![Risk shares](portfolio_risk_shares.png)

![Walk-forward](portfolio_walk_forward.png)
