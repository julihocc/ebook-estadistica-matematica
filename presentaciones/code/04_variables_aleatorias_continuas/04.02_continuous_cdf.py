"""
Computational Lab: Section 04.02 - Continuous CDF and Quantiles
================================================================
Validates continuous CDF properties (F(-inf)=0, F(+inf)=1, monotonicity),
computes interval probabilities and quantiles via inversion, implements
the inverse transform sampling method, and applies the Kolmogorov-Smirnov
goodness-of-fit test.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import stats
from scipy.optimize import brentq


def verify_cdf_and_quantiles():
    """Validates CDF properties and computes quantiles via numerical inversion."""
    print("=== Block 1: CDF Validation & Quantile Inversion ===")
    # Validation with three standard distributions
    distributions = [
        ("Uniform(0, 1)", stats.uniform, (0, 1)),
        ("Exponential(2.0)", stats.expon, (0, 0.5)),  # scale = 1/lambda
        ("Normal(0, 1)", stats.norm, (0, 1))
    ]

    print("CDF boundary properties:")
    for name, dist, _ in distributions:
        f_neg_inf = dist.cdf(-1e10)
        f_pos_inf = dist.cdf(1e10)
        print(f"  {name:25s}: F(-inf) = {f_neg_inf:.2e}, F(+inf) = {f_pos_inf:.6f}")

    # Monotonicity check: F(x) should be non-decreasing on a fine grid
    print("\nMonotonicity check (Uniform, Exponential, Normal on 100-point grid):")
    for name, dist, params in distributions:
        if hasattr(dist, 'ppf'):
            x_grid = np.linspace(dist.ppf(0.001), dist.ppf(0.999), 100)
        else:
            x_grid = np.linspace(-5, 5, 100)
        cdf_values = dist.cdf(x_grid)
        diffs = np.diff(cdf_values)
        is_monotonic = np.all(diffs >= -1e-12)
        max_increase = np.max(diffs)
        print(f"  {name:25s}: monotonic = {is_monotonic}, max increase = {max_increase:.6f}")

    # Quantile inversion via brentq
    print("\nQuantile computation via numerical inversion:")
    for name, dist, _ in distributions:
        for p in [0.025, 0.5, 0.975]:
            q_scipy = dist.ppf(p)
            # Numerical inversion: find x such that F(x) - p = 0
            try:
                lo, hi = dist.ppf(0.001), dist.ppf(0.999)
                q_numerical = brentq(lambda x: dist.cdf(x) - p, lo, hi)
            except Exception:
                q_numerical = np.nan
            match = abs(q_scipy - q_numerical) < 1e-5 if not np.isnan(q_numerical) else False
            print(f"  {name} q_{p}: scipy={q_scipy:.6f}, numerical={q_numerical:.6f}, match={match}")


def verify_inverse_transform_sampling():
    """Implements inverse transform sampling for various continuous distributions."""
    print("\n=== Block 2: Inverse Transform Sampling ===")
    np.random.seed(42)
    n_samples = 100_000

    # Exponential(lambda=2): F^(-1)(U) = -ln(1-U)/lambda
    print("Exponential(lambda=2) via inverse transform:")
    U = np.random.uniform(0, 1, size=n_samples)
    X_exp = -np.log(1 - U) / 2.0
    print(f"  Empirical mean: {np.mean(X_exp):.4f} (theoretical: {1/2:.4f})")
    print(f"  Empirical var:  {np.var(X_exp, ddof=1):.4f} (theoretical: {1/4:.4f})")
    ks_exp = stats.kstest(X_exp, stats.expon(scale=0.5).cdf)
    print(f"  Kolmogorov-Smirnov test: stat={ks_exp.statistic:.6f}, p-value={ks_exp.pvalue:.4f}")

    # Uniform(0, 5): F^(-1)(U) = 5*U
    print("\nUniform(0, 5) via inverse transform:")
    U2 = np.random.uniform(0, 1, size=n_samples)
    X_unif = 5.0 * U2
    print(f"  Empirical mean: {np.mean(X_unif):.4f} (theoretical: {2.5:.4f})")
    print(f"  Empirical var:  {np.var(X_unif, ddof=1):.4f} (theoretical: {25/12:.4f})")
    ks_unif = stats.kstest(X_unif, stats.uniform(0, 5).cdf)
    print(f"  Kolmogorov-Smirnov test: stat={ks_unif.statistic:.6f}, p-value={ks_unif.pvalue:.4f}")

    # CDF verification of generated exponential samples
    print("\nCDF comparison (generated vs theoretical Exponential):")
    for x in [0.0, 0.25, 0.5, 1.0, 2.0]:
        cdf_emp = np.mean(X_exp <= x)
        cdf_theo = stats.expon(scale=0.5).cdf(x)
        print(f"  F({x:.2f}): empirical={cdf_emp:.4f}, theoretical={cdf_theo:.4f}, diff={abs(cdf_emp - cdf_theo):.4f}")


def verify_quantile_based_statistics():
    """Applies quantile-based statistics and Kolmogorov-Smirnov goodness-of-fit test."""
    print("\n=== Block 3: Quantile-Based Statistics & KS Test ===")
    np.random.seed(123)
    n = 50
    # Generate Uniform(0, 1) samples and test against Uniform distribution
    samples = np.random.uniform(0, 1, size=n)

    # Empirical CDF and KS statistic
    sorted_samples = np.sort(samples)
    ecdf = np.arange(1, n + 1) / n
    cdf_theo = sorted_samples  # Uniform(0, 1) CDF is the identity
    D_plus = np.max(ecdf - cdf_theo)
    D_minus = np.max(cdf_theo - (np.arange(0, n) / n))
    D_stat = max(D_plus, D_minus)
    print(f"Empirical KS statistic for n={n} Uniform(0,1) samples: D = {D_stat:.4f}")

    # Compare with theoretical asymptotic distribution
    critical_value_05 = 1.358 / np.sqrt(n)
    critical_value_01 = 1.628 / np.sqrt(n)
    print(f"  Critical value (alpha=0.05): {critical_value_05:.4f}")
    print(f"  Critical value (alpha=0.01): {critical_value_01:.4f}")
    p_value = stats.kstest(samples, stats.uniform(0, 1).cdf).pvalue
    print(f"  SciPy KS p-value: {p_value:.4f}")
    print(f"  Decision at alpha=0.05: {'Reject H0' if D_stat > critical_value_05 else 'Fail to reject H0'}")

    # Sample quantiles
    print("\nSample quantiles vs theoretical:")
    for p in [0.10, 0.25, 0.50, 0.75, 0.90]:
        q_emp = np.quantile(samples, p)
        q_theo = p  # For Uniform(0, 1)
        print(f"  q_{p:.2f}: empirical={q_emp:.4f}, theoretical={q_theo:.4f}, diff={abs(q_emp - q_theo):.4f}")

    # Confidence interval for the median using order statistics
    print("\n95% CI for median (using order statistics):")
    alpha = 0.05
    lower_idx = int(np.floor(n / 2 - np.sqrt(n) * 1.96 / 2))
    upper_idx = int(np.ceil(n / 2 + np.sqrt(n) * 1.96 / 2))
    print(f"  Order statistic range: [{lower_idx}, {upper_idx}]")
    ci_lower = sorted_samples[lower_idx]
    ci_upper = sorted_samples[upper_idx]
    print(f"  95% CI for median: [{ci_lower:.4f}, {ci_upper:.4f}]")


if __name__ == "__main__":
    verify_cdf_and_quantiles()
    verify_inverse_transform_sampling()
    verify_quantile_based_statistics()
