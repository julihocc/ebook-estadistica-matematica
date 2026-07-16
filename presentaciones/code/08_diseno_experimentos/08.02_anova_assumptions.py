"""
Computational Lab: Section 08.02 - ANOVA Assumptions and Diagnostics
====================================================================
Verifies the homoscedasticity assumption via Bartlett's test and the
mean-centered Levene test (the latter reproduced as an ordinary one-way ANOVA
applied to absolute deviations, per Section 08.01), audits residual normality
with the Shapiro-Wilk test, and contrasts the parametric F-test against the
nonparametric Kruskal-Wallis alternative on skewed data.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import stats


def bartlett_and_levene_tests():
    """Audits homoscedasticity for 3 CI/CD pipelines via Bartlett and Levene."""
    print("=== Block 1: Bartlett and Levene Tests for Homoscedasticity ===")
    pipeline_a = np.array([40, 42, 38, 44, 41.0])
    pipeline_b = np.array([50, 55, 48, 52, 60.0])
    pipeline_c = np.array([41, 40, 42, 39, 43.0])
    groups = [pipeline_a, pipeline_b, pipeline_c]

    b_stat, b_p = stats.bartlett(*groups)
    print(f"Bartlett's test: B={b_stat:.4f}, p-value={b_p:.4f}")

    z = [np.abs(g - g.mean()) for g in groups]
    k, N = len(z), sum(len(g) for g in z)
    grand_mean_z = np.concatenate(z).mean()
    sstr_z = sum(len(zi) * (zi.mean() - grand_mean_z) ** 2 for zi in z)
    sse_z = sum(np.sum((zi - zi.mean()) ** 2) for zi in z)
    df_tr, df_e = k - 1, N - k
    w_stat = (sstr_z / df_tr) / (sse_z / df_e)
    p_value = stats.f.sf(w_stat, df_tr, df_e)
    print(f"Levene (manual, mean-centered): W={w_stat:.4f} (df={df_tr},{df_e}), p={p_value:.4f}")

    w_scipy, p_scipy = stats.levene(*groups, center="mean")
    print(f"scipy.stats.levene(center='mean') check: W={w_scipy:.4f}, p={p_scipy:.4f}")


def shapiro_wilk_residual_normality():
    """Fits a one-way ANOVA and audits residual normality via Shapiro-Wilk."""
    print("\n=== Block 2: Shapiro-Wilk Test on ANOVA Residuals ===")
    rng = np.random.default_rng(seed=7)
    true_means = [100.0, 105.0, 98.0]
    groups = [rng.normal(loc=mu, scale=5.0, size=10) for mu in true_means]

    residuals = np.concatenate([g - g.mean() for g in groups])
    w_stat, p_value = stats.shapiro(residuals)
    print(f"Residuals (N={len(residuals)}) from a 3-group ANOVA fit.")
    print(f"Shapiro-Wilk: W={w_stat:.4f}, p-value={p_value:.4f}")
    if p_value > 0.05:
        print("  p > 0.05: no evidence against normality of residuals.")
    else:
        print("  p <= 0.05: evidence against normality of residuals.")


def kruskal_wallis_nonparametric_alternative():
    """Compares the parametric F-test against Kruskal-Wallis on skewed data."""
    print("\n=== Block 3: Kruskal-Wallis Nonparametric Alternative ===")
    rng = np.random.default_rng(seed=99)
    group1 = rng.exponential(scale=2.0, size=15)
    group2 = rng.exponential(scale=2.0, size=15) + 0.8
    group3 = rng.exponential(scale=2.0, size=15) + 1.6

    f_stat, f_p = stats.f_oneway(group1, group2, group3)
    h_stat, h_p = stats.kruskal(group1, group2, group3)

    print("Data: 3 groups drawn from right-skewed exponential distributions")
    print("(normality assumption violated by construction).")
    print(f"Parametric one-way ANOVA:  F={f_stat:.4f}, p-value={f_p:.4f}")
    print(f"Kruskal-Wallis (rank-based): H={h_stat:.4f}, p-value={h_p:.4f}")
    print("Both flag the shift in location, but Kruskal-Wallis does not")
    print("assume normality or homoscedasticity, only exchangeability under H0.")


if __name__ == "__main__":
    bartlett_and_levene_tests()
    shapiro_wilk_residual_normality()
    kruskal_wallis_nonparametric_alternative()
