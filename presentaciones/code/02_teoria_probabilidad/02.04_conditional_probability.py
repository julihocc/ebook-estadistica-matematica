"""
Computational Laboratory 02.04: Conditional Probability and Independence
========================================================================
Empirical demonstration of sample space rescaling, multiplication rules,
statistical independence tests, and Monte Carlo resolution of the
Monty Hall Paradox.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import random

# Fix random seed for exact reproducibility
random.seed(20260714)

# ==============================================================================
# 1. SAMPLING WITHOUT REPLACEMENT (PROBLEM 2.4.2: RED AND BLUE BALL URN)
# ==============================================================================
# Urn containing 5 red balls and 3 blue balls (8 total).
# A = "First ball is red", B = "Second ball is red".

N_sim = 100_000
count_A = 0             # Times A occurs (1st red)
count_A_comp = 0        # Times A' occurs (1st blue)
count_B_given_A = 0     # Times B occurs given A occurred
count_B_given_Acomp = 0 # Times B occurs given A' occurred
count_B_total = 0       # Total times B occurs

for _ in range(N_sim):
    # Create fresh urn on each iteration: 'R' (Red), 'B' (Blue)
    urn = ['R']*5 + ['B']*3
    random.shuffle(urn)
    
    # First draw
    ball_1 = urn.pop()
    # Second draw (without replacement)
    ball_2 = urn.pop()
    
    if ball_1 == 'R':
        count_A += 1
        if ball_2 == 'R':
            count_B_given_A += 1
            count_B_total += 1
    else:
        count_A_comp += 1
        if ball_2 == 'R':
            count_B_given_Acomp += 1
            count_B_total += 1

# Empirical vs theoretical probabilities
P_emp_A = count_A / N_sim
P_emp_B_given_A = count_B_given_A / count_A
P_emp_B_given_Acomp = count_B_given_Acomp / count_A_comp
P_emp_B_total = count_B_total / N_sim

print("--- 1. Sampling without Replacement (Urn 5 Red, 3 Blue) ---")
print(f"P(1st Red) [A]:               Empirical = {P_emp_A:.4f} | Theoretical = 0.6250 (5/8)")
print(f"P(2nd Red | 1st Red) [B|A]:   Empirical = {P_emp_B_given_A:.4f} | Theoretical = 0.5714 (4/7)")
print(f"P(2nd Red | 1st Blue) [B|A']: Empirical = {P_emp_B_given_Acomp:.4f} | Theoretical = 0.7143 (5/7)")
print(f"P(2nd Red Total) [B]:         Empirical = {P_emp_B_total:.4f} | Theoretical = 0.6250")
print()

# ==============================================================================
# 2. INDEPENDENCE VERIFICATION (PROBLEM 2.4.1: TWO DICE)
# ==============================================================================
# Rolling two fair dice.
# Event A: Sum of dice >= 9
# Event B: First die is even {2, 4, 6}

count_die_A = 0
count_die_B = 0
count_die_A_and_B = 0

for _ in range(N_sim):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    suma = d1 + d2
    
    is_A = (suma >= 9)
    is_B = (d1 % 2 == 0)
    
    if is_A:
        count_die_A += 1
    if is_B:
        count_die_B += 1
    if is_A and is_B:
        count_die_A_and_B += 1

P_die_A = count_die_A / N_sim
P_die_B = count_die_B / N_sim
P_die_A_and_B = count_die_A_and_B / N_sim
P_die_A_given_B = count_die_A_and_B / count_die_B

# Theoretical exact values:
# Total cases = 36.
# A (sum >= 9) = {(3,6), (4,5), (4,6), (5,4), (5,5), (5,6), (6,3), (6,4), (6,5), (6,6)} -> 10/36 = 5/18 = 0.2778
# B (d1 even) = 18/36 = 0.5000
# A cap B (sum >= 9 & d1 even) = {(4,5), (4,6), (6,3), (6,4), (6,5), (6,6)} -> 6/36 = 1/6 = 0.1667
# P(A|B) = (6/36) / (18/36) = 6/18 = 1/3 = 0.3333

print("--- 2. Independence and Dependence Test (Two Dice) ---")
print(f"P(Sum >= 9) [A]:              Empirical = {P_die_A:.4f} | Theoretical = 0.2778 (10/36)")
print(f"P(First die even) [B]:        Empirical = {P_die_B:.4f} | Theoretical = 0.5000 (18/36)")
print(f"P(A inter B):                 Empirical = {P_die_A_and_B:.4f} | Theoretical = 0.1667 (6/36)")
print(f"P(A | B):                     Empirical = {P_die_A_given_B:.4f} | Theoretical = 0.3333 (1/3)")
print(f"Product P(A) * P(B):          {P_die_A * P_die_B:.4f} != P(A inter B) -> DEPENDENT!")
print()

# ==============================================================================
# 3. THE MONTY HALL PARADOX (PROBLEM 2.4.10)
# ==============================================================================
# Three doors: 1 car (prize) and 2 goats. Contestant chooses Door 1.
# Host always opens a door revealing a goat (different from chosen & car).

count_win_staying = 0
count_win_switching = 0

for _ in range(N_sim):
    doors = [0, 1, 2]
    prize_door = random.choice(doors)
    chosen_door = random.choice(doors)
    
    # Host opens a door that is NOT the chosen door AND NOT the prize door
    host_options = [d for d in doors if d != chosen_door and d != prize_door]
    opened_door = random.choice(host_options)
    
    # The remaining door after switching
    switched_door = [d for d in doors if d != chosen_door and d != opened_door][0]
    
    if chosen_door == prize_door:
        count_win_staying += 1
    if switched_door == prize_door:
        count_win_switching += 1

print("--- 3. Monty Hall Paradox (100,000 games) ---")
print(f"P(Win staying):               {count_win_staying/N_sim:.4f} (Theoretical: 1/3 = 0.3333)")
print(f"P(Win switching doors):       {count_win_switching/N_sim:.4f} (Theoretical: 2/3 = 0.6667)")
