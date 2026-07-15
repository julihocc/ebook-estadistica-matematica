"""
Computational Lab: Section 03.07 - Poisson Distribution
========================================================
Validates the Poisson PMF, equidispersion property (mu = sigma^2 = lambda),
the Law of Rare Events (Binomial -> Poisson limit with Total Variation
Distance), and the additivity/conditional Binomial properties of independent
Poisson random variables.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import stats


def verify_poisson_pmf_and_equidispersion():
    """Validates support, normalization, and mu = sigma^2 = lambda."""
    print("=== Block 1: Poisson PMF & Equidispersion Validation ===")
    # Call center scenario: lambda = 3 calls per minute
    rate_lam = 3.0
    k_vals = np.arange(0, 15)
    pmf = stats.poisson.pmf(k_vals, mu=rate_lam)

    # Check 1: Total probability sums to 1 (Taylor series of exp(lambda))
    total = np.sum(pmf)

    # Check 2: Direct summation of expectation and variance
    mean_th = np.sum(k_vals * pmf)
    var_th = np.sum((k_vals - mean_th) ** 2 * pmf)

    # Check 3: Closed-form equidispersion (mu = sigma^2 = lambda)
    # Tolerance relaxed to 1e-3 to account for tail truncation at k=15
    mu_closed = rate_lam
    var_closed = rate_lam
    equidispersion = np.isclose(var_th, mu_closed, atol=1e-3)

    # Check 4: Tail probability P(X >= 10) for queueing analysis
    tail_p = 1.0 - stats.poisson.cdf(9, mu=rate_lam)

    print(f"Lambda = {rate_lam} (calls/min) | Rate parameter: mu = sigma^2 = lambda")
    print(f"PMF total probability: {total:.12f}")
    print(f"Direct mean: {mean_th:.4f} | Direct var: {var_th:.4f}")
    print(f"Closed-form mu={mu_closed} | Closed-form sigma^2={var_closed}")
    print(f"Equidispersion property verified: {equidispersion}")
    print(f"P(X=0)={pmf[0]:.6f} | P(X=1)={pmf[1]:.6f} | P(X=2)={pmf[2]:.6f}")
    print(f"P(X=3)={pmf[3]:.6f} | P(X>=10)={tail_p:.6f}\n")


def verify_law_of_rare_events():
    """Shows Bin(n, p) converges to Poisson(lambda) as n grows, p -> 0."""
    print("=== Block 2: Law of Rare Events (Binomial -> Poisson Limit) ===")
    # Clinical trial: n=2000 patients, p=0.001 (rare adverse event) -> lambda=2
    lam = 2.0
    target_k = 2
    k_vals = np.arange(0, 21)

    print("Total Variation Distance (TVD) for increasing n (p=lambda/n):")
    for n in [50, 100, 500, 2000, 10000]:
        p = lam / n
        binom_pmf = stats.binom.pmf(k_vals, n, p)
        pois_pmf = stats.poisson.pmf(k_vals, mu=lam)
        tvd = 0.5 * np.sum(np.abs(binom_pmf - pois_pmf))
        binom_at_2 = stats.binom.pmf(target_k, n, p)
        pois_at_2 = stats.poisson.pmf(target_k, mu=lam)
        print(f"  n={n:5d} p={p:.4f} | Binom P(X=2)={binom_at_2:.6f} | "
              f"Pois P(X=2)={pois_at_2:.6f} | TVD={tvd:.6f}")

    # Monte Carlo simulation: empirical mean and variance vs theoretical
    np.random.seed(42)
    sim_n = 250_000
    n_binom, p_binom = 2000, 0.001
    empirical = np.random.binomial(n_binom, p_binom, sim_n)
    print(f"\nMonte Carlo (n={n_binom}, p={p_binom}, N={sim_n:,}):")
    print(f"  Empirical mean: {np.mean(empirical):.4f} (theoretical: {lam})")
    print(f"  Empirical var:  {np.var(empirical, ddof=1):.4f} (theoretical: {lam})\n")


def verify_additivity_and_conditional_binomial():
    """Shows X + Y ~ Pois(lambda1+lambda2) and X | (X+Y=n) ~ Bin(n, p_cond)."""
    print("=== Block 3: Additivity & Conditional Binomial Property ===")
    # Two independent Poisson servers
    sim_n = 250_000
    lam1, lam2 = 3.0, 5.0
    np.random.seed(42)
    X = np.random.poisson(lam1, sim_n)
    Y = np.random.poisson(lam2, sim_n)
    Z = X + Y

    # Additivity check: Z ~ Pois(lam1 + lam2) implies mean = var = lam1 + lam2
    print(f"Independent Poisson servers: lambda1={lam1}, lambda2={lam2}")
    print(f"Z = X + Y (N={sim_n:,} samples):")
    print(f"  Empirical mean: {np.mean(Z):.4f} (theoretical: {lam1 + lam2})")
    print(f"  Empirical var:  {np.var(Z, ddof=1):.4f} (theoretical: {lam1 + lam2})")

    # Conditional Binomial property: P(X = k | X + Y = n) = Bin(n, p_cond)
    fixed_n = 8
    p_cond = lam1 / (lam1 + lam2)
    cond_X = X[X + Y == fixed_n]
    print(f"\nConditional X | (X + Y = {fixed_n}) with p_cond = {p_cond:.4f}:")
    print(f"  {'k':>3} | {'Empirical':>10} | {'Theoretical Binom':>18} | {'|Diff|':>10}")
    print(f"  {'-' * 3}-+-{'-' * 10}-+-{'-' * 18}-+-{'-' * 10}")
    for k in range(fixed_n + 1):
        emp = np.mean(cond_X == k) if len(cond_X) > 0 else 0.0
        theo = stats.binom.pmf(k, fixed_n, p_cond)
        print(f"  {k:>3} | {emp:>10.4f} | {theo:>18.4f} | {abs(emp - theo):>10.4f}")


if __name__ == "__main__":
    verify_poisson_pmf_and_equidispersion()
    verify_law_of_rare_events()
    verify_additivity_and_conditional_binomial()
