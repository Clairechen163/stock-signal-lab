import numpy as np
import pandas as pd

from stocklab import stats


def test_benjamini_hochberg_known_values():
    q = stats.benjamini_hochberg([0.01, 0.04, 0.03, 0.5])
    np.testing.assert_allclose(q, [0.04, 0.05333333, 0.05333333, 0.5], rtol=1e-6)


def test_bootstrap_no_difference_for_identical_series():
    r = np.random.default_rng(0).normal(0.0005, 0.01, 1000)
    res = stats.bootstrap_diff_ci(r, r, n_boot=200)
    assert res["diff"] == 0 and res["ci_low"] <= 0 <= res["ci_high"]


def test_bootstrap_detects_large_difference():
    rng = np.random.default_rng(1)
    noise = rng.normal(0, 0.01, 2000)
    res = stats.bootstrap_diff_ci(noise + 0.003, noise - 0.001, n_boot=300)
    assert res["ci_low"] > 0


def test_diebold_mariano_prefers_better_forecast():
    rng = np.random.default_rng(2)
    y = rng.normal(0, 1, 500)
    good = y - (y + rng.normal(0, 0.3, 500))
    bad = y - rng.normal(0, 1, 500)
    assert stats.diebold_mariano(good, bad)["p_value"] < 0.01


def test_monte_carlo_event_pvalue_flags_bad_days():
    rng = np.random.default_rng(3)
    s = pd.Series(rng.normal(0, 1, 2000))
    mask = pd.Series(False, index=s.index)
    mask.iloc[::40] = True
    s[mask] -= 1.5  # events genuinely followed by worse outcomes
    p, k = stats.monte_carlo_event_pvalue(s, mask, n_sims=500)
    assert k == 50 and p < 0.01


def test_max_drawdown():
    assert np.isclose(stats.max_drawdown([0.1, -0.5, 0.2]), -0.5)
