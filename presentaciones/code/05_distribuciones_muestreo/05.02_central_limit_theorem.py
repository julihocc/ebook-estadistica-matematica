"""
Computational Lab: Section 05.02 - Central Limit Theorem: Asymptotic Convergence
====================================================================
Verifies CLT convergence from a strongly skewed (exponential) population via
Kolmogorov-Smirnov tests across sample sizes, empirically confirms the
Berry-Esseen O(1/sqrt(n)) rate of convergence, and applies the CLT to sums
and proportions (insurance claims, sample proportions).

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import stats


def verify_clt_convergence_from_skewed_population():
    """Verifies CLT convergence for Xbar starting from a skewed Exponential population."""
    print("=== Block 1: CLT Convergence from a Skewed Population ===")
    lam = 0.25  # rate, mean = 1/lambda = 4
    mu, sigma = 1 / lam, 1 / lam
    n_trials = 100_000
    rng = np.random.default_rng(42)

    print(f"Population: Exp(lambda={lam}), mu={mu}, sigma={sigma} (skewness=2, strongly asymmetric)")
    print(f"  {'n':>5} | {'KS statistic D':>14} | {'KS p-value':>10}")
    print(f"  {'-'*5}-+-{'-'*14}-+-{'-'*10}")
    for n in [5, 30, 100]:
        samples = rng.exponential(scale=1 / lam, size=(n_trials, n))
        xbars = np.mean(samples, axis=1)
        z_scores = (xbars - mu) / (sigma / np.sqrt(n))
        ks = stats.kstest(z_scores, "norm")
        print(f"  {n:>5} | {ks.statistic:>14.5f} | {ks.pvalue:>10.4f}")

    print("\nAs n grows, the KS statistic D shrinks toward 0, confirming convergence to N(0,1).")


def verify_berry_esseen_rate():
    """Empirically estimates the max CDF gap vs Normal and compares its decay rate to 1/sqrt(n)."""
    print("\n=== Block 2: Berry-Esseen Rate of Convergence ===")
    lam = 0.25
    mu, sigma = 1 / lam, 1 / lam
    n_trials = 200_000
    rng = np.random.default_rng(42)

    grid = np.linspace(-4, 4, 400)
    max_gaps = {}
    for n in [10, 40, 160]:
        samples = rng.exponential(scale=1 / lam, size=(n_trials, n))
        xbars = np.mean(samples, axis=1)
        z_scores = (xbars - mu) / (sigma / np.sqrt(n))
        empirical_cdf = np.array([np.mean(z_scores <= z) for z in grid])
        normal_cdf = stats.norm.cdf(grid)
        max_gap = np.max(np.abs(empirical_cdf - normal_cdf))
        max_gaps[n] = max_gap
        print(f"  n={n:>4}: max|F_Zn(z) - Phi(z)| = {max_gap:.5f}")

    print("\nRatio check against the O(1/sqrt(n)) Berry-Esseen rate:")
    ns = list(max_gaps.keys())
    for i in range(1, len(ns)):
        n_prev, n_curr = ns[i - 1], ns[i]
        observed_ratio = max_gaps[n_curr] / max_gaps[n_prev]
        theoretical_ratio = np.sqrt(n_prev / n_curr)
        print(f"  n={n_prev}->{n_curr}: observed ratio={observed_ratio:.4f}, theoretical sqrt(n1/n2)={theoretical_ratio:.4f}")


def verify_clt_for_sums_and_proportions():
    """Applies the CLT to a sum of insurance claims and to a Bernoulli sample proportion."""
    print("\n=== Block 3: CLT for Sums and Proportions ===")
    # Insurance claims: sum of n iid claims
    n_claims, mu_claim, sigma_claim = 100, 800.0, 300.0
    threshold = 85_000.0
    mean_total = n_claims * mu_claim
    sd_total = np.sqrt(n_claims) * sigma_claim
    z_claims = (threshold - mean_total) / sd_total
    p_claims = 1 - stats.norm.cdf(z_claims)
    print(f"Insurance claims: n={n_claims}, mu={mu_claim}, sigma={sigma_claim}")
    print(f"  E(T)={mean_total:.1f}, SD(T)={sd_total:.1f}, Z={z_claims:.4f}")
    print(f"  P(T > {threshold:.0f}) approx = {p_claims:.4f}")

    # Sample proportion: Bernoulli(p) mean is itself a CLT application
    n_survey, p_true = 200, 0.3
    sd_phat = np.sqrt(p_true * (1 - p_true) / n_survey)
    z_phat = (0.35 - p_true) / sd_phat
    p_phat = 1 - stats.norm.cdf(z_phat)
    print(f"\nSample proportion: n={n_survey}, p={p_true}")
    print(f"  SD(phat)={sd_phat:.4f}, Z={z_phat:.4f}")
    print(f"  P(phat > 0.35) approx = {p_phat:.4f}")

    # Monte Carlo cross-check of the proportion result
    rng = np.random.default_rng(42)
    n_trials = 200_000
    bernoulli_samples = rng.binomial(1, p_true, size=(n_trials, n_survey))
    phats = np.mean(bernoulli_samples, axis=1)
    empirical_p = np.mean(phats > 0.35)
    print(f"  Monte Carlo empirical P(phat > 0.35) = {empirical_p:.4f}")


if __name__ == "__main__":
    verify_clt_convergence_from_skewed_population()
    verify_berry_esseen_rate()
    verify_clt_for_sums_and_proportions()
