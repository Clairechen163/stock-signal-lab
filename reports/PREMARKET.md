# After-hours board, 16:39 ET on 2026-11-27

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest trade standing in for today's close; the history before it is daily closes. The volume rules keep their value from the last close, so a label changes only when the price move switches a price-based rule (the last column says which).

| ticker | label now | board at close | close | latest | change | pullback entry | breakout | stop | session | what the move changes |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | WATCH | WATCH | 254.12 | 254.87 | +0.3% | 243.65 | 271.41 | 222.70 | after-hours |  |
| TSLA | WATCH | WATCH | 400.00 | 398.73 | -0.3% | 381.98 | 404.63 | 342.61 | after-hours |  |
| IBM | WATCH | WATCH | 248.08 | 248.83 | +0.3% | 241.80 | 256.55 | 226.91 | after-hours |  |
| AMD | REDUCE | REDUCE | 424.54 | 422.74 | -0.4% |  |  |  | after-hours |  |
| DELL | REDUCE | REDUCE | 316.96 | 314.45 | -0.8% |  |  |  | after-hours |  |
| MRVL | REDUCE | REDUCE | 140.54 | 140.05 | -0.4% |  |  |  | after-hours |  |
| SPCX | REDUCE* | REDUCE* | 133.59 | 132.60 | -0.7% |  |  |  | after-hours |  |
| BE | REDUCE | REDUCE | 163.02 | 162.47 | -0.3% |  |  |  | after-hours |  |
| ALAB | REDUCE | REDUCE | 206.84 | 204.92 | -0.9% |  |  |  | after-hours |  |
| TSM | SELL | SELL | 353.34 | 353.00 | -0.1% |  |  |  | after-hours |  |
| ETN | SELL | SELL | 325.92 | 325.37 | -0.2% |  |  |  | regular session (no trades yet today) |  |
| GEV | SELL | SELL | 735.31 | 733.78 | -0.2% |  |  |  | after-hours |  |
| GOOG | SELL | SELL | 272.44 | 273.53 | +0.4% |  |  |  | after-hours |  |
| CEG | SELL | SELL | 238.10 | 238.70 | +0.3% |  |  |  | regular session (no trades yet today) |  |
| NVDA | SELL | SELL | 150.49 | 149.81 | -0.5% |  |  |  | after-hours |  |
| VST | SELL | SELL | 122.65 | 122.31 | -0.3% |  |  |  | after-hours |  |
| SKHY | SELL* | SELL* | 119.50 | 118.69 | -0.7% |  |  |  | after-hours |  |
| FSLR | SELL | SELL | 149.77 | 149.78 | +0.0% |  |  |  | after-hours |  |

## Does deciding before the open help?

From 2022-02-23 to 2026-11-24 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +39.2% a year (worst drawdown -37.7%) against +32.3% (-44.6%) for labels set at the previous close; the two agreed on 89% of stock-weeks. Sharpe ratio difference +0.16 (95% block-bootstrap CI [-0.04, +0.36]): deciding before the open has been **not distinguishable from deciding on the previous close**. *Stability: same verdict in 10 of the last 10 runs.*

## Do opening gaps carry into the day?

Across 19,079 stock-days (18 watchlist stocks, 2021-11-30 to 2026-11-27), each 1% of opening gap went with a -0.03% move from the open to the close (95% block-bootstrap CI [-0.09%, +0.02%]): no reliable relationship, so the size of a gap has not told you which way the session goes. *Stability: same verdict in 10 of the last 10 runs.*

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 811 | -5.2% | +0.31% | 50% |
| down 1-3% | 2923 | -1.7% | +0.06% | 52% |
| within 1% | 10993 | +0.0% | +0.01% | 50% |
| up 1-3% | 3391 | +1.7% | +0.06% | 51% |
| gap up 3%+ | 961 | +5.6% | -0.20% | 47% |
