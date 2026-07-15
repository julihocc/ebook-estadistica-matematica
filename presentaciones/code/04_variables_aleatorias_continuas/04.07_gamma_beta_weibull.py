"""
Computational Lab: Section 04.07 - Gamma, Beta, and Weibull Distributions
====================================================================
Validates the Gamma PDF normalization and its Erlang/Exponential/Chi-squared
special cases, computes Beta distribution moments and its symmetry property
with a Bayesian conjugate-prior update, and analyzes the Weibull hazard
function for reliability engineering across shape parameters.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import integrate, stats


def verify_gamma_distribution_and_erlang():
    """Validates Gamma PDF normalization and its special cases (Erlang, Exponential, Chi-squared)."""
    print("=== Block 1: Gamma Distribution & Erlang ===")
    # Gamma(alpha=3, beta=2), scale parametrization: mean=alpha*beta, var=alpha*beta^2
    alpha, beta = 3.0, 2.0

    # Verify PDF normalization
    result, error = integrate.quad(lambda x: stats.gamma.pdf(x, a=alpha, scale=beta), 0, np.inf)
    print(f"Gamma(alpha={alpha}, beta={beta}) PDF integral: {result:.8f} (should be 1.0)")
    print(f"  Mean: {stats.gamma.mean(a=alpha, scale=beta):.4f} (theoretical alpha*beta = {alpha*beta:.4f})")
    print(f"  Variance: {stats.gamma.var(a=alpha, scale=beta):.4f} (theoretical alpha*beta^2 = {alpha*beta**2:.4f})")

    # Erlang additive property: sum of n i.i.d. Exp(lambda) ~ Gamma(n, 1/lambda)
    print("\nErlang additive property (sum of i.i.d. Exponential variables):")
    lam = 3.0  # calls per minute
    n_calls = 3
    scale_exp = 1.0 / lam
    print(f"  T_i ~ Exp(lambda={lam}) => T = sum of {n_calls} => Gamma({n_calls}, {scale_exp:.4f})")
    p_direct = 1 - stats.gamma.cdf(1.5, a=n_calls, scale=scale_exp)
    print(f"  P(T > 1.5) via Gamma CDF: {p_direct:.6f}")

    # Special case 1: Exponential (alpha=1)
    print("\nSpecial case: Exponential (alpha=1)")
    beta_exp = 4.0
    lambda_equiv = 1.0 / beta_exp
    p_gamma1 = 1 - stats.gamma.cdf(6, a=1, scale=beta_exp)
    p_exp = 1 - stats.expon.cdf(6, scale=1 / lambda_equiv)
    print(f"  Gamma(1, {beta_exp}) vs Exp(lambda={lambda_equiv}): P(X>6) = {p_gamma1:.6f} vs {p_exp:.6f}")

    # Special case 2: Chi-squared (alpha=nu/2, beta=2)
    print("\nSpecial case: Chi-squared (alpha=nu/2, beta=2)")
    for nu in [3, 5]:
        p_gamma_chi = 1 - stats.gamma.cdf(7.815, a=nu / 2, scale=2)
        p_chi2 = 1 - stats.chi2.cdf(7.815, df=nu)
        print(f"  nu={nu}: Gamma(nu/2, 2) vs Chi2(nu): P(X>7.815) = {p_gamma_chi:.6f} vs {p_chi2:.6f}")


def verify_beta_distribution_and_moments():
    """Computes Beta distribution moments, verifies the symmetry property, and a Bayesian update."""
    print("\n=== Block 2: Beta Distribution & Moments ===")
    alpha, beta_param = 3.0, 5.0

    # Verify PDF normalization and moments
    result, error = integrate.quad(lambda x: stats.beta.pdf(x, a=alpha, b=beta_param), 0, 1)
    print(f"Beta(alpha={alpha}, beta={beta_param}) PDF integral: {result:.8f} (should be 1.0)")
    mean_analytic = alpha / (alpha + beta_param)
    var_analytic = (alpha * beta_param) / ((alpha + beta_param) ** 2 * (alpha + beta_param + 1))
    print(f"  Mean: {stats.beta.mean(a=alpha, b=beta_param):.6f} (theoretical: {mean_analytic:.6f})")
    print(f"  Variance: {stats.beta.var(a=alpha, b=beta_param):.6f} (theoretical: {var_analytic:.6f})")

    # Symmetry property: Beta(a,b) at x  ==  1 - Beta(b,a) at (1-x)
    print("\nSymmetry property Beta(a,b) = 1 - Beta(b,a):")
    x_point = 0.3
    a2, b2 = 2.0, 5.0
    lhs = stats.beta.cdf(x_point, a=a2, b=b2)
    rhs = 1 - stats.beta.cdf(1 - x_point, a=b2, b=a2)
    print(f"  P(X<={x_point}) for Beta({a2},{b2}) = {lhs:.6f}")
    print(f"  1 - P(Y<={1-x_point}) for Beta({b2},{a2}) = {rhs:.6f} (should match)")

    # Bayesian conjugate prior update: Beta(2,2) prior, n=20 trials, k=14 successes
    print("\nBayesian conjugate update (prior Beta(2,2), n=20, k=14 successes):")
    prior_a, prior_b = 2.0, 2.0
    n_trials, k_successes = 20, 14
    post_a = prior_a + k_successes
    post_b = prior_b + n_trials - k_successes
    print(f"  Posterior: Beta({post_a:.0f}, {post_b:.0f})")
    print(f"  Posterior mean E(p|data): {stats.beta.mean(a=post_a, b=post_b):.6f}")


def verify_weibull_and_reliability():
    """Analyzes the Weibull hazard function and reliability curves across shape parameters."""
    print("\n=== Block 3: Weibull & Reliability Analysis ===")
    # Weibull(beta=1.5, eta=4): component lifetime in years
    shape, scale = 1.5, 4.0

    # Verify PDF normalization
    result, error = integrate.quad(lambda t: stats.weibull_min.pdf(t, c=shape, scale=scale), 0, np.inf)
    print(f"Weibull(shape={shape}, scale={scale}) PDF integral: {result:.8f} (should be 1.0)")

    reliability_3 = 1 - stats.weibull_min.cdf(3, c=shape, scale=scale)
    print(f"  R(3) = P(T > 3) = {reliability_3:.6f}")

    # Hazard function comparison across shape parameters (same scale eta=10)
    print("\nHazard function h(t) = (shape/scale)*(t/scale)^(shape-1), eta=10:")
    eta = 10.0
    shapes = {"A (beta=1, no aging)": 1.0, "B (beta=2, wear-out)": 2.0}
    print(f"  {'Lot':<24} | {'Mean':>8} | {'h(5)':>8} | {'h(15)':>8}")
    print(f"  {'-'*24}-+-{'-'*8}-+-{'-'*8}-+-{'-'*8}")
    for label, beta_shape in shapes.items():
        mean_life = stats.weibull_min.mean(c=beta_shape, scale=eta)
        h5 = (beta_shape / eta) * (5 / eta) ** (beta_shape - 1)
        h15 = (beta_shape / eta) * (15 / eta) ** (beta_shape - 1)
        print(f"  {label:<24} | {mean_life:>8.4f} | {h5:>8.4f} | {h15:>8.4f}")

    # Reliability at several time points for the wear-out lot
    print("\nReliability curve for Lot B (beta=2, eta=10):")
    for t in [2, 5, 10, 15, 20]:
        r_t = 1 - stats.weibull_min.cdf(t, c=2.0, scale=eta)
        print(f"  R({t}) = {r_t:.6f}")


if __name__ == "__main__":
    verify_gamma_distribution_and_erlang()
    verify_beta_distribution_and_moments()
    verify_weibull_and_reliability()
