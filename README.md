# AI/ML Agent Workflow Practice

A tiny training repository for **Lesson 2 + Lesson 3**.

The goal is not to build a personal Capstone yet. The goal is to learn one safe workflow:

**GitHub repo → local clone → first commit/push → inspect with an agent → run a baseline → approve one small change → CHECK → review diff → commit/push → update project status.**

## What this repository contains

```text
ai-ml-agent-practice/
├── README.md
├── AGENTS.md
├── PROJECT_STATUS.md
├── .gitignore
├── requirements.txt
├── docs/
│   └── learning_notes.md
├── learning/
│   └── 03_baseline.py
└── scripts/
    └── check_report.py
```

The `results/` folder is created **only after you run the baseline**.

## The 3 core project files

- `AGENTS.md` — simple rules for the coding agent.
- `PROJECT_STATUS.md` — what is true in the project right now: completed work, blockers, and next step.
- `README.md` — a human-readable overview: what the project is and how to use it.

## ML exercise

`learning/03_baseline.py` uses the small Iris dataset and compares:

1. `DummyClassifier(strategy="most_frequent")` — a simple baseline.
2. `LogisticRegression` — a trained classification model.

Both models use the **same train/validation split** and the **same accuracy metric**.
The final test split is created but kept protected. It is not used to choose the model.

Run:

```bash
python learning/03_baseline.py
```

On some Windows computers use:

```bash
py learning/03_baseline.py
```

After the run you should have:

```text
results/lesson03_metrics.csv
```

## Agent task

The agent must **not improve the model**. It has one small job:

> Read the real validation results and fill the comparison table in `docs/learning_notes.md`.

Then run:

```bash
python scripts/check_report.py
```

A successful result ends with `PASS`.

## Important safety rules

- Do not change the data split during the agent task.
- Do not change `DummyClassifier` or `LogisticRegression` during the agent task.
- Do not change the metric.
- Do not use the protected test set.
- Do not invent numbers.
- Do not commit or push before you have reviewed the real change.

Read `AGENTS.md` before asking the agent to work.
