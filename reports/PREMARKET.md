# Pre-market board, 06:00 ET on 2026-11-06

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest pre-market trade standing in for today's close; the history before it is daily closes. The volume rules keep their value from the last close, so a label changes only when the price move switches a price-based rule (the last column says which).

| ticker | pre-market label | board at close | close | pre-market | change | pullback entry | breakout | stop | session | what the move changes |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | BUY | BUY | 260.21 | 258.02 | -0.8% | 254.21 | 266.56 | 236.33 | pre-market |  |
| IBM | REDUCE (changed) | WATCH | 247.11 | 243.50 | -1.5% |  |  |  | pre-market | now below 200-day average (246.19); rule now on: MACD bearish; rule now off: RSI rollover |
| FSLR | AVOID | AVOID | 195.76 | 197.00 | +0.6% |  |  |  | pre-market |  |
| AMD | SELL | SELL | 404.40 | 430.97 | +6.6% |  |  |  | pre-market | now above 200-day average (415.00) |
| MRVL | SELL | SELL | 133.55 | 142.70 | +6.9% |  |  |  | pre-market |  |
| NVDA | SELL | SELL | 181.60 | 188.89 | +4.0% |  |  |  | pre-market |  |
| ALAB | SELL | SELL | 179.47 | 194.99 | +8.6% |  |  |  | pre-market |  |
| ETN | SELL | SELL | 327.02 | 341.00 | +4.3% |  |  |  | pre-market |  |
| GOOG | SELL | SELL | 281.74 | 282.51 | +0.3% |  |  |  | pre-market |  |
| SPCX | SELL* | SELL* | 123.62 | 128.16 | +3.7% |  |  |  | pre-market |  |
| TSLA | SELL | SELL | 343.69 | 348.78 | +1.5% |  |  |  | pre-market |  |
| SKHY | SELL* | SELL* | 123.90 | 129.05 | +4.2% |  |  |  | pre-market |  |

## Does deciding before the open help?

From 2022-02-03 to 2026-11-04 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +34.2% a year (worst drawdown -28.3%) against +33.2% (-24.7%) for labels set at the previous close; the two agreed on 89% of stock-weeks. Sharpe ratio difference +0.04 (95% block-bootstrap CI [-0.12, +0.19]): deciding before the open has been **not distinguishable from deciding on the previous close**. *Stability: same verdict in 3 of the last 3 runs.*

## Do opening gaps carry into the day?

Across 12,121 stock-days (12 watchlist stocks, 2021-11-09 to 2026-11-05), each 1% of opening gap went with a -0.02% move from the open to the close (95% block-bootstrap CI [-0.07%, +0.03%]): no reliable relationship, so the size of a gap has not told you which way the session goes. *Stability: same verdict in 3 of the last 3 runs.*

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 479 | -5.2% | +0.19% | 48% |
| down 1-3% | 1890 | -1.7% | +0.05% | 53% |
| within 1% | 7105 | +0.0% | +0.02% | 51% |
| up 1-3% | 2101 | +1.7% | +0.07% | 52% |
| gap up 3%+ | 546 | +5.4% | -0.24% | 46% |
