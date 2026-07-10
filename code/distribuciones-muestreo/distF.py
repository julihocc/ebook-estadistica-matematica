import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Distribuci\'on F con varios grados de libertad
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Panel izquierdo: variando d_1 (d_2 fijo)
x = np.linspace(0.01, 5, 500)
for d1, d2 in [(2, 10), (5, 10), (10, 10), (20, 10)]:
    f_dist = stats.f(d1, d2)
    axes[0].plot(x, f_dist.pdf(x), lw=2, label=f'F({d1},{d2})')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].set_title('Distribuci\'on F (variando d1, d2=10)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Panel derecho: ANOVA con 3 grupos
np.random.seed(42)
g1 = np.random.normal(86.6, 4.9, 5)  # m\'etodo A
g2 = np.random.normal(81.0, 3.2, 5)  # m\'etodo B
g3 = np.random.normal(91.6, 2.4, 5)  # m\'etodo C

# F-test usando scipy
f_stat, p_value = stats.f_oneway(g1, g2, g3)
print(f"F = {f_stat:.3f}, p-valor = {p_value:.4f}")
##F = 9.539, p-valor = 0.0034

# Cr\'itico
f_crit = stats.f.ppf(0.95, 2, 12)
print(f"Valor cr\'itico F(0.05, 2, 12) = {f_crit:.3f}")
##Valor cr\'itico F(0.05, 2, 12) = 3.885

# Histograma de F bajo H0
F_samples = [stats.f.rvs(2, 12) for _ in range(10000)]
axes[1].hist(F_samples, bins=50, density=True, alpha=0.5, label='F(2,12) bajo H0')
axes[1].axvline(f_stat, color='red', lw=2, label=f'Estad\'istico observado = {f_stat:.2f}')
axes[1].axvline(f_crit, color='black', lw=2, linestyle='--', label=f'Cr\'itico = {f_crit:.2f}')
axes[1].set_xlabel('F')
axes[1].set_ylabel('Densidad')
axes[1].set_title('Prueba F en ANOVA')
axes[1].legend()
axes[1].grid(True, alpha=0.3)
axes[1].set_xlim(0, 10)

plt.tight_layout()
plt.savefig('pe/distF.png', dpi=100, bbox_inches='tight')
plt.show()
