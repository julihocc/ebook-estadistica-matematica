import numpy as np
from scipy import stats

# 1. Sample dataset (e.g., salaries in thousands or response times)
data = np.array([5, 8, 11, 9, 12, 6, 14, 10])

# 2. Classic measures of central tendency
mean_val = np.mean(data)
median_val = np.median(data)
mode_res = stats.mode(data, keepdims=True)

print(f"--- Classic Measures ---")
print(f"Arithmetic Mean: {mean_val:.2f}")
print(f"Median:          {median_val:.2f}")
print(f"Mode (if any):   {mode_res.mode[0]} (count: {mode_res.count[0]})\n")

# 3. Demonstration of Computation via Pivot (P = 9)
pivot = 9
deviations = data - pivot
mean_via_pivot = pivot + np.mean(deviations)

print(f"--- Computation via Pivot (P = {pivot}) ---")
print(f"Deviations (d_i): {deviations}")
print(f"Sum of d_i:       {np.sum(deviations)}")
print(f"Mean via pivot:   {pivot} + ({np.sum(deviations)}/{len(data)}) = {mean_via_pivot:.2f}")
assert np.isclose(mean_val, mean_via_pivot), "Mean computed via pivot must match exactly!"
