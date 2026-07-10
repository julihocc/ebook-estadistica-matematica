import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Ejemplo: distribuci\'on log-normal
np.random.seed(0)
mu, sigma = 0, 0.5
X = np.random.normal(mu, sigma, size=10000)
Y = np.exp(X)  # transformaci\'on

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].hist(X, bins=50, density=True, alpha=0.7, color='steelblue')
x_norm = np.linspace(-3, 3, 100)
axes[0].plot(x_norm, stats.norm.pdf(x_norm, mu, sigma), 'r-', lw=2)
axes[0].set_title('X ~ N(0, 0.5) (normal)')
axes[0].set_xlabel('x')

axes[1].hist(Y, bins=50, density=True, alpha=0.7, color='coral')
y_grid = np.linspace(0.01, 5, 100)
lognorm_pdf = stats.lognorm.pdf(y_grid, s=sigma, scale=np.exp(mu))
axes[1].plot(y_grid, lognorm_pdf, 'r-', lw=2)
axes[1].set_title('Y = exp(X) (log-normal)')
axes[1].set_xlabel('y')

plt.tight_layout()
plt.savefig('pe/transformaciones.png', dpi=100, bbox_inches='tight')
plt.show()

# Transformaci\'on Box-Cox
from scipy.stats import boxcox
datos = np.random.exponential(scale=2, size=1000)
datos_transformados, lambda_opt = boxcox(datos)
print(f"Lambda \'optimo: {lambda_opt:.3f}")
##Lambda \'optimo: 0.279
