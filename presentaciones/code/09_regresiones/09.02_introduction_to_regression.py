"""
Computational Lab: Section 09.02 - Introduction to Linear Regression
====================================================================
Contrasts deterministic and stochastic models, fits both a simple and a
multiple regression on a synthetic house-price example (price as a function
of size, amenities, and transit access) to show why more predictors can
capture more of the picture, and runs a quick numeric preview of the five
classical assumptions later audited in full in Section 09.09.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np


def deterministic_vs_stochastic_models():
    """Contrasts a deterministic physical law with a stochastic regression model."""
    print("=== Block 1: Deterministic vs. Stochastic Models ===")
    mass = np.array([2.0, 4.0, 6.0, 8.0, 10.0])
    acceleration = np.array([1.5, 1.5, 1.5, 1.5, 1.5])
    force_deterministic = mass * acceleration
    print(f"Deterministic model F=ma: residual variance = {np.var(force_deterministic - mass * acceleration):.6f}")

    rng = np.random.default_rng(seed=1)
    size = np.linspace(50, 200, 20)
    price_stochastic = 20.0 + 1.2 * size + rng.normal(scale=15.0, size=20)
    beta1 = np.sum((size - size.mean()) * (price_stochastic - price_stochastic.mean())) / np.sum((size - size.mean()) ** 2)
    beta0 = price_stochastic.mean() - beta1 * size.mean()
    residuals = price_stochastic - (beta0 + beta1 * size)
    print(f"Stochastic model (price~size): residual variance = {np.var(residuals):.4f} (nonzero, as expected)")


def simple_vs_multiple_regression():
    """Fits price on size alone, then on size+amenities+transit, comparing R^2."""
    print("\n=== Block 2: Simple vs. Multiple Regression (House Price) ===")
    rng = np.random.default_rng(seed=4)
    n = 60
    size = rng.uniform(50, 250, n)
    amenities = rng.uniform(0, 10, n)
    transit = rng.uniform(0, 10, n)
    true_price = 15.0 + 0.9 * size + 8.0 * amenities + 5.0 * transit
    price = true_price + rng.normal(scale=20.0, size=n)

    def r_squared(X, y):
        beta, *_ = np.linalg.lstsq(X, y, rcond=None)
        fitted = X @ beta
        ss_res = np.sum((y - fitted) ** 2)
        ss_tot = np.sum((y - y.mean()) ** 2)
        return 1 - ss_res / ss_tot, beta

    X_simple = np.column_stack([np.ones(n), size])
    r2_simple, beta_simple = r_squared(X_simple, price)
    print(f"Simple model  (price~size):                R^2={r2_simple:.4f}, beta={np.round(beta_simple, 3)}")

    X_multiple = np.column_stack([np.ones(n), size, amenities, transit])
    r2_multiple, beta_multiple = r_squared(X_multiple, price)
    print(f"Multiple model (price~size+amenities+transit): R^2={r2_multiple:.4f}, beta={np.round(beta_multiple, 3)}")
    print(f"R^2 improvement from adding amenities and transit: {r2_multiple - r2_simple:.4f}")


def classical_assumptions_quick_preview():
    """Quick numeric spot-check preview of the five classical assumptions."""
    print("\n=== Block 3: Classical Assumptions --- Quick Preview ===")
    rng = np.random.default_rng(seed=9)
    n = 100
    x = rng.uniform(1, 10, n)
    y = 5.0 + 2.0 * x + rng.normal(scale=1.5, size=n)

    X = np.column_stack([np.ones(n), x])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    residuals = y - X @ beta

    print(f"Zero-mean check:       mean(residuals) = {residuals.mean():.6f} (should be near 0)")
    half = n // 2
    var_first_half = np.var(residuals[:half])
    var_second_half = np.var(residuals[half:])
    print(f"Homoscedasticity check: Var(first half)={var_first_half:.4f}, Var(second half)={var_second_half:.4f} (should be similar)")
    print("Full formal audits of these assumptions (Durbin-Watson, Breusch-Pagan,")
    print("Shapiro-Wilk, Cook's Distance) are developed in Section 09.09.")


if __name__ == "__main__":
    deterministic_vs_stochastic_models()
    simple_vs_multiple_regression()
    classical_assumptions_quick_preview()
