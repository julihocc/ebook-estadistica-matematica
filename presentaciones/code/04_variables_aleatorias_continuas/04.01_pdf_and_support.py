"""
Computational Lab: Section 04.01 - PDF and Continuous Support
==============================================================
Validates the Probability Density Function (PDF) normalization property,
computes the Cumulative Distribution Function (CDF) and interval probabilities
via numerical integration, and verifies the continuous LOTUS theorem for
expectation and variance calculation.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import integrate, stats


# ---------- Module-level PDF definitions ----------
def exp_pdf(x, lam=0.5):
    """Exponential PDF with rate lam; support x >= 0."""
    return lam * np.exp(-lam * x) * (x >= 0)


def rayleigh_pdf(x, sigma=1.0):
    """Rayleigh PDF with scale sigma; support x >= 0."""
    return (x / sigma**2) * np.exp(-x**2 / (2 * sigma**2)) * (x >= 0)


def custom_quadratic_pdf(x):
    """Quadratic PDF (3/10)(2 - x^2) on [-1, 1]."""
    return (3.0 / 10.0) * (2.0 - x**2) * (np.abs(x) <= 1.0)


def verify_pdf_and_normalization():
    """Validates PDF normalization, support, and integral = 1 property."""
    print("=== Block 1: PDF Validation & Normalization ===")
    integrals = {}
    for name, pdf, bounds in [
        ("Exponential(0.5)", lambda x: exp_pdf(x, lam=0.5), (0, 50)),
        ("Rayleigh(1.0)", rayleigh_pdf, (0, 30)),
        ("Quadratic(3/10)", custom_quadratic_pdf, (-1, 1))
    ]:
        result, error = integrate.quad(pdf, bounds[0], bounds[1])
        integrals[name] = result
        print(f"  {name:25s}: integral = {result:.8f} (error est. = {error:.2e})")

    # Verify Rayleigh PDF by checking against scipy.stats.rayleigh
    scipy_rayleigh_int, _ = integrate.quad(stats.rayleigh.pdf, 0, 30)
    print(f"\n  SciPy Rayleigh verification: integral = {scipy_rayleigh_int:.8f}")
    print(f"  Match with manual implementation: {abs(scipy_rayleigh_int - 1.0) < 1e-6}")

    # Continuous support check
    print("\n  Support analysis:")
    print("  Exponential(0.5):    support = [0, infinity) (right-unbounded)")
    print("  Rayleigh(1.0):       support = [0, infinity) (right-unbounded)")
    print("  Quadratic(3/10):     support = [-1, 1] (bounded, symmetric)")


def verify_cdf_and_interval_probabilities():
    """Computes CDFs and interval probabilities for various continuous distributions."""
    print("\n=== Block 2: CDF Computation & Interval Probabilities ===")
    lam = 0.5
    print("Exponential(0.5) CDF and interval probabilities:")

    def exp_cdf(x):
        return 1.0 - np.exp(-lam * x)

    test_points = [0.5, 1.0, 2.0, 5.0]
    for x in test_points:
        cdf_exact = exp_cdf(x)
        cdf_numerical, _ = integrate.quad(lambda t: exp_pdf(t, lam), 0, x)
        print(f"  F({x:.1f}) exact={cdf_exact:.6f}, numerical={cdf_numerical:.6f}, "
              f"diff={abs(cdf_exact - cdf_numerical):.2e}")

    # Interval probability P(a <= X <= b) for Exponential(0.5)
    print("\nInterval probabilities for Exponential(0.5):")
    intervals = [(0, 1), (1, 3), (2, 5), (0, 10)]
    for a, b in intervals:
        p_exact = exp_cdf(b) - exp_cdf(a)
        p_numerical, _ = integrate.quad(lambda t: exp_pdf(t, lam), a, b)
        print(f"  P({a} <= X <= {b}) = exact={p_exact:.6f}, numerical={p_numerical:.6f}")

    # Rayleigh distribution
    print("\nRayleigh(1.0) CDF at key points:")
    for x in [0.5, 1.0, 2.0, 3.0]:
        cdf_rayleigh, _ = integrate.quad(lambda t: rayleigh_pdf(t, 1.0), 0, x)
        cdf_scipy = stats.rayleigh.cdf(x)
        print(f"  F({x:.1f}) numerical={cdf_rayleigh:.6f}, scipy={cdf_scipy:.6f}, "
              f"diff={abs(cdf_rayleigh - cdf_scipy):.2e}")

    # Quadratic distribution
    print("\nQuadratic(3/10) on [-1,1] CDF at key points:")
    for x in [-0.5, 0.0, 0.5, 1.0]:
        cdf_quad, _ = integrate.quad(lambda t: custom_quadratic_pdf(t), -1, x)
        print(f"  F({x:.1f}) numerical={cdf_quad:.6f}")


def verify_continuous_lotus_and_moments():
    """Verifies continuous LOTUS theorem and computes moments via integration."""
    print("\n=== Block 3: Continuous LOTUS & Moments ===")
    # Exponential(0.5): E[X] = 1/lam = 2, Var(X) = 1/lam^2 = 4
    lam = 0.5

    # E[X] via LOTUS
    mean_numerical, _ = integrate.quad(lambda x: x * exp_pdf(x, lam), 0, 100)
    mean_closed_form = 1.0 / lam
    print(f"Exponential(0.5):")
    print(f"  E[X] numerical = {mean_numerical:.6f}")
    print(f"  E[X] closed form = {mean_closed_form:.6f}")

    # E[X^2] via LOTUS
    second_moment, _ = integrate.quad(lambda x: x**2 * exp_pdf(x, lam), 0, 100)
    var_numerical = second_moment - mean_numerical**2
    var_closed_form = 1.0 / lam**2
    print(f"  E[X^2] numerical = {second_moment:.6f}")
    print(f"  Var(X) numerical = {var_numerical:.6f}")
    print(f"  Var(X) closed form = {var_closed_form:.6f}")

    # Rayleigh(1.0): E[X] = sigma*sqrt(pi/2), Var(X) = (4-pi)/2 * sigma^2
    sigma = 1.0
    print(f"\nRayleigh({sigma}):")
    mean_rayleigh, _ = integrate.quad(lambda x: x * rayleigh_pdf(x, sigma), 0, 30)
    mean_rayleigh_cf = sigma * np.sqrt(np.pi / 2)
    print(f"  E[X] numerical = {mean_rayleigh:.6f}, closed form = {mean_rayleigh_cf:.6f}")

    second_moment_r, _ = integrate.quad(lambda x: x**2 * rayleigh_pdf(x, sigma), 0, 30)
    var_rayleigh = second_moment_r - mean_rayleigh**2
    var_rayleigh_cf = (4 - np.pi) / 2 * sigma**2
    print(f"  Var(X) numerical = {var_rayleigh:.6f}, closed form = {var_rayleigh_cf:.6f}")

    # Verify LOTUS for a nonlinear function: E[sqrt(X)] for Exponential(0.5)
    print("\nLOTUS verification: E[sqrt(X)] for Exponential(0.5):")
    e_sqrt_x, _ = integrate.quad(lambda x: np.sqrt(x) * exp_pdf(x, lam), 0, 100)
    exp_dist = stats.expon(scale=1.0/lam)
    e_sqrt_x_scipy = exp_dist.expect(func=np.sqrt)
    print(f"  E[sqrt(X)] numerical = {e_sqrt_x:.6f}")
    print(f"  E[sqrt(X)] SciPy = {e_sqrt_x_scipy:.6f}")
    print(f"  Match: {abs(e_sqrt_x - e_sqrt_x_scipy) < 1e-4}")


if __name__ == "__main__":
    verify_pdf_and_normalization()
    verify_cdf_and_interval_probabilities()
    verify_continuous_lotus_and_moments()
