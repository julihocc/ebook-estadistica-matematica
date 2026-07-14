import numpy as np

# 1. Frequentist vs Classical (Laplace) Probability Simulation
# Set seed for exact pedagogical reproducibility
np.random.seed(42)
N = 10000

# Simulation of N coin tosses (0: Tails, 1: Heads)
coin_tosses = np.random.randint(0, 2, size=N)
empirical_prob_heads = np.mean(coin_tosses == 1)
classical_prob_heads = 1 / 2

# Simulation of N rolls of a fair 6-sided die
die_rolls = np.random.randint(1, 7, size=N)
empirical_prob_four = np.mean(die_rolls == 4)
classical_prob_four = 1 / 6

print("--- 1. Frequentist vs Classical Approach (N = 10,000) ---")
print(f"Coin P(Heads):    Empirical = {empirical_prob_heads:.4f} | Classical = {classical_prob_heads:.4f}")
print(f"Die  P(X=4):      Empirical = {empirical_prob_four:.4f} | Classical = {classical_prob_four:.4f}\n")

# 2. Kolmogorov Axioms & Addition Rule Verification (52-card Deck)
total_cards = 52
spades_cards = 13      # Event A: Drawing a Spade
kings_cards = 4        # Event B: Drawing a King
king_of_spades = 1     # Event A cap B: Drawing the King of Spades

prob_spade = spades_cards / total_cards
prob_king = kings_cards / total_cards
prob_king_spade = king_of_spades / total_cards

# Verification of Axiom 1 and Axiom 2
assert 0 <= prob_spade <= 1 and 0 <= prob_king <= 1, "Axiom 1: Non-negativity verified"
assert total_cards / total_cards == 1.0, "Axiom 2: Normalization verified"

# General Addition Rule: P(A cup B) = P(A) + P(B) - P(A cap B)
prob_spade_or_king = prob_spade + prob_king - prob_king_spade

# Verification via direct inclusion-exclusion count (13 spades + 3 remaining kings = 16 cards)
prob_spade_or_king_direct = 16 / total_cards
assert np.isclose(prob_spade_or_king, prob_spade_or_king_direct), "Inclusion-Exclusion verified"

print("--- 2. Axioms & Addition Rule (English Deck) ---")
print(f"P(Spade):         {prob_spade:.4f} (13/52)")
print(f"P(King):          {prob_king:.4f} (4/52)")
print(f"P(King cap Spade):{prob_king_spade:.4f} (1/52)")
print(f"P(Spade cup King):{prob_spade_or_king:.4f} (16/52 via Inclusion-Exclusion)")
