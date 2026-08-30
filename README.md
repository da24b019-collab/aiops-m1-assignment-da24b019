# AIOps Module 1 Assignment

**Author:** Dhanush (DA24B019)
**Course:** AI Operations (AIOps)

This repository contains the work for Questions 1–3 of the Module 1 assignment. Question 4
(the paired capstone with partner DA24B020) is submitted as a separate joint repository,
linked below.

---

## Question 1 — Technical Debt Diagnosis

Conceptual analysis mapping three scenarios (feature entanglement, an undeclared downstream
consumer, and an undocumented shell-script pipeline) to the six hidden-technical-debt
categories from Lecture 1, plus one proposed mitigation using MLflow Projects.

**Deliverable:** [`AIOPS_Assgn_1.pdf`](./AIOPS_Assgn_1.pdf)

---

## Question 2 — MLflow Experiment Comparison

**Folder:** [`q2-mlflow/`](./q2-mlflow/)

Trains an `MLPClassifier` on a 10,000-image MNIST subsample (in place of the lecture's
RandomForest-on-IRIS baseline), sweeping two hyperparameters — `learning_rate_init`
(0.1, 0.01, 0.001) and `batch_size` (32, 128) — across six MLflow-tracked runs. Per-epoch
`train_loss` and `val_accuracy` are logged as time-series metrics to support overfitting
analysis.

**Contents:**
- `train_mnist_mlp.py` — training script with manual `mlflow.log_param` / `mlflow.log_metric`
  calls
- `mlflow_comparison.png` — screenshot of the MLflow UI's 6-run comparison table

**To reproduce:**
```bash
cd q2-mlflow
pip install mlflow scikit-learn
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns \
    --host 0.0.0.0 --port 5000   # in one terminal
python train_mnist_mlp.py         # in a second terminal
```

---

## Question 3 — DVC Data Versioning & Rollback

**Folder:** [`q3-dvc/`](./q3-dvc/)

A filename-list CSV (`data.csv`) generated from the `data/` directory (sourced via
`dvc get` from the `iterative/dataset-registry` tutorial dataset) is tracked and versioned
with DVC across two revisions:

| Version | Tag | Row count (excl. header) |
|---|---|---|
| v1 | `v1` | 1,800 |
| v2 | `v2` | 2,800 |

**Contents:**
- `create_csv.py` — script that builds `data.csv` from the contents of `data/`
- `data.csv` / `data.csv.dvc` — the tracked file list and its DVC pointer
- `data/` — the extracted image dataset (DVC-cached, not directly committed to Git)

**Rollback verification:**
```bash
git checkout v1
dvc checkout
wc -l data.csv   # confirms row count matches v1 exactly
```

---

## Question 4 — Capstone: End-to-End Reproducibility Drill

Completed jointly with partner **DA24B020**, in a separate repository so that both partners'
commit history is preserved independently.

**Repo:** https://github.com/DA24B020/aiops-m1-da24b019-da24b020

Summary of the protocol followed:
1. Partner A (DA24B019) trained a model with a fixed seed, logged the run to MLflow (params,
   metrics, a `git_commit` tag, and the model artifact), versioned the dataset with DVC, and
   committed code + `.dvc` file together in a single commit. The model was registered and
   transitioned to the `Staging` stage.
2. Partner A shared the repository URL and commit hash with Partner B — no further
   communication about environment, data, or hyperparameters.
3. Partner B reproduced the result using only `git clone`, `git checkout <commit>`,
   `dvc checkout`, and `mamba env create -f environment.yml`, then reran the training script.
4. Partner B logged a note on the original MLflow run documenting whether the reproduced
   metric matched within tolerance.

---

## Repository Structure

```
aiops-m1-assignment/
├── AIOPS_Assgn_1.pdf        # Q1 write-up
├── q2-mlflow/
│   ├── train_mnist_mlp.py
│   └── mlflow_comparison.png
├── q3-dvc/
│   ├── create_csv.py
│   ├── data.csv
│   ├── data.csv.dvc
│   └── data/
├── .dvc/
├── .dvcignore
└── README.md
```
