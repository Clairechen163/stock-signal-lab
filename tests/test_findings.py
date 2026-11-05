import pandas as pd

from stocklab import findings


def _rec(as_of, sig="", board="not distinguishable", fc_sig=0):
    return {"as_of": as_of, "watchlist": "AAA;BBB", "event_tests": 33, "event_significant": sig,
            "backtest_tests": 48, "backtest_better": 1, "backtest_worse": 2, "backtest_beyond_chance": False,
            "forecast_tests": 32, "forecast_significant": fc_sig, "forecast_median_auc": 0.52,
            "board_verdict": board, "timing_verdict": "not distinguishable", "gap_verdict": "none"}


def test_first_run_has_no_stability_record(tmp_path):
    log = findings.append(_rec("2026-11-03"), str(tmp_path / "log.csv"))
    assert "first logged run" in findings.stability(log)["study"]


def test_same_data_date_replaces_the_earlier_run(tmp_path):
    path = str(tmp_path / "log.csv")
    findings.append(_rec("2026-11-03"), path)
    log = findings.append(_rec("2026-11-03", sig="death_cross (21d)"), path)
    assert len(log) == 1 and log.iloc[0]["event_significant"] == "death_cross (21d)"


def test_stability_counts_agreeing_runs(tmp_path):
    path = str(tmp_path / "log.csv")
    findings.append(_rec("2026-11-02"), path)
    findings.append(_rec("2026-11-03", sig="death_cross (21d)", board="better"), path)
    log = findings.append(_rec("2026-11-04", sig="death_cross (21d);rsi_rollover (63d)"), path)
    st = findings.stability(log)
    assert st["study"] == "significant in the last 3 runs: death_cross (21d) in 2, rsi_rollover (63d) in 1"
    assert st["board"] == "same verdict in 2 of the last 3 runs"
    assert st["forecast"] == "a test survived correction in 0 of the last 3 runs"
    # stability is measured up to the run it describes, not past it
    assert findings.stability(log, "2026-11-03")["board"] == "same verdict in 1 of the last 2 runs"


def test_forecast_tests_use_fdr_across_stocks():
    pvals = [("AAA", "Logistic regression", "accuracy vs majority class", 0.001)]
    pvals += [("BBB", f"m{i}", "error vs zero forecast", 0.04) for i in range(30)]  # 30 nominal "hits" at p = 0.04
    f = findings.forecast_tests({"pvals": pvals, "auc": {"AAA": 0.56, "BBB": 0.51}})
    assert f["tests"] == 31 and f["stocks"] == 2
    assert f["significant"] >= 1 and f["hits"][0].startswith("AAA")
    lone = findings.forecast_tests({"pvals": [("AAA", "m", "t", 0.04)] + [("AAA", f"n{i}", "t", 0.9) for i in range(9)]})
    assert lone["significant"] == 0  # one p = 0.04 among ten tests does not survive


def test_backtest_counts_against_chance():
    tab = pd.DataFrame({"_ci_low": [0, 0.1, -1, -1], "_ci_high": [0, 0.9, 1, -0.2]}, index=["Buy & Hold", "a", "b", "c"])
    bt = findings.backtest_counts({"X": tab})
    assert (bt["better"], bt["worse"], bt["total"]) == (1, 1, 3)
