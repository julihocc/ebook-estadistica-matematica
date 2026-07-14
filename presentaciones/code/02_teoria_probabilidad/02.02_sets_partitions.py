import numpy as np

# -------------------------------------------------------------------------
# 1. Basic Set Operations in Python
# -------------------------------------------------------------------------
S = set(range(1, 11))  # Sample space: {1, 2, ..., 10}
A = {2, 4, 6, 8, 10}   # Event A: Even numbers
B = {1, 2, 3, 4, 5}    # Event B: Numbers <= 5

print("--- 1. Basic Set Operations ---")
print(f"Sample Space (S):       {sorted(list(S))}")
print(f"Event A (Even):         {sorted(list(A))}")
print(f"Event B (<= 5):         {sorted(list(B))}")
print(f"Union (A union B):      {sorted(list(A | B))}")
print(f"Intersection (A & B):   {sorted(list(A & B))}")
print(f"Difference (A \\ B):     {sorted(list(A - B))}")
print(f"Complement (A'):        {sorted(list(S - A))}\n")

# -------------------------------------------------------------------------
# 2. Algebraic Solution of Counting Problem via Standard Partition
# -------------------------------------------------------------------------
# Problem: Survey of N = 100 attendees at a technical conference:
# |E| (Speak English) = 60
# |F| (Speak French)  = 45
# |E & F| (Speak both) = 30
#
# Standard partition into 4 disjoint elementary regions (puzzle pieces):
# x0 = |E' & F'| (Speak neither English nor French)
# x1 = |E' & F|  (Speak only French)
# x2 = |E & F'|  (Speak only English)
# x3 = |E & F|   (Speak both languages)
#
# Linear system of equations M * x = b:
# x0 + x1 + x2 + x3 = 100  (Total sample space S)
#      x1      + x3 = 45   (Total set F)
#           x2 + x3 = 60   (Total set E)
#                x3 = 30   (Intersection E & F)

M = np.array([
    [1, 1, 1, 1],
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
])
b = np.array([100, 45, 60, 30])
x = np.linalg.solve(M, b).astype(int)

print("--- 2. Algebraic Solution via Standard Partition (4 Pieces) ---")
print(f"x3 (|E & F|   - Both languages):          {x[3]:2d} attendees")
print(f"x2 (|E \\ F|   - English only):            {x[2]:2d} attendees")
print(f"x1 (|F \\ E|   - French only):             {x[1]:2d} attendees")
print(f"x0 (|E' & F'| - Neither language):        {x[0]:2d} attendees")
print(f"Verified partition total:                 {sum(x):2d} attendees")
assert sum(x) == 100, "The partition must sum exactly to the cardinal of S!"
