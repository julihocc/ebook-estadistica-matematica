"""
Computational Lab: Section 06.04 - Confidence Intervals for Population Means (Z and t)
====================================================================
Compares Z-based and t-based confidence intervals for a single mean,
computes the pooled two-sample t confidence interval for the difference of
two means, and verifies the frequentist coverage interpretation of a
confidence interval via repeated Monte Carlo sampling.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import stats


def compare_z_and_t_intervals():
    """Compares Z-based (known sigma) and t-based (unknown sigma) CIs for a single mean."""
    print("=== Block 1: Z-Based vs t-Based CI for a Single Mean ===")
    xbar = 500.4
    n = 16
    alpha = 0.05

    # Case 1: sigma known
    sigma = 2.0
    se_z = sigma / np.sqrt(n)
    z_crit = stats.norm.ppf(1 - alpha / 2)
    margin_z = z_crit * se_z
    print(f"Known sigma={sigma}: SE={se_z:.4f}, z_crit={z_crit:.4f}")
    print(f"  95% CI: [{xbar - margin_z:.2f}, {xbar + margin_z:.2f}]")

    # Case 2: sigma unknown, estimated by S
    s = 2.3
    se_t = s / np.sqrt(n)
    t_crit = stats.t.ppf(1 - alpha / 2, df=n - 1)
    margin_t = t_crit * se_t
    print(f"Unknown sigma (S={s}): SE={se_t:.4f}, t_crit(df={n-1})={t_crit:.4f}")
    print(f"  95% CI: [{xbar - margin_t:.2f}, {xbar + margin_t:.2f}]")
    print(f"  t-interval is {(margin_t/margin_z - 1)*100:.1f}% wider than the Z-interval")


def pooled_two_sample_ci():
    """Computes the pooled two-sample t confidence interval for a difference of means."""
    print("\n=== Block 2: Pooled Two-Sample t CI (Catalyst Comparison) ===")
    n1, xbar1, s1 = 10, 85.0, 4.0
    n2, xbar2, s2 = 12, 81.0, 5.0
    alpha = 0.05

    sp2 = ((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (n1 + n2 - 2)
    se_pooled = np.sqrt(sp2 * (1 / n1 + 1 / n2))
    df = n1 + n2 - 2
    t_crit = stats.t.ppf(1 - alpha / 2, df=df)
    diff = xbar1 - xbar2
    margin = t_crit * se_pooled

    print(f"Catalyst A: n1={n1}, xbar1={xbar1}, s1={s1}")
    print(f"Catalyst B: n2={n2}, xbar2={xbar2}, s2={s2}")
    print(f"  Pooled variance Sp^2 = {sp2:.4f}, SE_pooled = {se_pooled:.4f}")
    print(f"  df={df}, t_crit={t_crit:.4f}")
    print(f"  Difference = {diff:.2f}, 95% CI: [{diff - margin:.4f}, {diff + margin:.4f}]")
    print(f"  Contains zero? {'Yes' if diff - margin <= 0 <= diff + margin else 'No'}")


def verify_frequentist_coverage():
    """Verifies the frequentist interpretation: X% of repeated-sample CIs capture the true mean."""
    print("\n=== Block 3: Frequentist Coverage via Repeated Sampling ===")
    mu_true, sigma_true = 78.0, 12.0
    n = 36
    n_trials = 100_000
    alpha = 0.05
    rng = np.random.default_rng(42)

    samples = rng.normal(mu_true, sigma_true, size=(n_trials, n))
    xbars = np.mean(samples, axis=1)
    se = sigma_true / np.sqrt(n)
    z_crit = stats.norm.ppf(1 - alpha / 2)
    lower = xbars - z_crit * se
    upper = xbars + z_crit * se

    covered = np.mean((lower <= mu_true) & (mu_true <= upper))
    print(f"True mu={mu_true}, sigma={sigma_true}, n={n}, trials={n_trials}")
    print(f"  Nominal confidence level: {1-alpha:.2f}")
    print(f"  Empirical coverage (fraction of intervals containing true mu): {covered:.4f}")

    # Show a handful of individual interval outcomes for illustration
    print("\n  Sample of 5 individual intervals (repeated sampling):")
    for i in range(5):
        contains = lower[i] <= mu_true <= upper[i]
        print(f"    Trial {i+1}: [{lower[i]:.2f}, {upper[i]:.2f}] -- contains mu? {contains}")


if __name__ == "__main__":
    compare_z_and_t_intervals()
    pooled_two_sample_ci()
    verify_frequentist_coverage()
