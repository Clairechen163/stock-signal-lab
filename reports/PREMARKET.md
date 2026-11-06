# Intraday board, 15:49 ET on 2026-11-06

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest trade standing in for today's close; the history before it is daily closes. The volume rules keep their value from the last close, so a label changes only when the price move switches a price-based rule (the last column says which).

| ticker | label now | board at close | close | latest | change | pullback entry | breakout | stop | session | what the move changes |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | BUY | BUY | 260.21 | 260.36 | +0.1% | 254.33 | 266.56 | 236.74 | regular session |  |
| IBM | REDUCE (changed) | WATCH | 247.11 | 245.24 | -0.8% |  |  |  | regular session | now below 200-day average (246.19); rule now on: MACD bearish; rule now off: RSI rollover |
| FSLR | AVOID | AVOID | 195.76 | 201.69 | +3.0% |  |  |  | regular session |  |
| AMD | SELL | SELL | 404.40 | 446.37 | +10.4% |  |  |  | regular session | now above 200-day average (415.00) |
| MRVL | SELL | SELL | 133.55 | 139.98 | +4.8% |  |  |  | regular session |  |
| NVDA | SELL | SELL | 181.60 | 187.36 | +3.2% |  |  |  | regular session |  |
| ALAB | SELL | SELL | 179.47 | 187.58 | +4.5% |  |  |  | regular session |  |
| ETN | SELL | SELL | 327.02 | 342.65 | +4.8% |  |  |  | regular session |  |
| GEV | SELL | SELL | 770.51 | 778.88 | +1.1% |  |  |  | regular session |  |
| GOOG | SELL | SELL | 281.74 | 284.46 | +1.0% |  |  |  | regular session |  |
| TSLA | SELL | SELL | 343.69 | 359.54 | +4.6% |  |  |  | regular session |  |
| SPCX | SELL* | SELL* | 123.62 | 133.96 | +8.4% |  |  |  | regular session |  |
| CEG | SELL | SELL | 239.65 | 250.75 | +4.6% |  |  |  | regular session |  |
| VST | SELL | SELL | 112.89 | 124.43 | +10.2% |  |  |  | regular session |  |
| SKHY | SELL* | SELL* | 123.90 | 126.77 | +2.3% |  |  |  | regular session |  |

## Does deciding before the open help?

From 2022-02-03 to 2026-11-04 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +42.5% a year (worst drawdown -31.8%) against +39.2% (-30.5%) for labels set at the previous close; the two agreed on 90% of stock-weeks. Sharpe ratio difference +0.06 (95% block-bootstrap CI [-0.09, +0.23]): deciding before the open has been **not distinguishable from deciding on the previous close**. *Stability: same verdict in 3 of the last 3 runs.*

## Do opening gaps carry into the day?

Across 15,233 stock-days (15 watchlist stocks, 2021-11-09 to 2026-11-05), each 1% of opening gap went with a -0.03% move from the open to the close (95% block-bootstrap CI [-0.08%, +0.03%]): no reliable relationship, so the size of a gap has not told you which way the session goes. *Stability: same verdict in 3 of the last 3 runs.*

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 564 | -5.2% | +0.29% | 49% |
| down 1-3% | 2242 | -1.7% | +0.11% | 53% |
| within 1% | 9157 | +0.0% | +0.00% | 50% |
| up 1-3% | 2609 | +1.7% | +0.08% | 51% |
| gap up 3%+ | 661 | +5.3% | -0.22% | 46% |
