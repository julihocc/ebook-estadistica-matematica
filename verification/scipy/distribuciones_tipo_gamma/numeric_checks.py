"""Numeric cross-check for distribuciones_tipo_gamma.tex and (p).tex.

Tier C: decimal evaluations needing e^x, not attempted in Lean.
"""

from math import exp

# exmp:2.8.3 -- T ~ Gamma(3, 1/3) (Erlang), P(T>1.5)
p_gt = exp(-4.5) * 15.625
print(f"P(T>1.5) = e^-4.5 * 15.625 = {p_gt:.4f} (book: 0.174)")
assert abs(p_gt - 0.174) < 1e-3

# exmp:2.8.8 -- Weibull(2,5), F(3)
F3 = 1 - exp(-0.36)
print(f"F(3) = 1-e^-0.36 = {F3:.4f} (book: 0.3023)")
assert abs(F3 - 0.3023) < 1e-4

print("\nConfirmed: all decimal values in this chapter match the book.")
