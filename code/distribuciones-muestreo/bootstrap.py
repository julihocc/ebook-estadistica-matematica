import numpy as np

# Simulaci\'on: poblaci\'on exponencial, estimamos la mediana
np.random.seed(42)
n = 50
poblacion = np.random.exponential(scale=2, size=10000)
muestra = np.random.exponential(scale=2, size=n)

# Mediana observada
theta_obs = np.median(muestra)
print(f"Mediana observada: {theta_obs:.3f}")
##Mediana observada: 1.485

# Bootstrap
B = 10000
thetas_boot = np.zeros(B)
for b in range(B):
    muestra_boot = np.random.choice(muestra, size=n, replace=True)
    thetas_boot[b] = np.median(muestra_boot)

# Estimaciones bootstrap
sesgo = np.mean(thetas_boot) - theta_obs
var = np.var(thetas_boot, ddof=1)
print(f"Sesgo bootstrap: {sesgo:.3f}")
print(f"Varianza bootstrap: {var:.4f}")
##Sesgo bootstrap: 0.029
##Varianza bootstrap: 0.0707

# IC al 95\% (m\'etodo percentil)
ic = np.percentile(thetas_boot, [2.5, 97.5])
print(f"IC 95% bootstrap: [{ic[0]:.3f}, {ic[1]:.3f}]")
##IC 95% bootstrap: [0.971, 2.025]
