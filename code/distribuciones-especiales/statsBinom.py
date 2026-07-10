from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

#Consideremos 6 experimentos con p de éxito 1/2
p=0.5
N=6
binDist = stats.binom(N,p)
#probabilidad de obtener dos éxitos
print(binDist.pmf(2))
##0.234375
#probabilidad de obtener al menos 4 éxitos
print(sum(binDist.pmf(np.arange(4,6+1))))
##0.34375
