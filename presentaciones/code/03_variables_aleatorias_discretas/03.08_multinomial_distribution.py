"""
Computational Lab: Section 03.08 - Multinomial Distribution
============================================================
Validates the Multinomial PMF, marginal reduction to Binomial distributions,
the negative covariance structure (Cov(X_i, X_j) = -n p_i p_j for i != j),
and conditional distributions given marginal totals (contingency tables).

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import stats


def verify_multinomial_pmf_and_marginalization():
    """Validates PMF normalization, marginal Binomial, and categorical counts."""
    print("=== Block 1: Multinomial PMF & Marginalization ===")
    # Political survey: n=100 voters, p=(0.45, 0.35, 0.20)
    n = 100
    probs = np.array([0.45, 0.35, 0.20])
    target = np.array([50, 30, 20])

    # PMF validation via scipy
    pmf_val = stats.multinomial.pmf(target, n=n, p=probs)
    print(f"n={n}, p={probs.tolist()}, target counts={target.tolist()}")
    print(f"P(X_1=50, X_2=30, X_3=20) = {pmf_val:.6e}")

    # PMF normalization check: sum over all valid (x_1, x_2, x_3) with x_1+x_2+x_3=n
    # Use a coarse sum over a representative range
    norm_sum = 0.0
    for x1 in range(n + 1):
        for x2 in range(n - x1 + 1):
            x3 = n - x1 - x2
            norm_sum += stats.multinomial.pmf([x1, x2, x3], n=n, p=probs)
    print(f"PMF normalization (coarse sum): {norm_sum:.6f}")

    # Marginal reduction: X_1 ~ Bin(n, p_1)
    x1_marginal_theo = stats.binom.pmf(50, n, probs[0])
    x1_marginal_sim = 0.0
    for x2 in range(n - 50 + 1):
        x3 = n - 50 - x2
        x1_marginal_sim += stats.multinomial.pmf([50, x2, x3], n=n, p=probs)
    print(f"Marginal X_1 ~ Bin(100, 0.45): theoretical P(X_1=50)={x1_marginal_theo:.6f}")
    print(f"  Summed from joint:            P(X_1=50)={x1_marginal_sim:.6f}")

    # Number of distinct configurations (3^n)
    n_configs = 3 ** n
    print(f"Number of distinct configurations: 3^{n} = {n_configs:,}\n")


def verify_covariance_structure():
    """Verifies Cov(X_i, X_j) = -n p_i p_j for i != j and Var(X_i) = n p_i (1-p_i)."""
    print("=== Block 2: Covariance Structure & Negative Correlations ===")
    # Three-category example: n=100, p=(0.5, 0.3, 0.2)
    n = 100
    probs = np.array([0.5, 0.3, 0.2])

    # Theoretical moments
    var_theo = n * probs * (1 - probs)
    cov_12 = -n * probs[0] * probs[1]
    cov_13 = -n * probs[0] * probs[2]
    cov_23 = -n * probs[1] * probs[2]
    means = n * probs

    print(f"Theoretical moments for Mult(100, [{probs[0]}, {probs[1]}, {probs[2]}]):")
    print(f"  E[X_1] = {means[0]:.1f}, Var(X_1) = {var_theo[0]:.2f}")
    print(f"  E[X_2] = {means[1]:.1f}, Var(X_2) = {var_theo[1]:.2f}")
    print(f"  E[X_3] = {means[2]:.1f}, Var(X_3) = {var_theo[2]:.2f}")
    print(f"  Cov(X_1, X_2) = {cov_12:.2f}")
    print(f"  Cov(X_1, X_3) = {cov_13:.2f}")
    print(f"  Cov(X_2, X_3) = {cov_23:.2f}")

    # Monte Carlo simulation with 250,000 trials
    np.random.seed(42)
    sim_n = 250_000
    samples = np.random.multinomial(n, probs, size=sim_n)

    emp_means = np.mean(samples, axis=0)
    emp_vars = np.var(samples, axis=0, ddof=1)
    emp_cov_12 = np.cov(samples[:, 0], samples[:, 1])[0, 1]
    emp_cov_13 = np.cov(samples[:, 0], samples[:, 2])[0, 1]
    emp_cov_23 = np.cov(samples[:, 1], samples[:, 2])[0, 1]

    print(f"\nEmpirical moments (N={sim_n:,} samples):")
    print(f"  E[X_1] = {emp_means[0]:.4f}, Var(X_1) = {emp_vars[0]:.4f}")
    print(f"  E[X_2] = {emp_means[1]:.4f}, Var(X_2) = {emp_vars[1]:.4f}")
    print(f"  E[X_3] = {emp_means[2]:.4f}, Var(X_3) = {emp_vars[2]:.4f}")
    print(f"  Cov(X_1, X_2) = {emp_cov_12:.4f}")
    print(f"  Cov(X_1, X_3) = {emp_cov_13:.4f}")
    print(f"  Cov(X_2, X_3) = {emp_cov_23:.4f}\n")


def verify_conditional_distributions():
    """Conditional distribution of (X_3, X_4) given X_3+X_4=m is Bin(m, p_cond)."""
    print("=== Block 3: Conditional Distributions & Contingency Tables ===")
    # Four categories: p = (0.4, 0.3, 0.2, 0.1), n=100
    n = 100
    probs = np.array([0.4, 0.3, 0.2, 0.1])
    p_cond = probs[2] / (probs[2] + probs[3])  # 0.2/0.3 = 2/3
    fixed_m = 30

    print(f"Mult(100, [0.4, 0.3, 0.2, 0.1]) | p_cond = p_3/(p_3+p_4) = {p_cond:.4f}")
    print(f"Conditional X_3 | (X_3 + X_4 = {fixed_m}) should be Bin({fixed_m}, {p_cond:.4f})")

    # Theoretical Binomial probabilities
    print(f"\nTheoretical Bin({fixed_m}, {p_cond:.4f}):")
    print(f"  {'k':>3} | {'P(X_3=k | X_3+X_4=30)':>20}")
    print(f"  {'-' * 3}-+-{'-' * 20}")
    for k in range(fixed_m + 1):
        theo = stats.binom.pmf(k, fixed_m, p_cond)
        print(f"  {k:>3} | {theo:>20.4f}")

    # Empirical via Monte Carlo
    np.random.seed(42)
    sim_n = 500_000
    samples = np.random.multinomial(n, probs, size=sim_n)
    x3 = samples[:, 2]
    x4 = samples[:, 3]
    mask = (x3 + x4) == fixed_m
    cond_x3 = x3[mask]
    print(f"\nEmpirical conditional distribution (N={sim_n:,} samples, |filter|={mask.sum():,}):")
    print(f"  {'k':>3} | {'Empirical':>10} | {'Theoretical':>11} | {'|Diff|':>10}")
    print(f"  {'-' * 3}-+-{'-' * 10}-+-{'-' * 11}-+-{'-' * 10}")
    for k in range(fixed_m + 1):
        emp = np.mean(cond_x3 == k) if len(cond_x3) > 0 else 0.0
        theo = stats.binom.pmf(k, fixed_m, p_cond)
        print(f"  {k:>3} | {emp:>10.4f} | {theo:>11.4f} | {abs(emp - theo):>10.4f}")

    # Specific problem 3.8.9: n=100, m=30, k=18
    p_specific = stats.binom.pmf(18, fixed_m, p_cond)
    print(f"\nProblem 3.8.9 verification: P(X_3=18 | X_3+X_4=30) = {p_specific:.4f}")


if __name__ == "__main__":
    verify_multinomial_pmf_and_marginalization()
    verify_covariance_structure()
    verify_conditional_distributions()
