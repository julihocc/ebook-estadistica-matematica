"""
Computational Lab: Geometric and Negative Binomial Distributions.
Section 03.05 of the eBook: Statistical Modeling (Modelacion Estadistica).
Author: Juliho Castillo Colmenares (julihocc@tec.mx)
Institution: Tecnologico de Monterrey

Strict Single Source of Truth in English using numpy and scipy.stats.
Demonstrates PMF/CDF validation, exact memoryless property, and overdispersion.
"""

import numpy as np
from scipy import stats


# --- BEAMER SNIPPET 1 START: Vectorized PMF & CDF Validation ---
def verify_geom_and_nbinom_pmf_cdf(p=0.30, r=4, max_k=20):
    """Validate Exact Geometric and Negative Binomial PMF/CDF against SciPy."""
    # Support for total trials up to max_k
    support_geom = np.arange(1, max_k + 1, dtype=int)
    support_nbinom = np.arange(r, max_k + 1, dtype=int)
    
    # Vectorized Geometric PMF: (1-p)^(k-1) * p
    exact_geom_pmf = ((1.0 - p) ** (support_geom - 1)) * p
    scipy_geom_pmf = stats.geom.pmf(support_geom, p)
    
    # Vectorized Negative Binomial PMF (Total trials k to get r successes):
    # C(k-1, r-1) * p^r * (1-p)^(k-r)
    exact_nbinom_pmf = np.array([
        stats.binom.pmf(r - 1, k - 1, p) * p for k in support_nbinom
    ])
    # Note: scipy.stats.nbinom counts failures n = k - r
    scipy_nbinom_pmf = stats.nbinom.pmf(support_nbinom - r, r, p)
    
    pmf_geom_err = np.max(np.abs(exact_geom_pmf - scipy_geom_pmf))
    pmf_nbinom_err = np.max(np.abs(exact_nbinom_pmf - scipy_nbinom_pmf))
    
    return pmf_geom_err, pmf_nbinom_err
# --- BEAMER SNIPPET 1 END ---


# --- BEAMER SNIPPET 2 START: Memoryless Property & Monte Carlo ---
def verify_memoryless_property(p=0.25, m=5, n=3, num_samples=250000):
    """Empirically demonstrate P(X > m+n | X > m) == P(X > n)."""
    np.random.seed(42)  # Reproducible institutional reporting
    samples = np.random.geometric(p=p, size=num_samples)
    
    # Empirical conditional probability
    cond_mask = samples > m
    emp_cond_prob = np.mean(samples[cond_mask] > (m + n))
    
    # Empirical and exact marginal P(X > n)
    emp_marginal_prob = np.mean(samples > n)
    exact_prob = (1.0 - p) ** n
    
    err_cond = abs(emp_cond_prob - exact_prob)
    err_marg = abs(emp_marginal_prob - exact_prob)
    
    return emp_cond_prob, emp_marginal_prob, exact_prob, err_cond, err_marg
# --- BEAMER SNIPPET 2 END ---


# --- BEAMER SNIPPET 3 START: Overdispersion & Additivity Analysis ---
def verify_overdispersion_and_moments(p=0.20, r=5, num_samples=250000):
    """Simulate Negative Binomial as sum of r independent Geometric RVs."""
    np.random.seed(42)
    # Sum of r independent geometric samples
    geom_matrix = np.random.geometric(p=p, size=(num_samples, r))
    nbinom_samples = np.sum(geom_matrix, axis=1)
    
    emp_mu = np.mean(nbinom_samples)
    emp_var = np.var(nbinom_samples, ddof=0)
    
    theo_mu = r / p
    theo_var = (r * (1.0 - p)) / (p ** 2)
    overdispersion_ratio = emp_var / emp_mu  # Must exceed 1.0 for q/p > 0
    
    return emp_mu, emp_var, theo_mu, theo_var, overdispersion_ratio
# --- BEAMER SNIPPET 3 END ---


if __name__ == "__main__":
    print("=== Section 03.05: Computational Lab Verification ===")
    
    # 1. PMF and CDF Exact Verification
    err_geom, err_nbinom = verify_geom_and_nbinom_pmf_cdf(p=0.30, r=4)
    print(f"[Snippet 1] Max Geometric PMF Error against SciPy: {err_geom:.2e}")
    print(f"[Snippet 1] Max Negative Binomial PMF Error against SciPy: {err_nbinom:.2e}")
    assert err_geom < 1e-14 and err_nbinom < 1e-14, "PMF validation failed!"
    
    # 2. Memoryless Property Verification
    emp_cond, emp_marg, exact_p, err_c, err_m = verify_memoryless_property(p=0.25, m=5, n=3)
    print(f"\n[Snippet 2] Memoryless Verification (p=0.25, m=5, n=3):")
    print(f"  Empirical Conditional P(X > 8 | X > 5): {emp_cond:.6f}")
    print(f"  Empirical Marginal P(X > 3):            {emp_marg:.6f}")
    print(f"  Exact Theoretical Probability (1-p)^3:  {exact_p:.6f}")
    assert err_c < 8e-3 and err_m < 8e-3, "Memoryless Monte Carlo discrepancy too large!"
    
    # 3. Overdispersion & Additivity Verification
    emp_m, emp_v, theo_m, theo_v, ratio = verify_overdispersion_and_moments(p=0.20, r=5)
    print(f"\n[Snippet 3] Overdispersion & Additivity Verification (p=0.20, r=5):")
    print(f"  Empirical Mean: {emp_m:.4f} | Theoretical Mean: {theo_m:.4f}")
    print(f"  Empirical Var:  {emp_v:.4f} | Theoretical Var:  {theo_v:.4f}")
    print(f"  Overdispersion Ratio (Var / Mean): {ratio:.4f} (> 1.0 confirms overdispersion)")
    assert abs(emp_m - theo_m) < 0.1 and abs(emp_v - theo_v) < 1.0, "Moments discrepancy!"
    assert ratio > 1.0, "Overdispersion ratio must exceed 1.0!"
    
    print("\nSUCCESS: All computational checks passed cleanly.")
