"""
Computational Lab: Section 09.02 - Multiple Linear Regression, the Normal
Equation, and Ridge/Lasso Regularization
====================================================================
Solves the multiple regression Normal Equation in matrix form and verifies
the Hat Matrix's symmetry/idempotence, fits Ridge regression via its closed
form and observes coefficient shrinkage as lambda grows, and implements
Lasso via coordinate descent to show it drives coefficients exactly to zero
(sparsity / automatic variable selection).

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np


def normal_equation_and_hat_matrix():
    """Solves beta_hat = (X^T X)^-1 X^T Y and verifies Hat Matrix properties."""
    print("=== Block 1: Normal Equation and the Hat Matrix ===")
    rng = np.random.default_rng(seed=21)
    n = 20
    x1 = rng.uniform(1, 10, n)
    x2 = rng.uniform(5, 20, n)
    true_beta = np.array([4.0, 2.0, -0.5])
    X = np.column_stack([np.ones(n), x1, x2])
    y = X @ true_beta + rng.normal(scale=1.5, size=n)

    beta_hat = np.linalg.inv(X.T @ X) @ X.T @ y
    beta_hat_lstsq, *_ = np.linalg.lstsq(X, y, rcond=None)
    print(f"beta_hat (normal equation) = {np.round(beta_hat, 4)}")
    print(f"beta_hat (np.linalg.lstsq check) = {np.round(beta_hat_lstsq, 4)}")

    H = X @ np.linalg.inv(X.T @ X) @ X.T
    symmetric_error = np.max(np.abs(H - H.T))
    idempotent_error = np.max(np.abs(H @ H - H))
    print(f"Hat matrix symmetry error  max|H - H^T| = {symmetric_error:.2e}")
    print(f"Hat matrix idempotence error max|H^2 - H| = {idempotent_error:.2e}")

    return X, y


def ridge_regression_shrinkage(X, y):
    """Fits Ridge regression for increasing lambda and observes coefficient shrinkage."""
    print("\n=== Block 2: Ridge Regression and Coefficient Shrinkage ===")
    p = X.shape[1]
    lambdas = [0.0, 1.0, 10.0, 100.0]
    for lam in lambdas:
        beta_ridge = np.linalg.inv(X.T @ X + lam * np.eye(p)) @ X.T @ y
        norm_beta = np.linalg.norm(beta_ridge[1:])
        print(f"lambda={lam:6.1f}: beta_ridge={np.round(beta_ridge, 4)}, ||beta[1:]||={norm_beta:.4f}")


def soft_threshold(rho, lam):
    """Soft-thresholding operator used by coordinate descent for Lasso."""
    if rho > lam:
        return rho - lam
    if rho < -lam:
        return rho + lam
    return 0.0


def lasso_coordinate_descent(X, y, lam, n_iter=300):
    """Fits Lasso via cyclic coordinate descent (intercept unpenalized)."""
    p = X.shape[1]
    beta = np.zeros(p)
    for _ in range(n_iter):
        for j in range(p):
            residual = y - X @ beta + X[:, j] * beta[j]
            rho = X[:, j] @ residual
            z = np.sum(X[:, j] ** 2)
            if j == 0:
                beta[j] = rho / z
            else:
                beta[j] = soft_threshold(rho, lam / 2) / z
    return beta


def lasso_sparsity_demo(X, y):
    """Runs Lasso for increasing lambda and shows coefficients driven to zero."""
    print("\n=== Block 3: Lasso Regression via Coordinate Descent (Sparsity) ===")
    for lam in [0.0, 50.0, 200.0, 1000.0]:
        beta_lasso = lasso_coordinate_descent(X, y, lam)
        n_zero = np.sum(np.isclose(beta_lasso[1:], 0.0, atol=1e-6))
        print(f"lambda={lam:6.1f}: beta_lasso={np.round(beta_lasso, 4)}, zero coefficients={n_zero}/{len(beta_lasso) - 1}")


if __name__ == "__main__":
    X, y = normal_equation_and_hat_matrix()
    ridge_regression_shrinkage(X, y)
    lasso_sparsity_demo(X, y)
