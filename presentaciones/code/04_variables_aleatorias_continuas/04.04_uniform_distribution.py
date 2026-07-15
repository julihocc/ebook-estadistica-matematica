"""
Computational Lab: Section 04.04 - Continuous Uniform Distribution
====================================================================
Validates the Uniform PDF and CDF, computes quantiles, generates Monte Carlo
samples, and verifies the Kolmogorov-Smirnov goodness-of-fit test against
a uniform reference distribution.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import integrate, stats


def verify_uniform_pdf_and_cdf():
    """Validates Uniform PDF normalization and CDF computation."""
    print("=== Block 1: Uniform PDF & CDF Validation ===")
    # Uniform(2, 8)
    a, b = 2.0, 8.0
    result, error = integrate.quad(lambda x: 1.0/(b - a), a, b)
    print(f"Uniform({a}, {b}) PDF integral: {result:.8f} (should be 1.0)")

    # CDF F(x) = (x - a)/(b - a) for x in [a, b]
    def uniform_cdf(x, a, b):
        if x < a:
            return 0.0
        elif x > b:
            return 1.0
        else:
            return (x - a) / (b - a)

    # Verify against SciPy
    test_points = [0.0, 1.0, 2.0, 3.5, 5.0, 8.0, 10.0, 15.0]
    print(f"\nCDF comparison for Uniform({a}, {b}):")
    print(f"  {'x':>5} | {'F(x) manual':>12} | {'F(x) scipy':>12} | {'|diff|':>10}")
    print(f"  {'-'*5}-+-{'-'*12}-+-{'-'*12}-+-{'-'*10}")
    for x in test_points:
        cdf_manual = uniform_cdf(x, a, b)
        cdf_scipy = stats.uniform.cdf(x, loc=a, scale=b - a)
        print(f"  {x:>5.1f} | {cdf_manual:>12.6f} | {cdf_scipy:>12.6f} | {abs(cdf_manual - cdf_scipy):>10.2e}")

    # Quantiles
    print(f"\nQuantiles for Uniform({a}, {b}):")
    for p in [0.10, 0.25, 0.50, 0.75, 0.90]:
        q_manual = a + p * (b - a)
        q_scipy = stats.uniform.ppf(p, loc=a, scale=b - a)
        print(f"  q_{p}: manual = {q_manual:.4f}, scipy = {q_scipy:.4f}, match = {abs(q_manual - q_scipy) < 1e-10}")


def verify_quantiles_and_monte_carlo():
    """Computes quantiles and Monte Carlo verification of moments."""
    print("\n=== Block 2: Quantiles & Monte Carlo Generation ===")
    # Quantile check
    quantiles = [0.05, 0.25, 0.50, 0.75, 0.95]
    print("Quantile verification for Uniform(0, 1):")
    for p in quantiles:
        q = stats.uniform.ppf(p, loc=0, scale=1)
        print(f"  q_{p:.2f} = {q:.4f} (CDF at q = {stats.uniform.cdf(q):.4f})")

    # Monte Carlo verification
    np.random.seed(42)
    n_samples = 100_000
    samples = np.random.uniform(0, 1, n_samples)
    emp_mean = np.mean(samples)
    emp_var = np.var(samples, ddof=1)
    print(f"\nMonte Carlo (N={n_samples:,} samples of U(0,1)):")
    print(f"  Empirical mean: {emp_mean:.4f} (theoretical: 0.5000)")
    print(f"  Empirical var:  {emp_var:.4f} (theoretical: {1/12:.4f})")
    print(f"  Empirical min:  {np.min(samples):.4f}")
    print(f"  Empirical max:  {np.max(samples):.4f}")

    # CDF comparison
    print(f"\nCDF comparison (empirical vs theoretical):")
    for x in [0.1, 0.3, 0.5, 0.7, 0.9]:
        cdf_emp = np.mean(samples <= x)
        cdf_theo = x
        print(f"  F({x:.1f}): empirical = {cdf_emp:.4f}, theoretical = {cdf_theo:.4f}, diff = {abs(cdf_emp - cdf_theo):.4f}")

    # Inverse transform sampling for Exponential
    print(f"\nInverse transform sampling for Exponential(lambda=2):")
    U = np.random.uniform(0, 1, 50_000)
    Y = -np.log(1 - U) / 2.0
    print(f"  Y mean: {np.mean(Y):.4f} (theoretical: 0.5000)")
    print(f"  Y var:  {np.var(Y, ddof=1):.4f} (theoretical: 0.2500)")
    print(f"  KS test vs Exp(2): stat = {stats.kstest(Y, stats.expon(scale=0.5).cdf).statistic:.4f}")


def verify_max_entropy_and_order_statistics():
    """Verifies maximum entropy property and analyzes order statistics."""
    print("\n=== Block 3: Maximum Entropy & Order Statistics ===")
    # Maximum entropy verification
    a, b = 0.0, 1.0
    # Entropy of Uniform(0,1) = log(b-a) = 0
    entropy_uniform, _ = integrate.quad(lambda x: -np.log(1.0/(b - a)) * (1.0/(b - a)), a, b)
    print(f"Entropy of Uniform(0, 1): {entropy_uniform:.6f} nats (theoretical: 0)")

    # Entropy of Beta(a, b) using direct numerical integration
    def beta_entropy_numerical(a_param, b_param):
        from scipy.special import beta as beta_func
        def integrand(x):
            if x <= 0 or x >= 1:
                return 0.0
            pdf = x**(a_param - 1) * (1 - x)**(b_param - 1) / beta_func(a_param, b_param)
            return -pdf * np.log(pdf + 1e-300)
        result, _ = integrate.quad(integrand, 0, 1)
        return result
    ent_normal = beta_entropy_numerical(2, 2)
    ent_uniform_compare = beta_entropy_numerical(1, 1)
    print(f"Entropy of Beta(2, 2): {ent_normal:.6f} nats (Uniform(0,1)={ent_uniform_compare:.6f})")
    print(f"  Uniform has maximum entropy among bounded support distributions")

    # Order statistics of Uniform(0, 1)
    n = 10
    np.random.seed(7)
    samples = np.random.uniform(0, 1, (100_000, n))
    order_stats = np.sort(samples, axis=1)
    for k in [1, 5, 10]:
        emp_mean = np.mean(order_stats[:, k - 1])
        theo_mean = k / (n + 1)
        print(f"  X_({k}) of n={n} samples: empirical mean = {emp_mean:.4f}, theoretical = {theo_mean:.4f}")

    # Kolmogorov-Smirnov test on uniform samples
    print("\nKolmogorov-Smirnov test on uniform samples:")
    ks_uniform = stats.kstest(samples[:, 0], stats.uniform(0, 1).cdf)
    print(f"  D = {ks_uniform.statistic:.4f}, p-value = {ks_uniform.pvalue:.4f}")
    print(f"  Decision: {'Reject H0' if ks_uniform.pvalue < 0.05 else 'Fail to reject H0'}")

    # Test on non-uniform (exponential) data
    exp_samples = np.random.exponential(1.0, 100_000)
    ks_exp = stats.kstest(exp_samples, stats.uniform(0, 1).cdf)
    print(f"\n  KS test for exponential samples vs U(0,1):")
    print(f"  D = {ks_exp.statistic:.4f}, p-value = {ks_exp.pvalue:.6e}")
    print(f"  Decision: {'Reject H0' if ks_exp.pvalue < 0.05 else 'Fail to reject H0'}")


if __name__ == "__main__":
    verify_uniform_pdf_and_cdf()
    verify_quantiles_and_monte_carlo()
    verify_max_entropy_and_order_statistics()
