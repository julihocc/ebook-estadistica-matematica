"""
Computational Lab: Section 07.01 - Foundations of Hypothesis Testing
====================================================================
Verifies the Type I error rate of a Z-test via repeated sampling under a true
null hypothesis, computes the Type II error probability and the power
function for a right-tailed Z-test, and determines (then verifies via
simulation) the minimum sample size required to reach a target power level.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import stats


def verify_type_i_error_rate():
    """Simulates repeated Z-tests under a true H0 and verifies the Type I error rate equals alpha."""
    print("=== Block 1: Type I Error Rate Under a True Null Hypothesis ===")
    mu0, sigma = 100.0, 15.0
    n = 25
    alpha = 0.05
    n_trials = 200_000
    rng = np.random.default_rng(42)

    z_crit = stats.norm.ppf(1 - alpha)
    samples = rng.normal(mu0, sigma, size=(n_trials, n))
    xbars = np.mean(samples, axis=1)
    z_stats = (xbars - mu0) / (sigma / np.sqrt(n))

    rejections = np.mean(z_stats > z_crit)
    print(f"H0: mu={mu0}, true mu={mu0} (H0 is true), sigma={sigma}, n={n}, trials={n_trials}")
    print(f"  Critical value z_crit (alpha={alpha}): {z_crit:.4f}")
    print(f"  Empirical Type I error rate (false rejection rate): {rejections:.4f}")
    print(f"  Nominal alpha: {alpha:.4f}")
    print(f"  Difference: {abs(rejections - alpha):.4f} (should be small by LLN)")


def power_function_and_type_ii_error():
    """Computes Type II error probability and power analytically, then verifies via simulation."""
    print("\n=== Block 2: Type II Error (beta) and Power Function ===")
    mu0, sigma = 100.0, 15.0
    n = 25
    alpha = 0.05
    mu_a = 108.0
    rng = np.random.default_rng(7)

    se = sigma / np.sqrt(n)
    z_crit = stats.norm.ppf(1 - alpha)
    c = mu0 + z_crit * se
    print(f"Rejection region: Xbar > {c:.4f} (critical value c)")

    beta_analytic = stats.norm.cdf((c - mu_a) / se)
    power_analytic = 1 - beta_analytic
    print(f"Analytic beta (mu_a={mu_a}): {beta_analytic:.4f}")
    print(f"Analytic power (1-beta): {power_analytic:.4f}")

    n_trials = 200_000
    samples = rng.normal(mu_a, sigma, size=(n_trials, n))
    xbars = np.mean(samples, axis=1)
    power_empirical = np.mean(xbars > c)
    print(f"Empirical power via Monte Carlo (true mu={mu_a}): {power_empirical:.4f}")

    print("\n  Power function Pow(mu_a) across a grid of true means:")
    for mu_grid in [100.0, 102.0, 104.0, 106.0, 108.0, 110.0, 114.0]:
        pow_val = 1 - stats.norm.cdf((c - mu_grid) / se)
        print(f"    mu_a={mu_grid:6.1f}  ->  Pow(mu_a) = {pow_val:.4f}")


def sample_size_for_target_power():
    """Computes the minimum sample size for a target power and verifies it via simulation."""
    print("\n=== Block 3: Sample Size for a Target Power ===")
    mu0, mu_a, sigma = 100.0, 108.0, 15.0
    alpha = 0.05
    target_power = 0.90
    rng = np.random.default_rng(99)

    z_alpha = stats.norm.ppf(1 - alpha)
    z_beta = stats.norm.ppf(target_power)
    n_exact = ((z_alpha + z_beta) * sigma / (mu_a - mu0)) ** 2
    n_required = int(np.ceil(n_exact))
    print(f"z_alpha={z_alpha:.4f}, z_beta={z_beta:.4f}")
    print(f"Exact n from formula: {n_exact:.4f}  ->  rounded up: n={n_required}")

    se = sigma / np.sqrt(n_required)
    z_crit = stats.norm.ppf(1 - alpha)
    c = mu0 + z_crit * se
    n_trials = 200_000
    samples = rng.normal(mu_a, sigma, size=(n_trials, n_required))
    xbars = np.mean(samples, axis=1)
    achieved_power = np.mean(xbars > c)
    print(f"Verification with n={n_required}: empirical power = {achieved_power:.4f} (target = {target_power})")

    n_one_less = n_required - 1
    se2 = sigma / np.sqrt(n_one_less)
    c2 = mu0 + z_crit * se2
    samples2 = rng.normal(mu_a, sigma, size=(n_trials, n_one_less))
    power_one_less = np.mean(np.mean(samples2, axis=1) > c2)
    print(f"  With n={n_one_less} (one less): empirical power = {power_one_less:.4f} (falls short of target)")


if __name__ == "__main__":
    verify_type_i_error_rate()
    power_function_and_type_ii_error()
    sample_size_for_target_power()
