"""
Computational Lab: Section 05.01 - Simple Random Sampling and the Unbiased Sample Variance
====================================================================
Validates the unbiasedness of the sample variance (Bessel's correction) via
Monte Carlo, verifies the sampling distribution of the mean (E(Xbar)=mu,
Var(Xbar)=sigma^2/n) across sample sizes, and quantifies the finite
population correction (FPC) for sampling without replacement.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import stats


def verify_unbiased_sample_variance():
    """Validates E(S^2)=sigma^2 (Bessel's correction) via Monte Carlo, vs the biased estimator."""
    print("=== Block 1: Unbiased Sample Variance (Bessel's Correction) ===")
    mu, sigma = 50.0, 10.0
    n = 5
    n_trials = 200_000

    rng = np.random.default_rng(42)
    samples = rng.normal(mu, sigma, size=(n_trials, n))

    s2_unbiased = np.var(samples, axis=1, ddof=1)   # divide by n-1
    s2_biased = np.var(samples, axis=1, ddof=0)     # divide by n

    print(f"Population: N({mu}, {sigma**2}), sample size n={n}, trials={n_trials}")
    print(f"  E(S^2) [unbiased, ddof=1]: {np.mean(s2_unbiased):.4f} (theoretical: {sigma**2:.4f})")
    print(f"  E(sigma_hat^2) [biased, ddof=0]: {np.mean(s2_biased):.4f} (theoretical: {(n-1)/n*sigma**2:.4f})")
    print(f"  Ratio biased/unbiased: {np.mean(s2_biased)/np.mean(s2_unbiased):.4f} (theoretical (n-1)/n: {(n-1)/n:.4f})")

    # Worked example: {8, 12, 10, 14, 6}
    data = np.array([8, 12, 10, 14, 6])
    xbar = np.mean(data)
    s2 = np.var(data, ddof=1)
    print(f"\nWorked example {{8,12,10,14,6}}: mean={xbar:.4f}, S^2={s2:.4f}")

    # Shortcut formula verification: S^2 = (sum(x^2) - n*xbar^2) / (n-1)
    shortcut = (np.sum(data**2) - len(data) * xbar**2) / (len(data) - 1)
    print(f"  Shortcut formula check: {shortcut:.4f} (should match S^2 above)")


def verify_sampling_distribution_of_mean():
    """Verifies E(Xbar)=mu and Var(Xbar)=sigma^2/n across sample sizes; SE scaling with sqrt(n)."""
    print("\n=== Block 2: Sampling Distribution of the Mean ===")
    mu, sigma = 500.0, 40.0
    n_trials = 200_000
    rng = np.random.default_rng(42)

    print(f"Population: N({mu}, {sigma**2})")
    print(f"  {'n':>5} | {'E(Xbar) emp':>12} | {'Var(Xbar) emp':>14} | {'sigma^2/n theo':>14} | {'SE emp':>8}")
    print(f"  {'-'*5}-+-{'-'*12}-+-{'-'*14}-+-{'-'*14}-+-{'-'*8}")
    for n in [25, 100, 400]:
        samples = rng.normal(mu, sigma, size=(n_trials, n))
        xbars = np.mean(samples, axis=1)
        emp_mean = np.mean(xbars)
        emp_var = np.var(xbars, ddof=1)
        theo_var = sigma**2 / n
        print(f"  {n:>5} | {emp_mean:>12.4f} | {emp_var:>14.4f} | {theo_var:>14.4f} | {np.sqrt(emp_var):>8.4f}")

    print("\nStandard error scaling (sigma=15):")
    sigma_meas = 15.0
    for n in [25, 100, 400]:
        se = sigma_meas / np.sqrt(n)
        print(f"  n={n}: SE = {se:.4f}")


def verify_finite_population_correction():
    """Compares naive infinite-population variance vs the finite population correction (FPC)."""
    print("\n=== Block 3: Finite Population Correction (FPC) ===")
    N = 200
    n = 20
    rng = np.random.default_rng(42)

    population = rng.normal(1000, 30, size=N)
    sigma2_pop = np.var(population, ddof=0)

    naive_var = sigma2_pop / n
    fpc_factor = (N - n) / (N - 1)
    fpc_var = naive_var * fpc_factor

    print(f"Population size N={N}, sample size n={n}, population variance = {sigma2_pop:.4f}")
    print(f"  Naive Var(Xbar) = sigma^2/n = {naive_var:.4f}")
    print(f"  FPC factor (N-n)/(N-1) = {fpc_factor:.4f}")
    print(f"  Var(Xbar) with FPC = {fpc_var:.4f}")

    # Empirical verification via exhaustive-like Monte Carlo sampling without replacement
    n_trials = 50_000
    xbars = np.empty(n_trials)
    for i in range(n_trials):
        sample_idx = rng.choice(N, size=n, replace=False)
        xbars[i] = np.mean(population[sample_idx])
    emp_var = np.var(xbars, ddof=1)
    print(f"  Empirical Var(Xbar) [sampling without replacement, {n_trials} trials]: {emp_var:.4f}")

    print(f"\nFPC factor approaches 1 as N -> infinity (sampling fraction n/N -> 0):")
    for N_large in [200, 2000, 20000]:
        factor = (N_large - n) / (N_large - 1)
        print(f"  N={N_large:>6}: FPC factor = {factor:.4f}")


if __name__ == "__main__":
    verify_unbiased_sample_variance()
    verify_sampling_distribution_of_mean()
    verify_finite_population_correction()
