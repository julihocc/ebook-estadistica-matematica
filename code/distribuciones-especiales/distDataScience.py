from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

#Simulación: ¿Poisson o Binomial Negativa?
np.random.seed(0)

#Datos con sobredispersión
datos = np.random.negative_binomial(n=5, p=0.5, size=1000) + np.random.poisson(2, 1000)
print(f"Media: {np.mean(datos):.2f}, Varianza: {np.var(datos):.2f}")
##Media: ~7.0, Varianza: ~9.0

#Ajuste de Poisson (forzando media=var=lam)
lam = np.mean(datos)
poisson_fit = stats.poisson(lam)
print(f"Log-likelihood Poisson: {np.sum(poisson_fit.logpmf(datos)):.2f}")

#Ajuste de Binomial Negativa (estimando parámetros)
from scipy.optimize import minimize

def neg_log_lik_nbinom(params, data):
    r, p = params
    if r <= 0 or p <= 0 or p >= 1:
        return 1e10
    return -np.sum(stats.nbinom.logpmf(data, r, p))

result = minimize(neg_log_lik_nbinom, x0=[2, 0.5], args=(datos,))
r_opt, p_opt = result.x
print(f"Parámetros NB ajustados: r={r_opt:.2f}, p={p_opt:.2f}")
nbinom_fit = stats.nbinom(r_opt, p_opt)
print(f"Log-likelihood Binomial Negativa: {np.sum(nbinom_fit.logpmf(datos)):.2f}")

#Si log-likelihood de NB es mayor (menos negativo), el ajuste es mejor

#Visualización
fig, ax = plt.subplots(1, 1, figsize=(8, 5))
ax.hist(datos, bins=range(0, 20), density=True, alpha=0.5, label="Datos")
x = np.arange(0, 20)
ax.plot(x, poisson_fit.pmf(x), 'ro-', label="Poisson", markersize=6)
ax.plot(x, nbinom_fit.pmf(x), 'b^--', label="Binomial Negativa", markersize=6)
ax.legend()
ax.set_xlabel("Número de eventos")
ax.set_ylabel("Probabilidad")
plt.show()
