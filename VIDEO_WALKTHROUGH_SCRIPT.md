# YouTube Walkthrough Script

## Opening (30–45 sec)

Hi, I'm Kalhar. This repository recreates and extends a portfolio of sixteen data-science experiments using an AI coding assistant. I intentionally rebuilt the implementations rather than copying the reference source. Every project is runnable locally, uses deterministic data where possible, and exposes the core data-science idea through an interactive Streamlit UI.

## Project walkthrough

### 00 — Dynamic Experiment Workspace (~45–75 sec)

Open `00_dynamic_todo_workspace/app.py`. Explain: Interactive experiment tracker with priorities, progress telemetry, filters, and reproducible JSON export. Show the main controls, the primary metric/chart, and one implementation detail. Mention what makes the validation or UX more robust than a notebook-only demo.

### 01 — NYC Taxi Trip Prediction (~45–75 sec)

Open `01_nyc_taxi_trip_prediction/app.py`. Explain: Synthetic geospatial regression benchmark comparing linear, random-forest, and gradient-boosting models. Show the main controls, the primary metric/chart, and one implementation detail. Mention what makes the validation or UX more robust than a notebook-only demo.

### 02 — Nano Transformer Lab (~45–75 sec)

Open `02_nano_llm_transformer/app.py`. Explain: Educational tokenization, attention-weight visualization, and tiny next-token language modeling simulator. Show the main controls, the primary metric/chart, and one implementation detail. Mention what makes the validation or UX more robust than a notebook-only demo.

### 03 — Customer Segmentation (~45–75 sec)

Open `03_customer_segmentation_clustering/app.py`. Explain: K-Means customer segmentation with scaling, silhouette analysis, PCA projection, and persona summaries. Show the main controls, the primary metric/chart, and one implementation detail. Mention what makes the validation or UX more robust than a notebook-only demo.

### 04 — Market Basket Mining (~45–75 sec)

Open `04_associative_pattern_mining/app.py`. Explain: Apriori-style frequent itemsets and association rules with support, confidence, and lift. Show the main controls, the primary metric/chart, and one implementation detail. Mention what makes the validation or UX more robust than a notebook-only demo.

### 05 — Data Science Skills Lab (~45–75 sec)

Open `05_data_science_skills_lab/app.py`. Explain: Interactive mini-labs for distributions, sampling, feature engineering, metrics, and model selection. Show the main controls, the primary metric/chart, and one implementation detail. Mention what makes the validation or UX more robust than a notebook-only demo.

### 06 — Anomaly Detection (~45–75 sec)

Open `06_anomaly_detection/app.py`. Explain: Isolation Forest and robust z-score anomaly scoring over synthetic telemetry. Show the main controls, the primary metric/chart, and one implementation detail. Mention what makes the validation or UX more robust than a notebook-only demo.

### 07 — AutoML Benchmark (~45–75 sec)

Open `07_automl_autogluon/app.py`. Explain: Lightweight AutoML-style leaderboard across several scikit-learn models with cross-validation. Show the main controls, the primary metric/chart, and one implementation detail. Mention what makes the validation or UX more robust than a notebook-only demo.

### 08 — Visual Data Science Mastery (~45–75 sec)

Open `08_datascience_visual_mastery/app.py`. Explain: Interactive statistical visualizations: distributions, regression, PCA, confusion matrices, and calibration. Show the main controls, the primary metric/chart, and one implementation detail. Mention what makes the validation or UX more robust than a notebook-only demo.

### 09 — FlowForge DAG Engine (~45–75 sec)

Open `09_flowforge_dag_engine/app.py`. Explain: DAG dependency simulator with topological sorting, critical-path metadata, and cycle detection. Show the main controls, the primary metric/chart, and one implementation detail. Mention what makes the validation or UX more robust than a notebook-only demo.

### 10 — CRISP-DM Mastery (~45–75 sec)

Open `10_crispdm_masters_curriculum/app.py`. Explain: Guided CRISP-DM lifecycle with phase checklists, experiment notes, and downloadable project brief. Show the main controls, the primary metric/chart, and one implementation detail. Mention what makes the validation or UX more robust than a notebook-only demo.

### 11 — Enterprise Data Science Audit (~45–75 sec)

Open `11_enterprise_ds_audit/app.py`. Explain: Automated dataset quality audit for missingness, duplicates, leakage risks, imbalance, and drift proxies. Show the main controls, the primary metric/chart, and one implementation detail. Mention what makes the validation or UX more robust than a notebook-only demo.

### 12 — TimePulse Forecasting (~45–75 sec)

Open `12_timeseries_forecasting/app.py`. Explain: Trend-seasonality decomposition, lag features, walk-forward backtesting, and multi-step forecasts. Show the main controls, the primary metric/chart, and one implementation detail. Mention what makes the validation or UX more robust than a notebook-only demo.

### 13 — NYC Taxi Audit Platform (~45–75 sec)

Open `13_crispdm_nyc_taxi_audit_platform/app.py`. Explain: CRISP-DM style taxi workflow combining data-quality audit, model evaluation, and explainability. Show the main controls, the primary metric/chart, and one implementation detail. Mention what makes the validation or UX more robust than a notebook-only demo.

### 14 — Multimodal AutoML Suite (~45–75 sec)

Open `14_autogluon_multimodal_automl_suite/app.py`. Explain: Tabular plus synthetic text feature fusion with model leaderboard and late-fusion comparison. Show the main controls, the primary metric/chart, and one implementation detail. Mention what makes the validation or UX more robust than a notebook-only demo.

### 15 — SPY Forecasting Research Lab (~45–75 sec)

Open `15_spy_timeseries_sota_forecasting/app.py`. Explain: Synthetic market-return research with leakage-safe lag features, walk-forward validation, and strategy metrics. Show the main controls, the primary metric/chart, and one implementation detail. Mention what makes the validation or UX more robust than a notebook-only demo.

## Closing (30 sec)

Show `PROMPTS.md`, `EXPERIMENT_NOTES.md`, and the top-level README. Explain that the AI assistant accelerated scaffolding and iteration, while the final repository standardizes reproducibility, validation, and UX. Finally, paste the uploaded YouTube URL into the README's Video Walkthrough section.

## Recording checklist

- Show the repository root and README first.
- Launch at least every project once; spend extra time on taxi prediction, clustering, anomaly detection, AutoML, time-series, multimodal, and SPY research.
- Show code and UX for each project.
- Mention that data is synthetic/local so the demos do not depend on external APIs.
- End on `PROMPTS.md` and explain how prompts were adapted instead of copied.
