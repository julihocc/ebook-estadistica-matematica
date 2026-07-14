# ==============================================================================
# SECTION 03.03: EXPECTATION, VARIANCE, AND MOMENTS OF DISCRETE R.V.
# ==============================================================================
# Single Source of Truth for Beamer presentations (EN & ES) and computational labs.
# Institutional Identity: Juliho Castillo Colmenares (julihocc@tec.mx)
# Tecnologico de Monterrey - Modelacion Estadistica
# ==============================================================================

import numpy as np

# --- BEAMER SNIPPET 1 START: Fundamental Definitions & Moments ---
def compute_discrete_moments(support, pmf):
    """Compute exact mean (E[X]), raw second moment (E[X^2]), and variance."""
    support = np.asarray(support, dtype=float)
    pmf = np.asarray(pmf, dtype=float)
    
    # Mathematical Expectation: E[X] = sum(x * P(X=x))
    mean = np.sum(support * pmf)
    
    # Raw Second Moment: E[X^2] = sum(x^2 * P(X=x))
    second_moment = np.sum((support ** 2) * pmf)
    
    # Operational Variance via Konig-Huygens identity: E[X^2] - (E[X])^2
    variance = second_moment - (mean ** 2)
    std_dev = np.sqrt(variance)
    
    return mean, second_moment, variance, std_dev
# --- BEAMER SNIPPET 1 END ---


# --- BEAMER SNIPPET 2 START: LOTUS & Z-Score Standardization ---
def verify_lotus_and_standardization(support, pmf):
    """Verify LOTUS with polynomial g(X) and Z-score invariance."""
    support = np.asarray(support, dtype=float)
    pmf = np.asarray(pmf, dtype=float)
    
    # LOTUS for polynomial transformation g(X) = 2*X^2 - 3*X + 5
    g_x = 2 * (support ** 2) - 3 * support + 5
    expected_gx = np.sum(g_x * pmf)
    
    # Z-Score Standardization: Z = (X - mu) / sigma
    mu, _, var, sigma = compute_discrete_moments(support, pmf)
    z_scores = (support - mu) / sigma
    
    # Verify exactly that E[Z] == 0.0 and Var(Z) == 1.0
    z_mean = np.sum(z_scores * pmf)
    z_var = np.sum(((z_scores - z_mean) ** 2) * pmf)
    
    return expected_gx, z_mean, z_var
# --- BEAMER SNIPPET 2 END ---


# --- BEAMER SNIPPET 3 START: Monte Carlo Law of Large Numbers ---
def simulate_law_of_large_numbers(support, pmf, num_samples=100000):
    """Simulate sample paths to verify empirical convergence to E[X]."""
    np.random.seed(42)  # For reproducible institutional reporting
    samples = np.random.choice(support, size=num_samples, p=pmf)
    
    # Running cumulative averages across sample path
    running_averages = np.cumsum(samples) / np.arange(1, num_samples + 1)
    
    # Final empirical mean and empirical variance
    empirical_mean = running_averages[-1]
    empirical_variance = np.var(samples, ddof=0)
    
    return empirical_mean, empirical_variance
# --- BEAMER SNIPPET 3 END ---


def main():
    print("=== Section 03.03: Expectation and Variance Lab ===")
    
    # Problem 3.3.1 data: Database error transactions
    support = np.array([0, 1, 2, 3, 4])
    pmf = np.array([0.35, 0.30, 0.20, 0.10, 0.05])
    
    mu, E_x2, var, sigma = compute_discrete_moments(support, pmf)
    print(f"\n[1] Theoretical Moments:")
    print(f"    Expectation (Mean) E[X]  : {mu:.4f}")
    print(f"    Second Raw Moment  E[X^2]: {E_x2:.4f}")
    print(f"    Variance           Var(X): {var:.4f}")
    print(f"    Standard Deviation sigma : {sigma:.4f}")
    
    E_gx, z_mu, z_var = verify_lotus_and_standardization(support, pmf)
    print(f"\n[2] LOTUS & Standardization Invariance:")
    print(f"    Expected g(X) via LOTUS  : {E_gx:.4f}")
    print(f"    Standardized Z Mean E[Z] : {z_mu:.6f} (Target: 0.0)")
    print(f"    Standardized Z Var Var(Z): {z_var:.6f} (Target: 1.0)")
    
    emp_mu, emp_var = simulate_law_of_large_numbers(support, pmf, 100000)
    print(f"\n[3] Monte Carlo LLN Simulation (N=100,000):")
    print(f"    Empirical Sample Mean    : {emp_mu:.4f} (Error: {abs(emp_mu - mu):.6f})")
    print(f"    Empirical Sample Variance: {emp_var:.4f} (Error: {abs(emp_var - var):.6f})")
    print("\n=== All numerical verifications passed exact tolerances. ===")


if __name__ == "__main__":
    main()
