"""
Computational Lab: Section 08.01 - One-Way ANOVA and the F-Test
====================================================================
Decomposes total sum of squares into treatment and error components for a
one-way ANOVA design, cross-checks the F statistic against scipy, applies
Tukey's HSD post-hoc procedure to identify which treatment pairs differ, and
demonstrates the variance-reduction benefit of blocking in a Randomized
Complete Block Design (RCBD).

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from scipy import stats


def one_way_anova_f_test():
    """Decomposes SST = SSTR + SSE for k=4 backend configurations and tests F."""
    print("=== Block 1: One-Way ANOVA Sum-of-Squares Decomposition and F-Test ===")
    rng = np.random.default_rng(seed=42)
    true_means = [120.0, 135.0, 128.0, 150.0]
    n_per_group = 6
    groups = [rng.normal(loc=mu, scale=8.0, size=n_per_group) for mu in true_means]
    labels = ["Config A", "Config B", "Config C", "Config D"]

    k = len(groups)
    n_i = np.array([len(g) for g in groups])
    N = n_i.sum()
    grand_mean = np.concatenate(groups).mean()
    group_means = np.array([g.mean() for g in groups])

    sstr = np.sum(n_i * (group_means - grand_mean) ** 2)
    sse = np.sum([np.sum((g - g.mean()) ** 2) for g in groups])
    sst = sstr + sse

    df_tr, df_e = k - 1, N - k
    cmtr, cme = sstr / df_tr, sse / df_e
    f_stat = cmtr / cme
    p_value = stats.f.sf(f_stat, df_tr, df_e)

    print(f"Groups: {labels}, n_i={n_i.tolist()}, N={N}")
    print(f"Group means: {np.round(group_means, 3)}, grand mean: {grand_mean:.3f}")
    print(f"SSTR={sstr:.4f} (df={df_tr}), SSE={sse:.4f} (df={df_e}), SST={sst:.4f}")
    print(f"CMTR={cmtr:.4f}, CME={cme:.4f}")
    print(f"F statistic = {f_stat:.4f}, p-value = {p_value:.6f}")

    f_scipy, p_scipy = stats.f_oneway(*groups)
    print(f"scipy.stats.f_oneway check: F={f_scipy:.4f}, p={p_scipy:.6f}")

    return groups, labels, cme, df_e


def tukey_hsd_posthoc(groups, labels, cme, df_e):
    """Applies Tukey's HSD to identify which pairs of the 4 configs differ."""
    print("\n=== Block 2: Tukey HSD Post-Hoc Pairwise Comparisons ===")
    k = len(groups)
    n = len(groups[0])
    group_means = np.array([g.mean() for g in groups])
    alpha = 0.05

    q_crit = stats.studentized_range.ppf(1 - alpha, k, df_e)
    hsd = q_crit * np.sqrt(cme / n)
    print(f"Studentized range critical value q(0.05, k={k}, df_E={df_e}) = {q_crit:.4f}")
    print(f"HSD threshold = q * sqrt(CME/n) = {hsd:.4f}")

    for i in range(k):
        for j in range(i + 1, k):
            diff = abs(group_means[i] - group_means[j])
            verdict = "SIGNIFICANT" if diff > hsd else "not significant"
            print(f"  |{labels[i]} - {labels[j]}| = {diff:.4f} -> {verdict}")


def randomized_complete_block_design():
    """Decomposes SST = SSTR + SSB + SSE for a 3-treatment, 4-block RCBD."""
    print("\n=== Block 3: Randomized Complete Block Design (RCBD) ===")
    data = np.array([
        [12.0, 15.5, 22.0, 28.5],
        [8.5, 11.0, 16.5, 22.0],
        [9.5, 12.5, 18.5, 23.5],
    ])
    k, b = data.shape

    grand_mean = data.mean()
    treatment_means = data.mean(axis=1)
    block_means = data.mean(axis=0)

    sstr = b * np.sum((treatment_means - grand_mean) ** 2)
    ssb = k * np.sum((block_means - grand_mean) ** 2)
    sst = np.sum((data - grand_mean) ** 2)
    sse = sst - sstr - ssb

    df_tr, df_b, df_e = k - 1, b - 1, (k - 1) * (b - 1)
    cmtr, cmb, cme = sstr / df_tr, ssb / df_b, sse / df_e
    f_tr, f_b = cmtr / cme, cmb / cme
    p_tr = stats.f.sf(f_tr, df_tr, df_e)
    p_b = stats.f.sf(f_b, df_b, df_e)

    print(f"Treatment means: {np.round(treatment_means, 3)}")
    print(f"Block means: {np.round(block_means, 3)}")
    print(f"SST={sst:.4f} = SSTR({sstr:.4f}) + SSB({ssb:.4f}) + SSE({sse:.4f})")
    print(f"F_TR = {f_tr:.4f} (df={df_tr},{df_e}), p={p_tr:.6f}")
    print(f"F_B  = {f_b:.4f} (df={df_b},{df_e}), p={p_b:.6f}")

    s2_dca_approx = ((b - 1) * cmb + b * (k - 1) * cme) / (k * b - 1)
    relative_efficiency = s2_dca_approx / cme
    print(f"Approx. CRD residual variance if blocks were ignored: {s2_dca_approx:.4f}")
    print(f"Relative Efficiency of blocking (RE = S^2_DCA / CME) = {relative_efficiency:.4f}")


if __name__ == "__main__":
    groups, labels, cme, df_e = one_way_anova_f_test()
    tukey_hsd_posthoc(groups, labels, cme, df_e)
    randomized_complete_block_design()
