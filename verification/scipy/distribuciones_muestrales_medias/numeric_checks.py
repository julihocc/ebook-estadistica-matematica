"""Numeric cross-check for distribuciones_muestrales_medias.tex and (p).tex.

Tier C: standard normal CDF Phi values, irrational.
"""

from scipy.stats import norm

# exmp:5.2.1
p1 = 1 - norm.cdf(1)
print(f"P(Z>1) = 1-Phi(1) = {p1:.4f} (book: 0.1587)")
assert abs(p1 - 0.1587) < 1e-4

# prob:6815de7
p2 = 1 - norm.cdf(5 / 3)
print(f"P(Z>5/3) = {p2:.4f} (book: 1-0.9522=0.0478)")
assert abs((1 - p2) - 0.9522) < 1e-3
assert abs(p2 - 0.0478) < 1e-3

# prob:2e2f544
p3 = 1 - norm.cdf(2)
print(f"P(Z>2) = {p3:.4f} (book: 1-0.9772=0.0228)")
assert abs((1 - p3) - 0.9772) < 1e-3
assert abs(p3 - 0.0228) < 1e-3

print("\nConfirmed: all decimal values in this chapter match the book.")
