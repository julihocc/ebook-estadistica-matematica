from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

#Distribución hipergeométrica
N = 20  # tamaño de la población
K = 5   # número de éxitos en la población
n = 4   # número de extracciones

hyperDist = stats.hypergeom(N, K, n)

#Probabilidad de obtener exactamente 2 defectuosas
print(hyperDist.pmf(2))
##0.21674922760096778

#Media y varianza
print(hyperDist.mean())
##n*K/N = 1.0
print(hyperDist.var())
##n*(K/N)*((N-K)/N)*((N-n)/(N-1)) = 0.631578947368421

#Comparación con la aproximación binomial
binomDist = stats.binom(n, K/N)
print(binomDist.pmf(2))
##0.2153125

#Ejemplo: póker - 3 reyes en 5 cartas
poker = stats.hypergeom(52, 4, 5)
print(poker.pmf(3))
##0.0017361536111111111

#Simulación
np.random.seed(0)
poblacion = np.array([1]*K + [0]*(N-K))
muestras = np.array([np.sum(np.random.choice(poblacion, n, replace=False)) for _ in range(1000)])
print(np.mean(muestras))
##~1.0
