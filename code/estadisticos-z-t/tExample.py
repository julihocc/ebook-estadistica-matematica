from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

def tp(x, nu):
	return stats.t.ppf(x, df=nu)

print(tp(0.05, 9))
##-1.83311293265
print(tp(1-0.05, 9))
##1.83311293265
