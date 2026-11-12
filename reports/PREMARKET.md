# Intraday board, 15:29 ET on 2026-11-12

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest trade standing in for today's close; the history before it is daily closes. The volume rules keep their value from the last close, so a label changes only when the price move switches a price-based rule (the last column says which).

| ticker | label now | board at close | close | latest | change | pullback entry | breakout | stop | session | what the move changes |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | BUY | BUY | 552.90 | 582.81 | +5.4% | 552.94 | 583.98 | 474.27 | regular session | now above breakout level (579.60) |
| AMZN | BUY | BUY | 266.17 | 268.06 | +0.7% | 256.53 | 271.41 | 238.71 | regular session |  |
| TSM | WATCH | WATCH | 413.35 | 405.56 | -1.9% | 389.25 | 440.39 | 356.62 | regular session |  |
| IBM | WATCH | WATCH | 248.22 | 245.16 | -1.2% | 236.25 | 257.02 | 223.07 | regular session |  |
| TSLA | WATCH | WATCH | 390.84 | 398.61 | +2.0% | 383.64 | 408.27 | 351.69 | regular session | now above 80% of the 52-week high (391.90) |
| DELL | REDUCE | REDUCE | 373.68 | 369.17 | -1.2% |  |  |  | regular session |  |
| ALAB | REDUCE | REDUCE | 230.91 | 225.98 | -2.1% |  |  |  | regular session |  |
| NVDA | REDUCE | REDUCE | 173.73 | 164.18 | -5.5% |  |  |  | regular session |  |
| CEG | WATCH (changed) | REDUCE | 274.73 | 281.15 | +2.3% | 269.58 | 281.71 | 243.23 | regular session | now above 200-day average (277.94) |
| SKHY | AVOID* (changed) | REDUCE* | 142.25 | 137.14 | -3.6% |  |  |  | regular session | rule now off: MACD bearish |
| BE | AVOID (changed) | REDUCE | 209.47 | 202.52 | -3.3% |  |  |  | regular session | rule now off: MACD bearish |
| MRVL | SELL | SELL | 168.80 | 164.85 | -2.3% |  |  |  | regular session |  |
| SPCX | REDUCE* (changed) | SELL* | 139.75 | 140.62 | +0.6% |  |  |  | regular session | rule now off: MACD bearish |
| ETN | REDUCE (changed) | SELL | 360.62 | 359.54 | -0.3% |  |  |  | regular session | rule now off: MACD bearish |
| GEV | SELL | SELL | 808.24 | 818.90 | +1.3% |  |  |  | regular session |  |
| GOOG | SELL | SELL | 290.63 | 295.88 | +1.8% |  |  |  | regular session |  |
| VST | SELL | SELL | 133.45 | 134.26 | +0.6% |  |  |  | regular session |  |
| FSLR | SELL | SELL | 178.11 | 172.46 | -3.2% |  |  |  | regular session |  |

## Does deciding before the open help?

From 2022-02-09 to 2026-11-10 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +45.4% a year (worst drawdown -33.1%) against +41.6% (-39.4%) for labels set at the previous close; the two agreed on 89% of stock-weeks. Sharpe ratio difference +0.08 (95% block-bootstrap CI [-0.10, +0.28]): deciding before the open has been **not distinguishable from deciding on the previous close**. *Stability: same verdict in 7 of the last 7 runs.*

## Do opening gaps carry into the day?

Across 19,011 stock-days (18 watchlist stocks, 2021-11-15 to 2026-11-11), each 1% of opening gap went with a -0.02% move from the open to the close (95% block-bootstrap CI [-0.08%, +0.03%]): no reliable relationship, so the size of a gap has not told you which way the session goes. *Stability: same verdict in 7 of the last 7 runs.*

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 770 | -5.2% | +0.30% | 50% |
| down 1-3% | 2905 | -1.7% | +0.09% | 52% |
| within 1% | 11035 | +0.0% | +0.02% | 50% |
| up 1-3% | 3370 | +1.7% | +0.09% | 52% |
| gap up 3%+ | 931 | +5.4% | -0.13% | 47% |
