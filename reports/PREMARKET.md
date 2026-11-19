# After-hours board, 17:06 ET on 2026-11-19

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest trade standing in for today's close; the history before it is daily closes. The volume rules keep their value from the last close, so a label changes only when the price move switches a price-based rule (the last column says which).

| ticker | label now | board at close | close | latest | change | pullback entry | breakout | stop | session | what the move changes |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | BUY | BUY | 257.37 | 257.28 | -0.0% | 255.23 | 271.41 | 236.01 | after-hours |  |
| AMD | WATCH | WATCH | 489.19 | 481.58 | -1.6% | 445.71 | 586.47 | 358.74 | after-hours |  |
| DELL | REDUCE | REDUCE | 312.54 | 310.80 | -0.6% |  |  |  | after-hours |  |
| SPCX | REDUCE* | REDUCE* | 138.43 | 137.46 | -0.7% |  |  |  | after-hours |  |
| TSLA | REDUCE | REDUCE | 374.41 | 373.25 | -0.3% |  |  |  | after-hours |  |
| CEG | REDUCE | REDUCE | 252.03 | 251.47 | -0.2% |  |  |  | after-hours |  |
| ALAB | REDUCE | REDUCE | 211.60 | 210.26 | -0.6% |  |  |  | after-hours |  |
| BE | REDUCE | REDUCE | 168.11 | 167.50 | -0.4% |  |  |  | after-hours |  |
| MRVL | SELL | SELL | 138.47 | 139.02 | +0.4% |  |  |  | after-hours |  |
| TSM | SELL | SELL | 352.09 | 350.86 | -0.3% |  |  |  | after-hours |  |
| ETN | SELL | SELL | 330.57 | 328.70 | -0.6% |  |  |  | after-hours |  |
| IBM | SELL | SELL | 223.88 | 223.06 | -0.4% |  |  |  | after-hours |  |
| GEV | SELL | SELL | 756.28 | 752.92 | -0.4% |  |  |  | after-hours |  |
| GOOG | SELL | SELL | 271.02 | 272.50 | +0.5% |  |  |  | after-hours |  |
| NVDA | SELL | SELL | 145.98 | 146.28 | +0.2% |  |  |  | after-hours |  |
| VST | SELL | SELL | 124.15 | 122.23 | -1.5% |  |  |  | after-hours |  |
| SKHY | SELL* | SELL* | 119.20 | 119.56 | +0.3% |  |  |  | after-hours |  |
| FSLR | SELL | SELL | 151.95 | 151.95 | +0.0% |  |  |  | after-hours |  |

## Does deciding before the open help?

From 2022-02-16 to 2026-11-17 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +43.5% a year (worst drawdown -33.1%) against +40.4% (-39.4%) for labels set at the previous close; the two agreed on 89% of stock-weeks. Sharpe ratio difference +0.05 (95% block-bootstrap CI [-0.12, +0.26]): deciding before the open has been **not distinguishable from deciding on the previous close**. *Stability: same verdict in 10 of the last 10 runs.*

## Do opening gaps carry into the day?

Across 19,041 stock-days (18 watchlist stocks, 2021-11-23 to 2026-11-19), each 1% of opening gap went with a -0.03% move from the open to the close (95% block-bootstrap CI [-0.09%, +0.02%]): no reliable relationship, so the size of a gap has not told you which way the session goes. *Stability: same verdict in 10 of the last 10 runs.*

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 785 | -5.2% | +0.33% | 50% |
| down 1-3% | 2919 | -1.7% | +0.08% | 52% |
| within 1% | 11007 | +0.0% | +0.01% | 50% |
| up 1-3% | 3393 | +1.7% | +0.07% | 51% |
| gap up 3%+ | 937 | +5.4% | -0.17% | 47% |
