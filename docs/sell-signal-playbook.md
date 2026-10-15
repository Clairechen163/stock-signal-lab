# Sell-signal playbook

Knowing when to sell is the hardest part of investing, because the decision is made
under stress, usually after a loss. This playbook writes the rules down in advance and
explains how `stocklab sell-check` and `stocklab sell-study` apply and test them.

> Educational material, not investment advice.

## Principle 1: decide your exit before you enter

Every position should have three things written down on the day you buy it:

| Item | Example | Why |
|---|---|---|
| **Thesis** | "Data-center capex keeps growing; KLAC's process-control share rises" | The strongest sell signal is a broken thesis, and you can only notice it if it was written down |
| **Stop** | Entry minus 2x ATR, or a fixed 15% | Caps the loss on any one idea; `screen` sizes the position so a stop-out costs about 1% of capital |
| **Review triggers** | Earnings, guidance cuts, the stock falling below its 200-day average | Forces a deliberate decision instead of drifting |

The price you paid is not on that list. The market does not know your entry price, and
"waiting to get back to even" is not a reason to hold.

## Principle 2: separate the kinds of sell decision

| Type | Question | Tool |
|---|---|---|
| **Thesis break** | Is the reason I bought still true? | Your notes; earnings and news |
| **Risk control** | Has the stock broken a level I pre-committed to? | Hard stop, chandelier stop, trailing stop |
| **Technical deterioration** | Is the trend or momentum weakening? | Moving averages, MACD, RSI divergence, distribution days |
| **Portfolio** | Has this position become too big or too correlated with the rest? | `stocklab portfolio` risk shares |
| **Opportunity cost** | Is there a clearly better use of this money? | `stocklab screen` |

## The rule library

`sell_signals.py` implements these rules. Each has a weight; the weighted sum gives the
status in `sell-check`.

| Rule | Category | Weight | Condition |
|---|---|---|---|
| `below_sma50` | trend | 1 | Close below the 50-day moving average |
| `below_sma200` | trend | 2 | Close below the 200-day moving average |
| `death_cross` | trend | 2 | 50-day average below the 200-day average |
| `rsi_divergence` | momentum | 1 | New 20-day price high without a new RSI high |
| `rsi_rollover` | momentum | 1 | RSI above 70 in the last 5 days, now below 65 |
| `macd_bearish` | momentum | 1 | MACD line below its signal line |
| `distribution_cluster` | volume | 1 | 5+ down days on rising volume in the last 25 sessions |
| `high_volume_breakdown` | volume | 2 | Down day closing below the 50-day average on 1.5x+ average volume |
| `drawdown_20` | risk | 1 | 20%+ below the 52-week high |
| `volatility_spike` | risk | 1 | 21-day volatility 1.5x+ its 1-year median |
| `chandelier_stop` | risk | 2 | Close below the 22-day high minus 3x ATR |

**Status bands:** 0-2 HOLD, 3-5 WATCH, 6-8 REDUCE, 9+ EXIT.
**Override:** if you give an entry price and the close is below your hard stop, the status
is EXIT regardless of the score. A pre-committed stop is not renegotiated in the moment.

What each status means in practice:

- **HOLD**: no action. Re-check after earnings or a sharp market move.
- **WATCH**: no action yet; note the "levels to watch" in the output. A close beyond the next one moves the status.
- **REDUCE**: trim, for example a third of the position, which lowers risk without betting everything on the signal being right.
- **EXIT**: close the position, or the rest of it, as your plan says.

## Principle 3: test the rules, don't just trust them

The weights above are a starting heuristic, not a finding. `stocklab sell-study` asks, for
every rule and for 5-, 21- and 63-day horizons:

> After this rule fires, are returns actually worse than on random days in the same stocks?

It answers with a Monte Carlo null (random dates, matched per stock), reports how often a
10%+ drop followed compared with the base rate, and controls the false discovery rate
across all 33 tests. Two outcomes are both useful:

- A rule with significantly worse forward returns earns its weight, or a higher one.
- A rule with *no* edge, or with *better* forward returns (common for overbought signals
  in strong trends), is a reason to drop it or lower its weight, and it explains why
  "sell when RSI is above 70" often costs money.

A rule can also be worth keeping without predicting lower *average* returns: a stop that
avoids rare deep losses improves drawdowns and the ability to stay invested. Read the
`drop10_after_signal` column alongside the mean.

## Common mistakes the rules are designed to prevent

1. **Anchoring to the entry price.** Ask instead: would I buy this today at this price?
2. **Moving the stop lower after it is hit.** That turns a small loss into a large one.
3. **Selling winners too early and holding losers too long** (the disposition effect).
   Trailing and chandelier stops let winners run while still protecting gains.
4. **All-or-nothing decisions.** Scaling out in thirds reduces the cost of being wrong on timing.
5. **Ignoring correlation.** Three chip stocks are closer to one big position than to three
   separate ones; `stocklab portfolio` shows how much of the risk they really carry.
