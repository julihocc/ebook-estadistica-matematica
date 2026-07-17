"""
Computational Lab: Section 09.11 - Categorical Variables and Dummy Variables
====================================================================
Manually encodes a two-level categorical predictor (Gender) as a single
dummy variable, encodes a three-level predictor (City Tier) using the
(n-1)-dummy rule, and demonstrates numerically why including all n dummies
alongside the intercept (the "dummy variable trap") makes the design matrix
singular, verified via its condition number.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np


def two_level_dummy_encoding():
    """Encodes a two-level categorical variable (Gender) as one dummy column."""
    print("=== Block 1: Two-Level Categorical Variable (Gender) ===")
    rng = np.random.default_rng(seed=6)
    n = 100
    monthly_income = rng.uniform(2000, 20000, n)
    gender = rng.choice(["Female", "Male"], size=n)
    male_dummy = (gender == "Male").astype(float)

    total_spend = (3500.0 + 0.15 * monthly_income + 250.0 * male_dummy
                   + rng.normal(scale=200.0, size=n))

    X = np.column_stack([np.ones(n), monthly_income, male_dummy])
    beta, *_ = np.linalg.lstsq(X, total_spend, rcond=None)

    print(f"Intercept (baseline: Female): {beta[0]:.2f}")
    print(f"Monthly Income coefficient:   {beta[1]:.4f}")
    print(f"Male dummy coefficient:       {beta[2]:.2f}")
    print(f"Interpretation: male customers spend, on average, {beta[2]:.2f} more")
    print("than female customers (the reference/baseline level), holding income fixed.")


def three_level_dummy_encoding_n_minus_1_rule():
    """Encodes a three-level categorical variable (City Tier) with 2 dummies (n-1 rule)."""
    print("\n=== Block 2: Three-Level Categorical Variable (City Tier), (n-1) Rule ===")
    rng = np.random.default_rng(seed=9)
    n = 150
    monthly_income = rng.uniform(2000, 20000, n)
    city_tier = rng.choice([1, 2, 3], size=n)

    tier1_dummy = (city_tier == 1).astype(float)
    tier2_dummy = (city_tier == 2).astype(float)
    # Tier 3 is the reference level: no dummy column needed for it.

    total_spend = (3000.0 + 0.12 * monthly_income + 400.0 * tier1_dummy
                   + 150.0 * tier2_dummy + rng.normal(scale=200.0, size=n))

    X = np.column_stack([np.ones(n), monthly_income, tier1_dummy, tier2_dummy])
    beta, *_ = np.linalg.lstsq(X, total_spend, rcond=None)

    print(f"Intercept (baseline: Tier 3): {beta[0]:.2f}")
    print(f"Income coefficient:           {beta[1]:.4f}")
    print(f"Tier 1 dummy coefficient:     {beta[2]:.2f}")
    print(f"Tier 2 dummy coefficient:     {beta[3]:.2f}")
    print(f"Design matrix has {X.shape[1]} columns for 3 levels: correctly (n-1)=2 dummies, no trap.")


def dummy_variable_trap_demo():
    """Shows that including all k dummies plus an intercept makes X singular."""
    print("\n=== Block 3: The Dummy Variable Trap ===")
    rng = np.random.default_rng(seed=9)
    n = 150
    city_tier = rng.choice([1, 2, 3], size=n)

    tier1_dummy = (city_tier == 1).astype(float)
    tier2_dummy = (city_tier == 2).astype(float)
    tier3_dummy = (city_tier == 3).astype(float)

    X_correct = np.column_stack([np.ones(n), tier1_dummy, tier2_dummy])
    X_trap = np.column_stack([np.ones(n), tier1_dummy, tier2_dummy, tier3_dummy])

    cond_correct = np.linalg.cond(X_correct)
    cond_trap = np.linalg.cond(X_trap)
    rank_trap = np.linalg.matrix_rank(X_trap)

    print(f"Correct encoding (intercept + 2 dummies): condition number = {cond_correct:.2f}")
    print(f"Trap encoding (intercept + all 3 dummies): condition number = {cond_trap:.2e}")
    print(f"Rank of the trap design matrix: {rank_trap} (columns: {X_trap.shape[1]}, rank-deficient: {rank_trap < X_trap.shape[1]})")
    print("Including all 3 dummies makes column 0 exactly equal to the sum of the other")
    print("three (1 = tier1 + tier2 + tier3 for every row): perfect multicollinearity.")


if __name__ == "__main__":
    two_level_dummy_encoding()
    three_level_dummy_encoding_n_minus_1_rule()
    dummy_variable_trap_demo()
