import numpy as np
from scipy import stats

# 1. Conjunto de datos de muestra (ej. salarios en miles o tiempos de respuesta)
datos = np.array([5, 8, 11, 9, 12, 6, 14, 10])

# 2. Medidas clásicas de tendencia central
media = np.mean(datos)
mediana = np.median(datos)
moda_res = stats.mode(datos, keepdims=True)

print(f"--- Medidas Clásicas ---")
print(f"Media aritmética: {media:.2f}")
print(f"Mediana:          {mediana:.2f}")
print(f"Moda (si existe): {moda_res.mode[0]} (frecuencia: {moda_res.count[0]})\n")

# 3. Demostración del Cálculo con Pivote (P = 9)
pivote = 9
desviaciones = datos - pivote
media_con_pivote = pivote + np.mean(desviaciones)

print(f"--- Cálculo con Pivote (P = {pivote}) ---")
print(f"Desviaciones (d_i): {desviaciones}")
print(f"Suma de d_i:        {np.sum(desviaciones)}")
print(f"Media vía pivote:   {pivote} + ({np.sum(desviaciones)}/{len(datos)}) = {media_con_pivote:.2f}")
assert np.isclose(media, media_con_pivote), "¡La media por pivote debe coincidir!"
