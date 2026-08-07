"""Numeric cross-check for prob:5e9408a (distribucion_poisson(p).tex).

Tier C: needs a Poisson(200) tail sum to k=220 (feasible in principle in
Lean but not attempted here, matching this chapter's Tier D scoping for
Poisson moments) plus the normal CDF, which Mathlib has no computable
version of.

Book claims: S_100 ~ Pois(200), P(S_100<=220) exact approx 0.9862;
normal approx with continuity correction Phi((220.5-200)/sqrt(200)) =
Phi(1.4496) approx 0.9265; absolute error approx 0.06 (used by the book to
argue the normal approximation is poor in the tail here).

FINDING: the book's "exact" Poisson value (0.9862) is wrong. The z-score
(1.4496) and the normal-approximation value (0.9265) it also states ARE
correct (both match scipy below) -- only the claimed exact Poisson CDF is
off. The true exact value is ~0.9247, essentially identical to the normal
approximation (difference ~0.0017, not ~0.06). This inverts the book's own
pedagogical point: the normal approximation is in fact excellent here, not
poor -- the "considerable tail error" conclusion does not hold once the
exact value is computed correctly.
"""

from math import sqrt

from scipy.stats import norm, poisson

lam = 200
exact = poisson.cdf(220, lam)

z = (220.5 - lam) / sqrt(lam)
normal_approx = norm.cdf(z)

print(f"P(S_100<=220) exact (Poisson)       = {exact:.4f} (book claims 0.9862)")
print(f"z = (220.5-200)/sqrt(200)           = {z:.4f} (book: 1.4496, correct)")
print(f"P(S_100<=220) normal approx         = {normal_approx:.4f} (book: 0.9265, correct)")
print(f"|exact - normal_approx|             = {abs(exact - normal_approx):.4f} (book claims ~0.06)")

assert abs(z - 1.4496) < 1e-3, "z-score does not match the book"
assert abs(normal_approx - 0.9265) < 1e-3, "normal approximation does not match the book"
assert abs(exact - 0.9862) > 1e-2, "expected the book's 'exact' Poisson CDF to be wrong"
assert abs(exact - 0.9247) < 1e-3, "corrected exact Poisson CDF should be ~0.9247"
print("\nConfirmed: book's 'exact' P(S_100<=220)=0.9862 is wrong; true value is ~0.9247,")
print("essentially equal to the normal approximation -- the book's conclusion that the")
print("normal approximation is poor in this tail does not hold.")
