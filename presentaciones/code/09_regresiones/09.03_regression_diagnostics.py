"""
Computational Lab: Section 09.03 - Residual Diagnostics, Multicollinearity
(VIF), and Classical Regression Assumptions
====================================================================
Implements the Durbin-Watson and Breusch-Pagan tests from scratch, computes
the Variance Inflation Factor for correlated predictors and verifies its
identity with the diagonal of the inverse correlation matrix, and computes
Cook's Distance for every observation in a fitted model to flag influential
points via both the leverage and residual-driven mechanisms.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import stats


def durbin_watson_and_breusch_pagan():
    """Computes DW on a synthetic autocorrelated residual series and runs Breusch-Pagan."""
    print("=== Block 1: Durbin-Watson and Breusch-Pagan Tests ===")
    e = np.array([2.1, 1.8, -0.5, -1.2, -2.0, -1.5, 0.8, 1.9, 2.2, 1.0])
    dw = np.sum(np.diff(e) ** 2) / np.sum(e ** 2)
    rho_hat = np.sum(e[1:] * e[:-1]) / np.sum(e ** 2)
    print(f"Durbin-Watson DW = {dw:.4f}  (approx 2(1-rho_hat) = {2 * (1 - rho_hat):.4f})")
    print("DW << 2 -> strong positive autocorrelation in the residuals")

    rng = np.random.default_rng(seed=5)
    n = 60
    X1 = rng.uniform(1, 10, n)
    X2 = rng.uniform(1, 10, n)
    resid = rng.normal(scale=1.0, size=n) * (1 + 0.3 * X1)
    X_design = np.column_stack([np.ones(n), X1, X2])
    beta_aux, *_ = np.linalg.lstsq(X_design, resid ** 2, rcond=None)
    fitted_aux = X_design @ beta_aux
    ss_res_aux = np.sum((resid ** 2 - fitted_aux) ** 2)
    ss_tot_aux = np.sum((resid ** 2 - np.mean(resid ** 2)) ** 2)
    r2_aux = 1 - ss_res_aux / ss_tot_aux
    lm_stat = n * r2_aux
    p_value = stats.chi2.sf(lm_stat, df=2)
    print(f"Breusch-Pagan: R2_aux={r2_aux:.4f}, LM={lm_stat:.4f}, p-value={p_value:.4f}")


def variance_inflation_factor_demo():
    """Computes VIF for correlated predictors and verifies VIF_j = (R^-1)_jj."""
    print("\n=== Block 2: Variance Inflation Factor (VIF) ===")
    rng = np.random.default_rng(seed=8)
    n = 100
    x1 = rng.normal(size=n)
    x2 = 0.9 * x1 + 0.1 * rng.normal(size=n)
    x3 = rng.normal(size=n)
    predictors = np.column_stack([x1, x2, x3])

    vifs = []
    for j in range(predictors.shape[1]):
        y_j = predictors[:, j]
        others = np.column_stack([np.ones(n)] + [predictors[:, k] for k in range(3) if k != j])
        beta_j, *_ = np.linalg.lstsq(others, y_j, rcond=None)
        fitted_j = others @ beta_j
        ss_res = np.sum((y_j - fitted_j) ** 2)
        ss_tot = np.sum((y_j - y_j.mean()) ** 2)
        r2_j = 1 - ss_res / ss_tot
        vif_j = 1 / (1 - r2_j)
        vifs.append(vif_j)
        print(f"Predictor {j + 1}: R2_aux={r2_j:.4f}, VIF={vif_j:.4f}")

    R = np.corrcoef(predictors, rowvar=False)
    R_inv_diag = np.diag(np.linalg.inv(R))
    print(f"VIF via 1/(1-R^2):        {np.round(vifs, 4)}")
    print(f"VIF via diag(R^-1):       {np.round(R_inv_diag, 4)}")


def cooks_distance_demo():
    """Fits a model with one high-leverage and one large-residual point, flags both via Cook's D."""
    print("\n=== Block 3: Cook's Distance and Influential Observations ===")
    rng = np.random.default_rng(seed=13)
    n = 30
    x = rng.uniform(1, 10, n)
    y = 3.0 + 2.0 * x + rng.normal(scale=1.0, size=n)

    x[0], y[0] = 25.0, 3.0 + 2.0 * 25.0  # high-leverage point, on-trend
    y[1] = y[1] + 15.0                    # large-residual outlier, typical leverage

    X = np.column_stack([np.ones(n), x])
    beta_hat, *_ = np.linalg.lstsq(X, y, rcond=None)
    fitted = X @ beta_hat
    residuals = y - fitted
    p_plus_1 = X.shape[1]

    H = X @ np.linalg.inv(X.T @ X) @ X.T
    leverage = np.diag(H)
    sigma_hat2 = np.sum(residuals ** 2) / (n - p_plus_1)
    studentized = residuals / np.sqrt(sigma_hat2 * (1 - leverage))
    cooks_d = (studentized ** 2 / p_plus_1) * (leverage / (1 - leverage))

    threshold = 4 / n
    print(f"Threshold 4/n = {threshold:.4f}")
    for i in [0, 1]:
        flag = "INFLUENTIAL" if cooks_d[i] > threshold else "not influential"
        print(f"  Obs {i}: leverage={leverage[i]:.4f}, studentized_resid={studentized[i]:.4f}, "
              f"Cook's D={cooks_d[i]:.4f} -> {flag}")
    n_influential = np.sum(cooks_d > threshold)
    print(f"Total influential observations (of {n}): {n_influential}")


if __name__ == "__main__":
    durbin_watson_and_breusch_pagan()
    variance_inflation_factor_demo()
    cooks_distance_demo()
