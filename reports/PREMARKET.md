# After-hours board, 16:51 ET on 2026-11-18

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest trade standing in for today's close; the history before it is daily closes. The volume rules keep their value from the last close, so a label changes only when the price move switches a price-based rule (the last column says which).

| ticker | label now | board at close | close | latest | change | pullback entry | breakout | stop | session | what the move changes |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | BUY | BUY | 530.14 | 524.57 | -1.1% | 514.64 | 586.47 | 433.98 | after-hours |  |
| AMZN | BUY | BUY | 267.74 | 267.50 | -0.1% | 257.13 | 271.41 | 239.09 | after-hours |  |
| TSLA | WATCH | WATCH | 383.72 | 382.25 | -0.4% | 375.81 | 408.27 | 344.54 | after-hours |  |
| SPCX | REDUCE* | REDUCE* | 143.50 | 142.92 | -0.4% |  |  |  | after-hours |  |
| ALAB | REDUCE | REDUCE | 216.75 | 215.26 | -0.7% |  |  |  | after-hours |  |
| CEG | REDUCE | REDUCE | 262.74 | 262.62 | -0.0% |  |  |  | after-hours |  |
| BE | REDUCE | REDUCE | 170.98 | 169.91 | -0.6% |  |  |  | after-hours |  |
| DELL | SELL | SELL | 313.11 | 312.10 | -0.3% |  |  |  | after-hours |  |
| MRVL | SELL | SELL | 145.54 | 144.10 | -1.0% |  |  |  | after-hours |  |
| TSM | SELL | SELL | 362.62 | 361.75 | -0.2% |  |  |  | after-hours |  |
| IBM | SELL | SELL | 228.53 | 228.53 | +0.0% |  |  |  | after-hours |  |
| ETN | SELL | SELL | 338.34 | 339.36 | +0.3% |  |  |  | after-hours |  |
| GOOG | SELL | SELL | 279.20 | 279.10 | -0.0% |  |  |  | after-hours |  |
| GEV | SELL | SELL | 772.22 | 773.10 | +0.1% |  |  |  | after-hours |  |
| NVDA | SELL | SELL | 150.96 | 150.09 | -0.6% |  |  |  | after-hours |  |
| VST | SELL | SELL | 125.58 | 125.01 | -0.5% |  |  |  | after-hours |  |
| SKHY | SELL* | SELL* | 122.47 | 121.65 | -0.7% |  |  |  | after-hours |  |
| FSLR | SELL | SELL | 150.98 | 150.98 | +0.0% |  |  |  | after-hours |  |

## Does deciding before the open help?

From 2022-02-15 to 2026-11-16 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +38.7% a year (worst drawdown -37.0%) against +36.6% (-40.5%) for labels set at the previous close; the two agreed on 89% of stock-weeks. Sharpe ratio difference +0.06 (95% block-bootstrap CI [-0.22, +0.29]): deciding before the open has been **not distinguishable from deciding on the previous close**. *Stability: same verdict in 10 of the last 10 runs.*

## Do opening gaps carry into the day?

Across 19,036 stock-days (18 watchlist stocks, 2021-11-22 to 2026-11-18), each 1% of opening gap went with a -0.03% move from the open to the close (95% block-bootstrap CI [-0.08%, +0.03%]): no reliable relationship, so the size of a gap has not told you which way the session goes. *Stability: same verdict in 10 of the last 10 runs.*

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 785 | -5.2% | +0.33% | 50% |
| down 1-3% | 2919 | -1.7% | +0.08% | 52% |
| within 1% | 11012 | +0.0% | +0.01% | 50% |
| up 1-3% | 3389 | +1.7% | +0.08% | 52% |
| gap up 3%+ | 931 | +5.4% | -0.13% | 47% |
