"""Static charts for the generated report (PNG, readable on GitHub in light mode)."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.colors import LinearSegmentedColormap  # noqa: E402
from matplotlib.ticker import FuncFormatter, LogLocator, NullFormatter  # noqa: E402

# Fixed categorical order (never cycled), plus neutral inks and surfaces
SERIES = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948"]
SURFACE, INK, INK2, MUTED, GRID, AXIS = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
DIVERGING = LinearSegmentedColormap.from_list("div", ["#eb6834", "#f0efec", "#2a78d6"])

plt.rcParams.update(
    {
        "figure.facecolor": SURFACE,
        "axes.facecolor": SURFACE,
        "axes.edgecolor": AXIS,
        "axes.labelcolor": INK2,
        "axes.titlecolor": INK,
        "axes.titlesize": 12,
        "axes.titleweight": "bold",
        "axes.titlelocation": "left",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.color": GRID,
        "grid.linewidth": 0.6,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "text.color": INK,
        "legend.frameon": False,
        "legend.fontsize": 8,
        "font.size": 9,
    }
)


def equity_curves(curves: dict[str, pd.DataFrame], path: str):
    """One panel per ticker; each strategy keeps its colour across panels."""
    names = list(next(iter(curves.values())).columns)
    fig, axes = plt.subplots(len(curves), 1, figsize=(10, 3.4 * len(curves)), squeeze=False)
    for ax, (t, c) in zip(axes[:, 0], curves.items()):
        for i, name in enumerate(names):
            lw = 2.4 if name == "Buy & Hold" else 1.3
            ax.plot(c.index, c[name], color=SERIES[i % len(SERIES)], lw=lw, label=name)
        ax.set_yscale("log")
        ax.yaxis.set_major_locator(LogLocator(base=10, subs=(1.0, 2.0, 5.0)))
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"${v:g}"))
        ax.yaxis.set_minor_formatter(NullFormatter())
        ax.set_title(f"{t}: growth of $1 by strategy (log scale)")
    axes[0, 0].legend(ncol=4, loc="upper left")
    fig.tight_layout()
    fig.savefig(path, dpi=130)
    plt.close(fig)


def event_study(res: pd.DataFrame, path: str, horizon: str = "63d"):
    """Forward-return gap after each sell rule vs random days; filled bars are significant (q < 0.10)."""
    d = res[(res["horizon"] == horizon) & (res["events"] >= 5)].sort_values("difference")
    fig, ax = plt.subplots(figsize=(9, 0.42 * len(d) + 1.4))
    y = np.arange(len(d))
    sig = d["q_value"] < 0.10
    colors = [SERIES[1] if v < 0 else SERIES[0] for v in d["difference"]]
    # Significant results are solid; non-significant ones are faded so they don't read as findings
    alphas = [1.0 if s else 0.35 for s in sig]
    for yi, (v, c, a) in enumerate(zip(d["difference"], colors, alphas)):
        ax.barh(yi, v * 100, color=c, alpha=a, height=0.6)
    ax.set_yticks(y, [f"{r}  (n={n})" for r, n in zip(d["rule"], d["events"])])
    ax.axvline(0, color=AXIS, lw=1)
    ax.set_xlabel(f"Mean {horizon} return after signal minus random days (percentage points)")
    ax.set_title(f"Do sell signals predict weaker {horizon} returns?", pad=20)
    ax.text(0, 1.01, "Solid: significant after false-discovery-rate control (q < 0.10).  Faded: not significant.", transform=ax.transAxes, color=INK2, fontsize=8, va="bottom")
    ax.grid(axis="y", visible=False)
    fig.tight_layout()
    fig.savefig(path, dpi=130)
    plt.close(fig)


def correlation_heatmap(returns: pd.DataFrame, path: str):
    corr = returns.corr()
    n = len(corr)
    fig, ax = plt.subplots(figsize=(1.0 + 0.7 * n, 0.8 + 0.6 * n))
    im = ax.imshow(corr, cmap=DIVERGING, vmin=-1, vmax=1)
    ax.set_xticks(range(n), corr.columns, rotation=45, ha="right")
    ax.set_yticks(range(n), corr.columns)
    ax.grid(False)
    for i in range(n):
        for j in range(n):
            ax.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center", fontsize=8, color=INK)
    fig.colorbar(im, ax=ax, shrink=0.8)
    ax.set_title("Daily return correlations")
    fig.tight_layout()
    fig.savefig(path, dpi=130)
    plt.close(fig)


def portfolio_curves(eq: pd.DataFrame, path: str):
    fig, ax = plt.subplots(figsize=(10, 3.6))
    for i, name in enumerate(eq.columns):
        ax.plot(eq.index, eq[name], color=SERIES[i], lw=1.6, label=name)
    ax.set_title("Walk-forward portfolios, rebalanced monthly (growth of $1)")
    ax.legend(ncol=4, loc="upper left")
    fig.tight_layout()
    fig.savefig(path, dpi=130)
    plt.close(fig)


def risk_shares(w_table: pd.DataFrame, path: str):
    """Weight vs share of risk, side by side, for equal weight and risk parity."""
    methods = ["Equal weight", "Risk parity"]
    tickers = list(w_table.index)
    fig, axes = plt.subplots(1, 2, figsize=(10, 0.4 * len(tickers) + 1.6), sharey=True, sharex=True)
    y = np.arange(len(tickers))
    for ax, m in zip(axes, methods):
        ax.barh(y + 0.18, w_table[("weight", m)] * 100, height=0.34, color=SERIES[0], label="% of dollars")
        ax.barh(y - 0.18, w_table[("risk share", m)] * 100, height=0.34, color=SERIES[1], label="% of risk")
        ax.set_title(m)
        ax.set_yticks(y, tickers)
        ax.grid(axis="y", visible=False)
    handles, labels = axes[0].get_legend_handles_labels()
    fig.suptitle("Where the money is vs where the risk is", x=0.01, ha="left", fontweight="bold")
    fig.legend(handles, labels, loc="upper right", ncol=2)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(path, dpi=130)
    plt.close(fig)


def forecast_importance(coef: pd.Series, path: str, ticker: str):
    c = coef.iloc[:10][::-1]
    fig, ax = plt.subplots(figsize=(8, 3.6))
    ax.barh(range(len(c)), c.values, color=[SERIES[0] if v > 0 else SERIES[1] for v in c.values], height=0.6)
    ax.set_yticks(range(len(c)), c.index)
    ax.axvline(0, color=AXIS, lw=1)
    ax.set_xlabel("Standardized logistic coefficient (effect on P(up tomorrow))")
    ax.set_title(f"{ticker}: what the next-day model leans on")
    ax.grid(axis="y", visible=False)
    fig.tight_layout()
    fig.savefig(path, dpi=130)
    plt.close(fig)


# Board labels are states, so they use the reserved status colours plus neutrals
ACTION_COLORS = {
    "BUY": "#0ca30c",
    "HOLD": "#86b6ef",
    "WATCH": "#fab219",
    "AVOID": "#c3c2b7",
    "REDUCE": "#ec835a",
    "SELL": "#d03b3b",
    "NO SIGNAL": "#f0efec",
}


def board_equity(eq: pd.DataFrame, path: str):
    """Board strategy vs equal-weight watchlist vs benchmark (log scale)."""
    fig, ax = plt.subplots(figsize=(10, 3.8))
    for i, name in enumerate(eq.columns):
        ax.plot(eq.index, eq[name], color=SERIES[i], lw=2.2 if i == 0 else 1.4, label=name)
    ax.set_yscale("log")
    ax.yaxis.set_major_locator(LogLocator(base=10, subs=(1.0, 2.0, 5.0)))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"${v:g}"))
    ax.yaxis.set_minor_formatter(NullFormatter())
    ax.set_title("Trading the board's labels: growth of $1 (log scale)")
    ax.legend(ncol=3, loc="upper left")
    fig.tight_layout()
    fig.savefig(path, dpi=130)
    plt.close(fig)


def rule_heatmap(results: pd.DataFrame, path: str):
    """Sharpe difference vs buy & hold for every rule and stock; significant cells are outlined."""
    rules = list(dict.fromkeys(results["rule"]))
    tickers = list(dict.fromkeys(results["ticker"]))
    grid = results.pivot(index="rule", columns="ticker", values="diff").reindex(index=rules, columns=tickers)
    verdict = results.pivot(index="rule", columns="ticker", values="verdict").reindex(index=rules, columns=tickers)
    lim = max(0.5, min(1.5, float(np.nanmax(np.abs(grid.to_numpy())))))
    fig, ax = plt.subplots(figsize=(1.6 + 0.62 * len(tickers), 1.4 + 0.42 * len(rules)))
    im = ax.imshow(grid.to_numpy(dtype=float), cmap=DIVERGING, vmin=-lim, vmax=lim, aspect="auto")
    ax.set_xticks(range(len(tickers)), tickers)
    ax.set_yticks(range(len(rules)), rules)
    ax.tick_params(axis="x", labeltop=True, labelbottom=False, length=0)
    ax.tick_params(axis="y", length=0)
    ax.grid(False)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_xticks(np.arange(-0.5, len(tickers), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(rules), 1), minor=True)
    ax.grid(which="minor", color=SURFACE, linewidth=2)
    ax.tick_params(which="minor", length=0)
    for i, rule in enumerate(rules):
        for j, t in enumerate(tickers):
            v = grid.iloc[i, j]
            if pd.isna(v):
                continue
            sig = verdict.iloc[i, j] != "not distinguishable"
            ax.text(j, i, "0.00" if abs(v) < 0.005 else f"{v:+.2f}", ha="center", va="center", fontsize=8, color=INK,
                    fontweight="bold" if sig else "normal")
            if sig:
                ax.add_patch(plt.Rectangle((j - 0.47, i - 0.47), 0.94, 0.94, fill=False, edgecolor=INK, linewidth=1.6))
    cb = fig.colorbar(im, ax=ax, shrink=0.85, pad=0.02)
    cb.set_label("Sharpe ratio minus buy & hold", color=INK2)
    cb.outline.set_visible(False)
    ax.set_title("Each rule vs holding the stock (blue: rule better; orange: worse; outlined: 95% CI excludes zero)",
                 fontsize=10, loc="left", pad=24)
    fig.tight_layout()
    fig.savefig(path, dpi=130)
    plt.close(fig)


def board_history(action: pd.DataFrame, path: str, weeks: int = 52):
    """Weekly label for each stock over the last year, one row per stock."""
    weekly = action.iloc[::-5][::-1].iloc[-weeks:]  # every 5th trading day, ending today
    tickers = list(action.columns)
    order = list(ACTION_COLORS)
    codes = weekly.apply(lambda col: col.map({a: i for i, a in enumerate(order)}))
    from matplotlib.colors import ListedColormap

    cmap = ListedColormap([ACTION_COLORS[a] for a in order])
    fig, ax = plt.subplots(figsize=(10, 0.36 * len(tickers) + 1.5))
    grid = np.ma.masked_invalid(codes.T.to_numpy(dtype=float))
    ax.imshow(grid, aspect="auto", cmap=cmap, vmin=-0.5, vmax=len(order) - 0.5, interpolation="nearest")
    ax.set_yticks(range(len(tickers)), tickers)
    step = max(1, len(weekly) // 6)
    ax.set_xticks(range(0, len(weekly), step), [d.strftime("%Y-%m") for d in weekly.index[::step]])
    ax.grid(False)
    for spine in ax.spines.values():
        spine.set_visible(False)
    # gaps between rows and columns, in the surface colour, so cells read as separate marks
    ax.set_xticks(np.arange(-0.5, len(weekly), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(tickers), 1), minor=True)
    ax.grid(which="minor", color=SURFACE, linewidth=1.5)
    ax.tick_params(which="minor", length=0)
    handles = [plt.Rectangle((0, 0), 1, 1, color=ACTION_COLORS[a]) for a in order]
    ax.legend(handles, order, ncol=len(order), loc="upper left", bbox_to_anchor=(0, -0.12), fontsize=8)
    ax.set_title("Board label each week, last 12 months")
    fig.tight_layout()
    fig.savefig(path, dpi=130)
    plt.close(fig)
