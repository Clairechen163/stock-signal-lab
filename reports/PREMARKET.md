# Intraday board, 15:55 ET on 2026-11-18

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest trade standing in for today's close; the history before it is daily closes. The volume rules keep their value from the last close, so a label changes only when the price move switches a price-based rule (the last column says which).

| ticker | label now | board at close | close | latest | change | pullback entry | breakout | stop | session | what the move changes |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | BUY | BUY | 257.89 | 267.57 | +3.8% | 257.12 | 271.41 | 239.18 | regular session |  |
| AMD | WATCH | WATCH | 503.41 | 528.90 | +5.1% | 514.58 | 586.47 | 435.55 | regular session | now above 80% of the 52-week high (519.54) |
| SPCX | REDUCE* | REDUCE* | 141.70 | 143.82 | +1.5% |  |  |  | regular session | now above chandelier stop (143.27) |
| TSLA | WATCH (changed) | REDUCE | 380.11 | 384.65 | +1.2% | 375.83 | 408.27 | 345.47 | regular session | now above 200-day average (382.27) |
| ALAB | REDUCE | REDUCE | 211.60 | 215.38 | +1.8% |  |  |  | regular session |  |
| CEG | REDUCE | REDUCE | 268.07 | 262.84 | -2.0% |  |  |  | regular session |  |
| BE | REDUCE | REDUCE | 173.46 | 170.99 | -1.4% |  |  |  | regular session |  |
| DELL | SELL | SELL | 322.79 | 314.52 | -2.6% |  |  |  | regular session |  |
| MRVL | SELL | SELL | 148.74 | 145.20 | -2.4% |  |  |  | regular session |  |
| TSM | SELL | SELL | 359.69 | 361.54 | +0.5% |  |  |  | regular session |  |
| IBM | SELL | SELL | 231.09 | 228.80 | -1.0% |  |  |  | regular session |  |
| ETN | SELL | SELL | 337.11 | 338.21 | +0.3% |  |  |  | regular session |  |
| GEV | SELL | SELL | 779.91 | 772.86 | -0.9% |  |  |  | regular session |  |
| GOOG | SELL | SELL | 277.60 | 279.43 | +0.7% |  |  |  | regular session |  |
| NVDA | SELL | SELL | 155.46 | 150.81 | -3.0% |  |  |  | regular session |  |
| VST | SELL | SELL | 127.15 | 125.32 | -1.4% |  |  |  | regular session |  |
| SKHY | SELL* | SELL* | 122.61 | 121.87 | -0.6% |  |  |  | regular session |  |
| FSLR | SELL | SELL | 152.97 | 151.09 | -1.2% |  |  |  | regular session |  |

## Does deciding before the open help?

From 2022-02-15 to 2026-11-16 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +38.7% a year (worst drawdown -37.0%) against +36.6% (-40.5%) for labels set at the previous close; the two agreed on 89% of stock-weeks. Sharpe ratio difference +0.06 (95% block-bootstrap CI [-0.22, +0.29]): deciding before the open has been **not distinguishable from deciding on the previous close**. *Stability: same verdict in 10 of the last 10 runs.*

## Do opening gaps carry into the day?

Across 19,031 stock-days (18 watchlist stocks, 2021-11-19 to 2026-11-17), each 1% of opening gap went with a -0.03% move from the open to the close (95% block-bootstrap CI [-0.08%, +0.03%]): no reliable relationship, so the size of a gap has not told you which way the session goes. *Stability: same verdict in 10 of the last 10 runs.*

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 785 | -5.2% | +0.33% | 50% |
| down 1-3% | 2921 | -1.7% | +0.09% | 52% |
| within 1% | 11015 | +0.0% | +0.01% | 50% |
| up 1-3% | 3380 | +1.7% | +0.08% | 52% |
| gap up 3%+ | 930 | +5.4% | -0.12% | 47% |
