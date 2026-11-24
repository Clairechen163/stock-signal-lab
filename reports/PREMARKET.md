# After-hours board, 17:47 ET on 2026-11-24

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest trade standing in for today's close; the history before it is daily closes. The volume rules keep their value from the last close, so a label changes only when the price move switches a price-based rule (the last column says which).

| ticker | label now | board at close | close | latest | change | pullback entry | breakout | stop | session | what the move changes |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | WATCH | WATCH | 252.29 | 252.60 | +0.1% | 242.30 | 271.41 | 222.31 | after-hours |  |
| AMD | REDUCE | REDUCE | 413.27 | 416.84 | +0.9% |  |  |  | after-hours |  |
| IBM | REDUCE | REDUCE | 235.62 | 235.21 | -0.2% |  |  |  | after-hours | now below 50-day average (235.50) |
| SPCX | REDUCE* | REDUCE* | 125.81 | 126.71 | +0.7% |  |  |  | after-hours |  |
| TSLA | REDUCE | REDUCE | 384.68 | 385.04 | +0.1% |  |  |  | after-hours |  |
| CEG | REDUCE | REDUCE | 244.84 | 245.44 | +0.2% |  |  |  | after-hours |  |
| BE | REDUCE | REDUCE | 156.41 | 157.73 | +0.8% |  |  |  | after-hours |  |
| ALAB | REDUCE | REDUCE | 191.30 | 193.60 | +1.2% |  |  |  | after-hours |  |
| DELL | SELL | SELL | 295.28 | 307.76 | +4.2% |  |  |  | after-hours |  |
| TSM | SELL | SELL | 349.20 | 352.00 | +0.8% |  |  |  | after-hours |  |
| MRVL | SELL | SELL | 131.57 | 132.54 | +0.7% |  |  |  | after-hours |  |
| ETN | SELL | SELL | 319.27 | 319.69 | +0.1% |  |  |  | after-hours |  |
| GOOG | SELL | SELL | 276.58 | 277.60 | +0.4% |  |  |  | after-hours |  |
| GEV | SELL | SELL | 720.65 | 717.14 | -0.5% |  |  |  | after-hours |  |
| NVDA | SELL | SELL | 155.38 | 154.05 | -0.9% |  |  |  | after-hours |  |
| VST | SELL | SELL | 120.72 | 120.50 | -0.2% |  |  |  | after-hours |  |
| SKHY | SELL* | SELL* | 111.98 | 112.79 | +0.7% |  |  |  | after-hours |  |
| FSLR | SELL | SELL | 148.00 | 148.73 | +0.5% |  |  |  | after-hours |  |

## Does deciding before the open help?

From 2022-02-22 to 2026-11-20 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +32.6% a year (worst drawdown -41.1%) against +35.4% (-42.1%) for labels set at the previous close; the two agreed on 89% of stock-weeks. Sharpe ratio difference -0.05 (95% block-bootstrap CI [-0.18, +0.07]): deciding before the open has been **not distinguishable from deciding on the previous close**. *Stability: same verdict in 10 of the last 10 runs.*

## Do opening gaps carry into the day?

Across 19,056 stock-days (18 watchlist stocks, 2021-11-29 to 2026-11-24), each 1% of opening gap went with a -0.03% move from the open to the close (95% block-bootstrap CI [-0.08%, +0.03%]): no reliable relationship, so the size of a gap has not told you which way the session goes. *Stability: same verdict in 10 of the last 10 runs.*

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 796 | -5.2% | +0.22% | 49% |
| down 1-3% | 2921 | -1.7% | +0.06% | 52% |
| within 1% | 10992 | +0.0% | +0.01% | 50% |
| up 1-3% | 3393 | +1.7% | +0.07% | 51% |
| gap up 3%+ | 954 | +5.6% | -0.21% | 46% |
