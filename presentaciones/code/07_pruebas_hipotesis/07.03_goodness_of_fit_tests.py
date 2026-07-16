"""
Computational Lab: Section 07.03 - Chi-Squared Goodness-of-Fit Tests
====================================================================
Runs a chi-squared goodness-of-fit test against a uniform hypothesis (dice
fairness), performs a goodness-of-fit test against a Poisson model whose rate
parameter is estimated from the same sample (adjusting degrees of freedom),
and demonstrates Cochran's Rule by merging low-expected-frequency cells.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import stats


def uniform_goodness_of_fit():
    """Tests whether a die is fair using the Pearson chi-squared goodness-of-fit statistic."""
    print("=== Block 1: Goodness-of-Fit Against a Uniform Hypothesis (Fair Die) ===")
    observed = np.array([18, 22, 20, 19, 23, 18])
    n = observed.sum()
    k = len(observed)
    expected = np.full(k, n / k)

    chi2_stat = np.sum((observed - expected) ** 2 / expected)
    df = k - 1
    p_value = 1 - stats.chi2.cdf(chi2_stat, df=df)

    print(f"Observed frequencies: {observed}, n={n}, k={k} categories")
    print(f"Expected under H0 (uniform): {expected}")
    print(f"  chi2 statistic = {chi2_stat:.4f}, df={df}")
    print(f"  p-value = {p_value:.4f}")

    chi2_scipy, p_scipy = stats.chisquare(observed)
    print(f"  scipy.stats.chisquare check: chi2={chi2_scipy:.4f}, p={p_scipy:.4f}")


def poisson_goodness_of_fit_estimated_parameter():
    """Tests goodness-of-fit to a Poisson model whose rate is estimated from the data."""
    print("\n=== Block 2: Goodness-of-Fit With an Estimated Parameter (Poisson) ===")
    counts = np.array([0, 1, 2, 3])
    observed = np.array([36, 40, 18, 6])
    n = observed.sum()

    lam_hat = np.sum(counts * observed) / n
    print(f"Observed: {observed}, n={n}, estimated lambda_hat = {lam_hat:.4f}")

    probs = stats.poisson.pmf([0, 1, 2], lam_hat)
    prob_tail = 1 - probs.sum()
    probs_full = np.append(probs, prob_tail)
    expected = n * probs_full

    chi2_stat = np.sum((observed - expected) ** 2 / expected)
    m_estimated_params = 1
    df = len(observed) - 1 - m_estimated_params
    p_value = 1 - stats.chi2.cdf(chi2_stat, df=df)

    print(f"Expected under Poisson(lambda_hat): {np.round(expected, 2)}")
    print(f"  chi2 statistic = {chi2_stat:.4f}, df = k-1-m = {len(observed)}-1-{m_estimated_params} = {df}")
    print(f"  p-value = {p_value:.4f}")

    chi2_scipy, p_scipy = stats.chisquare(observed, f_exp=expected, ddof=m_estimated_params)
    print(f"  scipy.stats.chisquare(ddof={m_estimated_params}) check: chi2={chi2_scipy:.4f}, p={p_scipy:.4f}")


def cochran_rule_and_cell_merging():
    """Demonstrates Cochran's Rule violation and the corrective cell-merging procedure."""
    print("\n=== Block 3: Cochran's Rule and Cell Merging ===")
    expected = np.array([45.2, 30.5, 3.2, 1.1])
    observed = np.array([48, 27, 4, 1])

    low_cells = expected < 5
    frac_low = np.mean(low_cells)
    print(f"Expected frequencies: {expected}")
    print(f"  Cells with E_i < 5: {low_cells.sum()} of {len(expected)} ({frac_low*100:.0f}%)")
    print(f"  Cochran's Rule violated (>20% of cells with E_i<5)? {frac_low > 0.20}")

    observed_merged = np.array([observed[0], observed[1], observed[2] + observed[3]])
    expected_merged = np.array([expected[0], expected[1], expected[2] + expected[3]])
    print(f"\n  Merged categories 3+4: observed={observed_merged}, expected={np.round(expected_merged, 2)}")

    chi2_stat = np.sum((observed_merged - expected_merged) ** 2 / expected_merged)
    df_merged = len(observed_merged) - 1
    p_value = 1 - stats.chi2.cdf(chi2_stat, df=df_merged)
    print(f"  Merged chi2 statistic = {chi2_stat:.4f}, df={df_merged}, p-value = {p_value:.4f}")


if __name__ == "__main__":
    uniform_goodness_of_fit()
    poisson_goodness_of_fit_estimated_parameter()
    cochran_rule_and_cell_merging()
