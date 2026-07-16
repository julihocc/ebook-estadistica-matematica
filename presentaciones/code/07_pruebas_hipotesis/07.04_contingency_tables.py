"""
Computational Lab: Section 07.04 - Contingency Tables and Independence Tests
====================================================================
Runs a chi-squared test of independence on a two-way contingency table,
performs a chi-squared test of homogeneity comparing category distributions
across several independent samples, and numerically verifies the exact
algebraic identity Z^2 = chi^2 for 2x2 tables.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import stats


def independence_test():
    """Runs a chi-squared test of independence between vehicle type and day of week."""
    print("=== Block 1: Chi-Squared Test of Independence ===")
    observed = np.array([
        [30, 25, 45],
        [20, 30, 30],
        [25, 20, 35],
        [15, 15, 10],
    ])
    row_totals = observed.sum(axis=1, keepdims=True)
    col_totals = observed.sum(axis=0, keepdims=True)
    n = observed.sum()
    expected = row_totals @ col_totals / n

    chi2_stat = np.sum((observed - expected) ** 2 / expected)
    df = (observed.shape[0] - 1) * (observed.shape[1] - 1)
    p_value = 1 - stats.chi2.cdf(chi2_stat, df=df)

    print(f"Observed table (4 vehicle types x 3 days):\n{observed}")
    print(f"Expected table under independence:\n{np.round(expected, 2)}")
    print(f"  chi2 statistic = {chi2_stat:.4f}, df={df}, p-value = {p_value:.4f}")

    chi2_scipy, p_scipy, df_scipy, _ = stats.chi2_contingency(observed, correction=False)
    print(f"  scipy.stats.chi2_contingency check: chi2={chi2_scipy:.4f}, df={df_scipy}, p={p_scipy:.4f}")


def homogeneity_test():
    """Runs a chi-squared test of homogeneity across three independent generational cohorts."""
    print("\n=== Block 2: Chi-Squared Test of Homogeneity (3 Independent Cohorts) ===")
    observed = np.array([
        [80, 120, 45],
        [30, 65, 70],
        [90, 65, 35],
    ])
    row_totals = observed.sum(axis=1, keepdims=True)
    col_totals = observed.sum(axis=0, keepdims=True)
    n = observed.sum()
    expected = row_totals @ col_totals / n

    chi2_stat = np.sum((observed - expected) ** 2 / expected)
    df = (observed.shape[0] - 1) * (observed.shape[1] - 1)
    p_value = 1 - stats.chi2.cdf(chi2_stat, df=df)

    print("Design: 3 independent samples (Gen Z n=200, Millennials n=250, Gen X n=150),")
    print("each classified by preferred monetization model (rows).")
    print(f"  chi2 statistic = {chi2_stat:.4f}, df={df}, p-value = {p_value:.6f}")
    print("  Same computational formula as independence, but the sampling design is")
    print("  fundamentally different: column totals were fixed by the researcher in advance.")


def z_squared_equals_chi_squared_2x2():
    """Verifies the exact algebraic identity Z^2 = chi^2 for a 2x2 contingency table."""
    print("\n=== Block 3: Z^2 = Chi^2 Identity in 2x2 Tables ===")
    n1, x1 = 150, 12   # vaccine group: infected
    n2, x2 = 150, 28   # placebo group: infected

    observed = np.array([[x1, n1 - x1], [x2, n2 - x2]])
    row_totals = observed.sum(axis=1, keepdims=True)
    col_totals = observed.sum(axis=0, keepdims=True)
    n = observed.sum()
    expected = row_totals @ col_totals / n
    chi2_stat = np.sum((observed - expected) ** 2 / expected)

    p1_hat, p2_hat = x1 / n1, x2 / n2
    p_pooled = (x1 + x2) / (n1 + n2)
    se_pooled = np.sqrt(p_pooled * (1 - p_pooled) * (1 / n1 + 1 / n2))
    z_stat = (p1_hat - p2_hat) / se_pooled

    print(f"2x2 table: vaccine {x1}/{n1} infected, placebo {x2}/{n2} infected")
    print(f"  chi2 (homogeneity) statistic = {chi2_stat:.4f}")
    print(f"  Z statistic (two-proportion test) = {z_stat:.4f}, Z^2 = {z_stat**2:.4f}")
    print(f"  |chi2 - Z^2| = {abs(chi2_stat - z_stat**2):.10f} (exact algebraic identity)")


if __name__ == "__main__":
    independence_test()
    homogeneity_test()
    z_squared_equals_chi_squared_2x2()
