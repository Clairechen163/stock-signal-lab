# After-hours board, 19:59 ET on 2026-11-23

> Educational research code, not investment advice. Past results do not predict future returns.

The board's rules with each stock's latest trade standing in for today's close; the history before it is daily closes. The volume rules keep their value from the last close, so a label changes only when the price move switches a price-based rule (the last column says which).

| ticker | label now | board at close | close | latest | change | pullback entry | breakout | stop | session | what the move changes |
|---|---|---|---|---|---|---|---|---|---|---|
| AMZN | WATCH | WATCH | 246.82 | 257.00 | +4.1% | 255.10 | 271.41 | 235.13 | after-hours | now above 50-day average (255.03) |
| DELL | SELL | SELL | 278.02 | 338.49 | +21.8% |  |  |  | after-hours |  |
| AMD | REDUCE (changed) | SELL | 424.39 | 451.22 | +6.3% |  |  |  | after-hours | now above 200-day average (429.79) |
| TSM | SELL | SELL | 318.71 | 369.99 | +16.1% |  |  |  | after-hours |  |
| MRVL | SELL | SELL | 122.28 | 145.81 | +19.2% |  |  |  | after-hours |  |
| SPCX | REDUCE* (changed) | SELL* | 127.79 | 134.75 | +5.4% |  |  |  | after-hours | now above chandelier stop (130.03) |
| IBM | SELL | SELL | 224.44 | 232.80 | +3.7% |  |  |  | after-hours |  |
| ETN | SELL | SELL | 311.33 | 338.50 | +8.7% |  |  |  | after-hours |  |
| TSLA | REDUCE (changed) | SELL | 345.82 | 388.15 | +12.2% |  |  |  | after-hours | now above 50-day average (375.64); now above 200-day average (381.66); now above chandelier stop (362.81) |
| GOOG | SELL | SELL | 264.00 | 282.22 | +6.9% |  |  |  | after-hours |  |
| GEV | SELL | SELL | 699.33 | 762.00 | +9.0% |  |  |  | after-hours |  |
| CEG | REDUCE (changed) | SELL | 237.41 | 251.72 | +6.0% |  |  |  | after-hours | now above chandelier stop (244.63) |
| NVDA | SELL | SELL | 125.53 | 166.79 | +32.9% |  |  |  | after-hours |  |
| VST | SELL | SELL | 115.25 | 124.32 | +7.9% |  |  |  | after-hours |  |
| ALAB | SELL | SELL | 180.35 | 224.04 | +24.2% |  |  |  | after-hours |  |
| BE | REDUCE (changed) | SELL | 142.39 | 171.68 | +20.6% |  |  |  | after-hours | now above chandelier stop (168.29) |
| SKHY | SELL* | SELL* | 103.57 | 125.72 | +21.4% |  |  |  | after-hours |  |
| FSLR | SELL | SELL | 137.59 | 146.95 | +6.8% |  |  |  | after-hours |  |

## Does deciding before the open help?

From 2022-02-17 to 2026-11-19 (239 weekly decisions, both traded at the open), labels set with the pre-market price returned +36.2% a year (worst drawdown -36.5%) against +34.4% (-35.9%) for labels set at the previous close; the two agreed on 89% of stock-weeks. Sharpe ratio difference +0.03 (95% block-bootstrap CI [-0.12, +0.20]): deciding before the open has been **not distinguishable from deciding on the previous close**. *Stability: same verdict in 10 of the last 10 runs.*

## Do opening gaps carry into the day?

Across 19,033 stock-days (18 watchlist stocks, 2021-11-26 to 2026-11-20), each 1% of opening gap went with a -0.02% move from the open to the close (95% block-bootstrap CI [-0.08%, +0.03%]): no reliable relationship, so the size of a gap has not told you which way the session goes. *Stability: same verdict in 10 of the last 10 runs.*

| opening gap | days | avg gap | avg open-to-close | closed above open |
|---|---|---|---|---|
| gap down 3%+ | 791 | -5.2% | +0.27% | 50% |
| down 1-3% | 2922 | -1.7% | +0.06% | 52% |
| within 1% | 10991 | +0.0% | +0.01% | 50% |
| up 1-3% | 3392 | +1.7% | +0.07% | 51% |
| gap up 3%+ | 937 | +5.4% | -0.17% | 47% |
