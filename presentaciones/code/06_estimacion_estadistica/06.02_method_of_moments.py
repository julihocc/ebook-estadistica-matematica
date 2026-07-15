"""
Computational Lab: Section 06.02 - Method of Moments (MoM)
====================================================================
Validates the Method of Moments estimators for the two-parameter Gamma
distribution, verifies the "delicate case" of U(-theta, theta) where the
first moment does not identify the parameter, and compares the relative
efficiency of MoM against MLE for the Gamma distribution via Monte Carlo.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import stats


def verify_mom_gamma():
    """Validates the closed-form MoM estimators for the Gamma distribution."""
    print("=== Block 1: Method of Moments for the Gamma Distribution ===")
    alpha_true, beta_true = 4.0, 2.5
    n = 500
    rng = np.random.default_rng(42)

    sample = rng.gamma(shape=alpha_true, scale=beta_true, size=n)
    xbar = np.mean(sample)
    s2 = np.var(sample, ddof=1)

    alpha_mom = xbar**2 / s2
    beta_mom = s2 / xbar
    print(f"True: alpha={alpha_true}, beta={beta_true}")
    print(f"Sample: xbar={xbar:.4f}, S^2={s2:.4f}, n={n}")
    print(f"  alpha_MoM = xbar^2/S^2 = {alpha_mom:.4f}")
    print(f"  beta_MoM = S^2/xbar = {beta_mom:.4f}")

    # Worked example from the theory: xbar=10, S^2=25
    xbar_ex, s2_ex = 10.0, 25.0
    print(f"\nWorked example: xbar={xbar_ex}, S^2={s2_ex}")
    print(f"  alpha_MoM = {xbar_ex**2/s2_ex:.4f}, beta_MoM = {s2_ex/xbar_ex:.4f}")


def verify_delicate_case_symmetric_uniform():
    """Verifies the MoM estimator for U(-theta, theta), where the first moment is uninformative."""
    print("\n=== Block 2: The Delicate Case U(-theta, theta) ===")
    theta_true = 5.0
    n = 500
    rng = np.random.default_rng(42)

    sample = rng.uniform(-theta_true, theta_true, size=n)
    m1 = np.mean(sample)
    m2 = np.mean(sample**2)
    theta_mom = np.sqrt(3 * m2)

    print(f"True theta={theta_true}, n={n}")
    print(f"  m1 = {m1:.4f} (theoretically 0 for any theta -- uninformative)")
    print(f"  m2 = {m2:.4f}")
    print(f"  theta_MoM = sqrt(3*m2) = {theta_mom:.4f}")

    # Small worked dataset: {-3, 2, -1, 4, -2}
    data = np.array([-3, 2, -1, 4, -2])
    m2_small = np.mean(data**2)
    theta_small = np.sqrt(3 * m2_small)
    print(f"\nWorked example {{-3,2,-1,4,-2}}: m2={m2_small:.4f}, theta_MoM={theta_small:.4f}")


def compare_mom_vs_mle_efficiency():
    """Compares the variance (efficiency) of MoM vs. MLE estimators for the Gamma shape parameter."""
    print("\n=== Block 3: MoM vs. MLE Efficiency for the Gamma Distribution ===")
    alpha_true, beta_true = 4.0, 2.5
    n = 30
    n_trials = 5_000
    rng = np.random.default_rng(42)

    alpha_mom_estimates = np.empty(n_trials)
    alpha_mle_estimates = np.empty(n_trials)

    for i in range(n_trials):
        sample = rng.gamma(shape=alpha_true, scale=beta_true, size=n)
        xbar = np.mean(sample)
        s2 = np.var(sample, ddof=1)
        alpha_mom_estimates[i] = xbar**2 / s2

        fitted_shape, _, fitted_scale = stats.gamma.fit(sample, floc=0)
        alpha_mle_estimates[i] = fitted_shape

    print(f"True alpha={alpha_true}, n={n}, trials={n_trials}")
    print(f"  MoM: mean={np.mean(alpha_mom_estimates):.4f}, Var={np.var(alpha_mom_estimates, ddof=1):.4f}")
    print(f"  MLE: mean={np.mean(alpha_mle_estimates):.4f}, Var={np.var(alpha_mle_estimates, ddof=1):.4f}")
    rel_eff = np.var(alpha_mom_estimates, ddof=1) / np.var(alpha_mle_estimates, ddof=1)
    print(f"  Relative efficiency Ef(MLE, MoM) = Var(MoM)/Var(MLE) = {rel_eff:.4f}")
    print("  (Ef > 1 confirms MLE is more efficient, as expected asymptotically)")


if __name__ == "__main__":
    verify_mom_gamma()
    verify_delicate_case_symmetric_uniform()
    compare_mom_vs_mle_efficiency()
