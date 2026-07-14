"""
02.05_bayes_theorem.py
Empirical Monte Carlo Simulations for Bayes' Theorem & Conditional Updating

This script provides programmatic validation of:
1. Medical Diagnostic Testing & the Base Rate Fallacy (Empirical vs. Theoretical PPV).
2. Naive Bayes Spam Classification under Conditional Independence.
3. Sequential Bayesian Updating across successive evidence observations.
"""

import numpy as np

# ==========================================
# 1. Medical Diagnostic & Base Rate Fallacy
# ==========================================
def simulate_medical_test(n_population=100_000, prevalence=0.02, 
                          sensitivity=0.95, specificity=0.90, seed=42):
    """Simulates clinical screening to evaluate Positive Predictive Value (PPV)."""
    np.random.seed(seed)
    
    # Generate population health status (True = Diseased, False = Healthy)
    diseased = np.random.rand(n_population) < prevalence
    
    # Administer clinical test based on conditional sensitivity/specificity
    test_positive = np.zeros(n_population, dtype=bool)
    
    # True Positives: Diseased individuals testing positive (Sensitivity)
    test_positive[diseased] = np.random.rand(diseased.sum()) < sensitivity
    
    # False Positives: Healthy individuals testing positive (1 - Specificity)
    healthy = ~diseased
    test_positive[healthy] = np.random.rand(healthy.sum()) < (1.0 - specificity)
    
    # Calculate Empirical PPV: P(Diseased | Test Positive)
    total_positives = test_positive.sum()
    true_positives = (diseased & test_positive).sum()
    empirical_ppv = true_positives / total_positives if total_positives > 0 else 0.0
    
    # Theoretical PPV via Bayes' Theorem
    p_pos = (sensitivity * prevalence) + ((1.0 - specificity) * (1.0 - prevalence))
    theoretical_ppv = (sensitivity * prevalence) / p_pos
    
    return empirical_ppv, theoretical_ppv, total_positives, true_positives

# ==========================================
# 2. Naive Bayes Spam Classification
# ==========================================
def evaluate_naive_bayes_spam(p_spam=0.60, p_legit=0.40):
    """Calculates exact posterior probability P(Spam | W1, W2, W3) under Naive Bayes."""
    # Likelihood vectors P(W_i | Class) for keywords [W1, W2, W3]
    lik_spam  = np.array([0.80, 0.70, 0.60])
    lik_legit = np.array([0.10, 0.20, 0.10])
    
    # Conditional independence: Joint likelihood is the product of marginals
    joint_lik_spam  = np.prod(lik_spam)
    joint_lik_legit = np.prod(lik_legit)
    
    # Total marginal probability P(W1 & W2 & W3)
    p_evidence = (joint_lik_spam * p_spam) + (joint_lik_legit * p_legit)
    
    # Posterior probability P(Spam | Evidence) via Bayes' Theorem
    posterior_spam = (joint_lik_spam * p_spam) / p_evidence
    return posterior_spam, joint_lik_spam, joint_lik_legit, p_evidence

# ==========================================
# 3. Sequential Bayesian Updating
# ==========================================
def sequential_coin_updating(observations=[1, 1, 0, 1, 1], prior_prob=0.50):
    """Tracks prior -> posterior transitions across sequential coin flips."""
    # Hypotheses regarding coin bias P(Heads): Fair (0.50) vs. Biased (0.80)
    theta_fair = 0.50
    theta_biased = 0.80
    
    # Initial prior beliefs P(Biased Coin) vs. P(Fair Coin)
    p_biased = prior_prob
    p_fair   = 1.0 - prior_prob
    
    history = [(0, p_biased)]
    
    for step, flip in enumerate(observations, start=1):
        # Likelihood P(Flip | Hypothesis)
        lik_b = theta_biased if flip == 1 else (1.0 - theta_biased)
        lik_f = theta_fair   if flip == 1 else (1.0 - theta_fair)
        
        # Marginal likelihood P(Flip) across current priors
        marginal = (lik_b * p_biased) + (lik_f * p_fair)
        
        # Bayes step: Posterior becomes the new prior for the next iteration
        p_biased = (lik_b * p_biased) / marginal
        p_fair   = 1.0 - p_biased
        history.append((step, p_biased))
        
    return history

if __name__ == "__main__":
    print("--- 1. Medical Diagnostic Test (Base Rate Fallacy) ---")
    emp_ppv, theo_ppv, tot_pos, tp = simulate_medical_test()
    print(f"Total Test Positives:  {tot_pos:,} / 100,000")
    print(f"True Positives:        {tp:,} (True Diseased among Positives)")
    print(f"Empirical PPV (Sim):   {emp_ppv:.4f} ({emp_ppv*100:.2f}%)")
    print(f"Theoretical PPV:       {theo_ppv:.4f} ({theo_ppv*100:.2f}%)\n")
    
    print("--- 2. Naive Bayes Spam Filter (Keywords W1, W2, W3) ---")
    post_spam, l_spam, l_legit, p_ev = evaluate_naive_bayes_spam()
    print(f"Joint Likelihood P(W|Spam):  {l_spam:.5f}")
    print(f"Joint Likelihood P(W|Legit): {l_legit:.5f}")
    print(f"Marginal Evidence P(W):      {p_ev:.5f}")
    print(f"Posterior P(Spam | W):       {post_spam:.6f} ({post_spam*100:.2f}%)\n")
    
    print("--- 3. Sequential Bayesian Updating (Coin Flips: H, H, T, H, H) ---")
    seq_history = sequential_coin_updating()
    for step, prob in seq_history:
        print(f"Step {step} | P(Biased Coin = 0.80): {prob:.4f} ({prob*100:.2f}%)")
