"""Numeric cross-check for distribucion_muestral_t.tex and (p).tex.

Tier C: Student-t quantiles, not expressible/verifiable in elementary
closed form, not attempted in Lean.
"""

from scipy.stats import t as student_t, norm

checks = [
    (9, 0.975, 2.262),
    (8, 0.975, 2.306),
    (4, 0.975, 2.776),
    (19, 0.975, 2.093),
    (5, 0.975, 2.571),
]
for df, q, expected in checks:
    val = student_t.ppf(q, df)
    print(f"t_({df},{1-q}) = {val:.3f} (book: {expected})")
    assert abs(val - expected) < 5e-3

z = norm.ppf(0.975)
print(f"z_0.025 = {z:.4f} (book: 1.96)")
assert abs(z - 1.96) < 5e-3

print("\nConfirmed: all t/z critical values in this chapter match the book.")
