# After-hours board, 18:01 ET on 2026-11-25

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest trade standing in for today's close; the history before it is daily closes. The volume rules keep their value from the last close, so a label changes only when the price move switches a price-based rule (the last column says which).

| ticker | label now | board at close | close | latest | change | pullback entry | breakout | stop | session | what the move changes |
|---|---|---|---|---|---|---|---|---|---|---|
| IBM | WATCH | WATCH | 243.47 | 244.12 | +0.3% | 242.22 | 257.02 | 227.06 | after-hours |  |
| DELL | REDUCE | REDUCE | 297.06 | 294.00 | -1.0% |  |  |  | after-hours |  |
| AMZN | REDUCE | REDUCE | 244.43 | 245.00 | +0.2% |  |  |  | after-hours |  |
| MRVL | REDUCE | REDUCE | 130.93 | 129.81 | -0.9% |  |  |  | after-hours |  |
| SPCX | REDUCE* | REDUCE* | 127.44 | 127.33 | -0.1% |  |  |  | after-hours |  |
| TSLA | REDUCE | REDUCE | 380.14 | 379.62 | -0.1% |  |  |  | after-hours |  |
| BE | REDUCE | REDUCE | 152.89 | 153.50 | +0.4% |  |  |  | after-hours |  |
| ALAB | REDUCE | REDUCE | 190.34 | 192.31 | +1.0% |  |  |  | after-hours |  |
| AMD | SELL | SELL | 406.03 | 405.74 | -0.1% |  |  |  | after-hours |  |
| TSM | SELL | SELL | 342.34 | 342.26 | -0.0% |  |  |  | after-hours |  |
| ETN | SELL | SELL | 317.81 | 317.11 | -0.2% |  |  |  | after-hours |  |
| GEV | SELL | SELL | 715.00 | 717.50 | +0.3% |  |  |  | after-hours |  |
| GOOG | SELL | SELL | 270.98 | 270.75 | -0.1% |  |  |  | after-hours |  |
| CEG | SELL | SELL | 235.28 | 236.00 | +0.3% |  |  |  | after-hours |  |
| NVDA | SELL | SELL | 149.30 | 149.54 | +0.2% |  |  |  | after-hours |  |
| VST | SELL | SELL | 121.32 | 121.70 | +0.3% |  |  |  | after-hours |  |
| SKHY | SELL* | SELL* | 111.14 | 110.94 | -0.2% |  |  |  | after-hours |  |
| FSLR | SELL | SELL | 147.88 | 148.30 | +0.3% |  |  |  | after-hours |  |

## Does deciding before the open help?

From 2022-02-23 to 2026-11-23 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +41.3% a year (worst drawdown -37.0%) against +34.3% (-40.6%) for labels set at the previous close; the two agreed on 89% of stock-weeks. Sharpe ratio difference +0.16 (95% block-bootstrap CI [-0.04, +0.36]): deciding before the open has been **not distinguishable from deciding on the previous close**. *Stability: same verdict in 10 of the last 10 runs.*

## Do opening gaps carry into the day?

Across 19,074 stock-days (18 watchlist stocks, 2021-11-29 to 2026-11-25), each 1% of opening gap went with a -0.03% move from the open to the close (95% block-bootstrap CI [-0.09%, +0.02%]): no reliable relationship, so the size of a gap has not told you which way the session goes. *Stability: same verdict in 10 of the last 10 runs.*

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 811 | -5.2% | +0.31% | 50% |
| down 1-3% | 2923 | -1.7% | +0.06% | 52% |
| within 1% | 10993 | +0.0% | +0.01% | 50% |
| up 1-3% | 3393 | +1.7% | +0.07% | 51% |
| gap up 3%+ | 954 | +5.6% | -0.21% | 46% |
