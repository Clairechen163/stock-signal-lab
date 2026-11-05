# Pre-market board, 05:02 ET on 2026-11-05

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest pre-market trade standing in for today's close; the history before it is daily closes. The volume rules can't fire on a pre-market price.

| ticker | pre-market label | board at close | close | pre-market | change | pullback entry | breakout | stop | session | crosses |
|---|---|---|---|---|---|---|---|---|---|---|
| TSLA | REDUCE (changed) | WATCH | 385.19 | 377.70 | -1.9% |  |  |  | pre-market | now below 200-day average (384.76) |
| AMD | REDUCE | REDUCE | 488.78 | 475.56 | -2.7% |  |  |  | pre-market |  |
| NVDA | REDUCE | REDUCE | 200.13 | 199.20 | -0.5% |  |  |  | pre-market |  |
| SKHY | REDUCE* | REDUCE* | 143.07 | 137.46 | -3.9% |  |  |  | pre-market |  |
| FSLR | AVOID (changed) | REDUCE | 194.51 | 198.76 | +2.2% |  |  |  | pre-market |  |
| MRVL | REDUCE (changed) | SELL | 159.80 | 156.20 | -2.3% |  |  |  | pre-market |  |
| ALAB | REDUCE (changed) | SELL | 223.27 | 217.00 | -2.8% |  |  |  | pre-market |  |
| ETN | SELL | SELL | 353.08 | 348.20 | -1.4% |  |  |  | pre-market |  |
| GOOG | SELL | SELL | 287.30 | 289.15 | +0.6% |  |  |  | pre-market |  |
| SPCX | SELL* | SELL* | 135.92 | 134.23 | -1.2% |  |  |  | pre-market |  |

## Does deciding before the open help?

From 2022-02-02 to 2026-11-03 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +38.5% a year (worst drawdown -38.1%) against +45.6% (-30.5%) for labels set at the previous close; the two agreed on 87% of stock-weeks. Sharpe ratio difference -0.15 (95% block-bootstrap CI [-0.50, +0.12]): deciding before the open has been **not distinguishable from deciding on the previous close**.

## Do opening gaps carry into the day?

Across 9,612 stock-days (10 watchlist stocks, 2021-11-08 to 2026-11-04), each 1% of opening gap went with a -0.02% move from the open to the close (95% block-bootstrap CI [-0.08%, +0.03%]): no reliable relationship, so the size of a gap has not told you which way the session goes.

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 431 | -5.2% | +0.26% | 49% |
| down 1-3% | 1651 | -1.7% | +0.04% | 53% |
| within 1% | 5170 | +0.0% | +0.02% | 50% |
| up 1-3% | 1857 | +1.7% | +0.09% | 52% |
| gap up 3%+ | 503 | +5.3% | -0.25% | 46% |
