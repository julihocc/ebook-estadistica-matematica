"""
Computational Lab: Section 09.01 - Simple Linear Regression (OLS) and R-Squared
====================================================================
Derives the ordinary least squares (OLS) estimators for the intercept and
slope of a simple linear model, decomposes total variability into regression
and residual components (SST = SSR + SSE) to verify R^2 = r^2, and tests the
statistical significance of the slope with a t-test and confidence/prediction
intervals.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import stats


def ols_coefficient_estimation():
    """Estimates beta_0, beta_1 by OLS and cross-checks against scipy.stats.linregress."""
    print("=== Block 1: OLS Coefficient Estimation ===")
    rng = np.random.default_rng(seed=11)
    x = np.linspace(2, 20, 15)
    true_beta0, true_beta1 = 5.0, 3.2
    y = true_beta0 + true_beta1 * x + rng.normal(scale=4.0, size=x.size)

    x_bar, y_bar = x.mean(), y.mean()
    sxx = np.sum((x - x_bar) ** 2)
    sxy = np.sum((x - x_bar) * (y - y_bar))
    beta1_hat = sxy / sxx
    beta0_hat = y_bar - beta1_hat * x_bar

    print(f"n={x.size}, x_bar={x_bar:.4f}, y_bar={y_bar:.4f}")
    print(f"S_xx={sxx:.4f}, S_xy={sxy:.4f}")
    print(f"beta_1_hat = {beta1_hat:.4f}, beta_0_hat = {beta0_hat:.4f}")

    result = stats.linregress(x, y)
    print(f"scipy.stats.linregress check: slope={result.slope:.4f}, intercept={result.intercept:.4f}")

    return x, y, beta0_hat, beta1_hat


def sum_of_squares_decomposition(x, y, beta0_hat, beta1_hat):
    """Verifies SST = SSR + SSE and the identity R^2 = r^2 (Pearson correlation squared)."""
    print("\n=== Block 2: Sum-of-Squares Decomposition and R^2 ===")
    y_hat = beta0_hat + beta1_hat * x
    y_bar = y.mean()

    sst = np.sum((y - y_bar) ** 2)
    ssr = np.sum((y_hat - y_bar) ** 2)
    sse = np.sum((y - y_hat) ** 2)
    r_squared = ssr / sst

    print(f"SST={sst:.4f} = SSR({ssr:.4f}) + SSE({sse:.4f}) -> sum={ssr + sse:.4f}")
    print(f"R^2 = SSR/SST = {r_squared:.4f}")

    r_pearson = np.corrcoef(x, y)[0, 1]
    print(f"Pearson r = {r_pearson:.4f}, r^2 = {r_pearson ** 2:.4f} (matches R^2)")

    return sse, r_squared


def slope_significance_and_intervals(x, y, beta0_hat, beta1_hat, sse):
    """Tests H0: beta_1=0 via a t-test and builds CI/PI for a new x0."""
    print("\n=== Block 3: Slope Significance Test and Prediction Intervals ===")
    n = x.size
    x_bar = x.mean()
    sxx = np.sum((x - x_bar) ** 2)
    df = n - 2
    mse = sse / df
    se_beta1 = np.sqrt(mse / sxx)

    t_stat = beta1_hat / se_beta1
    p_value = 2 * stats.t.sf(np.abs(t_stat), df)
    print(f"SE(beta_1_hat)={se_beta1:.4f}, t={t_stat:.4f} (df={df}), p-value={p_value:.6f}")

    x0 = 12.0
    y0_hat = beta0_hat + beta1_hat * x0
    t_crit = stats.t.ppf(0.975, df)
    se_mean = np.sqrt(mse * (1 / n + (x0 - x_bar) ** 2 / sxx))
    se_pred = np.sqrt(mse * (1 + 1 / n + (x0 - x_bar) ** 2 / sxx))

    ci = (y0_hat - t_crit * se_mean, y0_hat + t_crit * se_mean)
    pi = (y0_hat - t_crit * se_pred, y0_hat + t_crit * se_pred)

    print(f"At x0={x0}: y_hat={y0_hat:.4f}")
    print(f"95% CI for mean response:   ({ci[0]:.4f}, {ci[1]:.4f})")
    print(f"95% PI for new observation: ({pi[0]:.4f}, {pi[1]:.4f})")


if __name__ == "__main__":
    x, y, beta0_hat, beta1_hat = ols_coefficient_estimation()
    sse, r_squared = sum_of_squares_decomposition(x, y, beta0_hat, beta1_hat)
    slope_significance_and_intervals(x, y, beta0_hat, beta1_hat, sse)
