"""Numeric cross-check for prob:14b3125 and prob:61a9dd8
(variables_aleatorias_continuas(p).tex).

Tier C: decimal evaluations needing e^x / ln x, irrational; the exact
symbolic forms (e^-1 - e^-3, 5*ln10, -5*ln0.05) were proved exactly in
Lean (VariablesAleatoriasContinuasProblemas.lean); this script only
confirms the book's stated decimal roundings.
"""

from math import exp, log

# prob:14b3125
p_1_le_X_le_3 = exp(-1) - exp(-3)
print(f"P(1<=X<=3) = e^-1 - e^-3 = {p_1_le_X_le_3:.4f} (book: 0.3181)")
assert abs(p_1_le_X_le_3 - 0.3181) < 1e-4

# prob:61a9dd8
p_X_le_3 = 1 - exp(-0.6)
p_X_ge_10 = exp(-2)
q90 = 5 * log(10)
t95 = -5 * log(0.05)
print(f"P(X<=3) = 1-e^-0.6 = {p_X_le_3:.4f} (book: 0.4512)")
print(f"P(X>=10) = e^-2 = {p_X_ge_10:.4f} (book: 0.1353)")
print(f"q_0.90 = 5*ln(10) = {q90:.2f} (book: 11.51)")
print(f"t (95%) = -5*ln(0.05) = {t95:.2f} (book: 14.98)")

assert abs(p_X_le_3 - 0.4512) < 1e-4
assert abs(p_X_ge_10 - 0.1353) < 1e-4
assert abs(q90 - 11.51) < 1e-2
assert abs(t95 - 14.98) < 1e-2
print("\nConfirmed: all decimal values match the book within its own stated rounding.")
