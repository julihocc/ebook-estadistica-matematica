"""
Section 03.01: Discrete Probability Mass Functions (PMF) and Support
Computational validation of normalization, support transformations,
and empirical Monte Carlo convergence for discrete random variables.
"""

import numpy as np

# --- 1. PMF Normalization & Polynomial Support ---
def verify_polynomial_pmf():
    support_X = np.array([1, 2, 3, 4])
    unnormalized_weights = support_X ** 2
    c_const = 1.0 / np.sum(unnormalized_weights)
    pmf_X = c_const * unnormalized_weights
    
    print("=== 1. Polynomial PMF Verification ===")
    print(f"Support S_X: {support_X}")
    print(f"Normalization Constant c: {c_const:.6f} (Exact: 1/30)")
    print(f"Total Probability Sum: {np.sum(pmf_X):.6f}")
    
    # Conditional probability P(X is even | X >= 2)
    mask_cond = support_X >= 2
    prob_cond = np.sum(pmf_X[mask_cond])
    mask_event = (support_X % 2 == 0) & mask_cond
    prob_event = np.sum(pmf_X[mask_event])
    cond_prob = prob_event / prob_cond
    print(f"P(X is even | X >= 2): {cond_prob:.4f} (Exact: 20/29)\n")

# --- 2. Monte Carlo Simulation of Discrete Dice Sum PMF ---
def simulate_dice_sum_pmf(num_trials=100000):
    np.random.seed(42)
    die1 = np.random.randint(1, 7, size=num_trials)
    die2 = np.random.randint(1, 7, size=num_trials)
    dice_sum = die1 + die2
    
    support_sum = np.arange(2, 13)
    exact_probs = np.array([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) / 36.0
    empirical_probs = np.array([np.mean(dice_sum == k) for k in support_sum])
    
    max_error = np.max(np.abs(empirical_probs - exact_probs))
    print("=== 2. Monte Carlo Dice Sum Validation ===")
    print(f"Trials: {num_trials:,}")
    print(f"Max Empirical vs Exact PMF Error: {max_error:.5f}")
    print(f"Empirical P(Sum=7): {empirical_probs[5]:.4f} (Exact: {6/36:.4f})\n")

# --- 3. Discrete Variable Transformation ---
def verify_transformed_pmf():
    support_X = np.array([-2, -1, 0, 1, 2])
    pmf_X = np.array([0.15, 0.25, 0.20, 0.30, 0.10])
    
    # Transformation Y = |X - 1|
    Y_values = np.abs(support_X - 1)
    support_Y = np.unique(Y_values)
    pmf_Y = np.array([np.sum(pmf_X[Y_values == y]) for y in support_Y])
    
    print("=== 3. Transformation Y = |X - 1| ===")
    print(f"Induced Support S_Y: {support_Y}")
    for y, prob in zip(support_Y, pmf_Y):
        print(f"  P(Y = {y}) = {prob:.2f}")
    print(f"Sum of Induced PMF: {np.sum(pmf_Y):.2f}\n")

if __name__ == "__main__":
    verify_polynomial_pmf()
    simulate_dice_sum_pmf()
    verify_transformed_pmf()
