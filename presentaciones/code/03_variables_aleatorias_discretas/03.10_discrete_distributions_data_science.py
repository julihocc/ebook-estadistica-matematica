"""
Computational Lab: Section 03.10 - Discrete Distributions in Data Science
==========================================================================
Validates MLE fitting for Poisson and Negative Binomial, overdispersion
detection via the dispersion index D = s^2/x_bar, likelihood ratio tests
for model selection (Wilks theorem), and bootstrap confidence intervals
for parameter uncertainty quantification.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import stats
from scipy.special import gammaln


def mle_fitting_and_overdispersion():
    """Fits Poisson and Negative Binomial to count data; checks overdispersion."""
    print("=== Block 1: MLE Fitting & Overdispersion Detection ===")
    # Simulated count data: 100 observations from a NegBin(r=2, p=0.4) -> mu=3, var=7.5
    np.random.seed(42)
    n_obs = 100
    r_true, p_true = 2.0, 0.4
    counts = stats.nbinom.rvs(n=r_true, p=p_true, size=n_obs)
    sample_mean = np.mean(counts)
    sample_var = np.var(counts, ddof=1)
    dispersion_index = sample_var / sample_mean
    print(f"Synthetic data: n={n_obs}, true NegBin(r={r_true}, p={p_true})")
    print(f"  Sample mean:  {sample_mean:.4f} (theoretical mu=3.0)")
    print(f"  Sample var:   {sample_var:.4f} (theoretical mu+mu^2/r=7.5)")
    print(f"  Dispersion index D = s^2/x_bar = {dispersion_index:.4f}")
    if dispersion_index > 1.5:
        print(f"  -> Strong overdispersion (D > 1.5): Negative Binomial is recommended")
    else:
        print(f"  -> Mild or no overdispersion: Poisson may suffice")

    # Poisson MLE
    lambda_mle = sample_mean
    log_lik_poisson = np.sum(stats.poisson.logpmf(counts, mu=lambda_mle))

    # Negative Binomial MLE via method of moments
    r_mom = sample_mean ** 2 / (sample_var - sample_mean)
    p_mom = sample_mean / sample_var
    log_lik_nbinom = np.sum(stats.nbinom.logpmf(counts, n=r_mom, p=p_mom))

    # AIC and BIC
    n = len(counts)
    aic_poisson = 2 * 1 - 2 * log_lik_poisson
    aic_nbinom = 2 * 2 - 2 * log_lik_nbinom
    bic_poisson = 1 * np.log(n) - 2 * log_lik_poisson
    bic_nbinom = 2 * np.log(n) - 2 * log_lik_nbinom
    print(f"\nModel comparison:")
    print(f"  Poisson(lambda={lambda_mle:.4f}): logLik={log_lik_poisson:.4f}, AIC={aic_poisson:.4f}, BIC={bic_poisson:.4f}")
    print(f"  NegBin(r={r_mom:.4f}, p={p_mom:.4f}): logLik={log_lik_nbinom:.4f}, AIC={aic_nbinom:.4f}, BIC={bic_nbinom:.4f}")
    print(f"  Delta AIC (Poisson - NegBin): {aic_poisson - aic_nbinom:.4f}")
    print(f"  Delta BIC (Poisson - NegBin): {bic_poisson - bic_nbinom:.4f}\n")


def likelihood_ratio_and_wilks():
    """Applies Wilks' theorem to test Poisson vs. Negative Binomial overdispersion."""
    print("=== Block 2: Likelihood Ratio Test & Wilks Theorem ===")
    # Generate a dataset with known overdispersion
    np.random.seed(123)
    counts = stats.nbinom.rvs(n=3.0, p=0.5, size=200)  # mu=3, var=9
    sample_mean = np.mean(counts)
    sample_var = np.var(counts, ddof=1)

    # Log-likelihoods
    log_lik_poisson = np.sum(stats.poisson.logpmf(counts, mu=sample_mean))
    r_mom = sample_mean ** 2 / max(sample_var - sample_mean, 0.1)
    p_mom = sample_mean / sample_var
    log_lik_nbinom = np.sum(stats.nbinom.logpmf(counts, n=r_mom, p=p_mom))

    # Likelihood ratio statistic (Wilks)
    lambda_lr = -2 * (log_lik_poisson - log_lik_nbinom)
    df = 1  # NegBin has 1 extra parameter
    p_value = 1 - stats.chi2.cdf(lambda_lr, df=df)
    print(f"Dataset: n=200, NegBin(r=3, p=0.5) -> mu=3, var=9")
    print(f"  Sample mean: {sample_mean:.4f}, sample var: {sample_var:.4f}")
    print(f"  Poisson logLik: {log_lik_poisson:.4f}")
    print(f"  NegBin logLik:  {log_lik_nbinom:.4f}")
    print(f"\nLikelihood ratio statistic: Lambda = -2(logL_0 - logL_1) = {lambda_lr:.4f}")
    print(f"Degrees of freedom: df = 1 (extra parameter in NegBin)")
    print(f"Critical value chi2(1, 0.05) = {stats.chi2.ppf(0.95, df=1):.4f}")
    print(f"P-value: {p_value:.6f}")
    if lambda_lr > stats.chi2.ppf(0.95, df=1):
        print("Decision: Reject H0 (Poisson). Negative Binomial is significantly better.")
    else:
        print("Decision: Fail to reject H0. Poisson is adequate.")

    # Power analysis: how does LR scale with overdispersion?
    print("\nLR statistic vs overdispersion strength (n=100):")
    for r_test in [10.0, 5.0, 2.0, 1.0, 0.5]:
        sim_counts = stats.nbinom.rvs(n=r_test, p=r_test / (r_test + 3.0), size=100)
        sim_mean = np.mean(sim_counts)
        sim_var = np.var(sim_counts, ddof=1)
        ll_p = np.sum(stats.poisson.logpmf(sim_counts, mu=sim_mean))
        r_m = sim_mean ** 2 / max(sim_var - sim_mean, 0.1)
        p_m = sim_mean / sim_var
        ll_nb = np.sum(stats.nbinom.logpmf(sim_counts, n=r_m, p=p_m))
        lr_stat = -2 * (ll_p - ll_nb)
        print(f"  r={r_test:5.1f} (var/mu={sim_var/sim_mean:.2f}): LR={lr_stat:7.4f}, p={1-stats.chi2.cdf(lr_stat, 1):.4f}\n")


def confidence_intervals_and_bootstrap():
    """Computes confidence intervals for Poisson lambda and bootstrap for BN params."""
    print("=== Block 3: Confidence Intervals & Bootstrap ===")
    # Insurance claims: 12 months of data
    np.random.seed(7)
    true_lambda = 47.3
    monthly_claims = stats.poisson.rvs(mu=true_lambda, size=12)
    sample_mean = np.mean(monthly_claims)
    n_obs = len(monthly_claims)
    print(f"Insurance claims: {n_obs} months of data")
    print(f"  Sample mean (MLE of lambda): {sample_mean:.4f}")

    # Wald CI for Poisson lambda
    se_wald = np.sqrt(sample_mean / n_obs)
    ci_wald = (sample_mean - 1.96 * se_wald, sample_mean + 1.96 * se_wald)
    print(f"  Wald 95% CI: [{ci_wald[0]:.4f}, {ci_wald[1]:.4f}]")

    # Exact Poisson CI (Garwood)
    ci_exact = (0.5 * stats.chi2.ppf(0.025, 2 * sum(monthly_claims)) / n_obs,
                0.5 * stats.chi2.ppf(0.975, 2 * (sum(monthly_claims) + 1)) / n_obs)
    print(f"  Exact 95% CI: [{ci_exact[0]:.4f}, {ci_exact[1]:.4f}]")

    # Bootstrap CI for the standard error of the MLE
    np.random.seed(42)
    n_boot = 10_000
    boot_means = np.array([np.mean(np.random.poisson(sample_mean, n_obs)) for _ in range(n_boot)])
    se_bootstrap = np.std(boot_means, ddof=1)
    ci_bootstrap = (np.percentile(boot_means, 2.5), np.percentile(boot_means, 97.5))
    print(f"  Bootstrap SE: {se_bootstrap:.4f} (Wald SE: {se_wald:.4f})")
    print(f"  Bootstrap 95% CI: [{ci_bootstrap[0]:.4f}, {ci_bootstrap[1]:.4f}]")

    # Bootstrap for Negative Binomial parameters
    print("\nNegative Binomial bootstrap for churn data:")
    churn_data = stats.nbinom.rvs(n=2.0, p=0.4, size=200)  # mu=3, var=7.5
    r_ests, p_ests = [], []
    for _ in range(n_boot):
        boot_sample = np.random.choice(churn_data, size=len(churn_data), replace=True)
        m_b, v_b = np.mean(boot_sample), np.var(boot_sample, ddof=1)
        if v_b > m_b:
            r_ests.append(m_b ** 2 / (v_b - m_b))
            p_ests.append(m_b / v_b)
    r_est = np.mean(churn_data) ** 2 / (np.var(churn_data, ddof=1) - np.mean(churn_data))
    p_est = np.mean(churn_data) / np.var(churn_data, ddof=1)
    print(f"  Method of moments: r={r_est:.4f}, p={p_est:.4f}")
    print(f"  Bootstrap mean:    r={np.mean(r_ests):.4f} +- {np.std(r_ests, ddof=1):.4f}")
    print(f"  Bootstrap mean:    p={np.mean(p_ests):.4f} +- {np.std(p_ests, ddof=1):.4f}")
    print(f"  Bootstrap 95% CI r: [{np.percentile(r_ests, 2.5):.4f}, {np.percentile(r_ests, 97.5):.4f}]")
    print(f"  Bootstrap 95% CI p: [{np.percentile(p_ests, 2.5):.4f}, {np.percentile(p_ests, 97.5):.4f}]")


if __name__ == "__main__":
    mle_fitting_and_overdispersion()
    likelihood_ratio_and_wilks()
    confidence_intervals_and_bootstrap()
