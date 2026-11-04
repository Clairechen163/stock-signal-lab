# Pre-market board, 15:04 ET on 2026-11-04

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest pre-market trade standing in for today's close; the history before it is daily closes. The volume rules can't fire on a pre-market price.

| ticker | pre-market label | board at close | close | pre-market | change | pullback entry | breakout | stop | session | crosses |
|---|---|---|---|---|---|---|---|---|---|---|
| NVDA | REDUCE (changed) | WATCH | 206.69 | 202.27 | -2.1% |  |  |  | regular session | now below 200-day average (204.27) |
| TSLA | WATCH | WATCH | 398.50 | 387.24 | -2.8% | 383.31 | 408.27 | 356.81 | regular session |  |
| AMD | REDUCE | REDUCE | 483.90 | 482.08 | -0.4% |  |  |  | regular session |  |
| MRVL | REDUCE | REDUCE | 171.97 | 156.00 | -9.3% |  |  |  | regular session |  |
| ETN | SELL (changed) | REDUCE | 391.70 | 352.79 | -9.9% |  |  |  | regular session |  |
| ALAB | REDUCE | REDUCE | 233.62 | 219.77 | -5.9% |  |  |  | regular session |  |
| SKHY | REDUCE* | REDUCE* | 150.79 | 142.49 | -5.5% |  |  |  | regular session |  |
| SPCX | REDUCE* | REDUCE* | 141.31 | 133.88 | -5.3% |  |  |  | regular session |  |
| FSLR | REDUCE | REDUCE | 185.90 | 194.44 | +4.6% |  |  |  | regular session | now above 50-day average (187.62) |
| GOOG | SELL | SELL | 278.27 | 289.82 | +4.2% |  |  |  | regular session |  |

## Does deciding before the open help?

From 2022-02-01 to 2026-11-02 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +27.1% a year (worst drawdown -43.0%) against +25.5% (-40.1%) for labels set at the previous close; the two agreed on 87% of stock-weeks. Sharpe ratio difference +0.04 (95% block-bootstrap CI [-0.17, +0.22]): deciding before the open has been **not distinguishable from deciding on the previous close**.

## Do opening gaps carry into the day?

Across 9,609 stock-days (10 watchlist stocks, 2021-11-05 to 2026-11-03), each 1% of opening gap went with a -0.02% move from the open to the close (95% block-bootstrap CI [-0.08%, +0.04%]): no reliable relationship, so the size of a gap has not told you which way the session goes.

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 426 | -5.2% | +0.28% | 49% |
| down 1-3% | 1650 | -1.7% | +0.04% | 53% |
| within 1% | 5173 | +0.0% | +0.02% | 50% |
| up 1-3% | 1858 | +1.7% | +0.08% | 52% |
| gap up 3%+ | 502 | +5.3% | -0.24% | 46% |
