# After-hours board, 16:22 ET on 2026-11-17

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest trade standing in for today's close; the history before it is daily closes. The volume rules keep their value from the last close, so a label changes only when the price move switches a price-based rule (the last column says which).

| ticker | label now | board at close | close | latest | change | pullback entry | breakout | stop | session | what the move changes |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | BUY | BUY | 257.89 | 257.39 | -0.2% | 256.86 | 271.41 | 239.03 | after-hours |  |
| AMD | WATCH | WATCH | 503.41 | 507.62 | +0.8% | 462.84 | 586.47 | 381.70 | after-hours |  |
| SPCX | REDUCE* | REDUCE* | 141.70 | 141.90 | +0.1% |  |  |  | after-hours |  |
| TSLA | REDUCE | REDUCE | 380.11 | 380.11 | +0.0% |  |  |  | after-hours |  |
| ALAB | REDUCE | REDUCE | 211.60 | 216.91 | +2.5% |  |  |  | after-hours |  |
| CEG | REDUCE | REDUCE | 268.07 | 268.07 | -0.0% |  |  |  | after-hours |  |
| BE | REDUCE | REDUCE | 173.46 | 175.00 | +0.9% |  |  |  | after-hours |  |
| DELL | SELL | SELL | 322.79 | 325.69 | +0.9% |  |  |  | after-hours |  |
| MRVL | SELL | SELL | 148.74 | 150.51 | +1.2% |  |  |  | after-hours |  |
| TSM | SELL | SELL | 359.69 | 364.00 | +1.2% |  |  |  | after-hours |  |
| IBM | SELL | SELL | 231.09 | 231.25 | +0.1% |  |  |  | after-hours |  |
| ETN | SELL | SELL | 337.11 | 339.47 | +0.7% |  |  |  | after-hours |  |
| GEV | SELL | SELL | 779.91 | 783.52 | +0.5% |  |  |  | after-hours |  |
| GOOG | SELL | SELL | 277.60 | 277.05 | -0.2% |  |  |  | after-hours |  |
| NVDA | SELL | SELL | 155.46 | 158.85 | +2.2% |  |  |  | after-hours |  |
| VST | SELL | SELL | 127.15 | 127.20 | +0.0% |  |  |  | after-hours |  |
| SKHY | SELL* | SELL* | 122.61 | 123.81 | +1.0% |  |  |  | after-hours |  |
| FSLR | SELL | SELL | 152.97 | 153.65 | +0.4% |  |  |  | after-hours |  |

## Does deciding before the open help?

From 2022-02-14 to 2026-11-13 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +33.1% a year (worst drawdown -41.1%) against +35.0% (-42.1%) for labels set at the previous close; the two agreed on 89% of stock-weeks. Sharpe ratio difference -0.03 (95% block-bootstrap CI [-0.16, +0.10]): deciding before the open has been **not distinguishable from deciding on the previous close**. *Stability: same verdict in 10 of the last 10 runs.*

## Do opening gaps carry into the day?

Across 19,031 stock-days (18 watchlist stocks, 2021-11-19 to 2026-11-17), each 1% of opening gap went with a -0.03% move from the open to the close (95% block-bootstrap CI [-0.08%, +0.03%]): no reliable relationship, so the size of a gap has not told you which way the session goes. *Stability: same verdict in 10 of the last 10 runs.*

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 785 | -5.2% | +0.33% | 50% |
| down 1-3% | 2921 | -1.7% | +0.09% | 52% |
| within 1% | 11015 | +0.0% | +0.01% | 50% |
| up 1-3% | 3380 | +1.7% | +0.08% | 52% |
| gap up 3%+ | 930 | +5.4% | -0.12% | 47% |
