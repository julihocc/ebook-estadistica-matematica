"""
Section 03.02: Cumulative Distribution Functions (Discrete CDF)
Computational validation of step accumulation, jump inversion,
interval probabilities, quantiles, and ECDF convergence.
"""

import numpy as np

# --- 1. Step CDF Construction from PMF ---
def compute_step_cdf(support_X, pmf_X):
    # Ensure support and PMF are sorted ascending by support values
    sort_idx = np.argsort(support_X)
    s_sorted, p_sorted = support_X[sort_idx], pmf_X[sort_idx]
    
    # Cumulative sum yields step heights F(x_k)
    cdf_values = np.cumsum(p_sorted)
    
    print("=== 1. Step CDF Construction ===")
    for x_val, f_val in zip(s_sorted, cdf_values):
        print(f"  F({x_val}) = P(X <= {x_val}) = {f_val:.4f}")
    return s_sorted, cdf_values

# --- 2. PMF Reconstruction via CDF Jumps ---
def extract_pmf_from_cdf(support_sorted, cdf_values):
    # First jump is F(x_1) - 0; subsequent jumps are F(x_k) - F(x_{k-1})
    pmf_reconstructed = np.diff(cdf_values, prepend=0.0)
    
    print("\n=== 2. PMF Jump Reconstruction ===")
    for x_val, p_val in zip(support_sorted, pmf_reconstructed):
        print(f"  f({x_val}) = Delta F({x_val}) = {p_val:.4f}")
    
    # Check normalization exactness
    error_norm = abs(np.sum(pmf_reconstructed) - 1.0)
    print(f"Total PMF Sum Error: {error_norm:.6e}")
    return pmf_reconstructed

# --- 3. Interval Probability & Quantile Queries ---
def evaluate_interval_and_quantiles(support_sorted, cdf_values):
    # Interval probability P(a < X <= b) = F(b) - F(a)
    # Example: P(1 < X <= 4) on fair die (support 1..6)
    idx_4 = np.searchsorted(support_sorted, 4)
    idx_1 = np.searchsorted(support_sorted, 1)
    prob_interval = cdf_values[idx_4] - cdf_values[idx_1]
    
    # Discrete quantiles: q_alpha = inf { x : F(x) >= alpha }
    q_50_idx = np.argmax(cdf_values >= 0.50)
    q_85_idx = np.argmax(cdf_values >= 0.85)
    
    print("\n=== 3. Interval & Quantiles ===")
    print(f"  P(1 < X <= 4) = F(4) - F(1) = {prob_interval:.4f}")
    print(f"  Median (q_0.50): {support_sorted[q_50_idx]}")
    print(f"  85th Percentile (q_0.85): {support_sorted[q_85_idx]}")

# --- 4. Empirical ECDF Monte Carlo Convergence ---
def simulate_empirical_ecdf(num_trials=100000):
    np.random.seed(42)
    # Simulate sum of two fair 6-sided dice: support in {2, ..., 12}
    dice_sums = np.random.randint(1, 7, size=num_trials) + \
                np.random.randint(1, 7, size=num_trials)
    
    support_theoretical = np.arange(2, 13)
    # Theoretical triangle PMF and step CDF
    pmf_theory = np.array([6 - abs(s - 7) for s in support_theoretical]) / 36.0
    cdf_theory = np.cumsum(pmf_theory)
    
    # Compute Empirical CDF (ECDF) F_n(x) = (1/n) sum_{i=1}^n I(X_i <= x)
    ecdf_values = np.array([np.mean(dice_sums <= x) for x in support_theoretical])
    max_abs_diff = np.max(np.abs(ecdf_values - cdf_theory))
    
    print("\n=== 4. Empirical ECDF Convergence ===")
    print(f"  Trials simulated: {num_trials:,}")
    print(f"  Supremum ECDF Error (sup |F_n(x) - F(x)|): {max_abs_diff:.6f}")
    assert max_abs_diff < 0.005, "ECDF failed to converge uniformly!"

if __name__ == "__main__":
    # Test on a fair 6-sided die
    s_die = np.arange(1, 7)
    p_die = np.full(6, 1.0 / 6.0)
    
    s_sorted, c_vals = compute_step_cdf(s_die, p_die)
    p_reconstructed = extract_pmf_from_cdf(s_sorted, c_vals)
    evaluate_interval_and_quantiles(s_sorted, c_vals)
    simulate_empirical_ecdf(num_trials=100000)
