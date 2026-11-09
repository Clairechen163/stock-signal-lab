# After-hours board, 17:44 ET on 2026-11-09

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest trade standing in for today's close; the history before it is daily closes. The volume rules keep their value from the last close, so a label changes only when the price move switches a price-based rule (the last column says which).

| ticker | label now | board at close | close | latest | change | pullback entry | breakout | stop | session | what the move changes |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | BUY | BUY | 266.93 | 268.06 | +0.4% | 254.65 | 267.46 | 235.30 | after-hours | now above breakout level (267.46) |
| IBM | WATCH | WATCH | 246.11 | 246.69 | +0.2% | 236.96 | 258.80 | 222.52 | after-hours |  |
| AMD | REDUCE | REDUCE | 508.58 | 509.74 | +0.2% |  |  |  | after-hours |  |
| ALAB | REDUCE | REDUCE | 216.87 | 218.14 | +0.6% |  |  |  | after-hours |  |
| SPCX | REDUCE* | REDUCE* | 142.07 | 142.20 | +0.1% |  |  |  | after-hours |  |
| CEG | REDUCE | REDUCE | 276.09 | 275.00 | -0.4% |  |  |  | after-hours |  |
| TSLA | REDUCE | REDUCE | 378.05 | 378.63 | +0.2% |  |  |  | after-hours |  |
| FSLR | REDUCE | REDUCE | 191.61 | 191.50 | -0.1% |  |  |  | after-hours |  |
| MRVL | SELL | SELL | 154.60 | 156.48 | +1.2% |  |  |  | after-hours |  |
| NVDA | SELL | SELL | 178.67 | 178.84 | +0.1% |  |  |  | after-hours |  |
| GEV | SELL | SELL | 829.34 | 830.00 | +0.1% |  |  |  | after-hours |  |
| ETN | SELL | SELL | 359.30 | 360.09 | +0.2% |  |  |  | after-hours |  |
| GOOG | SELL | SELL | 286.01 | 288.20 | +0.8% |  |  |  | after-hours |  |
| VST | SELL | SELL | 133.92 | 133.18 | -0.6% |  |  |  | after-hours |  |
| SKHY | SELL* | SELL* | 134.38 | 134.81 | +0.3% |  |  |  | after-hours |  |

## Does deciding before the open help?

From 2022-02-03 to 2026-11-05 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +41.7% a year (worst drawdown -31.8%) against +38.5% (-30.5%) for labels set at the previous close; the two agreed on 90% of stock-weeks. Sharpe ratio difference +0.06 (95% block-bootstrap CI [-0.10, +0.22]): deciding before the open has been **not distinguishable from deciding on the previous close**. *Stability: same verdict in 4 of the last 4 runs.*

## Do opening gaps carry into the day?

Across 15,243 stock-days (15 watchlist stocks, 2021-11-11 to 2026-11-09), each 1% of opening gap went with a -0.02% move from the open to the close (95% block-bootstrap CI [-0.09%, +0.04%]): no reliable relationship, so the size of a gap has not told you which way the session goes. *Stability: same verdict in 4 of the last 4 runs.*

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 563 | -5.2% | +0.30% | 49% |
| down 1-3% | 2241 | -1.7% | +0.11% | 53% |
| within 1% | 9151 | +0.0% | +0.01% | 50% |
| up 1-3% | 2614 | +1.7% | +0.09% | 52% |
| gap up 3%+ | 674 | +5.3% | -0.18% | 46% |
