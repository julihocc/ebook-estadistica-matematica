"""
Computational Lab: Section 09.04 - Linear Regression on Simulated Data
====================================================================
Simulates data from a known population model (true alpha, beta, sigma),
fits OLS to recover estimates close to the true parameters, and shows that
the exact SST=SSR+SSE decomposition proven in Section 09.03 requires the
actual least-squares fit -- it does NOT hold, even approximately in the
same exact way, if one instead plugs in the true population line.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np


def simulate_known_population_model():
    """Generates X, Y from a population model with known true alpha, beta, sigma."""
    print("=== Block 1: Simulating Data from a Known Population Model ===")
    rng = np.random.default_rng(seed=1234)
    true_alpha, true_beta, true_sigma = 2.0, 0.3, 0.5
    x = 2.5 * rng.standard_normal(100) + 1.5
    noise = true_sigma * rng.standard_normal(100)
    y = true_alpha + true_beta * x + noise

    print(f"True population parameters: alpha={true_alpha}, beta={true_beta}, sigma={true_sigma}")
    print(f"Simulated n={len(x)} points; sample mean(x)={x.mean():.4f}, sample mean(y)={y.mean():.4f}")
    return x, y, true_alpha, true_beta


def fit_ols_and_compare_to_truth(x, y, true_alpha, true_beta):
    """Fits OLS on the simulated sample and compares to the known true parameters."""
    print("\n=== Block 2: OLS Fit vs. True Population Parameters ===")
    x_bar, y_bar = x.mean(), y.mean()
    beta_hat = np.sum((x - x_bar) * (y - y_bar)) / np.sum((x - x_bar) ** 2)
    alpha_hat = y_bar - beta_hat * x_bar
    print(f"Fitted:      alpha_hat={alpha_hat:.4f}, beta_hat={beta_hat:.4f}")
    print(f"True:        alpha={true_alpha:.4f},     beta={true_beta:.4f}")
    print(f"Estimation error: |alpha_hat-alpha|={abs(alpha_hat - true_alpha):.4f}, |beta_hat-beta|={abs(beta_hat - true_beta):.4f}")

    y_fitted = alpha_hat + beta_hat * x
    sst = np.sum((y - y_bar) ** 2)
    ssr = np.sum((y_fitted - y_bar) ** 2)
    sse = np.sum((y - y_fitted) ** 2)
    print(f"Fitted-line decomposition: SST={sst:.4f}, SSR={ssr:.4f}, SSE={sse:.4f}, SSR+SSE={ssr + sse:.4f}")
    print(f"Exact match to SST: {np.isclose(sst, ssr + sse)}")

    return alpha_hat, beta_hat, sst


def fitted_line_versus_oracle_line(x, y, alpha_hat, beta_hat, true_alpha, true_beta, sst):
    """Shows the exact decomposition holds for the fit but not for the true oracle line."""
    print("\n=== Block 3: Why the Fitted Line, Not the True Line ===")
    y_bar = y.mean()

    y_fitted = alpha_hat + beta_hat * x
    ssr_fit = np.sum((y_fitted - y_bar) ** 2)
    sse_fit = np.sum((y - y_fitted) ** 2)
    r2_fit = ssr_fit / sst
    print(f"Using the FITTED line:  SSR+SSE={ssr_fit + sse_fit:.4f} (matches SST={sst:.4f}), R^2={r2_fit:.4f}")

    y_oracle = true_alpha + true_beta * x
    ssr_oracle = np.sum((y_oracle - y_bar) ** 2)
    sse_oracle = np.sum((y - y_oracle) ** 2)
    r2_oracle = ssr_oracle / sst
    print(f"Using the TRUE (oracle) line: SSR+SSE={ssr_oracle + sse_oracle:.4f} (does NOT match SST={sst:.4f})")
    print(f"R^2 with oracle line = {r2_oracle:.4f} (different from the fitted R^2={r2_fit:.4f})")
    print("The exact decomposition requires sum(e_i)=0 and sum(x_i*e_i)=0,")
    print("which the normal equations guarantee ONLY for the least-squares fit,")
    print("not for the true population line evaluated on a finite sample.")


if __name__ == "__main__":
    x, y, true_alpha, true_beta = simulate_known_population_model()
    alpha_hat, beta_hat, sst = fit_ols_and_compare_to_truth(x, y, true_alpha, true_beta)
    fitted_line_versus_oracle_line(x, y, alpha_hat, beta_hat, true_alpha, true_beta, sst)
