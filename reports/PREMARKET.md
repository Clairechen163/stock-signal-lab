# Pre-market board, 06:07 ET on 2026-11-05

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest pre-market trade standing in for today's close; the history before it is daily closes. The volume rules can't fire on a pre-market price.

| ticker | pre-market label | board at close | close | pre-market | change | pullback entry | breakout | stop | session | crosses |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | BUY | BUY | 266.03 | 269.50 | +1.3% | 254.90 | 270.04 | 238.48 | pre-market | now above breakout level (266.56) |
| TSLA | REDUCE (changed) | WATCH | 385.19 | 377.07 | -2.1% |  |  |  | pre-market | now below 200-day average (384.76) |
| AMD | REDUCE | REDUCE | 488.78 | 474.75 | -2.9% |  |  |  | pre-market |  |
| NVDA | REDUCE | REDUCE | 200.13 | 198.48 | -0.8% |  |  |  | pre-market |  |
| SKHY | REDUCE* | REDUCE* | 143.07 | 136.10 | -4.9% |  |  |  | pre-market |  |
| FSLR | AVOID (changed) | REDUCE | 194.51 | 200.61 | +3.1% |  |  |  | pre-market |  |
| MRVL | REDUCE (changed) | SELL | 159.80 | 154.60 | -3.3% |  |  |  | pre-market |  |
| ALAB | REDUCE (changed) | SELL | 223.27 | 216.80 | -2.9% |  |  |  | pre-market |  |
| ETN | SELL | SELL | 353.08 | 351.00 | -0.6% |  |  |  | pre-market |  |
| GOOG | SELL | SELL | 287.30 | 289.90 | +0.9% |  |  |  | pre-market |  |
| SPCX | SELL* | SELL* | 135.92 | 133.91 | -1.5% |  |  |  | pre-market |  |

## Does deciding before the open help?

From 2022-02-02 to 2026-11-03 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +37.7% a year (worst drawdown -30.6%) against +43.1% (-30.6%) for labels set at the previous close; the two agreed on 87% of stock-weeks. Sharpe ratio difference -0.13 (95% block-bootstrap CI [-0.41, +0.11]): deciding before the open has been **not distinguishable from deciding on the previous close**.

## Do opening gaps carry into the day?

Across 10,865 stock-days (11 watchlist stocks, 2021-11-08 to 2026-11-04), each 1% of opening gap went with a -0.03% move from the open to the close (95% block-bootstrap CI [-0.08%, +0.03%]): no reliable relationship, so the size of a gap has not told you which way the session goes.

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 458 | -5.2% | +0.31% | 49% |
| down 1-3% | 1811 | -1.7% | +0.04% | 52% |
| within 1% | 6032 | +0.0% | +0.01% | 50% |
| up 1-3% | 2033 | +1.7% | +0.08% | 52% |
| gap up 3%+ | 531 | +5.4% | -0.26% | 46% |
