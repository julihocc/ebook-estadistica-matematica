"""
Computational Lab: Section 06.05 - Confidence Intervals for Variances (Chi-Squared) and Proportions
====================================================================
Computes the chi-squared confidence interval for a population variance and
compares the Wald and Wilson (score) intervals for a proportion, builds the
F-based confidence interval for a ratio of two variances alongside a
two-proportion A/B test interval, and verifies the Fisher Z-transformation
interval for a correlation coefficient with a Wald-vs-Wilson coverage study.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import stats


def variance_ci_and_wilson_vs_wald():
    """Computes the chi-squared CI for sigma^2 and compares Wald vs. Wilson proportion CIs."""
    print("=== Block 1: Variance CI (Chi-Squared) and Wald vs. Wilson Proportion CI ===")
    n, s = 21, 1.45
    alpha = 0.10
    df = n - 1
    chi2_lower = stats.chi2.ppf(alpha / 2, df)
    chi2_upper = stats.chi2.ppf(1 - alpha / 2, df)
    ss = (n - 1) * s**2
    var_lo, var_hi = ss / chi2_upper, ss / chi2_lower
    print(f"Variance CI: n={n}, S={s}, df={df}, chi2_lower={chi2_lower:.3f}, chi2_upper={chi2_upper:.3f}")
    print(f"  90% CI for sigma^2: [{var_lo:.4f}, {var_hi:.4f}]")
    print(f"  90% CI for sigma:   [{np.sqrt(var_lo):.4f}, {np.sqrt(var_hi):.4f}]")

    # Wald vs Wilson for a small-n proportion
    x, n2 = 4, 20  # small sample, p_hat=0.2
    p_hat = x / n2
    z = stats.norm.ppf(0.975)
    se_wald = np.sqrt(p_hat * (1 - p_hat) / n2)
    wald_lo, wald_hi = p_hat - z * se_wald, p_hat + z * se_wald

    center = (p_hat + z**2 / (2 * n2)) / (1 + z**2 / n2)
    half_width = (z / (1 + z**2 / n2)) * np.sqrt(p_hat * (1 - p_hat) / n2 + z**2 / (4 * n2**2))
    wilson_lo, wilson_hi = center - half_width, center + half_width

    print(f"\nSmall-sample proportion: x={x}, n={n2}, p_hat={p_hat}")
    print(f"  Wald 95% CI:   [{wald_lo:.4f}, {wald_hi:.4f}]")
    print(f"  Wilson 95% CI: [{wilson_lo:.4f}, {wilson_hi:.4f}] (does not dip below 0)")


def variance_ratio_and_ab_test():
    """Computes the F-based CI for a ratio of variances and a two-proportion A/B test interval."""
    print("\n=== Block 2: Variance Ratio CI (F) and A/B Proportion Test ===")
    n1, s1_sq = 16, 0.36
    n2, s2_sq = 13, 0.12
    alpha = 0.02
    f_upper = stats.f.ppf(1 - alpha / 2, n1 - 1, n2 - 1)
    f_lower = stats.f.ppf(alpha / 2, n1 - 1, n2 - 1)
    ratio = s1_sq / s2_sq
    ci_lo, ci_hi = ratio / f_upper, ratio / f_lower
    print(f"Variance ratio: S1^2={s1_sq}, S2^2={s2_sq}, ratio={ratio:.4f}")
    print(f"  98% CI for sigma1^2/sigma2^2: [{ci_lo:.4f}, {ci_hi:.4f}] (contains 1? {'Yes' if ci_lo <= 1 <= ci_hi else 'No'})")

    # A/B test for difference of proportions
    x1, n1_ab = 144, 800
    x2, n2_ab = 187, 850
    p1, p2 = x1 / n1_ab, x2 / n2_ab
    se_diff = np.sqrt(p1 * (1 - p1) / n1_ab + p2 * (1 - p2) / n2_ab)
    z = stats.norm.ppf(0.975)
    diff = p1 - p2
    print(f"\nA/B test: p1={p1:.4f}, p2={p2:.4f}, diff={diff:.4f}")
    print(f"  95% CI for p1-p2: [{diff - z*se_diff:.4f}, {diff + z*se_diff:.4f}]")


def fisher_z_correlation_and_coverage_study():
    """Builds the Fisher Z-transform CI for a correlation and compares Wald/Wilson coverage."""
    print("\n=== Block 3: Fisher Z-Transformation for Correlation & Coverage Study ===")
    r, n = 0.82, 28
    z_r = np.arctanh(r)
    se_z = 1 / np.sqrt(n - 3)
    z_crit = stats.norm.ppf(0.975)
    z_lo, z_hi = z_r - z_crit * se_z, z_r + z_crit * se_z
    rho_lo, rho_hi = np.tanh(z_lo), np.tanh(z_hi)
    print(f"r={r}, n={n}: Z(r)={z_r:.4f}, SE_Z={se_z:.4f}")
    print(f"  95% CI for rho: [{rho_lo:.4f}, {rho_hi:.4f}] (asymmetric around r={r})")

    # Coverage study: Wald vs Wilson for small n, p near an extreme
    p_true = 0.1
    n_small = 20
    n_trials = 50_000
    alpha = 0.05
    rng = np.random.default_rng(42)
    z = stats.norm.ppf(1 - alpha / 2)

    successes = rng.binomial(n_small, p_true, size=n_trials)
    p_hat = successes / n_small
    se_wald = np.sqrt(p_hat * (1 - p_hat) / n_small)
    wald_lo = p_hat - z * se_wald
    wald_hi = p_hat + z * se_wald
    wald_coverage = np.mean((wald_lo <= p_true) & (p_true <= wald_hi))

    center = (p_hat + z**2 / (2 * n_small)) / (1 + z**2 / n_small)
    half_width = (z / (1 + z**2 / n_small)) * np.sqrt(p_hat * (1 - p_hat) / n_small + z**2 / (4 * n_small**2))
    wilson_lo = center - half_width
    wilson_hi = center + half_width
    wilson_coverage = np.mean((wilson_lo <= p_true) & (p_true <= wilson_hi))

    print(f"\nCoverage study: p_true={p_true}, n={n_small}, trials={n_trials}, nominal=0.95")
    print(f"  Wald empirical coverage:   {wald_coverage:.4f}")
    print(f"  Wilson empirical coverage: {wilson_coverage:.4f}")


if __name__ == "__main__":
    variance_ci_and_wilson_vs_wald()
    variance_ratio_and_ab_test()
    fisher_z_correlation_and_coverage_study()
