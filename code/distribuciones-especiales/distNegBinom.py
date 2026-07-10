from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

#Distribución binomial negativa: fracasos antes del r-ésimo éxito
r = 3
p = 0.3
nbDist = stats.nbinom(r, p)

#Probabilidad de 4 fracasos antes del tercer éxito
print(nbDist.pmf(4))
##0.0972405

#Media y varianza
print(nbDist.mean())
##r*(1-p)/p = 7.0
print(nbDist.var())
##r*(1-p)/p^2 = 23.333...

#Distribución geométrica como caso particular
geomDist = stats.geom(p)
print(geomDist.pmf(5))  # P(X=5) para geométrica
##0.08192000000000001
print(stats.nbinom(1, p).pmf(4))  # P(X=4) para binom neg con r=1
##0.08192000000000002

#Simulación
np.random.seed(0)
muestras = np.random.negative_binomial(r, p, size=1000)
print(np.mean(muestras))
##6.9...
