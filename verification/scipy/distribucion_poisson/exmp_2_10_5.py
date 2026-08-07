"""Numeric cross-check for exmp:2.10.5 / prob:8fd3390 (distribucion_poisson.tex).

Tier C: the final decimal values need e^-5, irrational; Mathlib has no
computable exp evaluation to a fixed precision usable in norm_num here.

Book claims: lambda=5, P(X<=3) approx 0.265, P(X>=8) = 1 - P(X<=7) approx
1 - 0.867 = 0.133.
"""

from scipy.stats import poisson

lam = 5
p_le_3 = poisson.cdf(3, lam)
p_le_7 = poisson.cdf(7, lam)
p_ge_8 = 1 - p_le_7

print(f"P(X<=3) = {p_le_3:.4f} (book: 0.265)")
print(f"P(X<=7) = {p_le_7:.4f} (book: 0.867)")
print(f"P(X>=8) = 1 - P(X<=7) = {p_ge_8:.4f} (book: 0.133)")

assert abs(p_le_3 - 0.265) < 1e-3, "P(X<=3) does not match the book"
assert abs(p_le_7 - 0.867) < 1e-3, "P(X<=7) does not match the book"
assert abs(p_ge_8 - 0.133) < 1e-3, "P(X>=8) does not match the book"
print("\nConfirmed: matches the book within its own stated rounding.")
