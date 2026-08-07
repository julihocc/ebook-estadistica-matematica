"""Numeric cross-check for prob:7cf587b (distribucion_hipergeometrica(p).tex).

Tier C: C(2000,20)-scale binomial coefficients time out in Lean's
norm_num [Nat.choose] unfolding (deterministic timeout at maxHeartbeats,
confirmed even after raising maxRecDepth) -- not infeasible in principle,
just too slow to grind through in this environment. Cross-checked here with
exact rational arithmetic (fractions.Fraction, not floating point) before
being logged as a finding.

Book claims: N=2000, K=100, n=20, P(X=2) (hypergeometric) approx 0.189725.

Finding: the correct value is approx 0.189525 -- the book's stated 0.189725
looks like a digit transposition (0.189"5"25 vs 0.189"7"25). The binomial
approximation P(Y=2) approx 0.188677 DOES match the book exactly.
"""

from fractions import Fraction
from math import comb

N, K, n, k = 2000, 100, 20, 2

PX2_exact = Fraction(comb(K, k) * comb(N - K, n - k), comb(N, n))
PX2 = float(PX2_exact)

p = K / N
PY2 = comb(n, k) * p**k * (1 - p) ** (n - k)

print(f"P(X=2) hypergeometric exact = {PX2:.6f} (book claims 0.189725)")
print(f"P(Y=2) binomial approx      = {PY2:.6f} (book claims 0.188677)")
print(f"|PX2 - PY2|                 = {abs(PX2 - PY2):.6f} (book claims 0.00105)")

assert abs(PY2 - 0.188677) < 1e-6, "P(Y=2) does not match the book"
assert abs(PX2 - 0.189725) > 1e-4, "expected the book's P(X=2) to be wrong"
assert abs(PX2 - 0.189525) < 1e-6, "corrected P(X=2) does not match 0.189525"
print("\nConfirmed: book's P(X=2)=0.189725 is off; correct value is 0.189525.")
