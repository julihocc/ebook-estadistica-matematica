from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

#Distribución geométrica: ensayos hasta el primer éxito
p = 0.2
geomDist = stats.geom(p)

#Probabilidad de necesitar exactamente 5 ensayos
print(geomDist.pmf(5))
##0.08192000000000001

#Probabilidad de necesitar a lo más 5 ensayos
print(geomDist.cdf(5))
##0.67232

#Probabilidad de necesitar más de 5 ensayos
print(1-geomDist.cdf(5))
##0.32768

#Media y varianza
print(geomDist.mean())
##5.0
print(geomDist.var())
##20.0

#Verificación de la propiedad de pérdida de memoria
print(1 - geomDist.cdf(3+2))
##0.3276800000000001
print((1-geomDist.cdf(3)) * (1-geomDist.cdf(2)))
##0.3276800000000001

#Simulación
np.random.seed(0)
muestras = np.random.geom(p, size=1000)
print(np.mean(muestras))
##4.984
