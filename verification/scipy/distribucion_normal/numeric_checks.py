"""Numeric cross-check for distribucion_normal.tex and (p).tex.

Tier C: standard normal CDF Phi values, irrational, not attempted in
Lean (Mathlib's Gaussian-distribution package is blocked by MAX_PATH in
this worktree -- see DistribucionNormal.lean's doc comment).
"""

from scipy.stats import norm

# Theory: empirical 68-95-99.7 rule
for k, expected in [(1, 0.6827), (2, 0.9545), (3, 0.9973)]:
    val = norm.cdf(k) - norm.cdf(-k)
    print(f"P(mu-{k}s<=X<=mu+{k}s) = {val:.4f} (book: {expected})")
    assert abs(val - expected) < 1e-4

# exmp:2.8.2 -- N(70,100), P(60<=X<=80) = Phi(1)-Phi(-1)
phi1 = norm.cdf(1)
phi_neg1 = norm.cdf(-1)
print(f"\nPhi(1) = {phi1:.4f} (book: 0.8413)")
print(f"Phi(-1) = {phi_neg1:.4f} (book: 0.1587)")
print(f"Phi(1)-Phi(-1) = {phi1 - phi_neg1:.4f} (book: 0.6827)")
assert abs(phi1 - 0.8413) < 1e-4
assert abs(phi_neg1 - 0.1587) < 1e-4
assert abs((phi1 - phi_neg1) - 0.6827) < 1e-4

# prob:48f2103 -- N(170,100)
p_gt_185 = 1 - norm.cdf(1.5)
p_between = norm.cdf(1) - norm.cdf(-1)
print(f"\nP(X>185) = 1-Phi(1.5) = {p_gt_185:.4f} (book: 0.0668)")
print(f"P(160<=X<=180) = {p_between:.4f} (book: 0.6827)")
assert abs(p_gt_185 - 0.0668) < 1e-4
assert abs(p_between - 0.6827) < 1e-4

# prob:1c4fda2 -- N(0.150, 0.0004), P(X<0.100) = Phi(-2.5)
p_false_start = norm.cdf(-2.5)
print(f"\nP(X<0.100) = Phi(-2.5) = {p_false_start:.4f} (book: 0.0062)")
assert abs(p_false_start - 0.0062) < 1e-4

print("\nConfirmed: all decimal values in this chapter match the book.")
