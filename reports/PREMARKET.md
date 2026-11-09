# Pre-market board, 05:32 ET on 2026-11-09

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest trade standing in for today's close; the history before it is daily closes. The volume rules keep their value from the last close, so a label changes only when the price move switches a price-based rule (the last column says which).

| ticker | label now | board at close | close | latest | change | pullback entry | breakout | stop | session | what the move changes |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | BUY | BUY | 259.30 | 261.67 | +0.9% | 254.39 | 266.56 | 236.98 | pre-market |  |
| FSLR | AVOID | AVOID | 201.14 | 198.38 | -1.4% |  |  |  | pre-market |  |
| AMD | REDUCE | REDUCE | 449.04 | 460.80 | +2.6% |  |  |  | pre-market |  |
| NVDA | REDUCE | REDUCE | 186.64 | 178.23 | -4.5% |  |  |  | pre-market |  |
| IBM | WATCH (changed) | REDUCE | 245.00 | 247.00 | +0.8% | 246.47 | 258.80 | 232.28 | pre-market | now above 200-day average (245.97) |
| ALAB | REDUCE | REDUCE | 190.71 | 194.97 | +2.2% |  |  |  | pre-market |  |
| MRVL | SELL | SELL | 141.20 | 139.88 | -0.9% |  |  |  | pre-market |  |
| ETN | SELL | SELL | 341.72 | 343.00 | +0.4% |  |  |  | pre-market |  |
| GEV | SELL | SELL | 774.11 | 780.01 | +0.8% |  |  |  | pre-market |  |
| GOOG | SELL | SELL | 283.93 | 286.73 | +1.0% |  |  |  | pre-market |  |
| SPCX | SELL* | SELL* | 134.27 | 135.61 | +1.0% |  |  |  | pre-market |  |
| TSLA | SELL | SELL | 358.22 | 359.65 | +0.4% |  |  |  | pre-market |  |
| CEG | SELL | SELL | 249.95 | 251.20 | +0.5% |  |  |  | pre-market |  |
| VST | SELL | SELL | 124.80 | 125.50 | +0.6% |  |  |  | pre-market |  |
| SKHY | SELL* | SELL* | 127.34 | 124.40 | -2.3% |  |  |  | pre-market |  |

## Does deciding before the open help?

From 2022-02-03 to 2026-11-05 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +41.7% a year (worst drawdown -31.8%) against +38.5% (-30.5%) for labels set at the previous close; the two agreed on 90% of stock-weeks. Sharpe ratio difference +0.06 (95% block-bootstrap CI [-0.10, +0.22]): deciding before the open has been **not distinguishable from deciding on the previous close**. *Stability: same verdict in 4 of the last 4 runs.*

## Do opening gaps carry into the day?

Across 15,248 stock-days (15 watchlist stocks, 2021-11-09 to 2026-11-06), each 1% of opening gap went with a -0.03% move from the open to the close (95% block-bootstrap CI [-0.09%, +0.03%]): no reliable relationship, so the size of a gap has not told you which way the session goes. *Stability: same verdict in 4 of the last 4 runs.*

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 564 | -5.2% | +0.29% | 49% |
| down 1-3% | 2243 | -1.7% | +0.11% | 53% |
| within 1% | 9160 | +0.0% | +0.01% | 50% |
| up 1-3% | 2611 | +1.7% | +0.08% | 51% |
| gap up 3%+ | 670 | +5.3% | -0.23% | 46% |
