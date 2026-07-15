"""
Computational Lab: Section 05.03 - Chi-Squared Distribution and Sample Variance
====================================================================
Validates core chi-squared properties (mean, variance, additivity, and the
Gamma connection), verifies Fisher's theorem (independence of Xbar and S^2,
and (n-1)S^2/sigma^2 ~ chi2_{n-1}) via Monte Carlo for normal samples, and
checks the empirical coverage of a chi-squared confidence interval for
sigma^2.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import stats


def verify_chi_squared_properties():
    """Validates mean, variance, additivity, and the Gamma(nu/2, 2) connection."""
    print("=== Block 1: Chi-Squared Properties ===")
    nu = 15
    print(f"chi2_{nu}: mean={stats.chi2.mean(df=nu):.4f} (theoretical: {nu})")
    print(f"chi2_{nu}: variance={stats.chi2.var(df=nu):.4f} (theoretical: {2*nu})")

    # Gamma(nu/2, 2) connection
    gamma_mean = stats.gamma.mean(a=nu / 2, scale=2)
    gamma_var = stats.gamma.var(a=nu / 2, scale=2)
    print(f"Gamma(nu/2={nu/2}, 2): mean={gamma_mean:.4f}, variance={gamma_var:.4f} (should match chi2_{nu})")

    # Additivity: sum of independent chi-squared variables
    rng = np.random.default_rng(42)
    n_trials = 200_000
    nu1, nu2 = 5, 8
    x = rng.chisquare(nu1, size=n_trials)
    y = rng.chisquare(nu2, size=n_trials)
    total = x + y
    ks = stats.kstest(total, "chi2", args=(nu1 + nu2,))
    print(f"\nAdditivity: chi2_{nu1} + chi2_{nu2} vs chi2_{nu1+nu2}")
    print(f"  Empirical mean of sum: {np.mean(total):.4f} (theoretical: {nu1+nu2})")
    print(f"  KS test vs chi2_{nu1+nu2}: D={ks.statistic:.5f}, p={ks.pvalue:.4f}")


def verify_fisher_theorem():
    """Verifies independence of Xbar and S^2, and (n-1)S^2/sigma^2 ~ chi2_{n-1}, for normal samples."""
    print("\n=== Block 2: Fisher's Theorem (Independence and Chi-Squared Statistic) ===")
    mu, sigma = 50.0, 2.0
    n = 10
    n_trials = 200_000
    rng = np.random.default_rng(42)

    samples = rng.normal(mu, sigma, size=(n_trials, n))
    xbars = np.mean(samples, axis=1)
    s2 = np.var(samples, axis=1, ddof=1)

    correlation = np.corrcoef(xbars, s2)[0, 1]
    print(f"Population: N({mu}, {sigma**2}), n={n}, trials={n_trials}")
    print(f"  Correlation(Xbar, S^2) = {correlation:.5f} (should be close to 0: independence)")

    stat = (n - 1) * s2 / sigma**2
    ks = stats.kstest(stat, "chi2", args=(n - 1,))
    print(f"  (n-1)*S^2/sigma^2: empirical mean={np.mean(stat):.4f} (theoretical: {n-1})")
    print(f"  KS test vs chi2_{n-1}: D={ks.statistic:.5f}, p={ks.pvalue:.4f}")

    # Worked example: n=10, S^2=7.2, sigma^2=4
    n_ex, s2_ex, sigma2_ex = 10, 7.2, 4.0
    stat_ex = (n_ex - 1) * s2_ex / sigma2_ex
    crit_95 = stats.chi2.ppf(0.95, df=n_ex - 1)
    print(f"\nWorked example: n={n_ex}, S^2={s2_ex}, sigma^2={sigma2_ex}")
    print(f"  Statistic = {stat_ex:.4f}, critical value chi2_{n_ex-1},0.95 = {crit_95:.4f}")
    print(f"  Reject H0 (sigma^2={sigma2_ex})? {'Yes' if stat_ex > crit_95 else 'No'}")


def verify_confidence_interval_coverage():
    """Checks the empirical coverage of a chi-squared-based confidence interval for sigma^2."""
    print("\n=== Block 3: Confidence Interval Coverage for sigma^2 ===")
    mu, sigma2 = 100.0, 25.0
    n = 20
    n_trials = 50_000
    alpha = 0.05
    rng = np.random.default_rng(42)

    chi2_lower = stats.chi2.ppf(alpha / 2, df=n - 1)
    chi2_upper = stats.chi2.ppf(1 - alpha / 2, df=n - 1)
    print(f"Population: N({mu}, {sigma2}), n={n}, trials={n_trials}, alpha={alpha}")
    print(f"  chi2_{n-1},{alpha/2} = {chi2_lower:.4f}, chi2_{n-1},{1-alpha/2} = {chi2_upper:.4f}")

    samples = rng.normal(mu, np.sqrt(sigma2), size=(n_trials, n))
    s2 = np.var(samples, axis=1, ddof=1)
    ci_lower = (n - 1) * s2 / chi2_upper
    ci_upper = (n - 1) * s2 / chi2_lower

    covered = np.mean((ci_lower <= sigma2) & (sigma2 <= ci_upper))
    print(f"  Empirical coverage: {covered:.4f} (nominal: {1-alpha:.4f})")

    # Single worked interval: n=20, S^2=45
    n_ex, s2_ex = 20, 45.0
    lo = (n_ex - 1) * s2_ex / chi2_upper
    hi = (n_ex - 1) * s2_ex / chi2_lower
    print(f"\nWorked example: n={n_ex}, S^2={s2_ex}")
    print(f"  95% CI for sigma^2: [{lo:.2f}, {hi:.2f}]")


if __name__ == "__main__":
    verify_chi_squared_properties()
    verify_fisher_theorem()
    verify_confidence_interval_coverage()
