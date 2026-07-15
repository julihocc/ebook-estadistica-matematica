"""
Computational Lab: Section 05.04 - Student's t-Distribution and Small Samples
====================================================================
Validates t-distribution variance and its convergence to the standard Normal
as degrees of freedom grow, compares t-based vs Z-based confidence intervals
across sample sizes, and verifies the empirical coverage of the t-based
confidence interval for the mean via Monte Carlo.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import stats


def verify_t_distribution_properties():
    """Validates Var(T) and the convergence of t quantiles to Normal quantiles as nu grows."""
    print("=== Block 1: t-Distribution Properties and Convergence ===")
    for nu in [10, 30]:
        theo_var = nu / (nu - 2)
        emp_var = stats.t.var(df=nu)
        print(f"t_{nu}: Var(T) = {emp_var:.4f} (theoretical nu/(nu-2) = {theo_var:.4f})")

    z_crit = stats.norm.ppf(0.975)
    print(f"\nConvergence of t quantiles to z_0.025={z_crit:.4f}:")
    print(f"  {'nu':>5} | {'t_nu,0.025':>10} | {'% diff vs z':>12}")
    print(f"  {'-'*5}-+-{'-'*10}-+-{'-'*12}")
    for nu in [5, 30, 120]:
        t_crit = stats.t.ppf(0.975, df=nu)
        pct_diff = (t_crit - z_crit) / z_crit * 100
        print(f"  {nu:>5} | {t_crit:>10.4f} | {pct_diff:>11.2f}%")


def compare_t_and_z_confidence_intervals():
    """Compares t-based and (incorrectly) z-based confidence intervals for the mean."""
    print("\n=== Block 2: t-Based vs Z-Based Confidence Intervals ===")
    # Worked example: n=9, xbar=48.5, S=3.2
    n, xbar, s = 9, 48.5, 3.2
    se = s / np.sqrt(n)
    t_crit = stats.t.ppf(0.975, df=n - 1)
    z_crit = stats.norm.ppf(0.975)
    margin_t = t_crit * se
    margin_z = z_crit * se
    print(f"Example: n={n}, xbar={xbar}, S={s}, SE={se:.4f}")
    print(f"  t_{n-1},0.025 = {t_crit:.4f} -> 95% CI (t): [{xbar-margin_t:.2f}, {xbar+margin_t:.2f}]")
    print(f"  z_0.025 = {z_crit:.4f} -> 95% CI (z, incorrect): [{xbar-margin_z:.2f}, {xbar+margin_z:.2f}]")
    print(f"  t-interval is {(margin_t/margin_z - 1)*100:.1f}% wider than the (incorrect) z-interval")

    # Small dataset example: {23, 25, 21, 27, 24}
    data = np.array([23, 25, 21, 27, 24])
    n2 = len(data)
    xbar2 = np.mean(data)
    s2 = np.std(data, ddof=1)
    se2 = s2 / np.sqrt(n2)
    t_crit2 = stats.t.ppf(0.975, df=n2 - 1)
    margin2 = t_crit2 * se2
    print(f"\nDataset {{23,25,21,27,24}}: xbar={xbar2:.4f}, S={s2:.4f}, SE={se2:.4f}")
    print(f"  95% CI: [{xbar2-margin2:.2f}, {xbar2+margin2:.2f}]")


def verify_one_sample_t_test_and_coverage():
    """Runs a one-sample t-test example and checks empirical CI coverage via Monte Carlo."""
    print("\n=== Block 3: One-Sample t-Test and CI Coverage ===")
    # One-sample t-test: H0: mu=100, n=25, xbar=104.2, S=12
    n, mu0, xbar, s = 25, 100.0, 104.2, 12.0
    t_stat = (xbar - mu0) / (s / np.sqrt(n))
    t_crit = stats.t.ppf(0.975, df=n - 1)
    print(f"One-sample t-test: H0: mu={mu0}, n={n}, xbar={xbar}, S={s}")
    print(f"  t = {t_stat:.4f}, critical t_{n-1},0.025 = {t_crit:.4f}")
    print(f"  Reject H0? {'Yes' if abs(t_stat) > t_crit else 'No'}")

    # Monte Carlo coverage check for the t-based CI
    mu_true, sigma_true = 50.0, 10.0
    n_mc = 10
    n_trials = 100_000
    alpha = 0.05
    rng = np.random.default_rng(42)

    samples = rng.normal(mu_true, sigma_true, size=(n_trials, n_mc))
    xbars = np.mean(samples, axis=1)
    s_mc = np.std(samples, axis=1, ddof=1)
    t_crit_mc = stats.t.ppf(1 - alpha / 2, df=n_mc - 1)
    margins = t_crit_mc * s_mc / np.sqrt(n_mc)
    covered = np.mean((xbars - margins <= mu_true) & (mu_true <= xbars + margins))
    print(f"\nMonte Carlo CI coverage (n={n_mc}, {n_trials} trials): {covered:.4f} (nominal: {1-alpha:.4f})")


if __name__ == "__main__":
    verify_t_distribution_properties()
    compare_t_and_z_confidence_intervals()
    verify_one_sample_t_test_and_coverage()
