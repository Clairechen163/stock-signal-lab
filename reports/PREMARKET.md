# Intraday board, 14:53 ET on 2026-11-11

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest trade standing in for today's close; the history before it is daily closes. The volume rules keep their value from the last close, so a label changes only when the price move switches a price-based rule (the last column says which).

| ticker | label now | board at close | close | latest | change | pullback entry | breakout | stop | session | what the move changes |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | BUY | BUY | 270.87 | 266.52 | -1.6% | 255.88 | 271.41 | 237.68 | regular session |  |
| AMD | BUY (changed) | WATCH | 515.21 | 559.33 | +8.6% | 550.56 | 579.60 | 471.62 | regular session | now above 50-day average (548.56); now above 80% of the 52-week high (519.54); rule now off: MACD bearish |
| IBM | WATCH | WATCH | 244.53 | 248.31 | +1.5% | 246.60 | 257.02 | 233.25 | regular session |  |
| TSM | WATCH (changed) | REDUCE | 396.48 | 414.43 | +4.5% | 410.44 | 440.39 | 376.84 | regular session | now above 200-day average (400.64); now above chandelier stop (404.27) |
| SPCX | SELL* (changed) | REDUCE* | 143.09 | 140.80 | -1.6% |  |  |  | regular session | now below chandelier stop (142.25) |
| ALAB | REDUCE | REDUCE | 216.18 | 232.68 | +7.6% |  |  |  | regular session |  |
| TSLA | WATCH (changed) | REDUCE | 379.78 | 391.59 | +3.1% | 381.87 | 408.27 | 349.20 | regular session | now above 200-day average (383.23) |
| CEG | REDUCE | REDUCE | 267.76 | 275.34 | +2.8% |  |  |  | regular session | now above 50-day average (269.87) |
| BE | AVOID (changed) | REDUCE | 185.42 | 212.43 | +14.6% |  |  |  | regular session | now above chandelier stop (212.07); rule now off: MACD bearish |
| DELL | REDUCE (changed) | SELL | 334.38 | 377.53 | +12.9% |  |  |  | regular session | now above 200-day average (338.91) |
| MRVL | SELL | SELL | 154.39 | 170.43 | +10.4% |  |  |  | regular session |  |
| ETN | SELL | SELL | 354.22 | 362.92 | +2.5% |  |  |  | regular session |  |
| NVDA | SELL | SELL | 168.89 | 175.74 | +4.1% |  |  |  | regular session |  |
| GOOG | SELL | SELL | 284.92 | 291.80 | +2.4% |  |  |  | regular session |  |
| GEV | SELL | SELL | 797.04 | 813.01 | +2.0% |  |  |  | regular session |  |
| VST | SELL | SELL | 131.18 | 134.87 | +2.8% |  |  |  | regular session |  |
| SKHY | REDUCE* (changed) | SELL* | 129.66 | 143.40 | +10.6% |  |  |  | regular session | now above chandelier stop (136.27) |
| FSLR | SELL | SELL | 180.98 | 179.18 | -1.0% |  |  |  | regular session |  |

## Does deciding before the open help?

From 2022-02-08 to 2026-11-09 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +41.3% a year (worst drawdown -37.0%) against +36.8% (-40.5%) for labels set at the previous close; the two agreed on 89% of stock-weeks. Sharpe ratio difference +0.10 (95% block-bootstrap CI [-0.15, +0.34]): deciding before the open has been **not distinguishable from deciding on the previous close**. *Stability: same verdict in 6 of the last 6 runs.*

## Do opening gaps carry into the day?

Across 19,006 stock-days (18 watchlist stocks, 2021-11-12 to 2026-11-10), each 1% of opening gap went with a -0.02% move from the open to the close (95% block-bootstrap CI [-0.08%, +0.03%]): no reliable relationship, so the size of a gap has not told you which way the session goes. *Stability: same verdict in 6 of the last 6 runs.*

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 770 | -5.2% | +0.30% | 50% |
| down 1-3% | 2907 | -1.7% | +0.09% | 52% |
| within 1% | 11041 | +0.0% | +0.02% | 50% |
| up 1-3% | 3366 | +1.7% | +0.09% | 52% |
| gap up 3%+ | 922 | +5.4% | -0.13% | 47% |
