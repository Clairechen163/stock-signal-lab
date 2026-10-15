"""Command-line interface.

    python -m stocklab backtest   --tickers KLAC VRT ALAB
    python -m stocklab sell-check KLAC:208 VRT:262 ALAB:333
    python -m stocklab sell-study
    python -m stocklab forecast   --tickers KLAC
    python -m stocklab screen
    python -m stocklab portfolio  --tickers KLAC VRT ALAB JPM XOM TLT GLD
    python -m stocklab report     --holdings KLAC:208 VRT:262 ALAB:333

Add --source synthetic to any command to run offline on simulated prices.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import sys

import pandas as pd

from . import backtest, data, forecast, indicators, plots, portfolio, screener, sell_signals

STUDY_UNIVERSE = sorted(
    set(screener.DEFAULT_UNIVERSE)
    | {"AMD", "MU", "INTC", "QCOM", "LRCX", "AMAT", "ASML", "TSM", "MRVL", "TXN", "ADI", "ON", "ARM"}
)
DIVERSIFIERS = ["JPM", "XOM", "UNH", "COST", "TLT", "GLD"]
DISCLAIMER = "Educational research code, not investment advice. Past results do not predict future returns."

pd.set_option("display.width", 220)
pd.set_option("display.max_columns", 40)


# ------------------------------------------------------------------- helpers
def parse_holdings(items):
    out = {}
    for it in items or []:
        if ":" in it:
            t, p = it.split(":", 1)
            out[t.upper()] = float(p)
        else:
            out[it.upper()] = None
    return out


def load_ind(tickers, args, min_rows=260):
    raw = data.load_many(tickers, args.years, args.source, args.csv_dir, min_rows=min_rows)
    return raw, {t: indicators.add_all(d) for t, d in raw.items()}


def md_table(df: pd.DataFrame, index=True, index_label: str | None = None) -> str:
    d = df.copy()
    if isinstance(d.columns, pd.MultiIndex):  # ('weight', 'Risk parity') -> 'weight: Risk parity'
        d.columns = [": ".join(str(x) for x in c if str(x)) for c in d.columns]
    if index:
        d.index.name = index_label or d.index.name or ""
        d = d.reset_index()
    cols = [str(c) for c in d.columns]
    lines = ["| " + " | ".join(cols) + " |", "|" + "|".join(["---"] * len(cols)) + "|"]
    for _, row in d.iterrows():
        lines.append("| " + " | ".join("" if pd.isna(v) else str(v) for v in row.values) + " |")
    return "\n".join(lines)


def pct(v, signed=True):
    return "" if pd.isna(v) else (f"{v:+.1%}" if signed else f"{v:.1%}")


def section(title):
    print(f"\n{'=' * 8} {title} {'=' * (70 - len(title))}")


# ------------------------------------------------------------------ commands
def cmd_backtest(args, md=None, outdir=None):
    _, frames = load_ind(args.tickers, args)
    curves = {}
    for t, d in frames.items():
        table, eq = backtest.backtest_ticker(d, args.cost_bps, n_boot=args.n_boot)
        curves[t] = eq
        start, end = eq.index[0].date(), eq.index[-1].date()
        section(f"Backtest {t} ({start} to {end})")
        ft = backtest.format_table(table)
        print(ft.to_string())
        if md is not None:
            md.append(f"### {t} ({start} to {end})\n\n{md_table(ft)}\n")
    if curves and outdir:
        path = os.path.join(outdir, "backtest_equity.png")
        plots.equity_curves(curves, path)
        if md is not None:
            md.append("![Strategy equity curves](backtest_equity.png)\n")
    return curves


def cmd_sell_check(args, md=None, outdir=None):
    holdings = parse_holdings(args.holdings)
    _, frames = load_ind(list(holdings), args)
    rows = []
    for t, d in frames.items():
        r = sell_signals.check_holding(d, holdings.get(t), args.stop)
        section(f"Sell check {t}")
        text = sell_signals.format_check(t, r)
        print(text)
        if md is not None:
            md.append(f"```\n{text}\n```\n")
        rows.append({"ticker": t, "status": r["status"], "score": f"{r['score']}/{r['max_score']}",
                     "P&L": pct(r.get("pnl")), "close": f"{r['close']:.2f}"})
    return pd.DataFrame(rows)


def cmd_sell_study(args, md=None, outdir=None):
    tickers = args.tickers or STUDY_UNIVERSE
    print(f"Loading {len(tickers)} stocks for the event study...")
    _, frames = load_ind(tickers, args)
    res = sell_signals.event_study(frames, n_sims=args.n_sims)
    section(f"Sell-signal event study ({len(frames)} stocks)")
    ft = sell_signals.format_event_study(res)
    cols = ["rule", "horizon", "events", "mean_after_signal", "mean_random_days", "difference",
            "p_value", "q_value", "drop10_after_signal", "drop10_base_rate", "verdict"]
    print(ft[cols].to_string(index=False))
    useful = res[res["verdict"] == "useful"]
    print(f"\nRules with significantly weaker forward returns (q < 0.10): {len(useful)} of {len(res)} tests")
    if md is not None:
        md.append(f"Panel: {len(frames)} stocks, {args.years} years. Null hypothesis: returns after a signal "
                  "look like returns on random days from the same stocks.\n")
        md.append(md_table(ft[cols], index=False) + "\n")
        md.append(f"**{len(useful)} of {len(res)} rule-by-horizon tests** show significantly weaker returns "
                  "after the signal (q < 0.10).\n")
    if outdir:
        plots.event_study(res, os.path.join(outdir, "sell_event_study.png"))
        if md is not None:
            md.append("![Sell signal event study](sell_event_study.png)\n")
    res.to_csv(os.path.join(outdir or ".", "sell_event_study.csv"), index=False)
    return res


def cmd_forecast(args, md=None, outdir=None):
    raw, frames = load_ind(args.tickers, args)
    market = None
    if args.benchmark:
        try:
            market = data.load(args.benchmark, args.years, args.source, args.csv_dir)["Close"]
        except Exception as e:
            print(f"  benchmark {args.benchmark} unavailable ({e}); continuing without it")
    for t, d in frames.items():
        X, y = forecast.build_features(d, market)
        try:
            preds = forecast.walk_forward(X, y)
        except ValueError as e:
            print(f"  {t}: {e}")
            continue
        clf, reg = forecast.evaluate(preds)
        tom = forecast.predict_tomorrow(X, y)
        section(f"Next-day forecast {t} (walk-forward test on {len(preds)} days)")
        reg = reg.round({"RMSE (bps)": 1, "R2 out-of-sample vs zero": 4, "direction hit rate": 3, "DM p (beats zero)": 3})
        clf = clf.round(3)
        print(clf.to_string())
        print()
        print(reg.to_string())
        print(f"\nForecast for the session after {tom['as_of']}:")
        lines = []
        for k, v in tom.items():
            if k == "as_of":
                continue
            s = f"{v:.1%}" if k.startswith("P(up)") else f"{v:+.2%}"
            lines.append(f"  {k:<32} {s}")
        print("\n".join(lines))
        best_auc = clf["AUC"].drop("Majority class (baseline)", errors="ignore").max()
        verdict = ("no reliable edge: treat the forecast as close to a coin flip"
                   if best_auc < 0.53 else "a small edge out of sample; still check the p-values before trusting it")
        print(f"  Best out-of-sample AUC {best_auc:.3f} -> {verdict}")
        if md is not None:
            md.append(f"### {t}\n\nWalk-forward test on {len(preds)} unseen days "
                      f"({preds.index[0].date()} to {preds.index[-1].date()}).\n")
            md.append(md_table(clf) + "\n")
            md.append(md_table(reg) + "\n")
            md.append("Forecast for the next session:\n\n```\n" + "\n".join(lines) + "\n```\n")
            md.append(f"Best out-of-sample AUC **{best_auc:.3f}**: {verdict}.\n")
        if outdir:
            plots.forecast_importance(forecast.feature_importance(X, y), os.path.join(outdir, f"forecast_{t}.png"), t)
            if md is not None:
                md.append(f"![{t} feature effects](forecast_{t}.png)\n")


def cmd_screen(args, md=None, outdir=None):
    tickers = args.tickers or screener.DEFAULT_UNIVERSE
    _, frames = load_ind(tickers, args)
    use_f = args.source == "yahoo" and not args.no_fundamentals
    table = screener.screen(frames, use_f, args.capital, args.risk, args.max_position)
    section(f"Stock screen ({len(table)} stocks, capital ${args.capital:,.0f}, risk {args.risk:.1%} per trade)")
    ft = screener.format_screen(table, args.top)
    print(ft.to_string())
    if md is not None:
        md.append(md_table(ft, index_label="ticker") + "\n")
    table.to_csv(os.path.join(outdir or ".", "screen.csv"))
    return table


def cmd_portfolio(args, md=None, outdir=None):
    raw, _ = load_ind(args.tickers, args)
    prices = data.close_matrix(raw)
    rets = prices.pct_change().dropna()
    recent = rets.iloc[-args.lookback:]
    w_table, diag = portfolio.build(recent, args.max_weight)
    section(f"Portfolio construction ({len(prices.columns)} assets, last {len(recent)} days)")
    wf = (w_table * 100).round(1)
    print("Weights and risk shares (%):")
    print(wf.to_string())
    print()
    dfmt = diag.copy()
    for c in ["expected volatility", "largest risk share"]:
        dfmt[c] = dfmt[c].map(lambda v: f"{v:.1%}")
    for c in ["diversification ratio", "effective number of bets"]:
        dfmt[c] = dfmt[c].map(lambda v: f"{v:.2f}")
    print(dfmt.to_string())
    warns = portfolio.correlation_warnings(recent)
    for w in warns:
        print(f"  ! {w}")
    try:
        summ, eq = portfolio.walk_forward(prices, args.lookback, 21, args.max_weight)
        sfmt = summ.copy()
        for c in ["CAGR", "Volatility", "Max drawdown"]:
            sfmt[c] = sfmt[c].map(lambda v: f"{v:+.1%}")
        sfmt["Sharpe"] = sfmt["Sharpe"].map(lambda v: f"{v:.2f}")
        print(f"\nWalk-forward, monthly rebalance ({eq.index[0].date()} to {eq.index[-1].date()}):")
        print(sfmt.to_string())
    except ValueError as e:
        summ, eq, sfmt = None, None, None
        print(f"  walk-forward skipped: {e}")
    if md is not None:
        md.append(f"Assets: {', '.join(prices.columns)}. Covariance: Ledoit-Wolf shrinkage on the last "
                  f"{len(recent)} trading days.\n\nWeights and share of risk (%):\n\n{md_table(wf, index_label='asset')}\n")
        md.append(md_table(dfmt, index_label="method") + "\n")
        if warns:
            md.append("Concentration warnings:\n\n" + "\n".join(f"- {w}" for w in warns) + "\n")
        if sfmt is not None:
            md.append(f"Out-of-sample comparison, monthly rebalance ({eq.index[0].date()} to {eq.index[-1].date()}; "
                      f"limited by the asset with the shortest history):\n\n{md_table(sfmt, index_label='method')}\n")
    if outdir:
        plots.correlation_heatmap(recent, os.path.join(outdir, "portfolio_correlation.png"))
        plots.risk_shares(w_table, os.path.join(outdir, "portfolio_risk_shares.png"))
        if eq is not None:
            plots.portfolio_curves(eq, os.path.join(outdir, "portfolio_walk_forward.png"))
        if md is not None:
            md.append("![Correlations](portfolio_correlation.png)\n\n![Risk shares](portfolio_risk_shares.png)\n")
            if eq is not None:
                md.append("![Walk-forward](portfolio_walk_forward.png)\n")


def cmd_report(args):
    """Run every module and write reports/REPORT.md with tables and charts."""
    holdings = parse_holdings(args.holdings)
    tickers = list(holdings)
    os.makedirs(args.out, exist_ok=True)
    md = [
        "# stocklab report",
        f"Generated {dt.date.today().isoformat()} | data source: `{args.source}` | history: {args.years} years\n",
        f"> {DISCLAIMER}\n",
    ]
    if args.source == "synthetic":
        md.append("> **These results use simulated prices.** Run without `--source synthetic` for real market data.\n")

    def sub(**kw):
        ns = argparse.Namespace(**vars(args))
        for k, v in kw.items():
            setattr(ns, k, v)
        return ns

    md.append("## 1. Sell check on current holdings\n")
    summary = cmd_sell_check(sub(holdings=args.holdings), md, args.out)
    md.append("## 2. Which sell signals actually work? (event study)\n")
    cmd_sell_study(sub(tickers=None), md, args.out)
    md.append("## 3. Strategy backtests\n")
    cmd_backtest(sub(tickers=tickers), md, args.out)
    md.append("## 4. Next-day forecasts\n")
    cmd_forecast(sub(tickers=tickers), md, args.out)
    md.append("## 5. Stock screen and entry plans\n")
    cmd_screen(sub(tickers=None), md, args.out)
    md.append("## 6. Portfolio construction\n")
    cmd_portfolio(sub(tickers=tickers + [t for t in DIVERSIFIERS if t not in tickers]), md, args.out)

    if summary is not None and len(summary):
        md.insert(md.index("## 1. Sell check on current holdings\n"), "**Holdings at a glance**\n\n" + md_table(summary, index=False) + "\n")
    path = os.path.join(args.out, "REPORT.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print(f"\nReport written to {path}")


# ---------------------------------------------------------------------- main
def build_parser():
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--source", choices=["yahoo", "csv", "synthetic"], default="yahoo")
    common.add_argument("--csv-dir", help="folder of <TICKER>.csv files (Date, Open, High, Low, Close, Volume)")
    common.add_argument("--years", type=int, default=5)
    common.add_argument("--out", default="reports", help="folder for charts and CSV outputs")

    p = argparse.ArgumentParser(prog="stocklab", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="command", required=True)

    b = sp.add_parser("backtest", parents=[common], help="compare buy/sell rules against buy & hold")
    b.add_argument("--tickers", nargs="+", default=["KLAC", "VRT", "ALAB"])
    b.add_argument("--cost-bps", type=float, default=5)
    b.add_argument("--n-boot", type=int, default=1000, help="bootstrap samples for significance (0 to skip)")

    c = sp.add_parser("sell-check", parents=[common], help="score current holdings: HOLD / WATCH / REDUCE / EXIT")
    c.add_argument("holdings", nargs="+", help="TICKER or TICKER:entry_price, e.g. VRT:262")
    c.add_argument("--stop", type=float, default=0.15, help="your hard stop-loss below entry (0.15 = 15%%)")

    s = sp.add_parser("sell-study", parents=[common], help="test which sell rules predict weaker returns")
    s.add_argument("--tickers", nargs="+")
    s.add_argument("--n-sims", type=int, default=2000)

    f = sp.add_parser("forecast", parents=[common], help="walk-forward next-day forecast vs baselines")
    f.add_argument("--tickers", nargs="+", default=["KLAC", "VRT", "ALAB"])
    f.add_argument("--benchmark", default="SPY")

    sc = sp.add_parser("screen", parents=[common], help="rank stocks and plan entries, stops and sizes")
    sc.add_argument("--tickers", nargs="+")
    sc.add_argument("--capital", type=float, default=100_000)
    sc.add_argument("--risk", type=float, default=0.01, help="max loss per position if its stop hits (0.01 = 1%%)")
    sc.add_argument("--max-position", type=float, default=0.10, help="max weight of any one position")
    sc.add_argument("--top", type=int, default=15)
    sc.add_argument("--no-fundamentals", action="store_true")

    po = sp.add_parser("portfolio", parents=[common], help="build diversified portfolios and compare out of sample")
    po.add_argument("--tickers", nargs="+", default=["KLAC", "VRT", "ALAB"] + DIVERSIFIERS)
    po.add_argument("--lookback", type=int, default=252)
    po.add_argument("--max-weight", type=float, default=0.30)

    r = sp.add_parser("report", parents=[common], help="run everything and write reports/REPORT.md")
    r.add_argument("--holdings", nargs="+", default=["KLAC:208", "VRT:262", "ALAB:333"])
    r.add_argument("--stop", type=float, default=0.15)
    r.add_argument("--cost-bps", type=float, default=5)
    r.add_argument("--n-boot", type=int, default=1000)
    r.add_argument("--n-sims", type=int, default=2000)
    r.add_argument("--benchmark", default="SPY")
    r.add_argument("--capital", type=float, default=100_000)
    r.add_argument("--risk", type=float, default=0.01)
    r.add_argument("--max-position", type=float, default=0.10)
    r.add_argument("--top", type=int, default=15)
    r.add_argument("--no-fundamentals", action="store_true")
    r.add_argument("--lookback", type=int, default=252)
    r.add_argument("--max-weight", type=float, default=0.30)
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    os.makedirs(args.out, exist_ok=True)
    print(DISCLAIMER)
    handlers = {
        "backtest": cmd_backtest,
        "sell-check": cmd_sell_check,
        "sell-study": cmd_sell_study,
        "forecast": cmd_forecast,
        "screen": cmd_screen,
        "portfolio": cmd_portfolio,
    }
    if args.command == "report":
        cmd_report(args)
    else:
        handlers[args.command](args, None, args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
