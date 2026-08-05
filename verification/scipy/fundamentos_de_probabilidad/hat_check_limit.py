"""Numeric cross-check for prob:a4ff50c (fundamentos_de_probabilidad(p).tex).

The book claims:
  P(at least one guest gets their own hat) = sum_{k=1}^n (-1)^(k-1) / k!
and that this converges to 1 - e^-1 ~= 0.63212, stabilizing "from n >= 6".

Lean (FundamentosProbabilidadProblemas.prob_a4ff50c_n3) checks the formula
exactly for n=3 via direct permutation counting -- an infinite-series limit
argument is out of reasonable scope for this pilot's Lean effort (Tier D),
so the limiting claim is cross-checked numerically here instead.
"""

import math

target = 1 - math.exp(-1)

print(f"1 - e^-1 = {target:.6f}\n")
print(f"{'n':>3} | {'partial sum':>12} | {'abs diff from 1-e^-1':>20}")
for n in range(1, 15):
    partial = sum((-1) ** (k - 1) / math.factorial(k) for k in range(1, n + 1))
    print(f"{n:>3} | {partial:>12.6f} | {abs(partial - target):>20.2e}")

# Book's specific claim: convergence has "stabilized" by n = 6.
partial_6 = sum((-1) ** (k - 1) / math.factorial(k) for k in range(1, 7))
assert abs(partial_6 - target) < 1e-3, "book's n=6 stabilization claim does not hold numerically"
print("\nConfirmed: partial sum at n=6 matches 1-e^-1 to within 1e-3, "
      "consistent with the book's claim.")
