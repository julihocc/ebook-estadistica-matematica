import numpy as np

# 1. Simulacion Frecuencial vs Enfoque Clasico (Laplace)
# Fijamos semilla para reproducibilidad pedagogica exacta
np.random.seed(42)
N = 10000

# Simulacion de N volados (0: Cruz, 1: Sol)
lanzamientos_moneda = np.random.randint(0, 2, size=N)
prob_empirica_sol = np.mean(lanzamientos_moneda == 1)
prob_clasica_sol = 1 / 2

# Simulacion de N lanzamientos de un dado de 6 caras
lanzamientos_dado = np.random.randint(1, 7, size=N)
prob_empirica_cuatro = np.mean(lanzamientos_dado == 4)
prob_clasica_cuatro = 1 / 6

print("--- 1. Enfoque Frecuencial vs Clasico (N = 10,000) ---")
print(f"Moneda P(Sol):    Empirica = {prob_empirica_sol:.4f} | Clasica = {prob_clasica_sol:.4f}")
print(f"Dado   P(X=4):    Empirica = {prob_empirica_cuatro:.4f} | Clasica = {prob_clasica_cuatro:.4f}\n")

# 2. Verificacion de Axiomas de Kolmogorov y Regla de la Suma en Baraja (52 cartas)
total_cartas = 52
cartas_pica = 13       # Evento A: Obtener una Pica (Spades)
cartas_rey = 4         # Evento B: Obtener un Rey (King)
cartas_rey_pica = 1    # Evento A inter B: El Rey de Picas

prob_pica = cartas_pica / total_cartas
prob_rey = cartas_rey / total_cartas
prob_rey_pica = cartas_rey_pica / total_cartas

# Verificacion del Axioma 1 y Axioma 2
assert 0 <= prob_pica <= 1 and 0 <= prob_rey <= 1, "Axioma 1: No negatividad verificado"
assert total_cartas / total_cartas == 1.0, "Axioma 2: Normalización verificada"

# Regla General de Adicion: P(A union B) = P(A) + P(B) - P(A inter B)
prob_pica_o_rey = prob_pica + prob_rey - prob_rey_pica

# Verificacion de Inclusio-Exclusion con conteo directo (13 picas + 3 reyes restantes = 16 cartas)
prob_pica_o_rey_directa = 16 / total_cartas
assert np.isclose(prob_pica_o_rey, prob_pica_o_rey_directa), "Inclusión-Exclusión verificada"

print("--- 2. Axiomas y Regla de Adicion (Baraja Inglesa) ---")
print(f"P(Pica):          {prob_pica:.4f} (13/52)")
print(f"P(Rey):           {prob_rey:.4f} (4/52)")
print(f"P(Rey inter Pica):{prob_rey_pica:.4f} (1/52)")
print(f"P(Pica union Rey):{prob_pica_o_rey:.4f} (16/52 via Inclusio-Exclusion)")
