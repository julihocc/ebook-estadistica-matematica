"""
Si 5,8,6,2 se presentan con frecuencias 3,2,4,1 respectivamente, su media aritm'etica es...
"""
import numpy as np
data = np.array([5,8,6,2])
freq = np.array([3,2,4,1])
n = np.sum(freq)
media = np.sum(freq*data)/n 
print(media) # 5.7
