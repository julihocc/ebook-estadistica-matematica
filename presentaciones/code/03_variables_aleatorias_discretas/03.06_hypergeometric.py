"""
Computational Lab: Section 03.06 - Hypergeometric Distribution
==============================================================
Validates exact combinatorial PMF, Finite Population Correction Factor (FPCF),
negative covariance without replacement, and Fisher's Exact Test.

Author: Juliho Castillo Colmenares
Institution: Tecnológico de Monterrey
"""

import numpy as np
from scipy import stats


def verify_hypergeometric_pmf_and_support():
    """Validates combinatorial PMF, support bounds, and Vandermonde sum."""
    print("=== Block 1: Hypergeometric PMF & Support Validation ===")
    # Lot setup: N=30 total, K=6 defectives, n=5 sample size
    pop_N, succ_K, samp_n = 30, 6, 5
    
    # Exact support: max(0, n - (N - K)) <= k <= min(n, K)
    k_min, k_max = max(0, samp_n - (pop_N - succ_K)), min(samp_n, succ_K)
    support = np.arange(k_min, k_max + 1)
    
    # Calculate PMF vector via SciPy: hypergeom(M=pop_N, n=succ_K, N=samp_n)
    pmf_vec = stats.hypergeom(M=pop_N, n=succ_K, N=samp_n).pmf(support)
    total_prob = np.sum(pmf_vec)  # Vandermonde identity check
    prob_acc = pmf_vec[0] + pmf_vec[1]  # P(X <= 1 defective)
    
    print(f"Lot Setup: N={pop_N}, K={succ_K}, n={samp_n} | Support: [{k_min}, {k_max}]")
    print(f"Vandermonde Total Sum Check: {total_prob:.12f}")
    print(f"P(X = 0): {pmf_vec[0]:.6f} | P(X = 1): {pmf_vec[1]:.6f}")
    print(f"Lot Acceptance Probability P(X <= 1): {prob_acc:.6f}\n")


def verify_fpc_and_correlated_sampling():
    """Demonstrates FPCF reduction and negative covariance via Monte Carlo."""
    print("=== Block 2: FPCF & Negative Covariance Analysis ===")
    pop_N, succ_K, samp_n = 50, 10, 20
    prop_p = succ_K / pop_N  # p = 0.20
    
    # Theoretical moments & FPCF
    var_bin = samp_n * prop_p * (1.0 - prop_p)
    fpcf = (pop_N - samp_n) / (pop_N - 1.0)
    var_hyper = var_bin * fpcf
    cov_theo = - (succ_K * (pop_N - succ_K)) / (pop_N**2 * (pop_N - 1.0))
    
    # Monte Carlo simulation (250,000 trials without replacement)
    np.random.seed(42)
    pop_arr = np.array([1] * succ_K + [0] * (pop_N - succ_K))
    sim_mat = np.array([np.random.choice(pop_arr, samp_n, False) for _ in range(250_000)])
    
    emp_var = np.var(np.sum(sim_mat, axis=1), ddof=1)
    emp_cov = np.cov(sim_mat[:, 0], sim_mat[:, 1])[0, 1]
    
    print(f"Binomial Var: {var_bin:.4f} | Theoretical FPCF: {fpcf:.6f}")
    print(f"Hypergeom Var -> Theo: {var_hyper:.4f} | Empirical: {emp_var:.4f}")
    print(f"Covariance(I_1, I_2) -> Theo: {cov_theo:.6f} | Empirical: {emp_cov:.6f}\n")


def verify_fisher_exact_and_asymptotic():
    """Applies Fisher's exact test and verifies convergence to Binomial."""
    print("=== Block 3: Fisher's Exact Test & Asymptotic Convergence ===")
    # Clinical trial 2x2 table: N=25 total, K=12 active, n=8 thrombosis events
    clin_N, act_K, events_n, obs_X = 25, 12, 8, 1
    p_val = stats.hypergeom(M=clin_N, n=act_K, N=events_n).cdf(obs_X)
    
    print(f"Clinical Trial: N={clin_N}, Active K={act_K}, Events n={events_n}, Obs X={obs_X}")
    print(f"Fisher Exact Test (Lower 1-sided p-value): {p_val:.6f}")
    print(f"Decision (alpha=0.05): {'Reject H0 (Efficacious)' if p_val < 0.05 else 'Fail to Reject'}\n")
    
    # Asymptotic convergence check keeping p=K/N=0.05, n=20 fixed at k=2
    samp_n, fixed_p, k_eval = 20, 0.05, 2
    binom_p = stats.binom.pmf(k_eval, samp_n, fixed_p)
    print(f"Asymptotic Convergence to Binomial P(Y={k_eval})={binom_p:.6f}:")
    for pop_size in [200, 2000, 20000]:
        hyper_p = stats.hypergeom.pmf(k_eval, pop_size, int(pop_size * fixed_p), samp_n)
        print(f"  N={pop_size:5d} -> Hyper P(X=2)={hyper_p:.6f} | Error={abs(hyper_p - binom_p):.6f}")


if __name__ == "__main__":
    verify_hypergeometric_pmf_and_support()
    verify_fpc_and_correlated_sampling()
    verify_fisher_exact_and_asymptotic()
