# AI-Assisted Data Science Experiments

- Name : Kalhar Mayurbhai Patel
- SJSU ID: 019140511

A runnable replication and extension of the public `dlmastery/data_science_examples` experiment catalog. The goal is not to copy source code; each project is rebuilt as a compact Streamlit application emphasizing reproducibility, modeling intuition, and clean UX.

## 🎥 Video Walkthrough

**YouTube:** https://youtu.be/r8yICoUDxsM

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run_app.py
```

Or run any project directly:

```bash
streamlit run 01_nyc_taxi_trip_prediction/app.py
```

## Authentication and security

This is a local, single-user Streamlit portfolio and currently has no
application authentication, external API credentials, tokens, or protected
backend endpoints. See [`AUTHENTICATION.md`](AUTHENTICATION.md) for the
component inventory, request flow, and credential-handling analysis.

## Project Portfolio

| # | Project | Main idea |
|---|---|---|
| 00 | [Dynamic Experiment Workspace](00_dynamic_todo_workspace/) | Interactive experiment tracker with priorities, progress telemetry, filters, and reproducible JSON export. |
| 01 | [NYC Taxi Trip Prediction](01_nyc_taxi_trip_prediction/) | Synthetic geospatial regression benchmark comparing linear, random-forest, and gradient-boosting models. |
| 02 | [Nano Transformer Lab](02_nano_llm_transformer/) | Educational tokenization, attention-weight visualization, and tiny next-token language modeling simulator. |
| 03 | [Customer Segmentation](03_customer_segmentation_clustering/) | K-Means customer segmentation with scaling, silhouette analysis, PCA projection, and persona summaries. |
| 04 | [Market Basket Mining](04_associative_pattern_mining/) | Apriori-style frequent itemsets and association rules with support, confidence, and lift. |
| 05 | [Data Science Skills Lab](05_data_science_skills_lab/) | Interactive mini-labs for distributions, sampling, feature engineering, metrics, and model selection. |
| 06 | [Anomaly Detection](06_anomaly_detection/) | Isolation Forest and robust z-score anomaly scoring over synthetic telemetry. |
| 07 | [AutoML Benchmark](07_automl_autogluon/) | Lightweight AutoML-style leaderboard across several scikit-learn models with cross-validation. |
| 08 | [Visual Data Science Mastery](08_datascience_visual_mastery/) | Interactive statistical visualizations: distributions, regression, PCA, confusion matrices, and calibration. |
| 09 | [FlowForge DAG Engine](09_flowforge_dag_engine/) | DAG dependency simulator with topological sorting, critical-path metadata, and cycle detection. |
| 10 | [CRISP-DM Mastery](10_crispdm_masters_curriculum/) | Guided CRISP-DM lifecycle with phase checklists, experiment notes, and downloadable project brief. |
| 11 | [Enterprise Data Science Audit](11_enterprise_ds_audit/) | Automated dataset quality audit for missingness, duplicates, leakage risks, imbalance, and drift proxies. |
| 12 | [TimePulse Forecasting](12_timeseries_forecasting/) | Trend-seasonality decomposition, lag features, walk-forward backtesting, and multi-step forecasts. |
| 13 | [NYC Taxi Audit Platform](13_crispdm_nyc_taxi_audit_platform/) | CRISP-DM style taxi workflow combining data-quality audit, model evaluation, and explainability. |
| 14 | [Multimodal AutoML Suite](14_autogluon_multimodal_automl_suite/) | Tabular plus synthetic text feature fusion with model leaderboard and late-fusion comparison. |
| 15 | [SPY Forecasting Research Lab](15_spy_timeseries_sota_forecasting/) | Synthetic market-return research with leakage-safe lag features, walk-forward validation, and strategy metrics. |

## What I improved

- Rebuilt all experiments with a consistent Streamlit UX.
- Added deterministic synthetic datasets so every project runs without external downloads or API keys.
- Added model comparisons, leakage-safe validation patterns, explainability-oriented outputs, and exportable artifacts where useful.
- Kept each project independent and easy to demo in a classroom or grading environment.
- Added a single launcher plus a complete narration script for the required YouTube walkthrough.

## AI Workflow

See [`PROMPTS.md`](PROMPTS.md) for the prompt sequence and [`EXPERIMENT_NOTES.md`](EXPERIMENT_NOTES.md) for technical decisions, assumptions, and extensions.

## Academic note

This repository is an original educational implementation inspired by a public experiment catalog. It intentionally avoids copying the reference repository's source code and uses synthetic/local data so results are reproducible.
