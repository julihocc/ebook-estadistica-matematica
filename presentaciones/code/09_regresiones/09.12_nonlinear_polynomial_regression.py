"""
Computational Lab: Section 09.12 - Nonlinear Transformations and Polynomial
Regression
====================================================================
Fits a quadratic model by expanding the design matrix with X^2 and solving
the ordinary Normal Equation, contrasts its R^2 against a misspecified
linear fit via a Partial F-Test, and demonstrates the inherent
multicollinearity between X and X^2 when X is confined to a narrow range.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np


def fit_quadratic_model():
    """Fits mpg ~ hp + hp^2 via the expanded design matrix and the Normal Equation."""
    print("=== Block 1: Fitting a Quadratic Model via the Expanded Design Matrix ===")
    hp = np.array([50.0, 75.0, 100.0, 125.0, 150.0])
    mpg = np.array([35.0, 28.0, 24.0, 26.0, 32.0])

    X_quad = np.column_stack([np.ones(5), hp, hp ** 2])
    c, *_ = np.linalg.lstsq(X_quad, mpg, rcond=None)

    print(f"hp = {hp}")
    print(f"mpg = {mpg}")
    print(f"Quadratic coefficients (c0, c1, c2): {np.round(c, 6)}")

    fitted = X_quad @ c
    sse = np.sum((mpg - fitted) ** 2)
    print(f"Fitted values: {np.round(fitted, 4)}")
    print(f"SSE = {sse:.4f}")

    return hp, mpg, c


def compare_linear_vs_quadratic(hp, mpg):
    """Compares a misspecified linear fit against the quadratic fit via a Partial F-Test."""
    print("\n=== Block 2: Linear vs. Quadratic Fit and the Partial F-Test ===")
    n = len(hp)
    sst = np.sum((mpg - mpg.mean()) ** 2)

    X_linear = np.column_stack([np.ones(n), hp])
    c_lin, *_ = np.linalg.lstsq(X_linear, mpg, rcond=None)
    sse_lin = np.sum((mpg - X_linear @ c_lin) ** 2)
    r2_lin = 1 - sse_lin / sst

    X_quad = np.column_stack([np.ones(n), hp, hp ** 2])
    c_quad, *_ = np.linalg.lstsq(X_quad, mpg, rcond=None)
    sse_quad = np.sum((mpg - X_quad @ c_quad) ** 2)
    r2_quad = 1 - sse_quad / sst

    print(f"Linear model:    R^2 = {r2_lin:.4f}")
    print(f"Quadratic model: R^2 = {r2_quad:.4f}")

    p1, p2 = 1, 2
    f_partial = ((r2_quad - r2_lin) / (p2 - p1)) / ((1 - r2_quad) / (n - p2 - 1))
    print(f"Partial F-statistic (H0: quadratic term not needed) = {f_partial:.4f}")


def polynomial_multicollinearity_demo():
    """Shows that X and X^2 become highly correlated when X is confined to a narrow range."""
    print("\n=== Block 3: Inherent Multicollinearity in Polynomial Terms ===")
    rng = np.random.default_rng(seed=17)
    x_narrow = rng.uniform(95, 105, 200)
    r_narrow = np.corrcoef(x_narrow, x_narrow ** 2)[0, 1]
    vif_narrow = 1 / (1 - r_narrow ** 2)

    x_wide = rng.uniform(1, 200, 200)
    r_wide = np.corrcoef(x_wide, x_wide ** 2)[0, 1]
    vif_wide = 1 / (1 - r_wide ** 2)

    print(f"Narrow range X in [95, 105]: corr(X, X^2) = {r_narrow:.4f}, VIF = {vif_narrow:.2f}")
    print(f"Wide range   X in [1, 200]:  corr(X, X^2) = {r_wide:.4f}, VIF = {vif_wide:.2f}")
    print("Confining X to a narrow range makes X^2 nearly linear in X (high VIF),")
    print("while a wide range breaks that near-linearity, sharply reducing VIF.")


if __name__ == "__main__":
    hp, mpg, c = fit_quadratic_model()
    compare_linear_vs_quadratic(hp, mpg)
    polynomial_multicollinearity_demo()
