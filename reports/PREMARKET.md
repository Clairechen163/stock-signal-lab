# Intraday board, 15:46 ET on 2026-11-20

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest trade standing in for today's close; the history before it is daily closes. The volume rules keep their value from the last close, so a label changes only when the price move switches a price-based rule (the last column says which).

| ticker | label now | board at close | close | latest | change | pullback entry | breakout | stop | session | what the move changes |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | WATCH (changed) | BUY | 257.37 | 247.43 | -3.9% | 237.80 | 271.41 | 218.54 | regular session | now below 50-day average (255.23); rule now on: MACD bearish; rule now off: volatility spike |
| AMD | SELL (changed) | WATCH | 489.19 | 428.11 | -12.5% |  |  |  | regular session | now below 200-day average (428.63); now below chandelier stop (463.55); rule now on: MACD bearish |
| DELL | REDUCE | REDUCE | 312.54 | 279.84 | -10.5% |  |  |  | regular session |  |
| SPCX | SELL* (changed) | REDUCE* | 138.43 | 129.53 | -6.4% |  |  |  | regular session | rule now on: MACD bearish |
| TSLA | SELL (changed) | REDUCE | 374.41 | 347.73 | -7.1% |  |  |  | regular session | now below chandelier stop (365.79); rule now on: volatility spike |
| CEG | SELL (changed) | REDUCE | 252.03 | 239.74 | -4.9% |  |  |  | regular session | now below chandelier stop (245.07); rule now on: MACD bearish |
| ALAB | REDUCE | REDUCE | 211.60 | 181.04 | -14.4% |  |  |  | regular session |  |
| BE | REDUCE | REDUCE | 168.11 | 143.40 | -14.7% |  |  |  | regular session |  |
| MRVL | SELL | SELL | 138.47 | 122.90 | -11.2% |  |  |  | regular session |  |
| TSM | SELL | SELL | 352.09 | 321.44 | -8.7% |  |  |  | regular session |  |
| ETN | SELL | SELL | 330.57 | 312.39 | -5.5% |  |  |  | regular session |  |
| IBM | SELL | SELL | 223.88 | 226.17 | +1.0% |  |  |  | regular session |  |
| GEV | SELL | SELL | 756.28 | 704.61 | -6.8% |  |  |  | regular session |  |
| GOOG | SELL | SELL | 271.02 | 265.74 | -1.9% |  |  |  | regular session |  |
| NVDA | SELL | SELL | 145.98 | 128.70 | -11.8% |  |  |  | regular session |  |
| VST | SELL | SELL | 124.15 | 115.82 | -6.7% |  |  |  | regular session |  |
| SKHY | SELL* | SELL* | 119.20 | 104.42 | -12.4% |  |  |  | regular session |  |
| FSLR | SELL | SELL | 151.95 | 138.80 | -8.7% |  |  |  | regular session |  |

## Does deciding before the open help?

From 2022-02-17 to 2026-11-18 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +38.3% a year (worst drawdown -35.5%) against +36.5% (-34.9%) for labels set at the previous close; the two agreed on 89% of stock-weeks. Sharpe ratio difference +0.03 (95% block-bootstrap CI [-0.12, +0.20]): deciding before the open has been **not distinguishable from deciding on the previous close**. *Stability: same verdict in 10 of the last 10 runs.*

## Do opening gaps carry into the day?

Across 19,041 stock-days (18 watchlist stocks, 2021-11-23 to 2026-11-19), each 1% of opening gap went with a -0.03% move from the open to the close (95% block-bootstrap CI [-0.09%, +0.02%]): no reliable relationship, so the size of a gap has not told you which way the session goes. *Stability: same verdict in 10 of the last 10 runs.*

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 785 | -5.2% | +0.33% | 50% |
| down 1-3% | 2919 | -1.7% | +0.08% | 52% |
| within 1% | 11007 | +0.0% | +0.01% | 50% |
| up 1-3% | 3393 | +1.7% | +0.07% | 51% |
| gap up 3%+ | 937 | +5.4% | -0.17% | 47% |
