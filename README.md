# stock-signal-lab

[![tests](https://github.com/Clairechen163/stock-signal-lab/actions/workflows/tests.yml/badge.svg)](https://github.com/Clairechen163/stock-signal-lab/actions/workflows/tests.yml)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

**Statistically honest tools for the hardest questions an individual investor faces:
when to sell, what to buy and at what price, how to spread risk, and whether tomorrow
is predictable at all.**

> **TL;DR.** During the October 2026 AI-chip selloff I tested 11 popular sell signals,
> 7 trading rules, 3 next-day forecasting models and 4 portfolio constructions on real
> market data, using walk-forward validation, block bootstrap and false-discovery-rate
> control. **Only 1 of 33 sell-signal tests survived; no rule beat buy & hold; next-day
> returns were unpredictable (best AUC 0.52); and three chip stocks carried 87% of a
> nine-asset portfolio's risk.** The practical lesson: treat selling as risk management,
> not prediction.

The project started from a real situation: in October 2026, AI chip stocks fell for six
straight sessions and I had to decide whether to sell three positions (KLAC, VRT, ALAB).
Online advice offered dozens of "sell signals" (moving-average breaks, RSI, volume
patterns) with no evidence behind them. This repository turns those rules into
hypotheses and tests them with the methods a statistician would use: walk-forward
validation, block bootstrap, Monte Carlo nulls and false-discovery-rate control.

> Educational research code. Nothing here is investment advice.

---

## What it does

| Command | Question it answers | Key methods |
|---|---|---|
| `sell-check` | What do my sell rules say about each holding today, and at what prices would that change? | Weighted rule scorecard, ATR/chandelier stops, pre-committed stop override |
| `sell-study` | Which sell signals actually predict weaker returns? | Event study, stratified Monte Carlo null, Benjamini-Hochberg FDR |
| `backtest` | Do buy/sell rules beat buy & hold after costs, by more than luck? | Next-day execution, paired circular block bootstrap of Sharpe differences |
| `forecast` | Can tomorrow's move be predicted? What does the model say for the next session? | Walk-forward ML vs naive baselines, binomial and Diebold-Mariano tests |
| `screen` | Which stocks pass the rules, and where should I enter, stop and size? | Winsorised multi-factor z-scores, ATR stops, fixed-risk position sizing |
| `portfolio` | How do I spread risk instead of just dollars? | Ledoit-Wolf covariance, risk parity, minimum variance, walk-forward comparison |
| `report` | All of the above in one Markdown report with charts | Writes `reports/REPORT.md` |

The most important module is the **sell-signal** pair: `sell-check` gives a transparent
answer for each holding, and `sell-study` tests whether the rules behind that answer have
any predictive value. See the [sell-signal playbook](docs/sell-signal-playbook.md).

## Quick start

```bash
git clone https://github.com/Clairechen163/stock-signal-lab.git
cd stock-signal-lab
pip install -e ".[dev]"

# Full report for your holdings (ticker:entry price)
python -m stocklab report --holdings KLAC:208 VRT:262 ALAB:333

# Individual modules
python -m stocklab sell-check KLAC:208 VRT:262 ALAB:333 --stop 0.15
python -m stocklab sell-study                       # ~36-stock panel, 5 years
python -m stocklab backtest  --tickers KLAC VRT ALAB
python -m stocklab forecast  --tickers KLAC --benchmark SPY
python -m stocklab screen    --capital 100000 --risk 0.01
python -m stocklab portfolio --tickers KLAC VRT ALAB JPM XOM UNH COST TLT GLD

# No internet? Every command runs offline on simulated prices
python -m stocklab report --source synthetic
```

On Windows, `python` works the same way; on macOS/Linux you may need `python3`.

## Results on real data (prices through 14 October 2026)

Full tables and charts: **[`reports/REPORT.md`](reports/REPORT.md)**. Five-year daily
history from Yahoo Finance; a 36-stock panel for the event study.

### 1. Most popular sell signals do not predict weaker returns

Across 33 rule-by-horizon tests on 36 stocks, **only one survived false-discovery-rate
control**: an RSI that was overbought (above 70) and then rolled over below 65 was followed
by 63-day returns of +8.5%, versus +11.4% on random days (q = 0.08).

* The **death cross** looked significant on its own at 21 days (p = 0.04), but with 33 tests
  that is roughly what chance produces (q = 0.47). This is the multiple-testing trap
  that single backtests fall into.
* Several "danger" signals were followed by *higher* returns: after a stock fell 20% below
  its 52-week high, the next 63 days averaged +14.7% vs +11.9% on random days, and
  high-volume breakdowns showed a similar pattern. This is short-term mean reversion.
* Trend and risk signals did **flag tail risk** even without lowering average returns:
  a 10%+ drop followed within 63 days 47% of the time after a death cross and 46% after a
  20% drawdown, versus a 34% base rate.

![Sell signal event study](reports/sell_event_study.png)

### 2. No rule beat buy & hold after accounting for uncertainty

On KLAC, VRT and ALAB, no strategy had a significantly higher Sharpe ratio than buy & hold.
Three were **significantly worse**: MACD on KLAC (Sharpe difference −0.89, 95% CI
[−1.57, −0.36]), the volume breakout on KLAC (−0.79, CI [−1.56, −0.08]) and the 50/200-day
cross on ALAB (−0.99, CI [−2.01, −0.24]). Some rules reduced drawdowns at a modest cost; on
VRT, holding only above the 50-day average cut the worst drawdown from −61% to −42% while
the Sharpe ratio went from 1.43 to 1.28.

![Strategy equity curves](reports/backtest_equity.png)

### 3. Tomorrow's move is not predictable from price and volume

In walk-forward tests over 550 unseen days (193 for ALAB), no model beat the
majority-class baseline in accuracy. The best AUCs were 0.52 (KLAC), 0.52 (VRT) and 0.48
(ALAB), and every regression model had an out-of-sample R² of essentially zero or below versus a
zero-return forecast (Diebold-Mariano p ≥ 0.48). The "next-session forecast" in the
report is therefore shown next to these scores, and should be read as close to a coin flip.
This is the result the efficient-market hypothesis predicts.

### 4. Three chip stocks were most of the risk

In an equal-weight portfolio of nine assets (KLAC, VRT, ALAB plus JPM, XOM, UNH, COST,
TLT and GLD), the three AI-hardware stocks were **33% of the money but 87% of the risk**;
ALAB alone contributed 38%. Risk parity cut expected volatility from 21.6% to 10.4%. In
the monthly-rebalanced walk-forward test (the window starts in 2025, because ALAB listed
in 2024), equal weight earned more (46% vs 24% a year) during the AI rally, but with twice
the drawdown (−13.7% vs −6.7%) and a similar Sharpe ratio (1.82 vs 1.84).

![Where the money is vs where the risk is](reports/portfolio_risk_shares.png)

### What this means for the sell decision

On 14 October 2026 the scorecard rated KLAC and VRT **EXIT** (10 and 12 out of 15, with
both trading just above their pre-set 15% stop-losses) and ALAB **REDUCE** (6/15). The
event study adds an important qualification: most of the rules behind those scores
describe a stock that is *already* falling and carrying more tail risk, rather than one
that will underperform on average. That points to treating the sell decision as **risk
management** (honouring pre-committed stops, cutting a position that dominates portfolio
risk) rather than as a prediction, and it motivates the next step below.

### Next steps

* Re-weight the scorecard using event-study evidence instead of hand-set weights.
* Test rules on stocks that crashed and never recovered (e.g. INTC, PYPL) to reduce the
  survivorship bias of a universe chosen in 2026.
* Add an earnings-date flag, since many large moves happen around reports.

## Repository structure

```
src/stocklab/
  data.py                  Yahoo Finance, CSV, or synthetic regime-switching prices
  indicators.py            SMA/EMA, RSI, MACD, ATR, volatility, drawdown (no look-ahead)
  stats.py                 Block bootstrap, Benjamini-Hochberg, Diebold-Mariano, binomial and Monte Carlo tests
  backtest.py              Strategy library and backtest engine with next-day execution
  sell_signals.py          Rule library, holdings scorecard, event study
  forecast.py              Feature engineering, walk-forward models, next-session forecast
  screener.py              Filters, factor scoring, entry/stop/position-size plans
  portfolio.py             Shrinkage covariance, risk parity, minimum variance, walk-forward
  plots.py                 Report charts
  cli.py                   Command-line interface and report generator
tests/                     24 unit tests, including look-ahead and leakage checks
docs/
  methodology.md           Statistical design and limitations
  sell-signal-playbook.md  How to use and test exit rules
reports/                   Generated REPORT.md and charts
```

## Statistical design highlights

* **No look-ahead.** Indicators use only past data (unit-tested by shocking future prices);
  backtests trade at the *next* close; forecasts are walk-forward with a gap between train and test.
* **Honest baselines.** Every model is compared with a naive alternative: buy & hold,
  majority class, or a zero-return random walk.
* **Uncertainty, not just point estimates.** Sharpe-ratio differences get block-bootstrap
  confidence intervals that respect volatility clustering.
* **Multiple testing.** 33 rule-by-horizon tests are FDR-controlled, so "one rule looked
  good" isn't mistaken for a discovery.
* **Built-in false-positive check.** On synthetic random-walk data, no signal should look
  significant. CI runs the full pipeline offline on every push.

Details: [docs/methodology.md](docs/methodology.md).

## Limitations

Universes chosen today carry survivorship bias; recent IPOs have short histories; costs
are simplified; 2022-2026 was an unusual bull market for AI stocks; and fundamental data
is a current snapshot, so it is used only for today's screen, never in backtests. These
are discussed in the methodology.

## Skills demonstrated

Time-series feature engineering and leakage control · walk-forward cross-validation ·
classification and regression with scikit-learn · resampling inference (block bootstrap,
Monte Carlo) · hypothesis testing and FDR control · forecast evaluation (AUC, Brier,
Diebold-Mariano) · covariance shrinkage and constrained optimisation (SciPy) · packaged
Python with CLI, unit tests and GitHub Actions CI.

## License

MIT. Data from Yahoo Finance is subject to its own terms of use.
