import numpy as np
from scipy import stats

# A/B testing
n_A, x_A = 1000, 120
n_B, x_B = 1000, 145
p_A = x_A / n_A
p_B = x_B / n_B
p_pool = (x_A + x_B) / (n_A + n_B)
se = np.sqrt(p_pool * (1 - p_pool) * (1/n_A + 1/n_B))
Z = (p_B - p_A) / se
p_valor = 2 * (1 - stats.norm.cdf(abs(Z)))
print(f"p_A = {p_A:.4f}, p_B = {p_B:.4f}")
print(f"Z = {Z:.3f}, p-valor = {p_valor:.4f}")
##p_A = 0.1200, p_B = 0.1450
##Z = 1.650, p-valor = 0.0989

# Bootstrap como alternativa no param\'etrica
np.random.seed(42)
boot_diffs = []
for _ in range(10000):
    boot_A = np.random.binomial(n_A, p_A) / n_A
    boot_B = np.random.binomial(n_B, p_B) / n_B
    boot_diffs.append(boot_B - boot_A)
ci = np.percentile(boot_diffs, [2.5, 97.5])
print(f"IC 95% bootstrap para p_B - p_A: [{ci[0]:.4f}, {ci[1]:.4f}]")
##IC 95% bootstrap para p_B - p_A: [-0.0002, 0.0498]
