# Intraday board, 15:52 ET on 2026-11-13

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest trade standing in for today's close; the history before it is daily closes. The volume rules keep their value from the last close, so a label changes only when the price move switches a price-based rule (the last column says which).

| ticker | label now | board at close | close | latest | change | pullback entry | breakout | stop | session | what the move changes |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | WATCH (changed) | BUY | 585.30 | 535.32 | -8.5% | 519.08 | 586.47 | 437.40 | regular session | now below 50-day average (552.99) |
| AMZN | BUY | BUY | 267.44 | 267.12 | -0.1% | 257.36 | 271.41 | 240.03 | regular session |  |
| TSM | AVOID (changed) | WATCH | 405.49 | 400.70 | -1.2% |  |  |  | regular session | now below 200-day average (401.36) |
| IBM | WATCH | WATCH | 244.67 | 247.39 | +1.1% | 236.53 | 257.02 | 223.72 | regular session |  |
| TSLA | WATCH | WATCH | 397.45 | 392.60 | -1.2% | 385.48 | 408.27 | 354.02 | regular session |  |
| CEG | WATCH | WATCH | 282.40 | 280.87 | -0.5% | 269.52 | 282.96 | 243.74 | regular session |  |
| BE | AVOID | AVOID | 201.93 | 192.82 | -4.5% |  |  |  | regular session | now below chandelier stop (193.52) |
| SKHY | REDUCE* (changed) | AVOID* | 137.71 | 132.37 | -3.9% |  |  |  | regular session | now below chandelier stop (135.40) |
| DELL | REDUCE | REDUCE | 371.17 | 345.83 | -6.8% |  |  |  | regular session |  |
| SPCX | REDUCE* | REDUCE* | 139.94 | 140.12 | +0.1% |  |  |  | regular session |  |
| ALAB | REDUCE | REDUCE | 227.79 | 223.55 | -1.9% |  |  |  | regular session |  |
| MRVL | SELL | SELL | 164.45 | 157.70 | -4.1% |  |  |  | regular session |  |
| ETN | REDUCE (changed) | SELL | 359.04 | 352.59 | -1.8% |  |  |  | regular session | rule now off: MACD bearish, below chandelier stop |
| GOOG | SELL | SELL | 295.35 | 292.81 | -0.9% |  |  |  | regular session |  |
| GEV | REDUCE (changed) | SELL | 818.49 | 802.48 | -2.0% |  |  |  | regular session | rule now off: below chandelier stop |
| NVDA | SELL | SELL | 166.19 | 162.79 | -2.0% |  |  |  | regular session |  |
| VST | SELL | SELL | 134.51 | 132.70 | -1.3% |  |  |  | regular session |  |
| FSLR | SELL | SELL | 172.30 | 172.40 | +0.1% |  |  |  | regular session |  |

## Does deciding before the open help?

From 2022-02-10 to 2026-11-11 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +34.8% a year (worst drawdown -34.2%) against +35.1% (-34.1%) for labels set at the previous close; the two agreed on 89% of stock-weeks. Sharpe ratio difference -0.02 (95% block-bootstrap CI [-0.20, +0.18]): deciding before the open has been **not distinguishable from deciding on the previous close**. *Stability: same verdict in 8 of the last 8 runs.*

## Do opening gaps carry into the day?

Across 19,016 stock-days (18 watchlist stocks, 2021-11-16 to 2026-11-12), each 1% of opening gap went with a -0.03% move from the open to the close (95% block-bootstrap CI [-0.08%, +0.03%]): no reliable relationship, so the size of a gap has not told you which way the session goes. *Stability: same verdict in 8 of the last 8 runs.*

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 776 | -5.2% | +0.36% | 50% |
| down 1-3% | 2911 | -1.7% | +0.09% | 52% |
| within 1% | 11027 | +0.0% | +0.02% | 50% |
| up 1-3% | 3371 | +1.7% | +0.09% | 52% |
| gap up 3%+ | 931 | +5.4% | -0.13% | 47% |
