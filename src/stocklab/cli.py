"""Command-line interface.

    python -m stocklab update                 # refresh everything and the README (what the daily job runs)
    python -m stocklab board                  # today's BUY / HOLD / WATCH / AVOID / REDUCE / SELL labels
    python -m stocklab premarket              # the board at the latest price (pre-market, intraday or after-hours)
    python -m stocklab live                   # the same, redrawn in the terminal every minute (Ctrl+C to stop)
    python -m stocklab report                 # full report in reports/REPORT.md
    python -m stocklab sell-check ALAB AMD:150 --stop 0.15
    python -m stocklab sell-study
    python -m stocklab backtest   --tickers NVDA AMD
    python -m stocklab forecast   --tickers NVDA
    python -m stocklab screen
    python -m stocklab portfolio

Commands without --tickers use the stocks in watchlist.csv.
Add --source synthetic to any command to run offline on simulated prices.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import sys

import pandas as pd
from scipy import stats as st

from . import backtest, board, config, data, findings, forecast, indicators, plots, portfolio, premarket, readme, screener, sell_signals

STUDY_UNIVERSE = sorted(
    set(screener.DEFAULT_UNIVERSE)
    | {"AMD", "MU", "INTC", "QCOM", "LRCX", "AMAT", "ASML", "TSM", "MRVL", "TXN", "ADI", "ON", "ARM"}
)  # the watchlist is added at run time
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


def watchlist(args) -> dict:
    """{ticker: entry price or None} from watchlist.csv (or the built-in default list)."""
    return config.read_watchlist(getattr(args, "watchlist", config.DEFAULT_PATH))


def tickers_or_watchlist(args) -> list[str]:
    return [t.upper() for t in args.tickers] if getattr(args, "tickers", None) else list(watchlist(args))


def load_ind(tickers, args, min_rows=260, skipped=None):
    raw = data.load_many(tickers, args.years, args.source, args.csv_dir, min_rows=min_rows, skipped=skipped)
    return raw, {t: indicators.add_all(d) for t, d in raw.items()}


def skipped_note(skipped: dict) -> str:
    return "Not included: " + "; ".join(f"{t} ({why})" for t, why in skipped.items()) + "." if skipped else ""


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
    skipped = {}
    _, frames = load_ind(tickers_or_watchlist(args), args, min_rows=backtest.MIN_BACKTEST_DAYS, skipped=skipped)
    curves, tables = {}, {}
    if md is not None and skipped:
        md.append(skipped_note(skipped) + "\n")
    for t, d in frames.items():
        table, eq = backtest.backtest_ticker(d, args.cost_bps, n_boot=args.n_boot)
        curves[t], tables[t] = eq, table
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
    return {"curves": curves, "tables": tables, "skipped": sorted(skipped)}


def cmd_sell_check(args, md=None, outdir=None):
    holdings = parse_holdings(args.holdings) if getattr(args, "holdings", None) else watchlist(args)
    _, frames = load_ind(list(holdings), args, min_rows=board.MIN_SIGNAL_DAYS)
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
    tickers = args.tickers or sorted(set(STUDY_UNIVERSE) | set(watchlist(args)))
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
    skipped = {}
    raw, frames = load_ind(tickers_or_watchlist(args), args, min_rows=backtest.MIN_BACKTEST_DAYS, skipped=skipped)
    if md is not None and skipped:
        md.append(skipped_note(skipped) + "\n")
    if outdir:  # charts for stocks no longer forecast would otherwise linger in the report folder
        for name in os.listdir(outdir):
            if name.startswith("forecast_") and name.endswith(".png") and name[9:-4] not in frames:
                os.remove(os.path.join(outdir, name))
    best, pvals = {}, []
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
        # Every model is tested against its naive baseline; the p-values are pooled across stocks
        # and corrected for multiple testing in the summary (findings.forecast_tests).
        for model, p in clf["p (beats majority)"].drop("Majority class (baseline)", errors="ignore").items():
            pvals.append((t, model, "accuracy vs majority class", float(p)))
        for model, p in reg["DM p (beats zero)"].drop("Zero / random walk (baseline)", errors="ignore").items():
            pvals.append((t, model, "error vs zero forecast", float(p)))
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
        min_p = min(p for tt, _, _, p in pvals if tt == t and pd.notna(p))
        verdict = (f"smallest p-value against a naive baseline {min_p:.3f}, before correcting for the four models "
                   "tested here and the other stocks (the corrected count is in the summary)")
        print(f"  Best out-of-sample AUC {best_auc:.3f}; {verdict}")
        best[t] = float(best_auc)
        if md is not None:
            md.append(f"### {t}\n\nWalk-forward test on {len(preds)} unseen days "
                      f"({preds.index[0].date()} to {preds.index[-1].date()}).\n")
            md.append(md_table(clf) + "\n")
            md.append(md_table(reg) + "\n")
            md.append("Forecast for the next session:\n\n```\n" + "\n".join(lines) + "\n```\n")
            md.append(f"Best out-of-sample AUC **{best_auc:.3f}**; {verdict}.\n")
        if outdir:
            plots.forecast_importance(forecast.feature_importance(X, y), os.path.join(outdir, f"forecast_{t}.png"), t)
            if md is not None:
                md.append(f"![{t} feature effects](forecast_{t}.png)\n")
    return {"auc": best, "pvals": pvals}


def cmd_screen(args, md=None, outdir=None):
    tickers = args.tickers or list(dict.fromkeys(list(watchlist(args)) + screener.DEFAULT_UNIVERSE))
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
    tickers = args.tickers or list(dict.fromkeys(list(watchlist(args)) + DIVERSIFIERS))
    skipped = {}
    # A covariance matrix needs the same dates for every asset, so recent listings would cut the
    # window for everyone; they are left out (and named) until they have `lookback` days of history.
    raw, _ = load_ind(tickers, args, min_rows=args.lookback, skipped=skipped)
    prices_all = data.close_matrix(raw)
    rets = prices_all.pct_change().dropna()
    recent = rets.iloc[-args.lookback:]
    w_table, diag = portfolio.build(recent, args.max_weight)
    section(f"Portfolio construction ({len(prices_all.columns)} assets, last {len(recent)} days)")
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
    long_hist = {t: d for t, d in raw.items() if len(d) >= args.lookback + 126}
    excluded = sorted(set(raw) - set(long_hist))
    summ = eq = sfmt = None
    try:
        summ, eq = portfolio.walk_forward(data.close_matrix(long_hist), args.lookback, 21, args.max_weight)
        sfmt = summ.copy()
        for c in ["CAGR", "Volatility", "Max drawdown"]:
            sfmt[c] = sfmt[c].map(lambda v: f"{v:+.1%}")
        sfmt["Sharpe"] = sfmt["Sharpe"].map(lambda v: f"{v:.2f}")
        print(f"\nWalk-forward, monthly rebalance ({eq.index[0].date()} to {eq.index[-1].date()}):")
        print(sfmt.to_string())
    except ValueError as e:
        print(f"  walk-forward skipped: {e}")
    if md is not None:
        if skipped:
            md.append(skipped_note(skipped) + "\n")
        md.append(f"Assets: {', '.join(prices_all.columns)}. Covariance: Ledoit-Wolf shrinkage on the last "
                  f"{len(recent)} trading days.\n\n"
                  f"Weights and share of risk (%):\n\n{md_table(wf, index_label='asset')}\n")
        md.append(md_table(dfmt, index_label="method") + "\n")
        if warns:
            md.append("Concentration warnings:\n\n" + "\n".join(f"- {w}" for w in warns) + "\n")
        if sfmt is not None:
            note = f"; {', '.join(excluded)} left out for lack of history" if excluded else ""
            md.append(f"Out-of-sample comparison, monthly rebalance ({eq.index[0].date()} to {eq.index[-1].date()}{note}):"
                      f"\n\n{md_table(sfmt, index_label='method')}\n")
    if outdir:
        plots.correlation_heatmap(recent, os.path.join(outdir, "portfolio_correlation.png"))
        plots.risk_shares(w_table, os.path.join(outdir, "portfolio_risk_shares.png"))
        if eq is not None:
            plots.portfolio_curves(eq, os.path.join(outdir, "portfolio_walk_forward.png"))
        if md is not None:
            md.append("![Correlations](portfolio_correlation.png)\n\n![Risk shares](portfolio_risk_shares.png)\n")
            if eq is not None:
                md.append("![Walk-forward](portfolio_walk_forward.png)\n")
    return {"w_table": w_table, "diag": diag, "assets": list(prices_all.columns), "skipped": skipped}


def board_frame(table: pd.DataFrame) -> pd.DataFrame:
    """Readable board for the terminal and the report."""
    out = pd.DataFrame(index=table.index)
    out["action"] = table["action"] + table["provisional"].map({True: "*", False: ""})
    out["close"] = table["close"].map(lambda v: f"{v:,.2f}")
    out["1 day"] = table["change_1d"].map(pct)
    out["1 month"] = table["change_1m"].map(pct)
    out["buy rank"] = table["buy_rank"]
    out["sell warnings"] = table["sell_warnings"]
    buyable = table["action"].isin(["BUY", "HOLD", "WATCH"])  # entry levels only where buying is on the table
    for c, label in [("pullback_entry", "pullback entry"), ("breakout_trigger", "breakout"), ("stop", "stop")]:
        vals = table[c] if c in table else pd.Series(float("nan"), index=table.index)
        out[label] = [f"{v:,.2f}" if ok and pd.notna(v) else "" for v, ok in zip(vals, buyable)]
    if "pnl" in table:
        out["your P&L"] = table["pnl"].map(pct)
    out["why"] = [board.why(r) for _, r in table.iterrows()]
    out.index.name = "ticker"
    return out


def cmd_board(args, md=None, outdir=None):
    wl = watchlist(args)
    tickers = [t.upper() for t in args.tickers] if getattr(args, "tickers", None) else list(wl)
    skipped = {}
    _, frames = load_ind(tickers, args, min_rows=1, skipped=skipped)
    if not frames:
        raise SystemExit("No price data could be loaded for the watchlist.")
    table, pan = board.today(frames, entries=wl, stop_pct=args.stop, capital=args.capital, risk_per_trade=args.risk,
                             max_weight=args.max_position)
    as_of = max(table["as_of"])
    section(f"Decision board ({len(table)} stocks, data as of {as_of})")
    bf = board_frame(table)
    print(bf.to_string())
    for t, why in skipped.items():
        print(f"  {t}: not on the board ({why})")
    evaluation = None
    bench = None
    if args.benchmark:
        try:
            bench = data.load(args.benchmark, args.years, args.source, args.csv_dir)["Close"].rename(args.benchmark)
        except Exception as e:
            print(f"  benchmark {args.benchmark} unavailable ({e})")
    try:
        evaluation = board.evaluate(pan, bench, cost_bps=args.cost_bps, n_boot=args.n_boot)
    except ValueError as e:
        print(f"  board evaluation skipped: {e}")
    if evaluation:
        etab = evaluation["table"].copy()
        for c in ["CAGR", "Max drawdown"]:
            etab[c] = etab[c].map(lambda v: f"{v:+.1%}")
        etab["Volatility"] = etab["Volatility"].map(lambda v: f"{v:.1%}")
        etab["Sharpe"] = etab["Sharpe"].map(lambda v: f"{v:.2f}")
        etab["Time invested"] = etab["Time invested"].map(lambda v: "" if pd.isna(v) else f"{v:.0%}")
        etab["Avg holdings"] = etab["Avg holdings"].map(lambda v: "" if pd.isna(v) else f"{v:.1f}")
        lab = evaluation["labels"].copy()
        col = [c for c in lab.columns if c.startswith("mean")][0]
        lab[col] = lab[col].map(pct)
        lab["hit rate"] = lab["hit rate"].map(lambda v: "" if pd.isna(v) else f"{v:.0%}")
        lab["p_value"] = lab["p_value"].map(lambda v: "" if pd.isna(v) else f"{v:.2f}")
        test = evaluation["sharpe_test"]
        print(f"\nTrading the labels, {evaluation['start'].date()} to {evaluation['end'].date()}:")
        print(etab.to_string())
        if test:
            print(f"  Sharpe difference vs equal weight {test['diff']:+.2f}, 95% CI [{test['ci_low']:+.2f}, {test['ci_high']:+.2f}]")
        print("\nForward 21-day return after each label, relative to the watchlist average:")
        print(lab.to_string())
    if md is not None:
        md.append(f"Data as of the {as_of} close. `*` = provisional (under 200 trading days of history).\n")
        md.append(md_table(bf) + "\n")
        if skipped:
            md.append(skipped_note(skipped) + "\n")
        md.append("![Board label each week](board_history.png)\n")
        if evaluation:
            md.append(f"**Trading the labels** ({evaluation['start'].date()} to {evaluation['end'].date()}): buy on BUY, "
                      "exit on SELL, REDUCE or AVOID, reviewed weekly with next-day execution and 5 bp costs.\n")
            md.append(md_table(etab, index_label="strategy") + "\n")
            if test:
                md.append(f"Sharpe difference vs equal weight: {test['diff']:+.2f}, 95% block-bootstrap CI "
                          f"[{test['ci_low']:+.2f}, {test['ci_high']:+.2f}].\n")
            md.append("Forward 21-day return after each label, relative to the watchlist average on the same date "
                      "(sampled every 21 days, t-test across dates):\n")
            md.append(md_table(lab, index_label="label") + "\n")
            md.append("![Board strategy vs holding](board_equity.png)\n")
    if outdir:
        plots.board_history(pan["action"], os.path.join(outdir, "board_history.png"))
        if evaluation:
            plots.board_equity(evaluation["equity"], os.path.join(outdir, "board_equity.png"))
        table.to_csv(os.path.join(outdir, "board.csv"))
    return {"table": table, "evaluation": evaluation, "as_of": as_of, "skipped": skipped}


def gap_table(g: dict) -> pd.DataFrame:
    b = g["buckets"].copy()
    b["avg gap"] = b["avg gap"].map(pct)
    b["avg open-to-close"] = b["avg open-to-close"].map(lambda v: "" if pd.isna(v) else f"{v:+.2%}")
    b["closed above open"] = b["closed above open"].map(lambda v: "" if pd.isna(v) else f"{v:.0%}")
    return b


def cmd_gaps(args, md=None, outdir=None, frames=None):
    """Gap study on the watchlist: do opening gaps continue or reverse during the session?"""
    if frames is None:
        _, frames = load_ind(list(watchlist(args)), args, min_rows=board.MIN_SIGNAL_DAYS)
    g = premarket.gap_study(frames, n_boot=args.n_boot)
    if not g:
        print("  gap study skipped: not enough history")
        return g
    section("Opening gaps vs the regular session")
    print(gap_table(g).to_string())
    print("\n" + premarket.gap_sentence(g))
    if md is not None:
        md.append(premarket.gap_sentence(g) + "\n")
        md.append(md_table(gap_table(g), index_label="opening gap") + "\n")
    return g


def timing_table(c: dict) -> pd.DataFrame:
    t = c["table"].copy()
    for col in ["CAGR", "Max drawdown"]:
        t[col] = t[col].map(lambda v: f"{v:+.1%}")
    t["Volatility"] = t["Volatility"].map(lambda v: f"{v:.1%}")
    t["Sharpe"] = t["Sharpe"].map(lambda v: f"{v:.2f}")
    return t


def cmd_timing(args, md=None, outdir=None, frames=None):
    """Deciding before the open (pre-market price) vs at the previous close, on the same trading days."""
    if frames is None:
        _, frames = load_ind(list(watchlist(args)), args, min_rows=board.MIN_SIGNAL_DAYS)
    print("Testing pre-market labels against close labels (about a minute)...")
    c = premarket.compare_timing(frames, cost_bps=args.cost_bps, n_boot=args.n_boot)
    if not c:
        print("  timing test skipped: not enough history")
        return c
    section("Deciding before the open vs at the previous close")
    print(timing_table(c).to_string())
    text = premarket.timing_sentence(c)
    print("\n" + text.replace("**", ""))
    if md is not None:
        md.append(text + "\n")
        md.append(md_table(timing_table(c), index_label="strategy") + "\n")
        md.append("The pre-market version uses the official opening price as a stand-in for the last pre-market trade "
                  "(free pre-market history is only days long), which slightly flatters it.\n")
    if outdir:  # the morning job reuses this instead of re-running a minute-long test
        import json

        with open(os.path.join(outdir, "timing_test.json"), "w", encoding="utf-8") as f:
            json.dump({"sentence": text, "end": str(c["end"].date())}, f, indent=2)
    return c


def _board_inputs(args):
    """Watchlist, daily frames and the close-based board that the latest-price views start from."""
    wl = watchlist(args)
    tickers = [t.upper() for t in args.tickers] if getattr(args, "tickers", None) else list(wl)
    _, frames = load_ind(tickers, args, min_rows=1)
    if not frames:
        raise SystemExit("No price data could be loaded for the watchlist.")
    table, _ = board.today(frames, entries=wl, stop_pct=args.stop, capital=args.capital, risk_per_trade=args.risk,
                           max_weight=args.max_position)
    return wl, frames, table


def _latest_show(v: pd.DataFrame) -> pd.DataFrame:
    """The latest-price board as a printable table."""
    show = pd.DataFrame(index=v.index)
    show["label now"] = v["premarket_label"] + v["changed"].map({True: " (changed)", False: ""})
    show["board at close"] = v["board"]
    show["close"] = v["close"].map(lambda x: f"{x:,.2f}")
    show["latest"] = v["price"].map(lambda x: "" if pd.isna(x) else f"{x:,.2f}")
    show["change"] = v["change"].map(pct)
    for c, label in [("pm_pullback_entry", "pullback entry"), ("pm_breakout", "breakout"), ("pm_stop", "stop")]:
        show[label] = v[c].map(lambda x: "" if pd.isna(x) else f"{x:,.2f}") if c in v else ""
    show["session"] = v["session"]
    show["what the move changes"] = v["crossed"]
    show.index.name = "ticker"
    return show


def cmd_premarket(args, md=None, outdir=None):
    """The board's rules with each stock's latest trade (pre-market, intraday or after-hours) as today's price."""
    wl, frames, table = _board_inputs(args)
    snap = premarket.snapshot(list(frames), args.source, frames)
    if snap.empty:
        raise SystemExit("No pre-market or intraday prices could be downloaded; nothing updated.")
    gaps = premarket.gap_study(frames, n_boot=args.n_boot)
    v = premarket.view(frames, table, snap, gaps, entries=wl, stop_pct=args.stop)
    out = args.out
    os.makedirs(out, exist_ok=True)

    timing_text = ""
    gap_text = premarket.gap_sentence(gaps) if gaps else ""
    path = os.path.join(out, "timing_test.json")
    if os.path.exists(path):
        import json

        with open(path, encoding="utf-8") as f:
            payload = json.load(f)
        timing_text = payload.get("sentence", "")
        if payload.get("stability"):
            timing_text += f" *Stability: {payload['stability']}.*"
        if gap_text and payload.get("gap_stability"):
            gap_text += f" *Stability: {payload['gap_stability']}.*"
    else:
        timing_text = premarket.timing_sentence(cmd_timing(args, None, out, frames))

    latest = max(pd.Timestamp(t) for t in snap["time"])
    session = premarket.session_of(latest)
    when = latest.strftime("%H:%M ET on %Y-%m-%d")
    title = readme.LATEST_TITLES.get(session, "Board at the latest prices")
    section(f"{title} ({when})")
    show = _latest_show(v)
    print(show.to_string())
    if timing_text:
        print("\n" + timing_text.replace("*", ""))
    if gaps:
        print("\n" + gap_text.replace("*", ""))

    md_lines = [f"# {title}, {when}\n", f"> {DISCLAIMER}\n",
                "The board's rules with each stock's latest trade standing in for today's close; the history before it "
                "is daily closes. The volume rules keep their value from the last close, so a label changes only when "
                "the price move switches a price-based rule (the last column says which).\n",
                md_table(show) + "\n"]
    if timing_text:
        md_lines += ["## Does deciding before the open help?\n", timing_text + "\n"]
    if gaps:
        md_lines += ["## Do opening gaps carry into the day?\n", gap_text + "\n",
                     md_table(gap_table(gaps), index_label="opening gap") + "\n"]
    with open(os.path.join(out, "PREMARKET.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    log = v.reset_index()[["ticker", "board", "premarket_label", "close", "price", "change", "session", "time"]]
    log_path = os.path.join(out, "premarket_log.csv")
    if os.path.exists(log_path):
        old = pd.read_csv(log_path)
        if "what_if" in old and "premarket_label" not in old:  # logs written before the column was renamed
            old["premarket_label"] = old.pop("what_if").astype(str).str.replace(" (changed)", "", regex=False)
        log = pd.concat([old, log]).drop_duplicates(["ticker", "time"], keep="last")
    log[[c for c in log.columns if c in ("ticker", "board", "premarket_label", "close", "price", "change", "session",
                                          "time")]].to_csv(log_path, index=False, float_format="%.4f")
    print(f"\nWritten: {os.path.join(out, 'PREMARKET.md')}")
    if getattr(args, "readme", None) and args.readme.lower() != "none":
        base = os.path.dirname(os.path.abspath(args.readme))
        rel = os.path.relpath(os.path.abspath(out), base).replace(os.sep, "/")
        block = readme.render_premarket(v, gaps, gap_text, when, session, args.source,
                                        f"{rel}/PREMARKET.md", timing_text)
        readme.write(args.readme, block, readme.PM_START, readme.PM_END)
        print(f"Latest-price section of {args.readme} updated.")
    return {"view": v, "gaps": gaps}


def sub_args(args, **kw):
    ns = argparse.Namespace(**vars(args))
    for k, v in kw.items():
        setattr(ns, k, v)
    return ns


def cmd_report(args):
    """Run every module and write REPORT.md with tables and charts. Returns the results for the README."""
    os.makedirs(args.out, exist_ok=True)
    wl = watchlist(args)
    md = [
        "# stocklab report",
        f"Generated {dt.date.today().isoformat()} | data source: `{args.source}` | history: {args.years} years | "
        f"watchlist: {', '.join(wl)}\n",
        f"> {DISCLAIMER}\n",
    ]
    if args.source == "synthetic":
        md.append("> **These results use simulated prices.** Run without `--source synthetic` for real market data.\n")

    md.append("## 1. Decision board\n")
    board_res = cmd_board(sub_args(args, tickers=None), md, args.out)
    md.append("## 2. Sell check, stock by stock\n")
    cmd_sell_check(sub_args(args, holdings=None), md, args.out)
    md.append("## 3. Which sell signals actually work? (event study)\n")
    study = cmd_sell_study(sub_args(args, tickers=None), md, args.out)
    md.append("## 4. Strategy backtests\n")
    bt = cmd_backtest(sub_args(args, tickers=None), md, args.out)
    md.append("## 5. Next-day forecasts\n")
    fc = cmd_forecast(sub_args(args, tickers=None), md, args.out)
    md.append("## 6. Stock screen and entry plans\n")
    cmd_screen(sub_args(args, tickers=None), md, args.out)
    md.append("## 7. Portfolio construction\n")
    pf = cmd_portfolio(sub_args(args, tickers=None), md, args.out)
    md.append("## 8. Opening gaps: do pre-market moves carry into the day?\n")
    gaps = cmd_gaps(sub_args(args, tickers=None), md, args.out)
    md.append("## 9. Deciding before the open vs at the previous close\n")
    timing = cmd_timing(sub_args(args, tickers=None), md, args.out)

    path = os.path.join(args.out, "REPORT.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print(f"\nReport written to {path}")
    return {"board": board_res, "study": study, "backtest": bt, "forecast": fc, "portfolio": pf, "gaps": gaps,
            "timing": timing, "watchlist": wl}


def key_findings(res: dict, stab: dict | None = None) -> dict:
    """Plain-English summary lines computed from the latest run (no hand-written numbers).

    `stab` adds, for each line, how many recent runs reached the same verdict.
    """
    stab = stab or {}
    out = {}

    def tail(key):
        return f" *Stability: {stab[key]}.*" if stab.get(key) else ""

    study = res.get("study")
    if study is not None and len(study):
        useful = study[study["verdict"] == "useful"]
        names = ", ".join(f"{r.rule} ({r.horizon})" for r in useful.itertuples())
        out["study"] = (f"Sell-signal event study: **{len(useful)} of {len(study)}** rule-by-horizon tests show significantly "
                        f"weaker returns after the signal once the false discovery rate is controlled (q < 0.10)"
                        + (f": {names}." if names else ".") + tail("study"))
    tables = (res.get("backtest") or {}).get("tables") or {}
    if tables:
        bt = findings.backtest_counts(tables)
        verdict = ("no more than chance alone would produce, so no rule has shown an edge" if not bt["beyond_chance"]
                   else "more than chance alone would produce (binomial p "
                   + ("< 0.001)" if bt["p_more"] < 0.001 else f"= {bt['p_more']:.3f})"))
        out["backtest"] = (f"Single-stock rule backtests: of {bt['total']} rule-by-stock tests on {len(tables)} stocks, "
                           f"**{bt['better']}** had a significantly higher Sharpe ratio than buy & hold and {bt['worse']} a "
                           f"significantly lower one. About {bt['expected']:.1f} of each would be expected by chance with "
                           f"{bt['total']} tests: {verdict}." + tail("backtest"))
    fc = res.get("forecast") or {}
    if fc.get("pvals"):
        f = findings.forecast_tests(fc)
        if f["significant"]:
            verdict = f"a possible edge worth watching: {', '.join(f['hits'])}"
        else:
            verdict = f"no reliable edge (smallest uncorrected p-value {f['min_p']:.3f})"
        out["forecast"] = (f"Next-day forecasts: **{f['significant']} of {f['tests']}** model-vs-baseline tests (4 models x "
                           f"{f['stocks']} stocks) beat their naive baseline once the false discovery rate is controlled "
                           f"(q < 0.10), with a median out-of-sample AUC of {f['median_auc']:.2f} (0.50 is a coin flip): "
                           f"{verdict}." + tail("forecast"))
    pf = res.get("portfolio")
    if pf:
        rs = pf["w_table"][("risk share", "Equal weight")].sort_values(ascending=False)
        top = rs.head(3)
        wl = set(res.get("watchlist") or [])
        wl_share = rs[[t for t in rs.index if t in wl]].sum()
        n_wl = sum(t in wl for t in rs.index)
        out["portfolio"] = (f"Risk concentration: in an equal-weight portfolio of {len(rs)} assets ({n_wl} watchlist stocks plus "
                            f"{len(rs) - n_wl} diversifiers), the watchlist stocks make up {n_wl / len(rs):.0%} of the money and "
                            f"**{wl_share:.0%} of the risk**; the largest risk contributors are {', '.join(top.index)}.")
        if pf.get("skipped"):
            out["portfolio"] += f" Not yet included for lack of history: {', '.join(pf['skipped'])}."
    tm = res.get("timing")
    if tm:
        text = premarket.timing_sentence(tm)
        out["timing"] = "Pre-market vs close: " + text[0].lower() + text[1:] + tail("timing")
    g = res.get("gaps")
    if g:
        text = premarket.gap_sentence(g)
        out["gaps"] = "Opening gaps: " + text[0].lower() + text[1:] + tail("gaps")
    return out


def append_log(table: pd.DataFrame, path: str, display_path: str | None = None) -> str:
    """Append today's labels to a running log: the board's live, out-of-sample track record."""
    rows = table.reset_index()[["as_of", "ticker", "action", "close", "buy_score", "sell_warnings"]]
    rows = rows.rename(columns={"as_of": "date"})
    if os.path.exists(path):
        old = pd.read_csv(path, dtype={"date": str})
        rows = pd.concat([old, rows]).drop_duplicates(["date", "ticker"], keep="last")
    rows = rows.sort_values(["date", "ticker"])
    rows.to_csv(path, index=False, float_format="%.4f")
    first, days = rows["date"].min(), rows["date"].nunique()
    shown = (display_path or path).replace(os.sep, "/")
    return (f"Live track record: {days} trading day{'s' if days != 1 else ''} of labels logged since {first} "
            f"in [`{shown}`]({shown}), so the board can later be judged on signals it published before the prices moved.")


def prefetch_for(args) -> None:
    """Batch-download everything a command will need (Yahoo only), so it makes one request, not dozens."""
    if args.source != "yahoo":
        return
    wl = list(watchlist(args))
    extra = {
        "report": STUDY_UNIVERSE + screener.DEFAULT_UNIVERSE + DIVERSIFIERS,
        "sell-study": STUDY_UNIVERSE,
        "screen": screener.DEFAULT_UNIVERSE,
        "portfolio": DIVERSIFIERS,
        "premarket": [],
        "live": [],
    }.get(args.command, [])
    chosen = getattr(args, "tickers", None) or [h.split(":")[0] for h in (getattr(args, "holdings", None) or [])] or wl
    data.prefetch([t.upper() for t in chosen] + extra + [getattr(args, "benchmark", "SPY")], args.years, args.source, args.csv_dir)


def cmd_live(args, md=None, outdir=None):
    """The board at the latest price, redrawn in the terminal every --every seconds until Ctrl+C.

    Nothing is written to disk or to the README. The daily history is reloaded when the New
    York date changes and again once the day's close is final (16:15 ET).
    """
    import time

    every = max(15, int(args.every))

    def stamp():
        now = premarket.now_ny()
        return now.date(), now.hour * 60 + now.minute >= 16 * 60 + 15

    loaded, before = None, {}
    try:
        while True:
            if loaded != stamp():
                if loaded is not None:
                    data._CACHE.clear()
                    prefetch_for(args)
                wl, frames, table = _board_inputs(args)
                loaded = stamp()
            snap = premarket.snapshot(list(frames), args.source, frames)
            cleared = sys.stdout.isatty() and not args.once
            if cleared:
                os.system("cls" if os.name == "nt" else "clear")
            checked = premarket.now_ny()
            if snap.empty:
                print(f"{checked:%H:%M:%S} ET: no prices could be downloaded.")
            else:
                v = premarket.view(frames, table, snap, entries=wl, stop_pct=args.stop)
                latest = max(pd.Timestamp(t) for t in snap["time"])
                session = premarket.session_of(latest)
                print(f"{readme.LATEST_TITLES.get(session, 'Board at the latest prices')}: last trade "
                      f"{latest:%Y-%m-%d %H:%M} ET, checked {checked:%H:%M:%S} ET\n")
                print(_latest_show(v).drop(columns="session").to_string())
                labels = v["premarket_label"].to_dict()
                moved = [f"{t} {before[t]} -> {lab}" for t, lab in labels.items() if before.get(t) and before[t] != lab]
                if moved:
                    print("\nChanged since the last refresh: " + "; ".join(moved))
                before = labels
                if session == "closed":
                    print("\nThe US market is closed; prices start moving again at 04:00 ET on the next weekday.")
            print(("\n" + DISCLAIMER if cleared else "") + "\nThe close-based board is the tested one; a label at an "
                  "intraday price can change by the close.")
            if args.once:
                return
            print(f"Refreshing every {every} seconds. Press Ctrl+C to stop.")
            time.sleep(every)
    except KeyboardInterrupt:
        print("\nStopped.")


def cmd_update(args):
    """Refresh data, the full report, the signal log and the README's live section."""
    wl = watchlist(args)
    print("Downloading prices...")
    prefetch_for(sub_args(args, command="report"))
    loaded = data.load_many(list(wl), args.years, args.source, args.csv_dir, verbose=False)
    if len(loaded) < max(1, len(wl) // 2):
        raise SystemExit(f"Only {len(loaded)} of {len(wl)} watchlist stocks loaded; not updating the README.")
    res = cmd_report(args)
    write_readme = args.readme and args.readme.lower() != "none"
    base = os.path.dirname(os.path.abspath(args.readme)) if write_readme else os.getcwd()
    rel = os.path.relpath(os.path.abspath(args.out), base).replace(os.sep, "/")
    log_info = append_log(res["board"]["table"], os.path.join(args.out, "board_log.csv"), f"{rel}/board_log.csv")
    flog = findings.append(findings.record(res, res["board"]["as_of"]), os.path.join(args.out, "findings_log.csv"))
    stab = findings.stability(flog, res["board"]["as_of"])
    print(f"Findings log: {len(flog)} run(s) recorded in {os.path.join(args.out, 'findings_log.csv')}")
    timing_json = os.path.join(args.out, "timing_test.json")
    if os.path.exists(timing_json) and (stab.get("timing") or stab.get("gaps")):  # the morning job shows the same notes
        import json

        with open(timing_json, encoding="utf-8") as f:
            payload = json.load(f)
        payload["stability"] = stab.get("timing", "")
        payload["gap_stability"] = stab.get("gaps", "")
        with open(timing_json, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)
    if write_readme:
        bt = res.get("backtest") or {}
        results = findings.rule_results(bt.get("tables") or {})
        chart = None
        if len(results):
            plots.rule_heatmap(results, os.path.join(args.out, "rules_vs_buyhold.png"))
            chart = f"{rel}/rules_vs_buyhold.png"
        rules_md = readme.render_rules(results, findings.backtest_counts(bt.get("tables") or {}), chart,
                                       f"{rel}/REPORT.md", bt.get("skipped"), args.cost_bps)
        block = readme.render(res["board"]["table"], res["board"]["evaluation"], key_findings(res, stab),
                              res["board"]["as_of"], args.source, rel, f"{rel}/REPORT.md", log_info,
                              board_stability=stab.get("board"), rules_section=rules_md)
        readme.write(args.readme, block)
        print(f"Live section of {args.readme} updated.")


# ---------------------------------------------------------------------- main
def build_parser():
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--source", choices=["yahoo", "csv", "synthetic"], default="yahoo")
    common.add_argument("--csv-dir", help="folder of <TICKER>.csv files (Date, Open, High, Low, Close, Volume)")
    common.add_argument("--years", type=int, default=5)
    common.add_argument("--out", default="reports", help="folder for charts and CSV outputs")
    common.add_argument("--watchlist", default=config.DEFAULT_PATH, help="CSV of tickers (and optional entry prices)")

    trade = argparse.ArgumentParser(add_help=False)
    trade.add_argument("--stop", type=float, default=0.15, help="your stop-loss below entry price (0.15 = 15%%)")
    trade.add_argument("--capital", type=float, default=100_000, help="account size used for position sizing")
    trade.add_argument("--risk", type=float, default=0.01, help="max loss per position if its stop hits (0.01 = 1%%)")
    trade.add_argument("--max-position", type=float, default=0.10, help="max weight of any one position")
    trade.add_argument("--cost-bps", type=float, default=5, help="trading cost per side, basis points")
    trade.add_argument("--n-boot", type=int, default=1000, help="bootstrap samples for significance (0 to skip)")
    trade.add_argument("--benchmark", default="SPY")

    full = argparse.ArgumentParser(add_help=False)
    full.add_argument("--n-sims", type=int, default=2000)
    full.add_argument("--top", type=int, default=15)
    full.add_argument("--no-fundamentals", action="store_true")
    full.add_argument("--lookback", type=int, default=252)
    full.add_argument("--max-weight", type=float, default=0.30)

    p = argparse.ArgumentParser(prog="stocklab", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="command", required=True)

    u = sp.add_parser("update", parents=[common, trade, full], help="refresh the report, the signal log and the README")
    u.add_argument("--readme", default="README.md", help="README to refresh ('none' to skip)")

    sp.add_parser("report", parents=[common, trade, full], help="run everything and write reports/REPORT.md")

    bd = sp.add_parser("board", parents=[common, trade], help="today's buy/sell labels for the watchlist")
    bd.add_argument("--tickers", nargs="+")

    pm = sp.add_parser("premarket", parents=[common, trade],
                       help="the board's rules at the latest price (pre-market, intraday or after-hours), "
                            "plus the timing and gap tests")
    pm.add_argument("--tickers", nargs="+")
    pm.add_argument("--readme", default="README.md", help="README whose pre-market section to refresh ('none' to skip)")

    lv = sp.add_parser("live", parents=[common, trade],
                       help="the board at the latest price, redrawn in the terminal every minute (Ctrl+C to stop)")
    lv.add_argument("--tickers", nargs="+")
    lv.add_argument("--every", type=int, default=60, help="seconds between refreshes (minimum 15)")
    lv.add_argument("--once", action="store_true", help="refresh once and exit")

    b = sp.add_parser("backtest", parents=[common, trade], help="compare buy/sell rules against buy & hold")
    b.add_argument("--tickers", nargs="+")

    c = sp.add_parser("sell-check", parents=[common, trade], help="score holdings: HOLD / WATCH / REDUCE / EXIT")
    c.add_argument("holdings", nargs="*", help="TICKER or TICKER:entry_price, e.g. NVDA:180 (default: watchlist)")

    s = sp.add_parser("sell-study", parents=[common, full], help="test which sell rules predict weaker returns")
    s.add_argument("--tickers", nargs="+")

    f = sp.add_parser("forecast", parents=[common, trade], help="walk-forward next-day forecast vs baselines")
    f.add_argument("--tickers", nargs="+")

    sc = sp.add_parser("screen", parents=[common, trade, full], help="rank stocks and plan entries, stops and sizes")
    sc.add_argument("--tickers", nargs="+")

    po = sp.add_parser("portfolio", parents=[common, full], help="build diversified portfolios and compare out of sample")
    po.add_argument("--tickers", nargs="+")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    os.makedirs(args.out, exist_ok=True)
    print(DISCLAIMER)
    handlers = {
        "board": cmd_board,
        "premarket": cmd_premarket,
        "live": cmd_live,
        "backtest": cmd_backtest,
        "sell-check": cmd_sell_check,
        "sell-study": cmd_sell_study,
        "forecast": cmd_forecast,
        "screen": cmd_screen,
        "portfolio": cmd_portfolio,
    }
    if args.command == "update":
        cmd_update(args)
        return 0
    prefetch_for(args)
    if args.command == "report":
        cmd_report(args)
    else:
        handlers[args.command](args, None, args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
