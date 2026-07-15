"""
Computational Lab: Section 06.03 - Maximum Likelihood Estimation (MLE) and Score
====================================================================
Verifies the score function properties (zero mean, information identity) for
the Exponential distribution, confirms the asymptotic normality of the MLE
for the Poisson rate via Monte Carlo, and validates the delta method for the
asymptotic variance of a transformed MLE (Rayleigh scale parameter).

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import stats


def verify_score_properties_exponential():
    """Verifies E[U(lambda;X)]=0 and Var[U(lambda;X)]=I(lambda) for the Exponential."""
    print("=== Block 1: Score Function Properties (Exponential) ===")
    lam = 2.0
    n_trials = 500_000
    rng = np.random.default_rng(42)

    x = rng.exponential(scale=1 / lam, size=n_trials)
    score = 1 / lam - x  # U(lambda; X) = 1/lambda - X

    print(f"lambda={lam}")
    print(f"  E[U(lambda;X)] empirical = {np.mean(score):.5f} (theoretical: 0)")
    print(f"  Var[U(lambda;X)] empirical = {np.var(score, ddof=1):.5f} (theoretical I(lambda)=1/lambda^2 = {1/lam**2:.5f})")


def verify_asymptotic_normality_poisson():
    """Verifies the asymptotic normality of the Poisson rate MLE via Monte Carlo."""
    print("\n=== Block 2: Asymptotic Normality of the MLE (Poisson) ===")
    lam_true = 3.5
    n = 100
    n_trials = 200_000
    rng = np.random.default_rng(42)

    samples = rng.poisson(lam_true, size=(n_trials, n))
    lambda_mle = np.mean(samples, axis=1)

    theo_var = lam_true / n  # 1/(n*I(lambda)), I(lambda)=1/lambda for Poisson
    print(f"True lambda={lam_true}, n={n}")
    print(f"  E[lambda_MLE] empirical = {np.mean(lambda_mle):.4f} (theoretical: {lam_true})")
    print(f"  Var[lambda_MLE] empirical = {np.var(lambda_mle, ddof=1):.4f} (theoretical 1/(n*I) = {theo_var:.4f})")

    ks = stats.kstest((lambda_mle - lam_true) / np.sqrt(theo_var), "norm")
    print(f"  KS test of standardized MLE vs N(0,1): D={ks.statistic:.5f}, p={ks.pvalue:.4f}")

    # Approximate 95% CI using a single sample estimate
    lambda_hat = 3.5
    se = np.sqrt(lambda_hat / n)
    ci = (lambda_hat - 1.96 * se, lambda_hat + 1.96 * se)
    print(f"\nApprox. 95% CI for lambda (n={n}, lambda_hat={lambda_hat}): [{ci[0]:.3f}, {ci[1]:.3f}]")


def verify_rayleigh_mle_and_delta_method():
    """Derives the Rayleigh MLE, Fisher information, and validates the delta method via Monte Carlo."""
    print("\n=== Block 3: Rayleigh MLE and the Delta Method ===")
    sigma_true = 4.0
    n = 200
    n_trials = 100_000
    rng = np.random.default_rng(42)

    samples = rng.rayleigh(scale=sigma_true, size=(n_trials, n))
    sigma2_mle = np.mean(samples**2, axis=1) / 2  # sigma^2_MLE = (1/(2n)) * sum(x_i^2)
    sigma_mle = np.sqrt(sigma2_mle)

    fisher_info = 4 / sigma_true**2
    var_sigma2_empirical = np.var(sigma2_mle, ddof=1)
    var_sigma_empirical = np.var(sigma_mle, ddof=1)

    # Asymptotic variance of sigma^2_MLE from Fisher information on sigma, converted via delta method
    # Var(sigma) ~ 1/(n*I(sigma)) = sigma^2/(4n); propagate to sigma^2 using g(sigma)=sigma^2, g'=2*sigma
    var_sigma_theoretical = sigma_true**2 / (4 * n)
    var_sigma2_theoretical = (2 * sigma_true) ** 2 * var_sigma_theoretical

    print(f"True sigma={sigma_true}, n={n}, I(sigma)=4/sigma^2={fisher_info:.4f}")
    print(f"  Var(sigma_MLE) empirical = {var_sigma_empirical:.5f} (theoretical sigma^2/(4n) = {var_sigma_theoretical:.5f})")
    print(f"  Var(sigma^2_MLE) empirical = {var_sigma2_empirical:.5f} (delta-method theoretical = {var_sigma2_theoretical:.5f})")

    # Delta method verification: Var(sigma) from Var(sigma^2) via g(x)=sqrt(x)
    delta_var_sigma = (1 / (2 * sigma_true)) ** 2 * var_sigma2_empirical
    print(f"  Delta-method estimate of Var(sigma) from empirical Var(sigma^2): {delta_var_sigma:.5f}")


if __name__ == "__main__":
    verify_score_properties_exponential()
    verify_asymptotic_normality_poisson()
    verify_rayleigh_mle_and_delta_method()
