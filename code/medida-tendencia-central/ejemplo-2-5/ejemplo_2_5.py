"""
La mediana de la lista de n'umeros 5, 4, 3, 8, 6, 2, 5, 2 es..
"""
data = [5, 4, 3, 8, 6, 2, 5, 2]
#ordenamos los datos
data = sorted(data)
print(data) # [2, 2, 3, 4, 4, 5, 6, 8]
n = len(data)
pos_mediana = (n-1)/2 
print(pos_mediana) # 3.5
m = (n-1)//2 # 3
mediana = (data[m]+data[m+1])/2
print(mediana) # 4.5

"""
La mediana de la lista de n'umeros 3, 9, 1, 1, 4, 1, 3, 2, 4 es..
"""
data = [3, 9, 1, 1, 4, 1, 3, 2, 4]
#ordenamos los datos
data = sorted(data)
print(data) # [1, 1, 1, 2, 3, 3, 4, 4, 9]
n = len(data)
pos_mediana = (n-1)/2 
print(pos_mediana) # 4
m = (n-1)//2
mediana = data[m]
print(mediana) # 3