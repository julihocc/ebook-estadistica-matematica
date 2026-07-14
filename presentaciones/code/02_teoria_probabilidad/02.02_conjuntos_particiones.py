import numpy as np

# -------------------------------------------------------------------------
# 1. Operaciones Básicas de Conjuntos en Python
# -------------------------------------------------------------------------
S = set(range(1, 11))  # Espacio muestral: {1, 2, ..., 10}
A = {2, 4, 6, 8, 10}   # Evento A: Números pares
B = {1, 2, 3, 4, 5}    # Evento B: Números <= 5

print("--- 1. Operaciones Básicas de Conjuntos ---")
print(f"Espacio Muestral (S):  {sorted(list(S))}")
print(f"Evento A (Pares):      {sorted(list(A))}")
print(f"Evento B (<= 5):       {sorted(list(B))}")
print(f"Unión (A union B):     {sorted(list(A | B))}")
print(f"Intersección (A & B):  {sorted(list(A & B))}")
print(f"Diferencia (A \\ B):    {sorted(list(A - B))}")
print(f"Complemento (A'):      {sorted(list(S - A))}\n")

# -------------------------------------------------------------------------
# 2. Resolución Algebraica de Problema de Conteo vía Partición Estándar
# -------------------------------------------------------------------------
# Problema: Encuesta a N = 100 usuarios en una conferencia técnica:
# |I| (Hablan Inglés) = 60
# |F| (Hablan Francés) = 45
# |I & F| (Hablan ambos) = 30
#
# Partición estándar en 4 regiones elementales disjuntas (rompecabezas):
# x0 = |I' & F'| (No hablan ni inglés ni francés)
# x1 = |I' & F|  (Hablan solo francés)
# x2 = |I & F'|  (Hablan solo inglés)
# x3 = |I & F|   (Hablan ambos idiomas)
#
# Sistema lineal de ecuaciones M * x = b:
# x0 + x1 + x2 + x3 = 100  (Total del espacio muestral S)
#      x1      + x3 = 45   (Total del conjunto F)
#           x2 + x3 = 60   (Total del conjunto I)
#                x3 = 30   (Intersección I & F)

M = np.array([
    [1, 1, 1, 1],
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
])
b = np.array([100, 45, 60, 30])
x = np.linalg.solve(M, b).astype(int)

print("--- 2. Resolución Algebraica vía Partición Estándar (4 Piezas) ---")
print(f"x3 (|I & F|   - Ambos idiomas):           {x[3]:2d} personas")
print(f"x2 (|I \\ F|   - Solo Inglés):            {x[2]:2d} personas")
print(f"x1 (|F \\ I|   - Solo Francés):           {x[1]:2d} personas")
print(f"x0 (|I' & F'| - Ninguno de los dos):      {x[0]:2d} personas")
print(f"Total verificado de la partición:        {sum(x):2d} personas")
assert sum(x) == 100, "¡La partición debe sumar exactamente el cardinal de S!"
