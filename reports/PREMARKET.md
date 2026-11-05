# Pre-market board, 15:18 ET on 2026-11-05

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest pre-market trade standing in for today's close; the history before it is daily closes. The volume rules keep their value from the last close, so a label changes only when the price move switches a price-based rule (the last column says which).

| ticker | pre-market label | board at close | close | pre-market | change | pullback entry | breakout | stop | session | what the move changes |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | BUY | BUY | 266.03 | 259.43 | -2.5% | 254.40 | 266.56 | 237.53 | regular session |  |
| TSLA | SELL (changed) | WATCH | 385.19 | 342.39 | -11.1% |  |  |  | regular session | now below 50-day average (372.11); now below 200-day average (384.76); now below chandelier stop (371.96); now below board stop (355.03); rule now on: MACD bearish |
| AMD | REDUCE | REDUCE | 488.78 | 415.56 | -15.0% |  |  |  | regular session |  |
| NVDA | REDUCE | REDUCE | 200.13 | 182.98 | -8.6% |  |  |  | regular session | now below 80% of the 52-week high (191.39) |
| SKHY | SELL* (changed) | REDUCE* | 143.07 | 127.11 | -11.2% |  |  |  | regular session | rule now on: MACD bearish |
| FSLR | REDUCE | REDUCE | 194.51 | 196.89 | +1.2% |  |  |  | regular session |  |
| MRVL | SELL | SELL | 159.80 | 137.01 | -14.3% |  |  |  | regular session |  |
| ALAB | SELL | SELL | 223.27 | 185.83 | -16.8% |  |  |  | regular session |  |
| ETN | SELL | SELL | 353.08 | 330.26 | -6.5% |  |  |  | regular session |  |
| GOOG | SELL | SELL | 287.30 | 283.56 | -1.3% |  |  |  | regular session |  |
| SPCX | SELL* | SELL* | 135.92 | 125.26 | -7.8% |  |  |  | regular session |  |

## Does deciding before the open help?

From 2022-02-02 to 2026-11-03 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +39.1% a year (worst drawdown -30.6%) against +43.1% (-30.6%) for labels set at the previous close; the two agreed on 89% of stock-weeks. Sharpe ratio difference -0.10 (95% block-bootstrap CI [-0.38, +0.14]): deciding before the open has been **not distinguishable from deciding on the previous close**. *Stability: same verdict in 2 of the last 2 runs.*

## Do opening gaps carry into the day?

Across 10,865 stock-days (11 watchlist stocks, 2021-11-08 to 2026-11-04), each 1% of opening gap went with a -0.03% move from the open to the close (95% block-bootstrap CI [-0.08%, +0.03%]): no reliable relationship, so the size of a gap has not told you which way the session goes. *Stability: same verdict in 2 of the last 2 runs.*

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 458 | -5.2% | +0.31% | 49% |
| down 1-3% | 1811 | -1.7% | +0.04% | 52% |
| within 1% | 6032 | +0.0% | +0.01% | 50% |
| up 1-3% | 2033 | +1.7% | +0.08% | 52% |
| gap up 3%+ | 531 | +5.4% | -0.26% | 46% |
