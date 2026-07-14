# Lab 1.1: Simulation of Population vs. Sample in Data Science
# Live demonstration for the Descriptive Statistics presentation

import numpy as np

# 1. Simulate a hidden POPULATION of 100,000 users (e.g., session duration in minutes)
np.random.seed(42)  # For classroom reproducibility
poblacion_mu = 45.0
poblacion_sigma = 12.0
population = np.random.normal(loc=poblacion_mu, scale=poblacion_sigma, size=100000)

# True parameter (theoretical/hidden in practice):
mu_real = np.mean(population)
sigma_real = np.std(population)
print("=== POPULATION TRUTH (PARAMETERS) ===")
print(f"Population mean (mu):       {mu_real:.2f} min")
print(f"Standard deviation (sigma): {sigma_real:.2f} min\n")

# 2. Extract a random SAMPLE of only 150 users
sample = np.random.choice(population, size=150, replace=False)

# Statistics computed from the sample (our estimators):
x_bar = np.mean(sample)
s_sample = np.std(sample, ddof=1)  # ddof=1 for unbiased sample variance estimator

print("=== DATA SCIENTIST OBSERVATION (STATISTICS) ===")
print(f"Sample mean (X-bar):       {x_bar:.2f} min")
print(f"Sample std dev (s):        {s_sample:.2f} min")
print(f"Mean estimation error:     {abs(x_bar - mu_real):.2f} min")
