"""
Computational Lab: Section 09.10 - Linear Regression with scikit-learn
====================================================================
NOTE ON LIBRARY POLICY: this project's Python labs are numpy/scipy only.
This single section is an explicit, approved exception: its entire subject
is the scikit-learn API itself, so the lab imports scikit-learn directly
(LinearRegression, train_test_split, RFE) to actually demonstrate it.

Fits a linear model with scikit-learn's train/test split workflow, verifies
its coefficients agree exactly with the from-scratch OLS engine built in
Section 09.03, and performs Recursive Feature Elimination (RFE) to rank and
select predictors automatically.

Author: Juliho Castillo Colmenares
Institution: Tecnologico de Monterrey
"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import RFE


def scikit_learn_fit_workflow():
    """Fits a scikit-learn LinearRegression using the standard train/test workflow."""
    print("=== Block 1: scikit-learn Fit, Score, and Predict Workflow ===")
    rng = np.random.default_rng(seed=3)
    n = 200
    tv = rng.uniform(0.7, 296.4, n)
    radio = rng.uniform(0, 49.6, n)
    sales = 2.92 + 0.046 * tv + 0.188 * radio + rng.normal(scale=1.7, size=n)

    X = np.column_stack([tv, radio])
    X_train, X_test, y_train, y_test = train_test_split(X, sales, test_size=0.2, random_state=42)

    lm = LinearRegression()
    lm.fit(X_train, y_train)

    print(f"Intercept: {lm.intercept_:.4f}")
    print(f"Coefficients (TV, Radio): {np.round(lm.coef_, 4)}")
    print(f"R^2 on training data: {lm.score(X_train, y_train):.4f}")
    print(f"R^2 on test data:     {lm.score(X_test, y_test):.4f}")

    return X_train, y_train, lm


def verify_against_scratch_ols(X_train, y_train, lm):
    """Verifies scikit-learn's coefficients match the from-scratch Normal Equation solution."""
    print("\n=== Block 2: Cross-Checking Against the Section 09.03/09.07 OLS Engine ===")
    n = len(y_train)
    X_design = np.column_stack([np.ones(n), X_train])
    beta_scratch = np.linalg.inv(X_design.T @ X_design) @ X_design.T @ y_train

    beta_sklearn = np.concatenate([[lm.intercept_], lm.coef_])
    max_diff = np.max(np.abs(beta_scratch - beta_sklearn))

    print(f"From-scratch (X^T X)^-1 X^T Y: {np.round(beta_scratch, 6)}")
    print(f"scikit-learn LinearRegression: {np.round(beta_sklearn, 6)}")
    print(f"Max absolute difference: {max_diff:.2e} (scikit-learn uses the same OLS mathematics)")


def recursive_feature_elimination_demo():
    """Runs RFE to automatically rank and select the most relevant predictors."""
    print("\n=== Block 3: Recursive Feature Elimination (RFE) ===")
    rng = np.random.default_rng(seed=3)
    n = 200
    tv = rng.uniform(0.7, 296.4, n)
    radio = rng.uniform(0, 49.6, n)
    newspaper = rng.uniform(0, 114.0, n)
    sales = 2.92 + 0.046 * tv + 0.188 * radio + 0.001 * newspaper + rng.normal(scale=1.7, size=n)

    X = np.column_stack([tv, radio, newspaper])
    feature_names = ["TV", "Radio", "Newspaper"]

    estimator = LinearRegression()
    selector = RFE(estimator, n_features_to_select=2, step=1)
    selector.fit(X, sales)

    print(f"Feature support (selected=True): {dict(zip(feature_names, selector.support_))}")
    print(f"Feature ranking (1=selected, higher=eliminated earlier): {dict(zip(feature_names, selector.ranking_))}")
    print("TV and Radio are selected; Newspaper (negligible true coefficient) is eliminated,")
    print("matching the manual model-comparison conclusions of Section 09.02/09.07.")


if __name__ == "__main__":
    X_train, y_train, lm = scikit_learn_fit_workflow()
    verify_against_scratch_ols(X_train, y_train, lm)
    recursive_feature_elimination_demo()
