from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# Distribuci\'on gamma con varios par\'ametros
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Panel izquierdo: variando alpha (beta=1 fijo)
x = np.linspace(0, 15, 500)
alphas = [1, 2, 3, 5]
for a in alphas:
    g = stats.gamma(a=a, scale=1.0)
    axes[0].plot(x, g.pdf(x), lw=2, label=f'alpha={a}, beta=1')

axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].set_title('Familia gamma (variando alpha)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Panel derecho: distribuciones exponencial y chi-cuadrada como casos particulares
x2 = np.linspace(0, 10, 500)
exp_dist = stats.expon(scale=1.0)              # Gamma(alpha=1, beta=1)
chi2_3 = stats.chi2(df=3)                      # Gamma(alpha=1.5, beta=2)
chi2_5 = stats.chi2(df=5)                      # Gamma(alpha=2.5, beta=2)

axes[1].plot(x2, exp_dist.pdf(x2), 'b-', lw=2, label='Exp(1) = Gamma(1,1)')
axes[1].plot(x2, chi2_3.pdf(x2), 'r-', lw=2, label='chi^2_3 = Gamma(1.5,2)')
axes[1].plot(x2, chi2_5.pdf(x2), 'g-', lw=2, label='chi^2_5 = Gamma(2.5,2)')
axes[1].set_xlabel('x')
axes[1].set_ylabel('f(x)')
axes[1].set_title('Exponencial y chi-cuadrada como casos de gamma')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('pe/distGamma.png', dpi=100, bbox_inches='tight')
plt.show()

# Ejemplo: tiempo hasta la tercera llamada
# Erlang(k, lambda) = Gamma(k, 1/lambda)
lam = 3
k = 3
T = stats.gamma(a=k, scale=1/lam)
print(f"P(T > 1.5) = {1 - T.cdf(1.5):.4f}")
##P(T > 1.5) = 0.1739

# Simulaci\'on
np.random.seed(0)
muestras = np.random.gamma(shape=k, scale=1/lam, size=10000)
print(f"Media muestral: {np.mean(muestras):.4f}")  # Esperado: 1
##Media muestral: 1.0036
