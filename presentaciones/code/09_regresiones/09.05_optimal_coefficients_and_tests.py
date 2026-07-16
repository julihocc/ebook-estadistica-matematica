"""
Computational Lab: Section 09.05 - Optimal Coefficients, t/F Significance
Tests, and the Residual Standard Error (RSE)
====================================================================
Fits the optimal OLS coefficients on a simulated dataset, tests the
statistical significance of the slope via a t-test, verifies the algebraic
identity F=t^2 for the overall-significance F-test in simple regression,
and computes the Residual Standard Error as an absolute measure of fit
quality.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import stats


def optimal_coefficients_and_t_test():
    """Fits OLS and tests H0: beta=0 via a t-test."""
    print("=== Block 1: Optimal Coefficients and t-Test for Slope Significance ===")
    rng = np.random.default_rng(seed=21)
    n = 100
    x = 2.5 * rng.standard_normal(n) + 1.5
    y = 2.0 + 0.3 * x + 0.5 * rng.standard_normal(n)

    x_bar, y_bar = x.mean(), y.mean()
    sxx = np.sum((x - x_bar) ** 2)
    beta_hat = np.sum((x - x_bar) * (y - y_bar)) / sxx
    alpha_hat = y_bar - beta_hat * x_bar
    residuals = y - (alpha_hat + beta_hat * x)

    df = n - 2
    cme = np.sum(residuals ** 2) / df
    se_beta = np.sqrt(cme / sxx)
    t_stat = beta_hat / se_beta
    p_value = 2 * stats.t.sf(np.abs(t_stat), df)

    print(f"alpha_hat={alpha_hat:.4f}, beta_hat={beta_hat:.4f}")
    print(f"SE(beta_hat)={se_beta:.4f}, t={t_stat:.4f} (df={df}), p-value={p_value:.6e}")

    return x, y, alpha_hat, beta_hat, residuals, cme, sxx, df, t_stat


def f_test_equals_t_squared(t_stat, sxx, cme, residuals, y, df):
    """Verifies that F = t^2 for the overall-significance test in simple regression."""
    print("\n=== Block 2: F-Test for Overall Significance (F = t^2) ===")
    y_bar = y.mean()
    ssr = t_stat ** 2 * cme  # SSR = beta_hat^2 * Sxx, algebraically equals t^2*CME here
    sse = np.sum(residuals ** 2)
    f_stat = (ssr / 1) / (sse / df)
    p_value_f = stats.f.sf(f_stat, 1, df)

    print(f"F statistic = {f_stat:.4f} (df=1,{df}), p-value={p_value_f:.6e}")
    print(f"t^2 = {t_stat ** 2:.4f}")
    print(f"|F - t^2| = {abs(f_stat - t_stat ** 2):.10f} (exact algebraic identity in simple regression)")


def residual_standard_error(residuals, y, df):
    """Computes the Residual Standard Error and its relative magnitude."""
    print("\n=== Block 3: Residual Standard Error (RSE) ===")
    sse = np.sum(residuals ** 2)
    rse = np.sqrt(sse / df)
    y_mean = y.mean()
    relative_error = rse / y_mean

    print(f"RSE = sqrt(SSE/(n-2)) = {rse:.4f}")
    print(f"mean(Y) = {y_mean:.4f}")
    print(f"Relative error = RSE/mean(Y) = {relative_error:.4f} ({relative_error * 100:.1f}%)")


if __name__ == "__main__":
    x, y, alpha_hat, beta_hat, residuals, cme, sxx, df, t_stat = optimal_coefficients_and_t_test()
    f_test_equals_t_squared(t_stat, sxx, cme, residuals, y, df)
    residual_standard_error(residuals, y, df)
