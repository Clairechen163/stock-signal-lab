import pandas as pd

from stocklab import findings, readme


def _tab(rows):
    cols = ["Sharpe vs B&H", "_ci_low", "_ci_high", "Max drawdown", "Time in market"]
    return pd.DataFrame(rows, columns=["strategy"] + cols).set_index("strategy")


TABLES = {
    "AAA": _tab([("Buy & Hold", None, None, None, -0.50, 1.0), ("Rule A", 0.60, 0.10, 1.20, -0.30, 0.6),
                 ("Rule B", -0.70, -1.30, -0.10, -0.45, 0.5)]),
    "BBB": _tab([("Buy & Hold", None, None, None, -0.40, 1.0), ("Rule A", 0.10, -0.30, 0.50, -0.20, 0.7),
                 ("Rule B", 0.00, -0.40, 0.40, -0.40, 0.5)]),
}


def test_rule_results_read_the_confidence_intervals():
    res = findings.rule_results(TABLES)
    assert len(res) == 4
    v = res.set_index(["ticker", "rule"])["verdict"]
    assert v[("AAA", "Rule A")] == "better" and v[("AAA", "Rule B")] == "worse"
    assert v[("BBB", "Rule A")] == "not distinguishable"
    dd = res.set_index(["ticker", "rule"])["dd_change"]
    assert abs(dd[("AAA", "Rule A")] - 0.20) < 1e-9  # -30% vs -50%: 20 points shallower


def test_rules_section_names_the_current_stocks_and_results():
    res = findings.rule_results(TABLES)
    text = readme.render_rules(res, findings.backtest_counts(TABLES), "reports/rules.png", "reports/REPORT.md", ["NEW"])
    assert text.startswith("### Do simple buy/sell rules beat buy & hold?")
    assert "**1 beat buy & hold** and **1 did worse**" in text
    assert "Rule A on AAA (+0.60" in text and "Rule B on AAA (-0.70" in text
    assert "NEW not yet" in text and "| Rule A | 1 of 2 | 0 of 2 |" in text
    assert readme.render_rules(res.iloc[0:0], {}, None, "r.md") == ""
