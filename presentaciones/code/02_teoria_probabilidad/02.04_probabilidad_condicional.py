"""
Laboratorio Computacional 02.04: Probabilidad Condicional e Independencia
===========================================================================
Demostración empírica del reescalamiento de espacios muestrales, reglas de
multiplicación, verificación de independencia estadística y resolución
Monte Carlo de la Paradoja de Monty Hall.

Autor: Juliho Castillo Colmenares
Institución: Tecnológico de Monterrey
"""

import random

# Fijar semilla para reproducibilidad exacta
random.seed(20260714)

# ==============================================================================
# 1. MUESTREO SIN REEMPLAZO (PROBLEMA 2.4.2: URNA DE BOLAS ROJAS Y AZULES)
# ==============================================================================
# Urna con 5 bolas rojas y 3 bolas azules (8 en total).
# A = "Primera bola es roja", B = "Segunda bola es roja".

N_sim = 100_000
count_A = 0             # Veces que A ocurre (1a roja)
count_A_comp = 0        # Veces que A' ocurre (1a azul)
count_B_given_A = 0     # Veces que B ocurre dado que A ocurrió
count_B_given_Acomp = 0 # Veces que B ocurre dado que A' ocurrió
count_B_total = 0       # Veces que B ocurre en total

for _ in range(N_sim):
    # Crear urna fresca en cada iteración: 'R' (Roja), 'A' (Azul)
    urna = ['R']*5 + ['A']*3
    random.shuffle(urna)
    
    # Primera extracción
    bola_1 = urna.pop()
    # Segunda extracción (sin reemplazo)
    bola_2 = urna.pop()
    
    if bola_1 == 'R':
        count_A += 1
        if bola_2 == 'R':
            count_B_given_A += 1
            count_B_total += 1
    else:
        count_A_comp += 1
        if bola_2 == 'R':
            count_B_given_Acomp += 1
            count_B_total += 1

# Probabilidades empíricas vs teóricas
P_emp_A = count_A / N_sim
P_emp_B_given_A = count_B_given_A / count_A
P_emp_B_given_Acomp = count_B_given_Acomp / count_A_comp
P_emp_B_total = count_B_total / N_sim

print("--- 1. Extracciones sin Reemplazo (Urna 5 Rojas, 3 Azules) ---")
print(f"P(1a Roja) [A]:               Empirica = {P_emp_A:.4f} | Teorica = 0.6250 (5/8)")
print(f"P(2a Roja | 1a Roja) [B|A]:   Empirica = {P_emp_B_given_A:.4f} | Teorica = 0.5714 (4/7)")
print(f"P(2a Roja | 1a Azul) [B|A']:  Empirica = {P_emp_B_given_Acomp:.4f} | Teorica = 0.7143 (5/7)")
print(f"P(2a Roja Total) [B]:         Empirica = {P_emp_B_total:.4f} | Teorica = 0.6250")
print()

# ==============================================================================
# 2. VERIFICACIÓN DE INDEPENDENCIA (PROBLEMA 2.4.1: DOS DADOS)
# ==============================================================================
# Lanzamiento de dos dados balanceados.
# Evento A: Suma de los dados >= 9
# Evento B: Primer dado es par {2, 4, 6}

count_dado_A = 0
count_dado_B = 0
count_dado_A_and_B = 0

for _ in range(N_sim):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    suma = d1 + d2
    
    es_A = (suma >= 9)
    es_B = (d1 % 2 == 0)
    
    if es_A:
        count_dado_A += 1
    if es_B:
        count_dado_B += 1
    if es_A and es_B:
        count_dado_A_and_B += 1

P_dado_A = count_dado_A / N_sim
P_dado_B = count_dado_B / N_sim
P_dado_A_and_B = count_dado_A_and_B / N_sim
P_dado_A_given_B = count_dado_A_and_B / count_dado_B

# Valores teóricos exactos:
# Casos totales = 36.
# A (suma >= 9) = {(3,6), (4,5), (4,6), (5,4), (5,5), (5,6), (6,3), (6,4), (6,5), (6,6)} -> 10/36 = 5/18 = 0.2778
# B (d1 par) = 18/36 = 0.5000
# A cap B (suma >= 9 y d1 par) = {(4,5), (4,6), (6,3), (6,4), (6,5), (6,6)} -> 6/36 = 1/6 = 0.1667
# P(A|B) = (6/36) / (18/36) = 6/18 = 1/3 = 0.3333

print("--- 2. Test de Independencia y Dependencia (Dos Dados) ---")
print(f"P(Suma >= 9) [A]:             Empirica = {P_dado_A:.4f} | Teorica = 0.2778 (10/36)")
print(f"P(Primer dado par) [B]:       Empirica = {P_dado_B:.4f} | Teorica = 0.5000 (18/36)")
print(f"P(A inter B):                 Empirica = {P_dado_A_and_B:.4f} | Teorica = 0.1667 (6/36)")
print(f"P(A | B):                     Empirica = {P_dado_A_given_B:.4f} | Teorica = 0.3333 (1/3)")
print(f"Producto P(A) * P(B):         {P_dado_A * P_dado_B:.4f} != P(A inter B) -> ¡DEPENDIENTES!")
print()

# ==============================================================================
# 3. LA PARADOJA DE MONTY HALL (PROBLEMA 2.4.10)
# ==============================================================================
# Tres puertas: 1 premio (Auto) y 2 cabras. El participante elige la Puerta 1.
# El presentador abre siempre una puerta con cabra (distinta a la elegida).

count_ganar_quedandose = 0
count_ganar_cambiando = 0

for _ in range(N_sim):
    puertas = [0, 1, 2]
    puerta_premio = random.choice(puertas)
    puerta_elegida = random.choice(puertas)
    
    # Presentador abre una puerta que NO sea la elegida ni la del premio
    opciones_presentador = [p for p in puertas if p != puerta_elegida and p != puerta_premio]
    puerta_abierta = random.choice(opciones_presentador)
    
    # La puerta restante al cambiar
    puerta_cambio = [p for p in puertas if p != puerta_elegida and p != puerta_abierta][0]
    
    if puerta_elegida == puerta_premio:
        count_ganar_quedandose += 1
    if puerta_cambio == puerta_premio:
        count_ganar_cambiando += 1

print("--- 3. Paradoja de Monty Hall (100,000 partidas) ---")
print(f"P(Ganar quedandose):          {count_ganar_quedandose/N_sim:.4f} (Teorica: 1/3 = 0.3333)")
print(f"P(Ganar cambiando de puerta): {count_ganar_cambiando/N_sim:.4f} (Teorica: 2/3 = 0.6667)")
