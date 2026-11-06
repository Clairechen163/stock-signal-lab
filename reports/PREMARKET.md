# Pre-market board, 04:38 ET on 2026-11-06

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest pre-market trade standing in for today's close; the history before it is daily closes. The volume rules keep their value from the last close, so a label changes only when the price move switches a price-based rule (the last column says which).

| ticker | pre-market label | board at close | close | pre-market | change | pullback entry | breakout | stop | session | what the move changes |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | BUY | BUY | 260.21 | 258.70 | -0.6% | 254.25 | 266.56 | 236.46 | pre-market |  |
| FSLR | AVOID | AVOID | 195.76 | 198.40 | +1.3% |  |  |  | pre-market |  |
| AMD | SELL | SELL | 404.40 | 436.00 | +7.8% |  |  |  | pre-market | now above 200-day average (415.00) |
| MRVL | SELL | SELL | 133.55 | 144.50 | +8.2% |  |  |  | pre-market |  |
| NVDA | SELL | SELL | 181.60 | 189.30 | +4.2% |  |  |  | pre-market |  |
| ALAB | SELL | SELL | 179.47 | 195.63 | +9.0% |  |  |  | pre-market |  |
| SPCX | SELL* | SELL* | 123.62 | 128.73 | +4.1% |  |  |  | pre-market |  |
| ETN | SELL | SELL | 327.02 | 343.00 | +4.9% |  |  |  | pre-market |  |
| GOOG | SELL | SELL | 281.74 | 285.42 | +1.3% |  |  |  | pre-market |  |
| TSLA | SELL | SELL | 343.69 | 353.73 | +2.9% |  |  |  | pre-market |  |
| SKHY | SELL* | SELL* | 123.90 | 130.01 | +4.9% |  |  |  | pre-market |  |

## Does deciding before the open help?

From 2022-02-03 to 2026-11-04 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +35.5% a year (worst drawdown -29.0%) against +33.0% (-31.3%) for labels set at the previous close; the two agreed on 89% of stock-weeks. Sharpe ratio difference +0.09 (95% block-bootstrap CI [-0.13, +0.37]): deciding before the open has been **not distinguishable from deciding on the previous close**. *Stability: same verdict in 3 of the last 3 runs.*

## Do opening gaps carry into the day?

Across 10,868 stock-days (11 watchlist stocks, 2021-11-09 to 2026-11-05), each 1% of opening gap went with a -0.02% move from the open to the close (95% block-bootstrap CI [-0.08%, +0.04%]): no reliable relationship, so the size of a gap has not told you which way the session goes. *Stability: same verdict in 3 of the last 3 runs.*

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 463 | -5.2% | +0.18% | 48% |
| down 1-3% | 1813 | -1.7% | +0.03% | 52% |
| within 1% | 6028 | +0.0% | +0.01% | 50% |
| up 1-3% | 2032 | +1.7% | +0.07% | 52% |
| gap up 3%+ | 532 | +5.4% | -0.27% | 46% |
