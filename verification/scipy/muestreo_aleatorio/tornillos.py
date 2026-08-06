"""Numeric cross-check for prob:b7567ec (muestreo_aleatorio(p).tex).

Tier C: the final probability needs Phi(1.6), the standard normal CDF, which
Mathlib does not provide as a computable function.

Book claims: mu=10mm, sigma=0.5mm, n=64, SE=0.0625mm, z1=-1.6, z2=1.6,
P(9.9 < Xbar < 10.1) = 2*Phi(1.6) - 1 = 2*0.9452 - 1 = 0.8904 (89.04%).
"""

from scipy.stats import norm

z = 1.6
phi_1_6 = norm.cdf(z)
prob = 2 * phi_1_6 - 1

print(f"Phi(1.6) = {phi_1_6:.4f} (book: 0.9452)")
print(f"P(9.9 < Xbar < 10.1) = 2*Phi(1.6)-1 = {prob:.4f} (book: 0.8904)")

assert abs(phi_1_6 - 0.9452) < 1e-3, "Phi(1.6) does not match the book's stated value"
assert abs(prob - 0.8904) < 1e-3, "final probability does not match the book's 0.8904"
print("\nConfirmed: matches the book within its own stated rounding.")
