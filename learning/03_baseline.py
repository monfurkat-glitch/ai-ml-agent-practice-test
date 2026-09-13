"""Lesson 3 training example: baseline vs LogisticRegression.

This file intentionally keeps one fixed preparation and split.
It creates real train/validation metrics and keeps the test split protected.
"""

from pathlib import Path

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results"
RESULTS_FILE = RESULTS_DIR / "lesson03_metrics.csv"


def main() -> None:
    print("=== L03 BASELINE PRACTICE ===")

    # 1) Load the same small teaching dataset used for the class example.
    iris = load_iris(as_frame=True)
    X = iris.data.copy()
    y = iris.target.copy()
    print(f"Data: Iris | rows={len(X)} | features={X.shape[1]}")

    # 2) Lock away the protected test set first.
    X_dev, X_test, y_dev, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        stratify=y,
        random_state=42,
    )

    # 3) Split the remaining development data into train and validation.
    X_train, X_val, y_train, y_val = train_test_split(
        X_dev,
        y_dev,
        test_size=0.25,
        stratify=y_dev,
        random_state=42,
    )

    print(
        f"Split: train={len(X_train)} | validation={len(X_val)} | "
        f"test(protected)={len(X_test)}"
    )
    print("Protected test score: NOT RUN")

    # 4) Simple reference strategy: always predict the most frequent class.
    baseline = DummyClassifier(strategy="most_frequent")
    baseline.fit(X_train, y_train)

    baseline_train_acc = accuracy_score(y_train, baseline.predict(X_train))
    baseline_val_acc = accuracy_score(y_val, baseline.predict(X_val))

    # 5) Real trained classifier using the same train/validation data.
    logistic = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("model", LogisticRegression(max_iter=500)),
        ]
    )
    logistic.fit(X_train, y_train)

    logistic_train_acc = accuracy_score(y_train, logistic.predict(X_train))
    logistic_val_acc = accuracy_score(y_val, logistic.predict(X_val))

    results = pd.DataFrame(
        [
            {
                "model": "DummyClassifier",
                "split": "train",
                "metric": "accuracy",
                "value": baseline_train_acc,
            },
            {
                "model": "DummyClassifier",
                "split": "validation",
                "metric": "accuracy",
                "value": baseline_val_acc,
            },
            {
                "model": "LogisticRegression",
                "split": "train",
                "metric": "accuracy",
                "value": logistic_train_acc,
            },
            {
                "model": "LogisticRegression",
                "split": "validation",
                "metric": "accuracy",
                "value": logistic_val_acc,
            },
        ]
    )
    results["value"] = results["value"].round(6)

    RESULTS_DIR.mkdir(exist_ok=True)
    results.to_csv(RESULTS_FILE, index=False)

    print("\nReal results:")
    print(results.to_string(index=False))
    print(f"\nSaved: {RESULTS_FILE.relative_to(ROOT)}")
    print("CHECKPOINT: compare the two VALIDATION rows; keep test protected.")


if __name__ == "__main__":
    main()
