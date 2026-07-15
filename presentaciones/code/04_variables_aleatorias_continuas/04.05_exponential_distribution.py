"""
Computational Lab: Section 04.05 - Exponential Distribution and Memoryless Processes
======================================================================================
Validates the Exponential PDF, demonstrates the memoryless property numerically,
computes the MLE lambda = 1/x_bar, derives the Erlang distribution as the sum of
i.i.d. exponentials, and applies the model to reliability systems in series.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import integrate, stats


def verify_pdf_and_memoryless_property():
    """Validates Exponential PDF normalization and memoryless property."""
    print("=== Block 1: PDF & Memoryless Property ===")
    # Exponential(2.0)
    lam = 2.0

    # Verify normalization
    result, error = integrate.quad(lambda x: lam * np.exp(-lam * x), 0, 50)
    print(f"Exponential(lambda={lam}) PDF integral: {result:.8f} (should be 1.0)")

    # Verify memoryless property: P(X > s + t | X > s) = P(X > t)
    print("\nMemoryless property verification (Exponential(2.0)):")
    print(f"  {'s':>5} | {'t':>5} | {'P(X>s+t|X>s)':>15} | {'P(X>t)':>10} | {'|diff|':>10}")
    print(f"  {'-'*5}-+-{'-'*5}-+-{'-'*15}-+-{'-'*10}-+-{'-'*10}")
    for s in [0.5, 1.0, 2.0]:
        for t in [0.3, 0.7, 1.5]:
            cond = stats.expon.sf(s + t, scale=1/lam) / stats.expon.sf(s, scale=1/lam)
            uncond = stats.expon.sf(t, scale=1/lam)
            print(f"  {s:>5.1f} | {t:>5.1f} | {cond:>15.6f} | {uncond:>10.6f} | {abs(cond - uncond):>10.2e}")

    # Compute moments by integration
    mean_num, _ = integrate.quad(lambda x: x * lam * np.exp(-lam * x), 0, 50)
    second_num, _ = integrate.quad(lambda x: x**2 * lam * np.exp(-lam * x), 0, 50)
    var_num = second_num - mean_num**2
    print(f"\nMoments by integration:")
    print(f"  E[X] = {mean_num:.6f} (theoretical: {1/lam:.6f})")
    print(f"  E[X^2] = {second_num:.6f} (theoretical: {2/lam**2:.6f})")
    print(f"  Var(X) = {var_num:.6f} (theoretical: {1/lam**2:.6f})")


def verify_mle_and_quantile_estimation():
    """MLE estimation and confidence intervals for Exponential parameter."""
    print("\n=== Block 2: MLE & Quantile Estimation ===")
    np.random.seed(42)
    n = 50
    true_lam = 2.0
    samples = np.random.exponential(1/true_lam, n)

    # MLE
    lambda_mle = 1.0 / np.mean(samples)
    print(f"True lambda: {true_lam:.4f}")
    print(f"  MLE estimate (1/x_bar): {lambda_mle:.4f}")
    print(f"  Sample mean x_bar: {np.mean(samples):.4f}")
    print(f"  1/x_bar = {1/np.mean(samples):.4f}")
    print(f"  1/s^2 = {1/np.var(samples, ddof=1):.4f} (incorrect for Exponential)")

    # Bootstrap confidence interval
    n_boot = 10_000
    boot_lambdas = np.array([1.0/np.mean(np.random.choice(samples, size=n, replace=True)) for _ in range(n_boot)])
    se_boot = np.std(boot_lambdas, ddof=1)
    ci_boot = (np.percentile(boot_lambdas, 2.5), np.percentile(boot_lambdas, 97.5))
    print(f"\nBootstrap (B={n_boot:,}):")
    print(f"  SE(lambda): {se_boot:.4f}")
    print(f"  95% CI: [{ci_boot[0]:.4f}, {ci_boot[1]:.4f}]")

    # Quantile estimates
    print(f"\nQuantile estimation:")
    for p in [0.10, 0.25, 0.50, 0.75, 0.90]:
        q_emp = np.quantile(samples, p)
        q_theo = stats.expon.ppf(p, scale=1/true_lam)
        q_mle = stats.expon.ppf(p, scale=1/lambda_mle)
        print(f"  q_{p}: empirical={q_emp:.4f}, theoretical (true)={q_theo:.4f}, MLE={q_mle:.4f}")

    # Verify large sample behavior: as n increases, MLE converges to true lambda
    print(f"\nConvergence of MLE with sample size:")
    for n_test in [10, 50, 200, 1000, 5000]:
        mle_test = 1.0 / np.mean(np.random.exponential(1/true_lam, n_test))
        print(f"  n={n_test:5d}: MLE = {mle_test:.4f}, |error| = {abs(mle_test - true_lam):.4f}")


def verify_erlang_and_reliability_systems():
    """Erlang distribution and reliability systems in series."""
    print("\n=== Block 3: Erlang Distribution & Reliability ===")
    # Erlang = Gamma(n, lambda) with integer shape
    n_comp = 5
    lam = 1.0

    # Verify sum of exponentials is Erlang
    np.random.seed(7)
    n_mc = 100_000
    samples_sum = np.sum(np.random.exponential(1/lam, (n_mc, n_comp)), axis=1)
    emp_mean = np.mean(samples_sum)
    emp_var = np.var(samples_sum, ddof=1)
    theo_mean = n_comp / lam
    theo_var = n_comp / lam**2
    print(f"Sum of {n_comp} i.i.d. Exp({lam}) = Erlang({n_comp}, {lam}):")
    print(f"  Empirical mean: {emp_mean:.4f} (theoretical: {theo_mean:.4f})")
    print(f"  Empirical var: {emp_var:.4f} (theoretical: {theo_var:.4f})")
    ks_erlang = stats.kstest(samples_sum, stats.gamma(a=n_comp, scale=1/lam).cdf)
    print(f"  KS test vs Gamma({n_comp}, {lam}): D={ks_erlang.statistic:.4f}, p={ks_erlang.pvalue:.4f}")

    # Reliability system: minimum of exponentials
    n_series = 10
    lam_comp = 0.001
    np.random.seed(11)
    samples_min = np.min(np.random.exponential(1/lam_comp, (n_mc, n_series)), axis=1)
    theo_rate = n_series * lam_comp
    print(f"\nReliability system ({n_series} components in series, lambda={lam_comp}):")
    print(f"  Empirical mean: {np.mean(samples_min):.4f} (theoretical: {1/theo_rate:.4f})")
    print(f"  Empirical P(T > 100): {np.mean(samples_min > 100):.4f} (theoretical: {np.exp(-theo_rate*100):.4f})")
    print(f"  Median: {np.median(samples_min):.4f} (theoretical: {np.log(2)/theo_rate:.4f})")
    print(f"  Effective rate: {theo_rate} failures/hour, MTTF: {1/theo_rate:.4f} hours")

    # M/M/1 queue system
    lam_arr = 5.0
    mu_serv = 6.0
    rho = lam_arr / mu_serv
    print(f"\nM/M/1 queue (lambda={lam_arr}, mu={mu_serv}):")
    print(f"  Traffic intensity: rho = {rho:.4f} (< 1: stable)")
    print(f"  P(system busy) = rho = {rho:.4f} ({rho*100:.1f}%)")
    print(f"  P(system idle) = 1 - rho = {1-rho:.4f} ({(1-rho)*100:.1f}%)")
    print(f"  Expected number in system: L = rho/(1-rho) = {rho/(1-rho):.4f}")
    print(f"  Expected waiting time: W = 1/(mu - lambda) = {1/(mu_serv - lam_arr):.4f} time units")


if __name__ == "__main__":
    verify_pdf_and_memoryless_property()
    verify_mle_and_quantile_estimation()
    verify_erlang_and_reliability_systems()
