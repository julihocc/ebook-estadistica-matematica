import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Panel izquierdo: FGM de varias distribuciones
t = np.linspace(-1.5, 1.5, 200)

# Bernoulli(0.5)
M_bernoulli = lambda t: 0.5 + 0.5*np.exp(t)
axes[0].plot(t, M_bernoulli(t), label='Bernoulli(0.5)', lw=2)

# Normal(0,1)
M_normal = lambda t: np.exp(t**2 / 2)
axes[0].plot(t, M_normal(t), label='N(0,1)', lw=2)

# Exponencial(lambda=1)
lam = 1
M_exp = lambda t: lam / (lam - t)
mask = t < lam - 0.01
axes[0].plot(t[mask], M_exp(t[mask]), label='Exp(1)', lw=2)

# Gamma(2, 1) = Erlang(2, 1)
# M(t) = (1 - t)^(-alpha) para beta=1
M_gamma = lambda t: (1 - t)**(-2)
mask_g = t < 0.99
axes[0].plot(t[mask_g], M_gamma(t[mask_g]), label='Gamma(2,1)', lw=2)

axes[0].set_xlabel('t')
axes[0].set_ylabel('M_X(t)')
axes[0].set_title('Funciones generadoras de momentos')
axes[0].set_ylim(-1, 8)
axes[0].legend()
axes[0].grid(True, alpha=0.3)
axes[0].axhline(y=0, color='k', lw=0.5)
axes[0].axvline(x=0, color='k', lw=0.5)

# Panel derecho: verificaci\'on de momentos de N(0,1)
X = np.random.normal(0, 1, 100000)
momentos_empiricos = [np.mean(X**k) for k in range(1, 6)]
print("Momentos emp\'iricos de N(0,1):", momentos_empiricos)
# Esperado: 0, 1, 0, 3, 0  (solo momentos pares son no cero)
##Momentos emp\'iricos de N(0,1): [0.001, 0.998, -0.001, 2.978, -0.011]

# FGM: suma de gamma independientes
# Si X_i ~ Gamma(1, 1) iid, entonces sum = Gamma(n, 1)
n_sumas = [1, 2, 5, 10]
x = np.linspace(0, 20, 200)
for n in n_sumas:
    g = stats.gamma(a=n, scale=1.0)
    axes[1].plot(x, g.pdf(x), lw=2, label=f'suma de {n} Exp(1)')
axes[1].set_xlabel('x')
axes[1].set_ylabel('f(x)')
axes[1].set_title('Suma de exponenciales = Erlang(Gamma)')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('pe/fgmDistribuciones.png', dpi=100, bbox_inches='tight')
plt.show()
