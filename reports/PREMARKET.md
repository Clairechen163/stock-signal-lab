# Intraday board, 15:59 ET on 2026-11-19

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest trade standing in for today's close; the history before it is daily closes. The volume rules keep their value from the last close, so a label changes only when the price move switches a price-based rule (the last column says which).

| ticker | label now | board at close | close | latest | change | pullback entry | breakout | stop | session | what the move changes |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | WATCH (changed) | BUY | 530.14 | 488.64 | -7.8% | 448.23 | 586.47 | 367.40 | regular session | now below 80% of the 52-week high (519.54) |
| AMZN | BUY | BUY | 267.74 | 257.42 | -3.9% | 255.23 | 271.41 | 237.01 | regular session |  |
| TSLA | REDUCE (changed) | WATCH | 383.72 | 374.29 | -2.5% |  |  |  | regular session | now below 50-day average (375.81); now below 200-day average (382.08) |
| SPCX | REDUCE* | REDUCE* | 143.50 | 138.07 | -3.8% |  |  |  | regular session |  |
| ALAB | REDUCE | REDUCE | 216.75 | 211.54 | -2.4% |  |  |  | regular session |  |
| CEG | REDUCE | REDUCE | 262.74 | 251.83 | -4.2% |  |  |  | regular session |  |
| BE | REDUCE | REDUCE | 170.98 | 167.66 | -1.9% |  |  |  | regular session |  |
| DELL | SELL | SELL | 313.11 | 312.33 | -0.2% |  |  |  | regular session |  |
| MRVL | SELL | SELL | 145.54 | 138.46 | -4.9% |  |  |  | regular session |  |
| TSM | SELL | SELL | 362.62 | 352.92 | -2.7% |  |  |  | regular session |  |
| IBM | SELL | SELL | 228.53 | 223.91 | -2.0% |  |  |  | regular session |  |
| ETN | SELL | SELL | 338.34 | 329.99 | -2.5% |  |  |  | regular session |  |
| GOOG | SELL | SELL | 279.20 | 270.93 | -3.0% |  |  |  | regular session |  |
| GEV | SELL | SELL | 772.22 | 755.16 | -2.2% |  |  |  | regular session |  |
| NVDA | SELL | SELL | 150.96 | 145.80 | -3.4% |  |  |  | regular session |  |
| VST | SELL | SELL | 125.58 | 123.79 | -1.4% |  |  |  | regular session |  |
| SKHY | SELL* | SELL* | 122.47 | 119.29 | -2.6% |  |  |  | regular session |  |
| FSLR | SELL | SELL | 150.98 | 151.87 | +0.6% |  |  |  | regular session |  |

## Does deciding before the open help?

From 2022-02-16 to 2026-11-17 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +43.5% a year (worst drawdown -33.1%) against +40.4% (-39.4%) for labels set at the previous close; the two agreed on 89% of stock-weeks. Sharpe ratio difference +0.05 (95% block-bootstrap CI [-0.12, +0.26]): deciding before the open has been **not distinguishable from deciding on the previous close**. *Stability: same verdict in 10 of the last 10 runs.*

## Do opening gaps carry into the day?

Across 19,036 stock-days (18 watchlist stocks, 2021-11-22 to 2026-11-18), each 1% of opening gap went with a -0.03% move from the open to the close (95% block-bootstrap CI [-0.08%, +0.03%]): no reliable relationship, so the size of a gap has not told you which way the session goes. *Stability: same verdict in 10 of the last 10 runs.*

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 785 | -5.2% | +0.33% | 50% |
| down 1-3% | 2919 | -1.7% | +0.08% | 52% |
| within 1% | 11012 | +0.0% | +0.01% | 50% |
| up 1-3% | 3389 | +1.7% | +0.08% | 52% |
| gap up 3%+ | 931 | +5.4% | -0.13% | 47% |
