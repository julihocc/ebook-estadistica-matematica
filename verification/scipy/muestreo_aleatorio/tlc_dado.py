"""Numeric cross-check for the fair-die CLT example in muestreo_aleatorio.tex.

Tier C: standardizing to Z-scores needs sqrt(Var(Xbar)), and the final
probability needs the standard normal CDF -- Mathlib has no computable Phi,
so this whole step is cross-checked numerically instead of in Lean.

Book claims (lines 55-73):
  mu = 3.5, sigma^2 = 35/12
  n = 36 -> Var(Xbar) = sigma^2/36 = 35/432
  Z1 = (3.0-3.5)/sqrt(Var(Xbar)) ~= -1.76, Z2 = (4.0-3.5)/sqrt(Var(Xbar)) ~= 1.76
  P(3.0 < Xbar < 4.0) = P(-1.76 < Z < 1.76) ~= 0.921
"""

import math
from scipy.stats import norm

mu = 3.5
sigma2 = 35 / 12
n = 36
var_xbar = sigma2 / n
se_xbar = math.sqrt(var_xbar)

z1 = (3.0 - mu) / se_xbar
z2 = (4.0 - mu) / se_xbar
prob = norm.cdf(z2) - norm.cdf(z1)

print(f"Var(Xbar) = {var_xbar:.6f} (book: 0.081)")
print(f"Z1 = {z1:.4f} (book: -1.76)")
print(f"Z2 = {z2:.4f} (book: 1.76)")
print(f"P(3.0 < Xbar < 4.0) = {prob:.4f} (book: ~=0.921)")

assert abs(z1 - (-1.76)) < 1e-2, "Z1 does not match the book's rounded value"
assert abs(z2 - 1.76) < 1e-2, "Z2 does not match the book's rounded value"
assert abs(prob - 0.921) < 1e-3, "final probability does not match the book's ~=0.921"
print("\nConfirmed: all values match the book within its own stated rounding.")
