"""Numeric cross-check for distribucion_muestral_chi_cuadrada.tex and (p).tex.

Tier C: chi-squared quantiles, not expressible/verifiable in elementary
closed form, not attempted in Lean.
"""

from scipy.stats import chi2

checks = [
    (9, 0.95, 16.92),
    (15, 0.95, 24.996),
    (20, 0.95, 31.410),
]
for df, q, expected in checks:
    val = chi2.ppf(q, df)
    print(f"chi2_({df},{q}) = {val:.3f} (book: {expected})")
    assert abs(val - expected) < 5e-3

print("\nConfirmed: all chi-squared critical values in this chapter match the book.")
