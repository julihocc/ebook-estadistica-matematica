"""
02.06_random_sampling.py
Empirical Validation of Random Sampling, Law of Large Numbers & Central Limit Theorem
Author: Juliho Castillo Colmenares <julih@tec.mx>
"""

import numpy as np

# --- BLOCK 1: SAMPLING WITH VS WITHOUT REPLACEMENT (FPC FACTOR) ---
def compare_sampling_schemes(N_pop=500, n_sample=50, n_trials=20_000, seed=42):
    """Compares sample mean variance with and without replacement."""
    np.random.seed(seed)
    population = np.random.normal(loc=100.0, scale=20.0, size=N_pop)
    true_mu, true_sigma = np.mean(population), np.std(population, ddof=0)
    
    means_with = [np.mean(np.random.choice(population, size=n_sample, replace=True)) for _ in range(n_trials)]
    means_without = [np.mean(np.random.choice(population, size=n_sample, replace=False)) for _ in range(n_trials)]
    
    var_with, var_without = np.var(means_with), np.var(means_without)
    fpc_theoretical = (N_pop - n_sample) / (N_pop - 1)
    fpc_empirical = var_without / var_with
    
    print("--- 1. Sampling With vs Without Replacement (Finite Population) ---")
    print(f"Population N = {N_pop}, Sample n = {n_sample}, True Sigma = {true_sigma:.4f}")
    print(f"Empirical Var(X_bar) With Replacement    : {var_with:.4f}")
    print(f"Empirical Var(X_bar) Without Replacement : {var_without:.4f}")
    print(f"Theoretical FPC Factor [(N-n)/(N-1)]     : {fpc_theoretical:.4f}")
    print(f"Empirical Variance Ratio (Without / With): {fpc_empirical:.4f}\n")
    return var_with, var_without, fpc_empirical

# --- BLOCK 2: LAW OF LARGE NUMBERS (LLN) CONVERGENCE ---
def verify_law_of_large_numbers(sample_sizes=[10, 50, 200, 1000, 5000], seed=42):
    """Demonstrates convergence in probability of sample mean to true mu."""
    np.random.seed(seed)
    true_mu, true_sigma = 3.5, np.sqrt(35.0 / 12.0)  # Fair 6-sided die
    
    print("--- 2. Law of Large Numbers (LLN) Convergence ---")
    print("Sample Size (n) | Empirical Mean | Absolute Error | Chebyshev Upper Bound (e=0.1)")
    print("-" * 75)
    for n in sample_sizes:
        sample = np.random.choice([1, 2, 3, 4, 5, 6], size=n, replace=True)
        sample_mean = np.mean(sample)
        abs_error = np.abs(sample_mean - true_mu)
        chebyshev_bound = min(1.0, (true_sigma**2) / (n * (0.1**2)))
        print(f"{n:15d} | {sample_mean:14.4f} | {abs_error:14.4f} | {chebyshev_bound:28.4f}")
    print()

# --- BLOCK 3: CENTRAL LIMIT THEOREM (CLT) STANDARDIZATION ---
def verify_central_limit_theorem(n_sample=36, n_simulations=50_000, seed=42):
    """Verifies convergence of standardized sample means to N(0,1)."""
    np.random.seed(seed)
    pop_mu, pop_sigma = 2.0, 2.0  # Exponential distribution (rate = 0.5)
    
    # Generate n_simulations samples of size n_sample
    samples = np.random.exponential(scale=pop_mu, size=(n_simulations, n_sample))
    sample_means = np.mean(samples, axis=1)
    
    # Standardize: Z = (X_bar - mu) / (sigma / sqrt(n))
    standard_error = pop_sigma / np.sqrt(n_sample)
    z_scores = (sample_means - pop_mu) / standard_error
    
    # Check empirical probabilities within symmetric standard deviation bands
    prob_1sd = np.mean(np.abs(z_scores) <= 1.0)
    prob_2sd = np.mean(np.abs(z_scores) <= 2.0)
    prob_196 = np.mean(np.abs(z_scores) <= 1.96)
    
    print("--- 3. Central Limit Theorem (CLT) Standardization (Exponential Pop) ---")
    print(f"Population Distribution: Exponential(mu={pop_mu}, sigma={pop_sigma}), Sample Size n = {n_sample}")
    print(f"Empirical P(|Z| <= 1.00) : {prob_1sd:.4f} (Theoretical N(0,1): 0.6827)")
    print(f"Empirical P(|Z| <= 1.96) : {prob_196:.4f} (Theoretical N(0,1): 0.9500)")
    print(f"Empirical P(|Z| <= 2.00) : {prob_2sd:.4f} (Theoretical N(0,1): 0.9545)")
    return prob_196

if __name__ == "__main__":
    compare_sampling_schemes()
    verify_law_of_large_numbers()
    verify_central_limit_theorem()
