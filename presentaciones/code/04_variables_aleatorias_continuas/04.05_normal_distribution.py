"""
Computational Lab: Section 04.05 - Normal Distribution and Z-Score
====================================================================
Validates the Normal PDF normalization, demonstrates Z-score standardization
and the 68-95-99.7 empirical rule, computes interval probabilities and
quantiles, and applies the Central Limit Theorem and the Binomial-Normal
approximation with Yates continuity correction.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import integrate, stats


def verify_normal_pdf_and_standardization():
    """Validates Normal PDF normalization and Z-score standardization."""
    print("=== Block 1: Normal PDF & Standardization ===")
    # Normal(100, 15^2)
    mu, sigma = 100.0, 15.0

    # Verify PDF normalization
    result, error = integrate.quad(lambda x: stats.norm.pdf(x, loc=mu, scale=sigma), mu - 6 * sigma, mu + 6 * sigma)
    print(f"Normal(mu={mu}, sigma={sigma}) PDF integral: {result:.8f} (should be 1.0)")

    # Standardization: Z = (X - mu)/sigma ~ N(0, 1)
    print("\nZ-score standardization (Normal(100, 15)):")
    print(f"  {'x':>6} | {'Z = (x-mu)/sigma':>15} | {'F(x) actual':>12} | {'Phi(Z)':>10} | {'|diff|':>10}")
    print(f"  {'-'*6}-+-{'-'*15}-+-{'-'*12}-+-{'-'*10}-+-{'-'*10}")
    for x in [70, 85, 100, 115, 130, 145]:
        z = (x - mu) / sigma
        f_actual = stats.norm.cdf(x, loc=mu, scale=sigma)
        f_z = stats.norm.cdf(z)
        print(f"  {x:>6.0f} | {z:>15.3f} | {f_actual:>12.6f} | {f_z:>10.6f} | {abs(f_actual - f_z):>10.2e}")

    # Empirical rule 68-95-99.7
    print("\nEmpirical rule 68-95-99.7:")
    for k in [1, 2, 3]:
        p = 2 * stats.norm.cdf(k) - 1
        print(f"  P(|X-mu| <= {k}*sigma) = {p:.6f} ({p*100:.2f}%)")


def verify_z_score_and_interval_probabilities():
    """Computes interval probabilities, quantiles, and performs a Z-test."""
    print("\n=== Block 2: Z-Score & Interval Probabilities ===")
    # Heights N(170, 100)
    mu, sigma = 170.0, 10.0
    print(f"Heights ~ N({mu}, {sigma**2}) (sigma={sigma}):")
    print(f"  P(X > 185) = P(Z > 1.5) = {1 - stats.norm.cdf(1.5):.4f}")
    print(f"  P(160 <= X <= 180) = P(-1 <= Z <= 1) = {2*stats.norm.cdf(1) - 1:.4f}")
    print(f"  P(X < 155) = P(Z < -1.5) = {stats.norm.cdf(-1.5):.4f}")

    # Quantiles
    print(f"\nQuantiles for standard Normal:")
    for p in [0.025, 0.05, 0.10, 0.50, 0.90, 0.95, 0.975]:
        q = stats.norm.ppf(p)
        print(f"  q_{p}: {q:+.4f} (CDF at q = {stats.norm.cdf(q):.4f})")

    # One-sample Z-test
    print("\nOne-sample Z-test (H0: mu=100, n=25, sigma=10, x_bar=103):")
    n_test = 25
    sigma_test = 10.0
    x_bar = 103.0
    mu_0 = 100.0
    z_stat = (x_bar - mu_0) / (sigma_test / np.sqrt(n_test))
    p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
    print(f"  Z = (103 - 100) / (10/sqrt(25)) = {z_stat:.4f}")
    print(f"  p-value (two-sided) = {p_value:.4f}")
    print(f"  Decision (alpha=0.05): {'Reject H0' if p_value < 0.05 else 'Fail to reject H0'}")


def verify_clt_and_normal_approximation():
    """Verifies CLT via Monte Carlo and Binomial-Normal approximation."""
    print("\n=== Block 3: CLT & Normal Approximation ===")
    # CLT: Sum of uniforms -> Normal
    np.random.seed(42)
    n_samples = 250_000
    n_sum = 30
    uniforms_sum = np.sum(np.random.uniform(0, 1, (n_samples, n_sum)), axis=1)
    emp_mean = np.mean(uniforms_sum)
    emp_var = np.var(uniforms_sum, ddof=1)
    theo_mean = n_sum * 0.5
    theo_var = n_sum / 12
    print(f"Sum of {n_sum} i.i.d. U(0,1) ~ N({theo_mean}, {theo_var:.4f}):")
    print(f"  Empirical mean: {emp_mean:.4f} (theoretical: {theo_mean:.4f})")
    print(f"  Empirical var: {emp_var:.4f} (theoretical: {theo_var:.4f})")
    normal_cdf = lambda x: stats.norm.cdf(
        x, loc=theo_mean, scale=np.sqrt(theo_var)
    )
    ks_clt = stats.kstest(uniforms_sum, normal_cdf)
    print(f"  KS test vs Normal({theo_mean}, {theo_var:.2f}): D={ks_clt.statistic:.4f}, p={ks_clt.pvalue:.4f}")

    # Binomial-Normal approximation with Yates correction
    print("\nBinomial-Normal approximation (n=400, p=0.25, target X>=120):")
    n_bin, p_bin = 400, 0.25
    mu_bin = n_bin * p_bin
    sigma_bin = np.sqrt(n_bin * p_bin * (1 - p_bin))
    print(f"  Bin({n_bin}, {p_bin}) approximated by N({mu_bin}, {sigma_bin**2:.2f})")
    # Exact
    p_exact = 1 - stats.binom.cdf(119, n_bin, p_bin)
    # Normal with Yates
    p_yates = 1 - stats.norm.cdf((119.5 - mu_bin) / sigma_bin)
    # Normal without Yates
    p_no_yates = 1 - stats.norm.cdf((120 - mu_bin) / sigma_bin)
    print(f"  Exact Binomial: P(X >= 120) = {p_exact:.4f}")
    print(f"  Normal with Yates: P(Y >= 119.5) = {p_yates:.4f}")
    print(f"  Normal without Yates: P(Y >= 120) = {p_no_yates:.4f}")
    print(f"  Error with Yates: {abs(p_exact - p_yates):.4f}")
    print(f"  Error without Yates: {abs(p_exact - p_no_yates):.4f}")

    # Required sample size for SE < 0.01
    target_se = 0.01
    required_n = p_bin * (1 - p_bin) / target_se**2
    print(f"\n  Required n for SE(p_hat) < {target_se}: n > {required_n:.0f}")


if __name__ == "__main__":
    verify_normal_pdf_and_standardization()
    verify_z_score_and_interval_probabilities()
    verify_clt_and_normal_approximation()
