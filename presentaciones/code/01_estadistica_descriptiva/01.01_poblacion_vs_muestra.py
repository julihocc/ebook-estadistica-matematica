# Laboratorio 1.1: Simulación de Población vs Muestra en Ciencia de Datos
# Demostración en vivo para la presentación de Estadística Descriptiva

import numpy as np
import pandas as pd

# 1. Simulamos una POBLACION oculta de 100,000 usuarios (ej. tiempo de sesión en minutos)
np.random.seed(42)  # Para reproducibilidad en clase
poblacion_mu = 45.0
poblacion_sigma = 12.0
poblacion = np.random.normal(loc=poblacion_mu, scale=poblacion_sigma, size=100000)

# Parametro real (teorico/oculto en la practica real):
mu_real = np.mean(poblacion)
sigma_real = np.std(poblacion)
print("=== VERDAD DE LA POBLACION (PARAMETROS) ===")
print(f"Media poblacional (mu):    {mu_real:.2f} min")
print(f"Desviacion estandar (sigma): {sigma_real:.2f} min\n")

# 2. Extraemos una MUESTRA aleatoria de solo 150 usuarios
muestra = np.random.choice(poblacion, size=150, replace=False)

# Estadisticos calculados a partir de la muestra (nuestros estimadores):
x_barra = np.mean(muestra)
s_muestra = np.std(muestra, ddof=1)  # ddof=1 para estimador insesgado de varianza muestral

print("=== OBSERVACION DEL CIENTIFICO DE DATOS (ESTADISTICOS) ===")
print(f"Media muestral (X-barra):  {x_barra:.2f} min")
print(f"Desviacion muestral (s):   {s_muestra:.2f} min")
print(f"Error de estimacion en media: {abs(x_barra - mu_real):.2f} min")
