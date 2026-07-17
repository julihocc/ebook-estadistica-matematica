"""
Computational Lab: Section 09.08 - Model Validation: Train/Test Split and
k-Fold Cross-Validation
====================================================================
Implements a manual train/test split to detect overfitting by comparing
in-sample vs. out-of-sample RSE, builds k-fold cross-validation from scratch
(no scikit-learn -- reserved for Section 09.10), and uses it to compare two
competing models on average out-of-fold R^2.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np


def fit_ols(X, y):
    """Fits OLS via the normal equation and returns the coefficient vector."""
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    return beta


def rse(X, y, beta):
    """Computes the in-sample Residual Standard Error (adjusted for estimated parameters)."""
    residuals = y - X @ beta
    df = len(y) - X.shape[1]
    return np.sqrt(np.sum(residuals ** 2) / df)


def rmse(X, y, beta):
    """Computes the out-of-sample RMSE (no parameter-count adjustment: no model is fit here)."""
    residuals = y - X @ beta
    return np.sqrt(np.mean(residuals ** 2))


def train_test_split_and_overfitting_check():
    """Splits data 80/20; an overparameterized model fits train noise but fails on test."""
    print("=== Block 1: Train/Test Split and Overfitting Detection ===")
    rng = np.random.default_rng(seed=15)
    n = 40
    x_true = rng.uniform(0, 100, n)
    y = 5.0 + 0.5 * x_true + rng.normal(scale=8.0, size=n)
    noise_predictors = rng.normal(size=(n, 15))

    idx = rng.permutation(n)
    n_train = int(0.8 * n)
    train_idx, test_idx = idx[:n_train], idx[n_train:]

    X = np.column_stack([np.ones(n), x_true, noise_predictors])
    X_train, y_train = X[train_idx], y[train_idx]
    X_test, y_test = X[test_idx], y[test_idx]

    beta = fit_ols(X_train, y_train)
    rse_train = rse(X_train, y_train, beta)
    rmse_test = rmse(X_test, y_test, beta)

    print(f"n_train={len(train_idx)}, n_test={len(test_idx)}, p=16 predictors (1 real + 15 pure noise)")
    print(f"RSE on training data: {rse_train:.4f}")
    print(f"RMSE on test data:    {rmse_test:.4f}")
    print(f"Difference (test - train): {rmse_test - rse_train:.4f}")
    print("The overparameterized model fits training noise (low train RSE) but")
    print("fails to generalize (much higher test RMSE): a clear overfitting signature.")


def k_fold_cross_validation(X, y, k=5, seed=7):
    """Implements k-fold CV from scratch and returns per-fold R^2 scores."""
    n = len(y)
    rng = np.random.default_rng(seed=seed)
    indices = rng.permutation(n)
    folds = np.array_split(indices, k)

    r2_scores = []
    for i in range(k):
        test_idx = folds[i]
        train_idx = np.concatenate([folds[j] for j in range(k) if j != i])

        beta = fit_ols(X[train_idx], y[train_idx])
        y_pred = X[test_idx] @ beta
        y_test = y[test_idx]

        ss_res = np.sum((y_test - y_pred) ** 2)
        ss_tot = np.sum((y_test - y_test.mean()) ** 2)
        r2_scores.append(1 - ss_res / ss_tot)

    return np.array(r2_scores)


def k_fold_demo():
    """Runs 5-fold CV on a single model and reports per-fold and averaged R^2."""
    print("\n=== Block 2: k-Fold Cross-Validation from Scratch ===")
    rng = np.random.default_rng(seed=15)
    n = 200
    x1 = rng.uniform(0, 300, n)
    x2 = rng.uniform(0, 50, n)
    y = 3.0 + 0.045 * x1 + 0.19 * x2 + rng.normal(scale=1.8, size=n)
    X = np.column_stack([np.ones(n), x1, x2])

    r2_scores = k_fold_cross_validation(X, y, k=5)
    for fold, r2 in enumerate(r2_scores, 1):
        print(f"Fold {fold}: R^2 = {r2:.4f}")
    print(f"Mean R^2 = {r2_scores.mean():.4f} +/- {r2_scores.std():.4f}")

    return x1, x2, y


def compare_models_with_cv(x1, x2, y):
    """Compares a single-predictor model against a two-predictor model via CV."""
    print("\n=== Block 3: Comparing Models via Cross-Validated R^2 ===")
    n = len(y)
    X_simple = np.column_stack([np.ones(n), x1])
    X_full = np.column_stack([np.ones(n), x1, x2])

    r2_simple = k_fold_cross_validation(X_simple, y, k=5)
    r2_full = k_fold_cross_validation(X_full, y, k=5)

    print(f"Model 1 (x1 only):      mean R^2 = {r2_simple.mean():.4f} +/- {r2_simple.std():.4f}")
    print(f"Model 2 (x1 + x2):      mean R^2 = {r2_full.mean():.4f} +/- {r2_full.std():.4f}")
    print("The model with a higher cross-validated R^2 and lower variability")
    print("across folds generalizes better to unseen data.")


if __name__ == "__main__":
    train_test_split_and_overfitting_check()
    x1, x2, y = k_fold_demo()
    compare_models_with_cv(x1, x2, y)
