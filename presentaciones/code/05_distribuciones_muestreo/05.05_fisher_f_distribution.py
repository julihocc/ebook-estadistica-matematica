"""
Computational Lab: Section 05.05 - Fisher-Snedecor F-Distribution
====================================================================
Validates F-distribution properties (mean, the reciprocal property, and the
T^2 = F_{1,nu} identity), verifies the F-test for equality of variances and
its associated confidence interval for sigma1^2/sigma2^2, and performs a
complete one-way ANOVA cross-checked against SciPy.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import stats


def verify_f_distribution_properties():
    """Validates E(F), the reciprocal property, and the T^2 ~ F_{1,nu} identity."""
    print("=== Block 1: F-Distribution Properties ===")
    d1, d2 = 5, 10
    print(f"F_{{{d1},{d2}}}: E(F) = {stats.f.mean(d1, d2):.4f} (theoretical d2/(d2-2) = {d2/(d2-2):.4f})")

    # Reciprocal property: 1/F_{d1,d2} ~ F_{d2,d1}
    rng = np.random.default_rng(42)
    n_trials = 200_000
    f_samples = rng.f(d1, d2, size=n_trials)
    reciprocal = 1 / f_samples
    ks = stats.kstest(reciprocal, "f", args=(d2, d1))
    print(f"Reciprocal property: 1/F_{{{d1},{d2}}} vs F_{{{d2},{d1}}}: KS D={ks.statistic:.5f}, p={ks.pvalue:.4f}")

    # Identity: T^2 ~ F_{1, nu}
    nu = 12
    t_samples = rng.standard_t(nu, size=n_trials)
    t_squared = t_samples**2
    ks2 = stats.kstest(t_squared, "f", args=(1, nu))
    print(f"Identity T^2 ~ F_{{1,{nu}}}: KS D={ks2.statistic:.5f}, p={ks2.pvalue:.4f}")


def verify_f_test_and_confidence_interval():
    """Verifies the F-test for equality of variances and its confidence interval."""
    print("\n=== Block 2: F-Test for Equal Variances and CI for sigma1^2/sigma2^2 ===")
    n1, s1_sq = 13, 45.0
    n2, s2_sq = 11, 20.0
    f_stat = s1_sq / s2_sq
    f_crit = stats.f.ppf(0.975, n1 - 1, n2 - 1)
    print(f"F-test: n1={n1}, S1^2={s1_sq}, n2={n2}, S2^2={s2_sq}")
    print(f"  F = {f_stat:.4f}, critical F_{{{n1-1},{n2-1}}},0.025 = {f_crit:.4f}")
    print(f"  Reject H0 (equal variances)? {'Yes' if f_stat > f_crit else 'No'}")

    f_lower = stats.f.ppf(0.025, n1 - 1, n2 - 1)
    f_upper_inv = stats.f.ppf(0.975, n2 - 1, n1 - 1)
    ci_lower = f_stat / f_crit
    ci_upper = f_stat * f_upper_inv
    print(f"  95% CI for sigma1^2/sigma2^2: [{ci_lower:.4f}, {ci_upper:.4f}]")

    # Monte Carlo coverage check
    sigma1_sq, sigma2_sq = 40.0, 40.0  # equal variances (true ratio = 1)
    n_trials = 50_000
    rng = np.random.default_rng(42)
    x1 = rng.normal(0, np.sqrt(sigma1_sq), size=(n_trials, n1))
    x2 = rng.normal(0, np.sqrt(sigma2_sq), size=(n_trials, n2))
    s1_mc = np.var(x1, axis=1, ddof=1)
    s2_mc = np.var(x2, axis=1, ddof=1)
    ratio_mc = s1_mc / s2_mc
    true_ratio = sigma1_sq / sigma2_sq
    covered = np.mean((ratio_mc / f_crit <= true_ratio) & (true_ratio <= ratio_mc * f_upper_inv))
    print(f"  Monte Carlo CI coverage (true ratio=1): {covered:.4f} (nominal: 0.95)")


def verify_anova_computation():
    """Computes a complete one-way ANOVA and cross-checks it against SciPy."""
    print("\n=== Block 3: One-Way ANOVA Verification ===")
    group_a = np.array([10, 12, 14, 12])
    group_b = np.array([8, 9, 11, 8])
    group_c = np.array([15, 16, 14, 15])
    groups = [group_a, group_b, group_c]

    means = [np.mean(g) for g in groups]
    grand_mean = np.mean(np.concatenate(groups))
    n_per_group = len(group_a)
    k = len(groups)
    n_total = sum(len(g) for g in groups)

    ss_treat = sum(n_per_group * (m - grand_mean) ** 2 for m in means)
    ss_error = sum(np.sum((g - m) ** 2) for g, m in zip(groups, means))
    f_stat = (ss_treat / (k - 1)) / (ss_error / (n_total - k))
    f_crit = stats.f.ppf(0.95, k - 1, n_total - k)

    print(f"Group means: A={means[0]:.1f}, B={means[1]:.1f}, C={means[2]:.1f}, grand mean={grand_mean:.1f}")
    print(f"  SS_treatment = {ss_treat:.2f}, SS_error = {ss_error:.2f}")
    print(f"  F = {f_stat:.4f}, critical F_{{{k-1},{n_total-k}}},0.05 = {f_crit:.4f}")
    print(f"  Reject H0 (equal means)? {'Yes' if f_stat > f_crit else 'No'}")

    # Cross-check against scipy's one-way ANOVA
    f_scipy, p_scipy = stats.f_oneway(group_a, group_b, group_c)
    print(f"  SciPy f_oneway: F={f_scipy:.4f}, p-value={p_scipy:.6f} (should match manual F above)")


if __name__ == "__main__":
    verify_f_distribution_properties()
    verify_f_test_and_confidence_interval()
    verify_anova_computation()
