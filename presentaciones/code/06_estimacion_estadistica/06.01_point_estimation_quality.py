"""
Computational Lab: Section 06.01 - Point Estimation, Unbiasedness, Efficiency, and Consistency
====================================================================
Validates the bias-variance-MSE decomposition and relative efficiency by
comparing the sample mean against a naive single-observation estimator,
verifies the optimal shrinkage estimator that trades bias for a lower MSE,
and confirms the consistency of the sample proportion via a Chebyshev bound
compared against empirical Monte Carlo coverage.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np


def verify_bias_variance_mse_and_efficiency():
    """Compares MSE and relative efficiency of Xbar vs. a naive single-observation estimator."""
    print("=== Block 1: Bias-Variance-MSE Decomposition and Relative Efficiency ===")
    mu, sigma = 50.0, 10.0
    n = 16
    n_trials = 200_000
    rng = np.random.default_rng(42)

    samples = rng.normal(mu, sigma, size=(n_trials, n))
    xbar = np.mean(samples, axis=1)
    t1 = samples[:, 0]

    for name, estimator in [("Xbar", xbar), ("T1 (single obs.)", t1)]:
        bias = np.mean(estimator) - mu
        var = np.var(estimator, ddof=1)
        mse = np.mean((estimator - mu) ** 2)
        print(f"{name}: bias={bias:.4f}, Var={var:.4f}, MSE={mse:.4f} (Var+bias^2={var+bias**2:.4f})")

    eff = np.var(t1, ddof=1) / np.var(xbar, ddof=1)
    print(f"Relative efficiency Ef(Xbar, T1) = {eff:.4f} (theoretical: n = {n})")


def verify_shrinkage_estimator():
    """Finds and verifies the optimal shrinkage constant c* that minimizes MSE."""
    print("\n=== Block 2: Shrinkage Estimator and Optimal MSE Trade-off ===")
    v, theta = 5.0, 3.0
    c_star = theta**2 / (v + theta**2)
    print(f"v={v}, theta={theta}: c* = theta^2/(v+theta^2) = {c_star:.4f}")

    def mse(c):
        bias = (c - 1) * theta
        var = c**2 * v
        return var + bias**2

    print(f"  MSE(c=1, unbiased) = {mse(1.0):.4f}")
    print(f"  MSE(c=c*) = {mse(c_star):.4f}")
    print(f"  MSE reduction: {(1 - mse(c_star) / mse(1.0)) * 100:.1f}%")

    # Sweep c to confirm c* is indeed the minimum
    c_grid = np.linspace(0.01, 1.5, 500)
    mse_grid = np.array([mse(c) for c in c_grid])
    c_argmin = c_grid[np.argmin(mse_grid)]
    print(f"  Grid search minimum at c = {c_argmin:.4f} (should match c* above)")


def verify_consistency_via_chebyshev():
    """Verifies consistency of the sample proportion via the Chebyshev bound vs. Monte Carlo."""
    print("\n=== Block 3: Consistency of the Sample Proportion via Chebyshev ===")
    p = 0.5
    epsilon = 0.05
    rng = np.random.default_rng(42)
    n_trials = 100_000

    print(f"p={p}, epsilon={epsilon}")
    print(f"  {'n':>6} | {'Chebyshev bound':>15} | {'Empirical P(|phat-p|>=eps)':>28}")
    print(f"  {'-'*6}-+-{'-'*15}-+-{'-'*28}")
    for n in [100, 1000, 4000]:
        chebyshev_bound = (p * (1 - p) / n) / epsilon**2
        samples = rng.binomial(n, p, size=n_trials) / n
        empirical = np.mean(np.abs(samples - p) >= epsilon)
        print(f"  {n:>6} | {chebyshev_bound:>15.4f} | {empirical:>28.4f}")

    # Minimum n required for Chebyshev bound <= 0.10
    target_bound = 0.10
    n_required = (p * (1 - p)) / (epsilon**2 * target_bound)
    print(f"\nMinimum n for Chebyshev bound <= {target_bound}: n >= {n_required:.0f}")


if __name__ == "__main__":
    verify_bias_variance_mse_and_efficiency()
    verify_shrinkage_estimator()
    verify_consistency_via_chebyshev()
