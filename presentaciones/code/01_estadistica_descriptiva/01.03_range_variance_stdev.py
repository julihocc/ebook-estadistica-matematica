import numpy as np

# 1. Two samples with identical mean but distinct variability
# A: Stable response times (ms) vs B: Erratic response times (ms)
sample_A = np.array([48, 49, 50, 51, 52])
sample_B = np.array([10, 30, 50, 70, 90])

mean_A = np.mean(sample_A)
mean_B = np.mean(sample_B)

# Population Variance (ddof=0: dividing by N)
var_pop_A = np.var(sample_A, ddof=0)
var_pop_B = np.var(sample_B, ddof=0)

# Sample Variance with Bessel's Correction (ddof=1: dividing by n-1)
var_sam_A = np.var(sample_A, ddof=1)
var_sam_B = np.var(sample_B, ddof=1)
std_sam_A = np.std(sample_A, ddof=1)
std_sam_B = np.std(sample_B, ddof=1)

print("--- Sample Comparison (Mean vs. Dispersion) ---")
print(f"Sample A: Mean = {mean_A:.1f} ms | Std Dev (S) = {std_sam_A:.2f} ms")
print(f"Sample B: Mean = {mean_B:.1f} ms | Std Dev (S) = {std_sam_B:.2f} ms\n")

# 2. Interquartile Range (IQR) and Robustness against Outliers
normal_data = np.array([45, 47, 48, 50, 51, 52, 54, 55])
# Add an extreme outlier (e.g., severe latency spike of 450 ms)
data_with_outlier = np.append(normal_data, 450)

# Computation of quantiles (Q1, Q2/Median, Q3) and Interquartile Range (IQR)
q25_norm, q75_norm = np.percentile(normal_data, [25, 75])
iqr_norm = q75_norm - q25_norm
std_norm = np.std(normal_data, ddof=1)

q25_out, q75_out = np.percentile(data_with_outlier, [25, 75])
iqr_out = q75_out - q25_out
std_out = np.std(data_with_outlier, ddof=1)

print("--- Outlier Impact on S vs. IQR ---")
print(f"Without outlier: Std Dev S = {std_norm:.2f} | IQR = {iqr_norm:.2f}")
print(f"With outlier:    Std Dev S = {std_out:.2f}  | IQR = {iqr_out:.2f}")
print(f"S Distortion: {std_out/std_norm:.1f}x greater       | IQR Distortion: {iqr_out/iqr_norm:.1f}x (virtually stable)")
