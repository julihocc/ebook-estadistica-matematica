"""
Computational Lab: Section 09.06 - Implementing Linear Regression in Python
(a `statsmodels`-Style Summary Built from Scratch)
====================================================================
Reproduces, using only numpy/scipy, every number a professional library like
`statsmodels` reports in its OLS summary table: coefficients, standard
errors, t-statistics, p-values, R^2, the overall F-statistic, and the
Residual Standard Error (RSE) -- on a synthetic advertising-style dataset
(TV spend vs. Sales) reconstructed to mirror the classic textbook example.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import stats


def simulate_advertising_style_data():
    """Reconstructs a synthetic TV-spend vs. Sales dataset in the spirit of the classic example."""
    print("=== Block 1: Reconstructing an Advertising-Style Dataset ===")
    rng = np.random.default_rng(seed=42)
    n = 200
    tv = rng.uniform(0.7, 296.4, n)
    sales = 7.03 + 0.0475 * tv + rng.normal(scale=3.25, size=n)
    print(f"Simulated n={n} observations of TV spend and Sales (synthetic reconstruction).")
    print(f"Sample mean(TV)={tv.mean():.2f}, mean(Sales)={sales.mean():.2f}")
    return tv, sales


def full_ols_summary_from_scratch(x, y):
    """Computes every entry of a statsmodels-style OLS summary table by hand."""
    print("\n=== Block 2: Full OLS Summary Table, Built from numpy/scipy ===")
    n = len(x)
    x_bar, y_bar = x.mean(), y.mean()
    sxx = np.sum((x - x_bar) ** 2)
    beta1 = np.sum((x - x_bar) * (y - y_bar)) / sxx
    beta0 = y_bar - beta1 * x_bar

    fitted = beta0 + beta1 * x
    residuals = y - fitted
    df = n - 2
    cme = np.sum(residuals ** 2) / df

    se_beta0 = np.sqrt(cme * (1 / n + x_bar ** 2 / sxx))
    se_beta1 = np.sqrt(cme / sxx)
    t_beta0 = beta0 / se_beta0
    t_beta1 = beta1 / se_beta1
    p_beta0 = 2 * stats.t.sf(np.abs(t_beta0), df)
    p_beta1 = 2 * stats.t.sf(np.abs(t_beta1), df)

    print(f"{'Coefficient':<12}{'Estimate':>12}{'Std Err':>12}{'t':>10}{'P>|t|':>12}")
    print(f"{'Intercept':<12}{beta0:>12.4f}{se_beta0:>12.4f}{t_beta0:>10.4f}{p_beta0:>12.2e}")
    print(f"{'TV':<12}{beta1:>12.4f}{se_beta1:>12.4f}{t_beta1:>10.4f}{p_beta1:>12.2e}")

    return beta0, beta1, residuals, cme, df, sxx


def r_squared_f_statistic_and_rse(x, y, residuals, cme, df, sxx, beta1):
    """Computes R^2, the overall F-statistic, and the Residual Standard Error."""
    print("\n=== Block 3: R^2, F-Statistic, and RSE ===")
    y_bar = y.mean()
    sst = np.sum((y - y_bar) ** 2)
    ssr = beta1 ** 2 * sxx
    sse = np.sum(residuals ** 2)
    r2 = ssr / sst

    f_stat = (ssr / 1) / (sse / df)
    p_value_f = stats.f.sf(f_stat, 1, df)
    rse = np.sqrt(cme)
    relative_error = rse / y_bar

    print(f"R-squared = {r2:.4f}")
    print(f"F-statistic = {f_stat:.4f} (p-value={p_value_f:.2e})")
    print(f"RSE = {rse:.4f}, mean(Sales) = {y_bar:.4f}, relative error = {relative_error:.4f} ({relative_error * 100:.1f}%)")


if __name__ == "__main__":
    tv, sales = simulate_advertising_style_data()
    beta0, beta1, residuals, cme, df, sxx = full_ols_summary_from_scratch(tv, sales)
    r_squared_f_statistic_and_rse(tv, sales, residuals, cme, df, sxx, beta1)
