"""
Computational Lab: Section 04.03 - Continuous Expectation, Variance and LOTUS
=============================================================================
Validates continuous expectation E[X] = integral x*f(x) dx, variance via
central moments, the Law of the Unconscious Statistician (LOTUS) for
transformations, and the law of total variance.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import integrate, stats


def verify_expectation_and_lotus():
    """Computes expectation via integration and verifies LOTUS for transformations."""
    print("=== Block 1: Expectation Computation & LOTUS Verification ===")
    # Triangular PDF: f(x) = 2x for 0 <= x <= 1
    def triangular_pdf(x):
        return 2.0 * x * ((x >= 0) & (x <= 1))

    mean_num, _ = integrate.quad(lambda x: x * triangular_pdf(x), 0, 1)
    second_moment, _ = integrate.quad(lambda x: x**2 * triangular_pdf(x), 0, 1)
    var_num = second_moment - mean_num**2
    print(f"Triangular(0,1): E[X] = {mean_num:.6f} (closed form: 2/3 = {2/3:.6f})")
    print(f"Triangular(0,1): E[X^2] = {second_moment:.6f} (closed form: 1/2 = {0.5:.6f})")
    print(f"Triangular(0,1): Var(X) = {var_num:.6f} (closed form: 1/18 = {1/18:.6f})")

    # LOTUS for E[sqrt(X)] on Triangular
    lotus_sqrt, _ = integrate.quad(lambda x: np.sqrt(x) * triangular_pdf(x), 0, 1)
    print(f"\nLOTUS E[sqrt(X)]: {lotus_sqrt:.6f}")
    print(f"  Theoretical: integral x^(1/2) * 2x dx from 0 to 1 = 4/7 = {4/7:.6f}")

    # LOTUS for E[log(X)] (when X > 0)
    lotus_log, _ = integrate.quad(lambda x: np.log(x) * triangular_pdf(x), 0.001, 1)
    print(f"\nLOTUS E[log(X)]: {lotus_log:.6f}")
    print(f"  Numerical: integral log(x) * 2x dx from 0 to 1 = -1/2 = {-0.5:.6f}")

    # Verify linearity E[aX + b] = a*E[X] + b
    a, b = 3.5, 10.0
    linear_num, _ = integrate.quad(lambda x: (a * x + b) * triangular_pdf(x), 0, 1)
    linear_closed = a * mean_num + b
    print(f"\nLinearity E[3.5X + 10] = {linear_num:.6f} (closed: {linear_closed:.6f})")


def verify_variance_and_central_moments():
    """Computes variance and central moments for various distributions."""
    print("\n=== Block 2: Variance & Central Moments ===")
    # Uniform(0, 1)
    mean_unif, _ = integrate.quad(lambda x: x * stats.uniform.pdf(x), 0, 1)
    var_unif, _ = integrate.quad(lambda x: (x - 0.5)**2 * stats.uniform.pdf(x), 0, 1)
    print(f"Uniform(0,1): E[X] = {mean_unif:.6f}, Var(X) = {var_unif:.6f}")
    print(f"  Closed forms: E[X] = 0.5, Var(X) = 1/12 = {1/12:.6f}")

    # Exponential(1.0)
    lam = 1.0
    mean_exp = 1.0 / lam
    var_exp = 1.0 / lam**2
    third_central, _ = integrate.quad(lambda x: (x - mean_exp)**3 * stats.expon.pdf(x), 0, 50)
    fourth_central, _ = integrate.quad(lambda x: (x - mean_exp)**4 * stats.expon.pdf(x), 0, 50)
    skewness = third_central / var_exp**1.5
    kurtosis = fourth_central / var_exp**2 - 3
    print(f"\nExponential(1.0): E[X] = {mean_exp:.6f}, Var(X) = {var_exp:.6f}")
    print(f"  Skewness: {skewness:.6f} (theoretical: 2.0)")
    print(f"  Excess kurtosis: {kurtosis:.6f} (theoretical: 6.0)")

    # Normal(0, 1)
    mean_norm, _ = integrate.quad(lambda x: x * stats.norm.pdf(x), -10, 10)
    var_norm, _ = integrate.quad(lambda x: (x - 0)**2 * stats.norm.pdf(x), -10, 10)
    print(f"\nNormal(0,1): E[X] = {mean_norm:.6f}, Var(X) = {var_norm:.6f}")

    # Law of total variance: Var(X) = E[Var(X|Y)] + Var(E[X|Y])
    # Demonstrate with a simple hierarchical model
    np.random.seed(42)
    n_groups = 100
    n_per_group = 50
    group_means = np.random.normal(0, 2.0, n_groups)
    samples = np.array([np.random.normal(mu, 1.0, n_per_group) for mu in group_means]).flatten()
    total_var = np.var(samples, ddof=1)
    group_vars = np.array([np.var(np.random.normal(mu, 1.0, n_per_group), ddof=1) for mu in group_means])
    e_within = np.mean(group_vars)
    between = np.var(group_means, ddof=1)
    print(f"\nHierarchical model: total Var(X) = {total_var:.4f}")
    print(f"  E[Var(X|Y)] (within) = {e_within:.4f}")
    print(f"  Var(E[X|Y]) (between) = {between:.4f}")
    print(f"  Sum (theoretical) = {e_within + between:.4f}")
    print(f"  Match: {abs(total_var - e_within - between) < 0.5}")


def verify_monte_carlo_and_applications():
    """Monte Carlo verification of moments and error propagation in measurement."""
    print("\n=== Block 3: Monte Carlo & Error Propagation ===")
    np.random.seed(42)
    n_samples = 250_000

    # Exponential moments via Monte Carlo
    samples_exp = np.random.exponential(1.0, n_samples)
    emp_mean = np.mean(samples_exp)
    emp_var = np.var(samples_exp, ddof=1)
    emp_skew = np.mean((samples_exp - emp_mean)**3) / emp_var**1.5
    emp_kurt = np.mean((samples_exp - emp_mean)**4) / emp_var**2 - 3
    print(f"Exponential(1.0) Monte Carlo (N={n_samples:,}):")
    print(f"  Empirical mean: {emp_mean:.4f} (theoretical: 1.0000)")
    print(f"  Empirical var: {emp_var:.4f} (theoretical: 1.0000)")
    print(f"  Empirical skewness: {emp_skew:.4f} (theoretical: 2.0000)")
    print(f"  Empirical kurtosis: {emp_kurt:.4f} (theoretical: 6.0000)")

    # Error propagation in measurement
    sigma = 0.1
    true_value = 5.0
    n_measurements_list = [1, 4, 16, 64, 256, 1024]
    print(f"\nError propagation for true value = {true_value}, sigma = {sigma}:")
    print(f"  {'n':>5} | {'SE = sigma/sqrt(n)':>18} | {'95% CI half-width':>20}")
    for n in n_measurements_list:
        se = sigma / np.sqrt(n)
        ci_width = 1.96 * se
        print(f"  {n:>5} | {se:>18.4f} | {ci_width:>20.4f}")

    # Find n for SE < 0.01
    target_se = 0.01
    required_n = (sigma / target_se) ** 2
    print(f"\n  For SE = {target_se}: required n = {required_n:.0f}")


if __name__ == "__main__":
    verify_expectation_and_lotus()
    verify_variance_and_central_moments()
    verify_monte_carlo_and_applications()
