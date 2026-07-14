import numpy as np

# 1. Dos muestras con idéntica media pero distinta variabilidad
# A: Tiempos estables (ms) vs B: Tiempos erráticos (ms)
muestra_A = np.array([48, 49, 50, 51, 52])
muestra_B = np.array([10, 30, 50, 70, 90])

media_A = np.mean(muestra_A)
media_B = np.mean(muestra_B)

# Varianza Poblacional (ddof=0: dividiendo por N)
var_pob_A = np.var(muestra_A, ddof=0)
var_pob_B = np.var(muestra_B, ddof=0)

# Varianza Muestral con Corrección de Bessel (ddof=1: dividiendo por n-1)
var_mue_A = np.var(muestra_A, ddof=1)
var_mue_B = np.var(muestra_B, ddof=1)
desv_mue_A = np.std(muestra_A, ddof=1)
desv_mue_B = np.std(muestra_B, ddof=1)

print("--- Comparación de Muestras (Media vs Dispersión) ---")
print(f"Muestra A: Media = {media_A:.1f} ms | Desv. Estándar (S) = {desv_mue_A:.2f} ms")
print(f"Muestra B: Media = {media_B:.1f} ms | Desv. Estándar (S) = {desv_mue_B:.2f} ms\n")

# 2. Rango Intercuartílico (IQR) y Robustez ante Outliers
datos_normales = np.array([45, 47, 48, 50, 51, 52, 54, 55])
# Añadimos un outlier extremo (ej. caída o latencia severa de 450 ms)
datos_con_outlier = np.append(datos_normales, 450)

# Cálculo de cuantiles (Q1, Q2/Mediana, Q3) y Rango Intercuartílico (IQR)
q25_norm, q75_norm = np.percentile(datos_normales, [25, 75])
iqr_norm = q75_norm - q25_norm
desv_norm = np.std(datos_normales, ddof=1)

q25_out, q75_out = np.percentile(datos_con_outlier, [25, 75])
iqr_out = q75_out - q25_out
desv_out = np.std(datos_con_outlier, ddof=1)

print("--- Impacto de Outliers en S vs IQR ---")
print(f"Sin outlier:  Desv. Estándar S = {desv_norm:.2f} | IQR = {iqr_norm:.2f}")
print(f"Con outlier:  Desv. Estándar S = {desv_out:.2f}  | IQR = {iqr_out:.2f}")
print(f"Distorsión S: {desv_out/desv_norm:.1f}x veces mayor | Distorsión IQR: {iqr_out/iqr_norm:.1f}x (prácticamente estable)")
