"""
Computational Lab: Section 09.03 - The Mathematics of Regression (OLS
Derivation, SST=SSR+SSE, and R-Squared Properties)
====================================================================
Verifies that the closed-form OLS estimators satisfy the normal equations
derived from calculus (zero-sum residuals, zero cross-product with X),
numerically confirms the SST=SSR+SSE decomposition and the vanishing cross
term behind its proof, and demonstrates the properties of R^2 (bounds,
R^2=r^2 identity, and the penalty structure of adjusted R^2).

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np


def normal_equations_satisfied():
    """Verifies the OLS closed-form solution satisfies the calculus-derived normal equations."""
    print("=== Block 1: OLS Estimators Satisfy the Normal Equations ===")
    rng = np.random.default_rng(seed=2)
    x = rng.uniform(2, 20, 200)
    y = 4.0 + 1.5 * x + rng.normal(scale=3.0, size=200)

    x_bar, y_bar = x.mean(), y.mean()
    beta1 = np.sum((x - x_bar) * (y - y_bar)) / np.sum((x - x_bar) ** 2)
    beta0 = y_bar - beta1 * x_bar
    residuals = y - (beta0 + beta1 * x)

    print(f"beta_0={beta0:.4f}, beta_1={beta1:.4f}")
    print(f"Normal equation 1: sum(residuals)      = {np.sum(residuals):.10f} (should be 0)")
    print(f"Normal equation 2: sum(x * residuals)  = {np.sum(x * residuals):.10f} (should be 0)")

    return x, y, beta0, beta1, residuals


def sst_ssr_sse_decomposition(x, y, beta0, beta1):
    """Verifies SST=SSR+SSE and the vanishing of the cross term in its proof."""
    print("\n=== Block 2: SST = SSR + SSE Decomposition ===")
    y_hat = beta0 + beta1 * x
    y_bar = y.mean()

    sst = np.sum((y - y_bar) ** 2)
    ssr = np.sum((y_hat - y_bar) ** 2)
    sse = np.sum((y - y_hat) ** 2)
    cross_term = np.sum((y_hat - y_bar) * (y - y_hat))

    print(f"SST={sst:.4f}, SSR={ssr:.4f}, SSE={sse:.4f}")
    print(f"SSR + SSE = {ssr + sse:.4f} (matches SST: {np.isclose(sst, ssr + sse)})")
    print(f"Cross term sum((y_hat-y_bar)(y-y_hat)) = {cross_term:.10f} (should be 0, proving the decomposition)")

    return sse, sst


def r_squared_properties(x, y, sse, sst):
    """Demonstrates R^2 bounds, the R^2=r^2 identity, and the adjusted R^2 penalty."""
    print("\n=== Block 3: R^2 Properties ===")
    r2 = 1 - sse / sst
    r_pearson = np.corrcoef(x, y)[0, 1]
    print(f"R^2 = {r2:.4f}, bounded in [0,1]: {0 <= r2 <= 1}")
    print(f"r^2 (Pearson squared) = {r_pearson ** 2:.4f} (matches R^2 exactly in simple regression)")

    rng = np.random.default_rng(seed=2)
    n = len(x)
    useless_predictor = rng.normal(size=n)
    X_with_useless = np.column_stack([np.ones(n), x, useless_predictor])
    beta_multi, *_ = np.linalg.lstsq(X_with_useless, y, rcond=None)
    fitted_multi = X_with_useless @ beta_multi
    ss_res_multi = np.sum((y - fitted_multi) ** 2)
    r2_multi = 1 - ss_res_multi / sst

    def adj_r2(r2_value, n_obs, p_predictors):
        return 1 - (1 - r2_value) * (n_obs - 1) / (n_obs - p_predictors - 1)

    adj_r2_simple = adj_r2(r2, n, 1)
    adj_r2_multi = adj_r2(r2_multi, n, 2)
    print(f"Adding a useless random predictor: R^2 {r2:.4f} -> {r2_multi:.4f} (never decreases)")
    print(f"Adjusted R^2:                       {adj_r2_simple:.4f} -> {adj_r2_multi:.4f} (penalizes the useless predictor)")


if __name__ == "__main__":
    x, y, beta0, beta1, residuals = normal_equations_satisfied()
    sse, sst = sst_ssr_sse_decomposition(x, y, beta0, beta1)
    r_squared_properties(x, y, sse, sst)
