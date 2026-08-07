"""Numeric cross-check for distribucion_muestral_f.tex and (p).tex.

Tier C: F-distribution quantiles, not expressible/verifiable in
elementary closed form, not attempted in Lean.

Also independently re-derives the exmp:3.2.6 ANOVA finding via
fractions.Fraction, matching the check already done inline before
writing the Lean theorem (kept here as a permanent, re-runnable record).
"""

from fractions import Fraction as F

from scipy.stats import f as f_dist

# F-quantile table values used in the chapter
checks = [
    (2, 12, 0.95, 3.89),
    (12, 10, 0.975, 3.62),
    (14, 11, 0.975, 3.36),
    (9, 7, 0.975, 4.82),
]
for d1, d2, q, expected in checks:
    val = f_dist.ppf(q, d1, d2)
    print(f"F_({d1},{d2},{1-q if q>0.5 else q}) = {val:.3f} (book: {expected})")
    assert abs(val - expected) < 5e-3

# exmp:3.2.6 -- ANOVA worked example, exact rational re-derivation
A = [F(85), F(90), F(78), F(92), F(88)]
B = [F(79), F(81), F(85), F(77), F(83)]
C = [F(92), F(95), F(88), F(90), F(93)]


def mean(xs):
    return sum(xs) / len(xs)


def ss(xs, m):
    return sum((x - m) ** 2 for x in xs)


mA, mB, mC = mean(A), mean(B), mean(C)
grand = (mA + mB + mC) / 3
sc_trat = 5 * (mA - grand) ** 2 + 5 * (mB - grand) ** 2 + 5 * (mC - grand) ** 2
ssA, ssB, ssC = ss(A, mA), ss(B, mB), ss(C, mC)
sc_error = ssA + ssB + ssC
F_stat = (sc_trat / 2) / (sc_error / 12)

print(f"\nSC_trat = {sc_trat} = {float(sc_trat)} (book: 290.0)")
print(f"Method C within-group SS = {ssC} = {float(ssC)} (book: 23.2)")
print(f"SC_error = {sc_error} = {float(sc_error)} (book: 182.4)")
print(f"F statistic = {float(F_stat):.4f} (book: 9.54)")

assert sc_trat == F(1406, 5)
assert ssC == F(146, 5)
assert sc_error == F(942, 5)
assert abs(float(F_stat) - 8.9554) < 1e-3
assert abs(float(sc_trat) - 290.0) > 1
assert abs(float(ssC) - 23.2) > 1

print("\nConfirmed: exmp:3.2.6 has two genuine arithmetic errors (SC_trat, Method C SS);")
print("the qualitative conclusion (reject H0) survives both errors since the corrected")
print("F statistic (8.955) still exceeds the critical value (3.89).")
