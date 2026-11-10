# Pre-market board, 06:48 ET on 2026-11-10

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest trade standing in for today's close; the history before it is daily closes. The volume rules keep their value from the last close, so a label changes only when the price move switches a price-based rule (the last column says which).

| ticker | label now | board at close | close | latest | change | pullback entry | breakout | stop | session | what the move changes |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | BUY | BUY | 266.93 | 267.82 | +0.3% | 255.11 | 268.36 | 237.01 | pre-market | now above breakout level (267.46) |
| IBM | REDUCE (changed) | WATCH | 246.11 | 245.50 | -0.2% |  |  |  | pre-market | now below 200-day average (245.77) |
| DELL | REDUCE | REDUCE | 346.31 | 345.85 | -0.1% |  |  |  | pre-market |  |
| AMD | WATCH (changed) | REDUCE | 508.58 | 504.80 | -0.7% | 468.58 | 579.60 | 396.13 | pre-market | rule now off: below chandelier stop |
| ALAB | REDUCE | REDUCE | 216.87 | 215.00 | -0.9% |  |  |  | pre-market |  |
| SPCX | SELL* (changed) | REDUCE* | 142.07 | 141.02 | -0.7% |  |  |  | pre-market | now below chandelier stop (142.01) |
| CEG | REDUCE | REDUCE | 276.09 | 274.92 | -0.4% |  |  |  | pre-market |  |
| TSLA | REDUCE | REDUCE | 378.05 | 375.78 | -0.6% |  |  |  | pre-market |  |
| BE | REDUCE | REDUCE | 193.88 | 191.11 | -1.4% |  |  |  | pre-market |  |
| FSLR | REDUCE | REDUCE | 191.61 | 190.61 | -0.5% |  |  |  | pre-market |  |
| MRVL | SELL | SELL | 154.60 | 152.16 | -1.6% |  |  |  | pre-market |  |
| TSM | REDUCE (changed) | SELL | 388.62 | 389.96 | +0.3% |  |  |  | pre-market | now above 80% of the 52-week high (388.64) |
| NVDA | SELL | SELL | 178.67 | 179.04 | +0.2% |  |  |  | pre-market |  |
| ETN | SELL | SELL | 359.30 | 359.80 | +0.1% |  |  |  | pre-market |  |
| GEV | SELL | SELL | 829.34 | 814.60 | -1.8% |  |  |  | pre-market |  |
| GOOG | SELL | SELL | 286.01 | 288.15 | +0.7% |  |  |  | pre-market |  |
| SKHY | SELL* | SELL* | 134.38 | 132.20 | -1.6% |  |  |  | pre-market |  |
| VST | SELL | SELL | 133.92 | 133.00 | -0.7% |  |  |  | pre-market |  |

## Does deciding before the open help?

From 2022-02-07 to 2026-11-06 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +33.1% a year (worst drawdown -41.1%) against +32.2% (-42.1%) for labels set at the previous close; the two agreed on 89% of stock-weeks. Sharpe ratio difference +0.03 (95% block-bootstrap CI [-0.12, +0.18]): deciding before the open has been **not distinguishable from deciding on the previous close**. *Stability: same verdict in 5 of the last 5 runs.*

## Do opening gaps carry into the day?

Across 19,001 stock-days (18 watchlist stocks, 2021-11-11 to 2026-11-09), each 1% of opening gap went with a -0.02% move from the open to the close (95% block-bootstrap CI [-0.08%, +0.03%]): no reliable relationship, so the size of a gap has not told you which way the session goes. *Stability: same verdict in 5 of the last 5 runs.*

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 768 | -5.2% | +0.30% | 50% |
| down 1-3% | 2896 | -1.7% | +0.09% | 52% |
| within 1% | 11046 | +0.0% | +0.02% | 50% |
| up 1-3% | 3367 | +1.7% | +0.09% | 52% |
| gap up 3%+ | 924 | +5.4% | -0.14% | 47% |
