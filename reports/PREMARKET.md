# After-hours board, 16:46 ET on 2026-11-20

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest trade standing in for today's close; the history before it is daily closes. The volume rules keep their value from the last close, so a label changes only when the price move switches a price-based rule (the last column says which).

| ticker | label now | board at close | close | latest | change | pullback entry | breakout | stop | session | what the move changes |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | WATCH | WATCH | 246.82 | 248.38 | +0.6% | 236.85 | 271.41 | 216.91 | after-hours |  |
| DELL | SELL | SELL | 278.02 | 283.30 | +1.9% |  |  |  | after-hours |  |
| AMD | SELL | SELL | 424.39 | 431.24 | +1.6% |  |  |  | after-hours | now above 200-day average (429.79) |
| TSM | SELL | SELL | 318.71 | 324.45 | +1.8% |  |  |  | after-hours |  |
| MRVL | SELL | SELL | 122.28 | 124.26 | +1.6% |  |  |  | after-hours |  |
| SPCX | SELL* | SELL* | 127.79 | 128.75 | +0.8% |  |  |  | after-hours |  |
| IBM | SELL | SELL | 224.44 | 224.44 | -0.0% |  |  |  | after-hours |  |
| ETN | SELL | SELL | 311.33 | 314.80 | +1.1% |  |  |  | after-hours |  |
| TSLA | SELL | SELL | 345.82 | 349.26 | +1.0% |  |  |  | after-hours |  |
| GOOG | SELL | SELL | 264.00 | 267.07 | +1.2% |  |  |  | after-hours |  |
| GEV | SELL | SELL | 699.33 | 709.00 | +1.4% |  |  |  | after-hours |  |
| CEG | SELL | SELL | 237.41 | 237.41 | -0.0% |  |  |  | after-hours |  |
| NVDA | SELL | SELL | 125.53 | 128.16 | +2.1% |  |  |  | after-hours |  |
| VST | SELL | SELL | 115.25 | 118.00 | +2.4% |  |  |  | after-hours |  |
| ALAB | SELL | SELL | 180.35 | 185.80 | +3.0% |  |  |  | after-hours |  |
| BE | SELL | SELL | 142.39 | 144.95 | +1.8% |  |  |  | after-hours |  |
| SKHY | SELL* | SELL* | 103.57 | 105.00 | +1.4% |  |  |  | after-hours |  |
| FSLR | SELL | SELL | 137.59 | 139.81 | +1.6% |  |  |  | after-hours |  |

## Does deciding before the open help?

From 2022-02-17 to 2026-11-18 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +38.3% a year (worst drawdown -35.5%) against +36.5% (-34.9%) for labels set at the previous close; the two agreed on 89% of stock-weeks. Sharpe ratio difference +0.03 (95% block-bootstrap CI [-0.12, +0.20]): deciding before the open has been **not distinguishable from deciding on the previous close**. *Stability: same verdict in 10 of the last 10 runs.*

## Do opening gaps carry into the day?

Across 19,059 stock-days (18 watchlist stocks, 2021-11-23 to 2026-11-20), each 1% of opening gap went with a -0.03% move from the open to the close (95% block-bootstrap CI [-0.08%, +0.03%]): no reliable relationship, so the size of a gap has not told you which way the session goes. *Stability: same verdict in 10 of the last 10 runs.*

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 791 | -5.2% | +0.27% | 50% |
| down 1-3% | 2928 | -1.7% | +0.06% | 52% |
| within 1% | 11010 | +0.0% | +0.01% | 50% |
| up 1-3% | 3393 | +1.7% | +0.07% | 51% |
| gap up 3%+ | 937 | +5.4% | -0.17% | 47% |
