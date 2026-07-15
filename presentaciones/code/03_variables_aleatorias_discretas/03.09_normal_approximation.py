"""
Computational Lab: Section 03.09 - Normal Distribution and Continuous Approximation
=====================================================================================
Validates the Normal PDF, Z-score standardization, the De Moivre-Laplace
approximation of Binomial by Normal with Yates continuity correction,
and the Poisson-to-Normal approximation including the Central Limit Theorem
applied to sums of i.i.d. exponential random variables.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import stats


def verify_normal_pdf_and_zscore():
    """Validates Normal PDF integration, symmetry, and Z-score standardization."""
    print("=== Block 1: Normal PDF & Z-Score Standardization ===")
    # Industrial process: diameters X ~ N(2.50, 0.05^2)
    mu, sigma = 2.50, 0.05
    x_grid = np.linspace(2.30, 2.70, 200)
    pdf_vals = stats.norm.pdf(x_grid, loc=mu, scale=sigma)

    # Check 1: Numerical integration of PDF over a wide range
    x_wide = np.linspace(mu - 6 * sigma, mu + 6 * sigma, 10000)
    pdf_wide = stats.norm.pdf(x_wide, loc=mu, scale=sigma)
    integral = np.trapezoid(pdf_wide, x_wide)
    print(f"X ~ N(mu={mu}, sigma={sigma}) | PDF numerical integral: {integral:.6f}")
    print(f"Peak PDF value at x=mu: {stats.norm.pdf(mu, loc=mu, scale=sigma):.4f}")

    # Check 2: Z-score standardization
    z_lower = (2.42 - mu) / sigma
    z_upper = (2.58 - mu) / sigma
    p_exact = stats.norm.cdf(z_upper) - stats.norm.cdf(z_lower)
    p_symmetry = 2 * stats.norm.cdf(z_upper) - 1  # by symmetry of standard normal
    print(f"\nP(2.42 <= X <= 2.58): exact = {p_exact:.6f}")
    print(f"By symmetry: 2*Phi({z_upper:.2f}) - 1 = {p_symmetry:.6f}")

    # Check 3: 68-95-99.7 rule
    p_1sigma = 2 * stats.norm.cdf(1) - 1
    p_2sigma = 2 * stats.norm.cdf(2) - 1
    p_3sigma = 2 * stats.norm.cdf(3) - 1
    print(f"\nEmpirical rule (68-95-99.7):")
    print(f"  P(|Z| <= 1) = {p_1sigma:.4f} (theoretical 0.6827)")
    print(f"  P(|Z| <= 2) = {p_2sigma:.4f} (theoretical 0.9545)")
    print(f"  P(|Z| <= 3) = {p_3sigma:.4f} (theoretical 0.9973)\n")


def verify_binomial_to_normal_approximation():
    """De Moivre-Laplace: Bin(n, p) -> N(np, np(1-p)) with Yates correction."""
    print("=== Block 2: Binomial-to-Normal Approximation (De Moivre-Laplace) ===")
    # Standardized exam: n=200 questions, p=0.25, target X >= 60
    n, p = 200, 0.25
    target_k = 60
    mu = n * p
    sigma = np.sqrt(n * p * (1 - p))

    # Exact Binomial
    p_exact = 1 - stats.binom.cdf(target_k - 1, n, p)

    # Normal approximation with Yates continuity correction
    z_yates = (target_k - 0.5 - mu) / sigma
    p_yates = 1 - stats.norm.cdf(z_yates)

    # Normal approximation without Yates correction
    z_no_yates = (target_k - mu) / sigma
    p_no_yates = 1 - stats.norm.cdf(z_no_yates)

    print(f"Bin(n={n}, p={p}): mu={mu:.1f}, sigma={sigma:.4f}")
    print(f"  P(X >= {target_k}) exact Binomial:  {p_exact:.6f}")
    print(f"  P(X >= {target_k}) with Yates:     {p_yates:.6f} (Z={z_yates:.4f})")
    print(f"  P(X >= {target_k}) without Yates:  {p_no_yates:.6f} (Z={z_no_yates:.4f})")
    print(f"  Error with Yates:    {abs(p_yates - p_exact):.6f}")
    print(f"  Error without Yates: {abs(p_no_yates - p_exact):.6f}")

    # Convergence with increasing n
    print(f"\nConvergence analysis for p=0.5 (symmetric case):")
    print(f"  {'n':>6} | {'P(25 <= X <= 75) exact':>22} | {'Normal approx':>15} | {'Error':>10}")
    print(f"  {'-' * 6}-+-{'-' * 22}-+-{'-' * 15}-+-{'-' * 10}")
    for n_test in [10, 50, 200, 1000, 5000]:
        mu_n = n_test * 0.5
        sigma_n = np.sqrt(n_test * 0.25)
        exact = stats.binom.cdf(75, n_test, 0.5) - stats.binom.cdf(24, n_test, 0.5)
        approx = stats.norm.cdf((75.5 - mu_n) / sigma_n) - stats.norm.cdf((24.5 - mu_n) / sigma_n)
        print(f"  {n_test:>6} | {exact:>22.6f} | {approx:>15.6f} | {abs(exact - approx):>10.6f}\n")


def verify_poisson_to_normal_and_clt():
    """Poisson approximation by Normal and Central Limit Theorem for sums."""
    print("=== Block 3: Poisson-to-Normal Approximation & Central Limit Theorem ===")
    # Insurance: lambda=100 daily claims
    lam = 100

    # Poisson -> Normal approximation
    p_exact = stats.poisson.cdf(115, mu=lam) - stats.poisson.cdf(84, mu=lam)
    p_normal = stats.norm.cdf((115.5 - lam) / np.sqrt(lam)) - stats.norm.cdf((84.5 - lam) / np.sqrt(lam))
    print(f"Pois({lam}) -> N({lam}, {lam}):")
    print(f"  P(85 <= X <= 115) exact:   {p_exact:.6f}")
    print(f"  Normal approx (Yates):     {p_normal:.6f}")
    print(f"  Error:                     {abs(p_exact - p_normal):.6f}")

    # CLT for sum of n=100 Poisson(2) random variables
    n_clt, lam_clt = 100, 2
    s_mean = n_clt * lam_clt
    s_var = n_clt * lam_clt
    s_std = np.sqrt(s_var)
    target = 220
    p_exact_clt = stats.poisson.cdf(target, mu=s_mean)
    p_normal_clt = stats.norm.cdf((target + 0.5 - s_mean) / s_std)
    print(f"\nSum of {n_clt} i.i.d. Pois({lam_clt}) -> S_{n_clt} ~ Pois({s_mean}):")
    print(f"  P(S_{n_clt} <= {target}) exact Poisson:  {p_exact_clt:.6f}")
    print(f"  Normal approx (Yates):                  {p_normal_clt:.6f}")
    print(f"  Error:                                  {abs(p_exact_clt - p_normal_clt):.6f}")

    # CLT for sum of n=50 i.i.d. Exp(1) random variables
    n_exp = 50
    s_mean_exp = n_exp * 1.0
    s_std_exp = np.sqrt(n_exp * 1.0)
    lower, upper = 45, 55
    z_low = (lower - s_mean_exp) / s_std_exp
    z_high = (upper - s_mean_exp) / s_std_exp
    p_normal_exp = stats.norm.cdf(z_high) - stats.norm.cdf(z_low)
    p_exact_exp = stats.gamma.cdf(upper, a=n_exp) - stats.gamma.cdf(lower, a=n_exp)
    print(f"\nSum of {n_exp} i.i.d. Exp(1) ~ Gamma({n_exp}, 1):")
    print(f"  P({lower} <= S_{n_exp} <= {upper}) exact Gamma:   {p_exact_exp:.6f}")
    print(f"  Normal approx:                                   {p_normal_exp:.6f}")
    print(f"  Error:                                           {abs(p_exact_exp - p_normal_exp):.6f}")

    # Monte Carlo simulation: empirical CLT verification
    np.random.seed(42)
    sim_n = 250_000
    samples = np.sum(np.random.exponential(1.0, size=(sim_n, n_exp)), axis=1)
    emp_mean = np.mean(samples)
    emp_std = np.std(samples, ddof=1)
    print(f"\nMonte Carlo verification (N={sim_n:,} sums of {n_exp} Exp(1)):")
    print(f"  Empirical mean: {emp_mean:.4f} (theoretical: {s_mean_exp})")
    print(f"  Empirical std:  {emp_std:.4f} (theoretical: {s_std_exp:.4f})")
    p_mc = np.mean((samples >= lower) & (samples <= upper))
    print(f"  P({lower} <= S <= {upper}) empirical: {p_mc:.6f}")


if __name__ == "__main__":
    verify_normal_pdf_and_zscore()
    verify_binomial_to_normal_approximation()
    verify_poisson_to_normal_and_clt()
