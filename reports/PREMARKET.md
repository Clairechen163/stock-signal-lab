# Pre-market board, 06:49 ET on 2026-11-06

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest pre-market trade standing in for today's close; the history before it is daily closes. The volume rules keep their value from the last close, so a label changes only when the price move switches a price-based rule (the last column says which).

| ticker | pre-market label | board at close | close | pre-market | change | pullback entry | breakout | stop | session | what the move changes |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | BUY | BUY | 260.21 | 262.09 | +0.7% | 254.42 | 266.56 | 236.58 | pre-market |  |
| IBM | REDUCE (changed) | WATCH | 247.11 | 243.45 | -1.5% |  |  |  | pre-market | now below 200-day average (246.19); rule now on: MACD bearish; rule now off: RSI rollover |
| FSLR | AVOID | AVOID | 195.76 | 197.03 | +0.6% |  |  |  | pre-market |  |
| AMD | SELL | SELL | 404.40 | 438.15 | +8.3% |  |  |  | pre-market | now above 200-day average (415.00) |
| MRVL | SELL | SELL | 133.55 | 146.71 | +9.9% |  |  |  | pre-market |  |
| NVDA | SELL | SELL | 181.60 | 190.57 | +4.9% |  |  |  | pre-market |  |
| ALAB | SELL | SELL | 179.47 | 196.50 | +9.5% |  |  |  | pre-market |  |
| ETN | SELL | SELL | 327.02 | 343.00 | +4.9% |  |  |  | pre-market |  |
| GEV | SELL | SELL | 770.51 | 801.10 | +4.0% |  |  |  | pre-market |  |
| GOOG | SELL | SELL | 281.74 | 282.65 | +0.3% |  |  |  | pre-market |  |
| TSLA | SELL | SELL | 343.69 | 352.50 | +2.6% |  |  |  | pre-market |  |
| SPCX | SELL* | SELL* | 123.62 | 129.70 | +4.9% |  |  |  | pre-market |  |
| CEG | SELL | SELL | 239.65 | 244.42 | +2.0% |  |  |  | pre-market |  |
| VST | SELL | SELL | 112.89 | 116.19 | +2.9% |  |  |  | pre-market |  |
| SKHY | SELL* | SELL* | 123.90 | 131.00 | +5.7% |  |  |  | pre-market |  |

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
