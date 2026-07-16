"""
Computational Lab: Section 07.02 - Z and t Tests for One- and Two-Sample Means
====================================================================
Performs a one-sample t-test with unknown population standard deviation,
compares the pooled-variance t-test against Welch's t-test for two
independent samples under homoscedasticity and heteroscedasticity, and
executes a paired t-test on before/after measurements.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import stats


def one_sample_t_test():
    """Runs a one-sample t-test when the population standard deviation is unknown."""
    print("=== Block 1: One-Sample t-Test (Unknown Sigma) ===")
    mu0 = 12.0
    rng = np.random.default_rng(11)
    sample = rng.normal(loc=12.9, scale=2.8, size=49)

    xbar = np.mean(sample)
    s = np.std(sample, ddof=1)
    n = len(sample)
    se = s / np.sqrt(n)
    t_stat = (xbar - mu0) / se
    df = n - 1
    p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df=df))

    print(f"H0: mu={mu0}, sample n={n}, xbar={xbar:.4f}, s={s:.4f}")
    print(f"  t statistic = {t_stat:.4f}, df={df}")
    print(f"  two-tailed p-value = {p_value:.4f}")

    t_scipy, p_scipy = stats.ttest_1samp(sample, popmean=mu0)
    print(f"  scipy.stats.ttest_1samp check: t={t_scipy:.4f}, p={p_scipy:.4f}")


def pooled_vs_welch_two_sample():
    """Compares the pooled-variance t-test with Welch's t-test under equal and unequal variances."""
    print("\n=== Block 2: Pooled t-Test vs. Welch t-Test (Two Independent Samples) ===")
    rng = np.random.default_rng(22)

    # Case A: similar variances (homoscedastic)
    n1, n2 = 16, 18
    x1 = rng.normal(14.2, 2.4, size=n1)
    x2 = rng.normal(16.8, 2.6, size=n2)

    s1, s2 = np.std(x1, ddof=1), np.std(x2, ddof=1)
    xbar1, xbar2 = np.mean(x1), np.mean(x2)
    sp2 = ((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (n1 + n2 - 2)
    se_pooled = np.sqrt(sp2 * (1 / n1 + 1 / n2))
    df_pooled = n1 + n2 - 2
    t_pooled = (xbar1 - xbar2) / se_pooled
    p_pooled = 2 * (1 - stats.t.cdf(abs(t_pooled), df=df_pooled))
    print(f"Homoscedastic case: xbar1={xbar1:.2f}, xbar2={xbar2:.2f}, Sp^2={sp2:.4f}")
    print(f"  Pooled t={t_pooled:.4f}, df={df_pooled}, p={p_pooled:.4f}")

    # Case B: markedly different variances (heteroscedastic) -> Welch
    n3, n4 = 15, 18
    y1 = rng.normal(85.2, 12.4, size=n3)
    y2 = rng.normal(74.5, 5.2, size=n4)

    sy1, sy2 = np.std(y1, ddof=1), np.std(y2, ddof=1)
    ybar1, ybar2 = np.mean(y1), np.mean(y2)
    se_welch = np.sqrt(sy1**2 / n3 + sy2**2 / n4)
    df_welch = (sy1**2 / n3 + sy2**2 / n4) ** 2 / (
        (sy1**2 / n3) ** 2 / (n3 - 1) + (sy2**2 / n4) ** 2 / (n4 - 1)
    )
    t_welch = (ybar1 - ybar2) / se_welch
    p_welch = 2 * (1 - stats.t.cdf(abs(t_welch), df=df_welch))
    print(f"Heteroscedastic case: ybar1={ybar1:.2f}, ybar2={ybar2:.2f}, s1={sy1:.2f}, s2={sy2:.2f}")
    print(f"  Welch t={t_welch:.4f}, df={df_welch:.4f} (fractional), p={p_welch:.4f}")

    t_scipy, p_scipy = stats.ttest_ind(y1, y2, equal_var=False)
    print(f"  scipy.stats.ttest_ind(equal_var=False) check: t={t_scipy:.4f}, p={p_scipy:.4f}")


def paired_t_test():
    """Runs a paired t-test on before/after measurements reduced to a single sample of differences."""
    print("\n=== Block 3: Paired t-Test (Before/After) ===")
    rng = np.random.default_rng(33)
    n = 12
    before = rng.normal(45.0, 3.5, size=n)
    after = before + rng.normal(3.8, 2.1, size=n)
    diffs = after - before

    dbar = np.mean(diffs)
    sd = np.std(diffs, ddof=1)
    se_d = sd / np.sqrt(n)
    t_stat = dbar / se_d
    df = n - 1
    p_value = 1 - stats.t.cdf(t_stat, df=df)

    print(f"n={n} paired observations, mean difference D-bar={dbar:.4f}, S_D={sd:.4f}")
    print(f"  t statistic = {t_stat:.4f}, df={df}")
    print(f"  one-tailed (right) p-value = {p_value:.6f}")

    t_scipy, p_scipy = stats.ttest_rel(after, before)
    print(f"  scipy.stats.ttest_rel check: t={t_scipy:.4f}, two-tailed p={p_scipy:.6f}")


if __name__ == "__main__":
    one_sample_t_test()
    pooled_vs_welch_two_sample()
    paired_t_test()
