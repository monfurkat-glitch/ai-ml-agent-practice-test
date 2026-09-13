# PROJECT_STATUS.md

## Current stage

Baseline has been run and verified. The comparison table in `docs/learning_notes.md` has been filled with the real validation values and the report check passes. Git commit/push for this change is still pending.

## Last verified result

- Baseline run: **VERIFIED** (ran `learning/03_baseline.py`, real output captured)
- Report check: **PASS** (ran `scripts/check_report.py`, output: "PASS: comparison table matches the real validation metrics.")
- Remote push: **NOT VERIFIED** (commit and push not yet run)

## Current verified result

From `results/lesson03_metrics.csv` (validation split, accuracy):

- DummyClassifier: 0.333333
- LogisticRegression: 0.933333

## Current constraints

- Keep the same Iris data.
- Keep the same train / validation / protected test split.
- Keep `DummyClassifier` and `LogisticRegression`.
- Keep accuracy as the comparison metric.
- Do not use the protected test set for model selection.
- Do not invent or manually change measured values.

## Open blockers / unfinished work

- `docs/learning_notes.md` table is filled but the change is not yet committed or pushed to `origin/main`.
- The "My explanation without AI" section in `docs/learning_notes.md` is still unfilled (student to write by hand).

## Next action

Choose and confirm a personal project brief.

## Commit info

- Branch: `main`
- Remote: `origin` (`https://github.com/monfurkat-glitch/ai-ml-agent-practice-test.git`)
- Current commit hash (HEAD, before the pending `docs/learning_notes.md` change): `d3f639744414003027bf513fd136fc412f779627`

## Brief status

Training repository baseline exercise verified. This training repository is completed **before** choosing the personal Capstone project.
