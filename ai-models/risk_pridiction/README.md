# ⚠️ Risk Prediction Model

This directory contains the pipeline for modeling accident risk scoring, route profiling, and localized hazard alerts based on geographic features and environmental metadata.

---

## 📁 Files Reference

- **`model.py`**: Wrapper class (`RiskPredictionModel`) providing explainable scoring rules. It combines numerical inputs (lat, lng) and categorical conditions (weather, traffic, roads) to produce hazard indicators.
- **`utils.py`**: Helper statistics and factor mappings mapping categorical inputs to risk values.
- **`predict.py`**: CLI tool for producing risk index scores from inputs.
- **`train.py`**: Tabular training pipeline to fit an estimator model on geographical risk datasets.
- **`demo.py`**: Sandbox script that trains a pipeline model using Scikit-Learn's `ColumnTransformer` + `RandomForestClassifier` on synthetic data, exports the joblib file, and runs a mock prediction.
- **`sample_training_data.csv`**: Starter synthetic dataset.
- **`requirements.txt`**: Project dependencies (scikit-learn, joblib, pandas).

---

## ⚡ Quick Start

### 1️⃣ Run the Sandbox Demo
To train the random forest classifier on the synthetic dataset and output a mock prediction:
```bash
python demo.py
```

### 2️⃣ Query the Risk CLI
Use `predict.py` to evaluate custom hazard factors directly:
```bash
python predict.py --lat 28.61 --lng 77.20 --time peak --weather rain --road pothole --traffic heavy --zone "NH-48"
```

---

## 🎛️ Risk Evaluation Parameters

The risk scoring pipeline evaluates the following categories:

| Parameter | Type | Example Values |
| :--- | :---: | :--- |
| `--lat` | `float` | `28.61` |
| `--lng` | `float` | `77.20` |
| `--time` | `string`| `peak`, `morning`, `night`, `busy` |
| `--weather`| `string`| `rain`, `heavy rain`, `fog`, `storm`, `clear` |
| `--road` | `string`| `pothole`, `waterlogging`, `damaged`, `construction`, `good` |
| `--traffic`| `string`| `heavy`, `congested`, `slow`, `moderate`, `light` |
| `--zone` | `string`| `NH-48 Ring Road`, `Mathura Road Flyover` |

---

## 🏋️ Training Custom Models

To train on your own real-world crash or hazard history, prepare a CSV with columns matching the parameters list above (plus a binary/categorical `label` column).

Run the training pipeline:
```bash
python train.py path/to/dataset.csv --output artifacts/custom_risk_model.joblib
```
