# After-hours board, 19:59 ET on 2026-11-25

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest trade standing in for today's close; the history before it is daily closes. The volume rules keep their value from the last close, so a label changes only when the price move switches a price-based rule (the last column says which).

| ticker | label now | board at close | close | latest | change | pullback entry | breakout | stop | session | what the move changes |
|---|---|---|---|---|---|---|---|---|---|---|
| IBM | WATCH | WATCH | 243.47 | 243.88 | +0.2% | 242.22 | 257.02 | 227.03 | after-hours |  |
| DELL | REDUCE | REDUCE | 297.06 | 302.98 | +2.0% |  |  |  | after-hours |  |
| AMZN | REDUCE | REDUCE | 244.43 | 246.77 | +1.0% |  |  |  | after-hours | now above 200-day average (245.78) |
| MRVL | REDUCE | REDUCE | 130.93 | 133.61 | +2.0% |  |  |  | after-hours |  |
| SPCX | REDUCE* | REDUCE* | 127.44 | 128.96 | +1.2% |  |  |  | after-hours |  |
| TSLA | REDUCE | REDUCE | 380.14 | 383.23 | +0.8% |  |  |  | after-hours | now above 200-day average (381.15) |
| BE | REDUCE | REDUCE | 152.89 | 157.71 | +3.2% |  |  |  | after-hours |  |
| ALAB | REDUCE | REDUCE | 190.34 | 196.50 | +3.2% |  |  |  | after-hours |  |
| AMD | SELL | SELL | 406.03 | 413.81 | +1.9% |  |  |  | after-hours |  |
| TSM | SELL | SELL | 342.34 | 347.20 | +1.4% |  |  |  | after-hours |  |
| ETN | SELL | SELL | 317.81 | 320.57 | +0.9% |  |  |  | after-hours |  |
| GEV | SELL | SELL | 715.00 | 721.00 | +0.8% |  |  |  | after-hours |  |
| GOOG | SELL | SELL | 270.98 | 272.80 | +0.7% |  |  |  | after-hours |  |
| CEG | SELL | SELL | 235.28 | 237.74 | +1.0% |  |  |  | after-hours |  |
| NVDA | SELL | SELL | 149.30 | 151.22 | +1.3% |  |  |  | after-hours |  |
| VST | SELL | SELL | 121.32 | 122.50 | +1.0% |  |  |  | after-hours |  |
| SKHY | SELL* | SELL* | 111.14 | 113.95 | +2.5% |  |  |  | after-hours |  |
| FSLR | SELL | SELL | 147.88 | 149.03 | +0.8% |  |  |  | after-hours |  |

## Does deciding before the open help?

From 2022-02-23 to 2026-11-24 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +39.2% a year (worst drawdown -37.7%) against +32.3% (-44.6%) for labels set at the previous close; the two agreed on 89% of stock-weeks. Sharpe ratio difference +0.16 (95% block-bootstrap CI [-0.04, +0.36]): deciding before the open has been **not distinguishable from deciding on the previous close**. *Stability: same verdict in 10 of the last 10 runs.*

## Do opening gaps carry into the day?

Across 19,074 stock-days (18 watchlist stocks, 2021-11-29 to 2026-11-25), each 1% of opening gap went with a -0.03% move from the open to the close (95% block-bootstrap CI [-0.09%, +0.02%]): no reliable relationship, so the size of a gap has not told you which way the session goes. *Stability: same verdict in 10 of the last 10 runs.*

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 811 | -5.2% | +0.31% | 50% |
| down 1-3% | 2923 | -1.7% | +0.06% | 52% |
| within 1% | 10993 | +0.0% | +0.01% | 50% |
| up 1-3% | 3393 | +1.7% | +0.07% | 51% |
| gap up 3%+ | 954 | +5.6% | -0.21% | 46% |
