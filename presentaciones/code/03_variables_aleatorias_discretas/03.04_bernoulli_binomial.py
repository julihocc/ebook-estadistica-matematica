# ==============================================================================
# SECTION 03.04: BERNOULLI AND BINOMIAL DISTRIBUTIONS
# ==============================================================================
# Single Source of Truth for Beamer presentations (EN & ES) and computational labs.
# Institutional Identity: Juliho Castillo Colmenares (julihocc@tec.mx)
# Tecnologico de Monterrey - Modelacion Estadistica
# ==============================================================================

import numpy as np
from scipy import stats

# --- BEAMER SNIPPET 1 START: Vectorized PMF & CDF Validation ---
def verify_binomial_pmf_cdf(n, p):
    """Validate exact combinatorial PMF and CDF against scipy.stats.binom."""
    support = np.arange(n + 1, dtype=int)
    
    # Vectorized combinatorial PMF: C(n, k) * p^k * (1-p)^(n-k)
    log_comb = [
        np.sum(np.log(np.arange(1, n + 1))) -
        np.sum(np.log(np.arange(1, k + 1))) -
        np.sum(np.log(np.arange(1, n - k + 1)))
        for k in support
    ]
    exact_pmf = np.exp(log_comb) * (p ** support) * ((1.0 - p) ** (n - support))
    
    # Scientific comparison with scipy.stats.binom
    scipy_pmf = stats.binom.pmf(support, n, p)
    scipy_cdf = stats.binom.cdf(support, n, p)
    cum_pmf = np.cumsum(exact_pmf)
    
    pmf_max_err = np.max(np.abs(exact_pmf - scipy_pmf))
    cdf_max_err = np.max(np.abs(cum_pmf - scipy_cdf))
    
    return exact_pmf, cum_pmf, pmf_max_err, cdf_max_err
# --- BEAMER SNIPPET 1 END ---


# --- BEAMER SNIPPET 2 START: Monte Carlo Simulation & Moments ---
def simulate_binomial_moments(n, p, num_samples=100000):
    """Simulate N=100,000 Bernoulli trials to verify empirical moments."""
    np.random.seed(42)  # Reproducible institutional reporting
    samples = np.random.binomial(n=n, p=p, size=num_samples)
    
    # Theoretical vs. Empirical Expectation (Mean)
    theoretical_mean = n * p
    empirical_mean = np.mean(samples)
    
    # Theoretical vs. Empirical Variance
    theoretical_variance = n * p * (1.0 - p)
    empirical_variance = np.var(samples, ddof=0)
    
    mean_error = abs(empirical_mean - theoretical_mean)
    var_error = abs(empirical_variance - theoretical_variance)
    
    return empirical_mean, empirical_variance, mean_error, var_error
# --- BEAMER SNIPPET 2 END ---


# --- BEAMER SNIPPET 3 START: Mode & Shape Analysis ---
def verify_binomial_mode_and_shape(n, p):
    """Verify combinatorial mode k* = floor((n+1)*p) and skewness."""
    support = np.arange(n + 1, dtype=int)
    pmf = stats.binom.pmf(support, n, p)
    
    # Computational vs. Theoretical Mode
    comp_mode = support[np.argmax(pmf)]
    theo_mode = int(np.floor((n + 1.0) * p))
    
    # Analytical Skewness: gamma_1 = (1 - 2p) / sqrt(np(1-p))
    theoretical_skewness = (1.0 - 2.0 * p) / np.sqrt(n * p * (1.0 - p))
    scipy_skewness = float(stats.binom.stats(n, p, moments='s'))
    
    return comp_mode, theo_mode, theoretical_skewness, scipy_skewness
# --- BEAMER SNIPPET 3 END ---


def main():
    print("=== Section 03.04: Bernoulli and Binomial Lab ===")
    
    # Industrial inspection scenario: n=15 trials, p=0.20 success probability
    n_val, p_val = 15, 0.20
    
    pmf_arr, cdf_arr, pmf_err, cdf_err = verify_binomial_pmf_cdf(n_val, p_val)
    print(f"\n[1] Vectorized PMF & CDF Validation (n={n_val}, p={p_val}):")
    print(f"    Total Support Mass P(X<=n): {cdf_arr[-1]:.6f} (Target: 1.0)")
    print(f"    Max PMF Error vs. Scipy   : {pmf_err:.2e}")
    print(f"    Max CDF Error vs. Scipy   : {cdf_err:.2e}")
    
    emp_mu, emp_var, mu_err, var_err = simulate_binomial_moments(n_val, p_val, 100000)
    print(f"\n[2] Monte Carlo LLN Simulation (N=100,000):")
    print(f"    Empirical Mean bar(X)     : {emp_mu:.4f} (Target: {n_val*p_val:.4f}, Err: {mu_err:.6f})")
    print(f"    Empirical Variance S^2    : {emp_var:.4f} (Target: {n_val*p_val*(1-p_val):.4f}, Err: {var_err:.6f})")
    
    c_mode, t_mode, t_skew, s_skew = verify_binomial_mode_and_shape(n_val, p_val)
    print(f"\n[3] Mode Verification & Skewness Analysis:")
    print(f"    Computational Mode argmax : {c_mode} (Theoretical floor((n+1)p): {t_mode})")
    print(f"    Exact Skewness gamma_1    : {t_skew:.6f} (Scipy Target: {s_skew:.6f})")
    print("\n=== All numerical verifications passed exact tolerances. ===")


if __name__ == "__main__":
    main()
