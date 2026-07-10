from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# Distribuci\'on normal
mu, sigma = 70, 10
normalDist = stats.norm(mu, sigma)

# P(60 <= X <= 80)
p = normalDist.cdf(80) - normalDist.cdf(60)
print(f"P(60 <= X <= 80) = {p:.4f}")
##P(60 <= X <= 80) = 0.6827

# Cuantiles
print(f"Percentil 95: {normalDist.ppf(0.95):.2f}")  # ~86.45
##Percentil 95: 86.45

# Gr\'afica de la densidad con regiones sombreadas
fig, ax = plt.subplots(figsize=(10, 5))
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 500)
ax.plot(x, normalDist.pdf(x), 'b-', lw=2, label=f'N({mu},{sigma**2})')

# Sombrear regi\'on [\mu-\sigma, \mu+\sigma]
x_fill = np.linspace(mu-sigma, mu+sigma, 100)
ax.fill_between(x_fill, normalDist.pdf(x_fill), alpha=0.3, color='blue',
                label='~68.27%')
ax.fill_between(x, normalDist.pdf(x),
                where=((x>=mu-2*sigma)&(x<=mu+2*sigma))&~((x>=mu-sigma)&(x<=mu+sigma)),
                alpha=0.2, color='green', label='~95.45% total')

ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Distribuci\'on N(70, 100) con regla 68-95-99.7')
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('pe/distNormalContinua.png', dpi=100, bbox_inches='tight')
plt.show()
