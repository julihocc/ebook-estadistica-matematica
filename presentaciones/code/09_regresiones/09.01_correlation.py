"""
Computational Lab: Section 09.01 - Correlation as the Premise of Regression
====================================================================
Computes the Pearson correlation coefficient from its raw definition and
verifies it against numpy, demonstrates its bounded range and the meaning
of sign/magnitude across datasets of varying association strength, and
illustrates the "correlation does not imply causation" warning via a
confounding-variable example resolved through partial correlation.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np


def pearson_correlation_from_definition():
    """Computes r from its raw sum-of-deviations definition and checks it against numpy."""
    print("=== Block 1: Pearson Correlation from Its Definition ===")
    rng = np.random.default_rng(seed=3)
    tv = rng.uniform(10, 300, 40)
    sales = 3.0 + 0.05 * tv + rng.normal(scale=2.0, size=40)

    x_bar, y_bar = tv.mean(), sales.mean()
    sxy = np.sum((tv - x_bar) * (sales - y_bar))
    sxx = np.sum((tv - x_bar) ** 2)
    syy = np.sum((sales - y_bar) ** 2)
    r = sxy / np.sqrt(sxx * syy)

    print(f"r (from definition) = {r:.4f}")
    print(f"np.corrcoef check    = {np.corrcoef(tv, sales)[0, 1]:.4f}")


def correlation_range_and_strength():
    """Shows r is bounded in [-1, 1] and how magnitude/sign reflect association strength."""
    print("\n=== Block 2: Range and Strength of the Correlation Coefficient ===")
    rng = np.random.default_rng(seed=7)
    n = 200
    x = rng.normal(size=n)

    scenarios = {
        "perfect positive (y=2x)": 2 * x,
        "strong positive (noisy)": 2 * x + rng.normal(scale=0.5, size=n),
        "weak positive (noisy)": 2 * x + rng.normal(scale=5.0, size=n),
        "no relationship": rng.normal(size=n),
        "strong negative (noisy)": -2 * x + rng.normal(scale=0.5, size=n),
        "perfect negative (y=-2x)": -2 * x,
    }
    for label, y in scenarios.items():
        r = np.corrcoef(x, y)[0, 1]
        print(f"{label:28s}: r = {r:+.4f}")


def correlation_is_not_causation():
    """Classic confounder demo: shoe size vs. vocabulary, both driven by age."""
    print("\n=== Block 3: Correlation Does Not Imply Causation ===")
    rng = np.random.default_rng(seed=11)
    n = 150
    age = rng.uniform(2, 18, n)
    shoe_size = 12.0 + 0.7 * age + rng.normal(scale=1.0, size=n)
    vocabulary = 200.0 + 350.0 * age + rng.normal(scale=300.0, size=n)

    r_raw = np.corrcoef(shoe_size, vocabulary)[0, 1]
    print(f"Raw correlation(shoe size, vocabulary) = {r_raw:.4f}  <- spurious, driven by age")

    r_sv = np.corrcoef(shoe_size, vocabulary)[0, 1]
    r_sa = np.corrcoef(shoe_size, age)[0, 1]
    r_va = np.corrcoef(vocabulary, age)[0, 1]
    partial_r = (r_sv - r_sa * r_va) / np.sqrt((1 - r_sa ** 2) * (1 - r_va ** 2))
    print(f"Partial correlation(shoe size, vocabulary | age) = {partial_r:.4f}")
    print("Controlling for age collapses the association: shoe size does not")
    print("cause vocabulary growth; both are driven by the lurking variable age.")


if __name__ == "__main__":
    pearson_correlation_from_definition()
    correlation_range_and_strength()
    correlation_is_not_causation()
