import numpy as np
import matplotlib.pyplot as plt

#Ejemplo de distribución binomial
N,p=100, 0.5
s = np.random.binomial(N,p,1000)

miHist = np.histogram(s, bins = np.arange(100+1))
print(miHist[0])
print(miHist[1])
print(np.mean(s))
print(N*p)
print(np.var(s))
print(N*p*(1-p))

plt.hist(s, bins = np.arange(100+1))
plt.show()
