# Experiment Notes

## Design principles

1. **Original implementation** — replicate learning objectives, not source code.
2. **No hidden network dependency** — synthetic datasets keep demos reliable.
3. **Leakage awareness** — chronological splits for time series and holdouts/CV for supervised learning.
4. **Observable results** — every app exposes metrics, tables, charts, or interactive controls.
5. **Grader-friendly** — one dependency file and a uniform run pattern.

## Extensions beyond the reference minimum

- Shared UI conventions and a single launcher.
- Interactive model/parameter exploration.
- Data-quality and leakage audit concepts.
- Walk-forward forecasting and strategy comparison in the market project.
- Multimodal late fusion using tabular + TF-IDF text features.
- Exportable CRISP-DM and task-workspace artifacts.
