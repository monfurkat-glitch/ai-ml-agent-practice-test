"""Check that the markdown table uses the real validation metrics."""

from pathlib import Path
import re
import sys

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
METRICS = ROOT / "results" / "lesson03_metrics.csv"
NOTES = ROOT / "docs" / "learning_notes.md"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> None:
    if not METRICS.exists():
        fail("results/lesson03_metrics.csv does not exist. Run the baseline first.")
    if not NOTES.exists():
        fail("docs/learning_notes.md does not exist.")

    metrics = pd.read_csv(METRICS)
    validation = metrics[metrics["split"] == "validation"].copy()

    expected_models = {"DummyClassifier", "LogisticRegression"}
    if set(validation["model"]) != expected_models or len(validation) != 2:
        fail("metrics CSV must contain exactly two validation rows for the two expected models.")

    expected = {
        row["model"]: float(row["value"])
        for _, row in validation.iterrows()
    }

    text = NOTES.read_text(encoding="utf-8")
    block_match = re.search(
        r"<!-- AGENT_TABLE_START -->(.*?)<!-- AGENT_TABLE_END -->",
        text,
        flags=re.S,
    )
    if not block_match:
        fail("agent table markers are missing from docs/learning_notes.md.")

    block = block_match.group(1)
    if "TODO" in block:
        fail("comparison table still contains TODO values.")

    found = {}
    row_pattern = re.compile(
        r"\|\s*(DummyClassifier|LogisticRegression)\s*"
        r"\|\s*validation\s*"
        r"\|\s*accuracy\s*"
        r"\|\s*([0-9]*\.?[0-9]+)\s*\|"
    )
    for model, value in row_pattern.findall(block):
        found[model] = float(value)

    if set(found) != expected_models:
        fail("table must contain exactly the DummyClassifier and LogisticRegression validation rows.")

    for model in sorted(expected_models):
        if abs(found[model] - expected[model]) > 1e-6:
            fail(
                f"{model} value does not match the real CSV: "
                f"table={found[model]} csv={expected[model]}"
            )

    print("PASS: comparison table matches the real validation metrics.")
    for model in ["DummyClassifier", "LogisticRegression"]:
        print(f"  {model}: validation accuracy = {expected[model]:.6f}")


if __name__ == "__main__":
    main()
