"""Numeric cross-check for prob:f43c638 and prob:9d4a41b
(esperanza_matematica(p).tex).

Tier C: exponential moments via improper integrals (integration by parts),
not attempted in Lean this chapter (would need Gamma-function machinery on
top of everything else already formalized). The exact rational values
(E[X]=2, E[X^2]=8, Var=4 for lambda=0.5; skewness/kurtosis for Exp(1)) are
also hand-derivable via E[X^n]=n!/lambda^n for Exp(lambda) -- confirmed
here numerically via integration.
"""

from scipy import integrate
from scipy.stats import expon

# prob:f43c638 -- X ~ Exp(lambda=0.5), i.e. scale = 1/lambda = 2
lam = 0.5
rv = expon(scale=1 / lam)
EX = rv.mean()
EX2 = rv.moment(2)
Var = rv.var()
print(f"E[X] = {EX} (book: 2 = 1/lambda)")
print(f"E[X^2] = {EX2} (book: 8; book mislabels this '=1/lambda^2'=4, correct label is 2/lambda^2=8)")
print(f"Var(X) = {Var} (book: 4 = 1/lambda^2)")
assert abs(EX - 2) < 1e-9
assert abs(EX2 - 8) < 1e-9
assert abs(Var - 4) < 1e-9
assert abs(2 / lam**2 - 8) < 1e-9  # the correct formula for E[X^2]
assert abs(1 / lam**2 - 4) < 1e-9  # 1/lambda^2 is Var, not E[X^2]

# prob:9d4a41b -- X ~ Exp(lambda=1)
rv1 = expon(scale=1)
mu, sigma = rv1.mean(), rv1.std()
m3 = integrate.quad(lambda x: (x - mu) ** 3 * rv1.pdf(x), 0, 100)[0]
m4 = integrate.quad(lambda x: (x - mu) ** 4 * rv1.pdf(x), 0, 100)[0]
gamma1 = m3 / sigma**3
gamma2 = m4 / sigma**4 - 3
print(f"\nE[(X-mu)^3] = {m3:.4f} (book: 2)")
print(f"E[(X-mu)^4] = {m4:.4f} (book: 9)")
print(f"gamma1 (skewness) = {gamma1:.4f} (book: 2)")
print(f"gamma2 (excess kurtosis) = {gamma2:.4f} (book: 6)")
assert abs(m3 - 2) < 1e-3
assert abs(m4 - 9) < 1e-3
assert abs(gamma1 - 2) < 1e-3
assert abs(gamma2 - 6) < 1e-3
print("\nConfirmed: all prob:9d4a41b values match the book exactly.")
