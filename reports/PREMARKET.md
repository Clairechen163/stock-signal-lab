# Intraday board, 15:02 ET on 2026-11-10

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest trade standing in for today's close; the history before it is daily closes. The volume rules keep their value from the last close, so a label changes only when the price move switches a price-based rule (the last column says which).

| ticker | label now | board at close | close | latest | change | pullback entry | breakout | stop | session | what the move changes |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | BUY | BUY | 266.93 | 271.52 | +1.7% | 255.30 | 272.06 | 236.67 | regular session | now above breakout level (267.46) |
| IBM | REDUCE (changed) | WATCH | 246.11 | 244.10 | -0.8% |  |  |  | regular session | now below 200-day average (245.77) |
| DELL | SELL (changed) | REDUCE | 346.31 | 330.50 | -4.6% |  |  |  | regular session | now below 200-day average (337.81) |
| AMD | WATCH (changed) | REDUCE | 508.58 | 515.41 | +1.3% | 478.97 | 579.60 | 406.09 | regular session | now above chandelier stop (511.22) |
| ALAB | REDUCE | REDUCE | 216.87 | 213.41 | -1.6% |  |  |  | regular session |  |
| SPCX | SELL* (changed) | REDUCE* | 142.07 | 141.08 | -0.7% |  |  |  | regular session | now below chandelier stop (142.01) |
| CEG | REDUCE | REDUCE | 276.09 | 266.16 | -3.6% |  |  |  | regular session | now below 50-day average (270.01) |
| TSLA | REDUCE | REDUCE | 378.05 | 377.59 | -0.1% |  |  |  | regular session |  |
| BE | REDUCE | REDUCE | 193.88 | 184.35 | -4.9% |  |  |  | regular session |  |
| FSLR | SELL (changed) | REDUCE | 191.61 | 180.04 | -6.0% |  |  |  | regular session | now below 50-day average (186.74); now below chandelier stop (182.76) |
| MRVL | SELL | SELL | 154.60 | 152.49 | -1.4% |  |  |  | regular session |  |
| TSM | REDUCE (changed) | SELL | 388.62 | 394.04 | +1.4% |  |  |  | regular session | now above 80% of the 52-week high (388.64) |
| NVDA | SELL | SELL | 178.67 | 166.45 | -6.8% |  |  |  | regular session |  |
| ETN | SELL | SELL | 359.30 | 352.60 | -1.9% |  |  |  | regular session |  |
| GEV | SELL | SELL | 829.34 | 782.43 | -5.7% |  |  |  | regular session |  |
| GOOG | SELL | SELL | 286.01 | 284.76 | -0.4% |  |  |  | regular session |  |
| SKHY | SELL* | SELL* | 134.38 | 129.03 | -4.0% |  |  |  | regular session |  |
| VST | SELL | SELL | 133.92 | 130.32 | -2.7% |  |  |  | regular session |  |

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
