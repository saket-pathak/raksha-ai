# 🕳️ Pothole Detection Model

This directory contains the machine learning classification pipeline for detecting road pothole hazards using image-derived color and texture statistics.

---

## 📁 Files Reference

- **`model.py`**: Wrapper class (`PotholeDetectionModel`) that abstracts prediction, formatting, and classification logic.
- **`pothole_detection.py`**: Core pipeline script handling preprocessing and feature extraction from raw images.
- **`predict.py`**: Command Line Interface (CLI) script for classifying a single target image.
- **`train.py`**: Training script to fit a Scikit-Learn `RandomForestClassifier` on tabular image statistics.
- **`demo.py`**: End-to-end sandbox runner that constructs a demo model, saves the joblib binary, and evaluates a mockup feature set.
- **`generate_sample_image.py`**: Utility to generate a placeholder image for CLI/testing runs.
- **`sample_training_data.csv`**: Synthetic tabular dataset containing image statistics (`mean_red`, `mean_green`, `mean_blue`, `std_red`, `std_green`, `std_blue`) and class labels.
- **`requirements.txt`**: Python dependencies for the AI model pipeline (pandas, scikit-learn, joblib, pillow).

---

## ⚡ Quick Start

### 1️⃣ Run the End-to-End Demo
To train a demo model using the sample CSV and run an evaluation:
```bash
python demo.py
```

### 2️⃣ Evaluate a Single Image
First, generate a dummy image (if you don't have one):
```bash
python generate_sample_image.py
```
Then classify the image using the CLI:
```bash
python predict.py sample_image.png
```

---

## 🏋️ Training Custom Models

To train the Random Forest classifier on your own dataset, format your data into a CSV with the following columns:
- `mean_red` (float): Mean red channel intensity
- `mean_green` (float): Mean green channel intensity
- `mean_blue` (float): Mean blue channel intensity
- `std_red` (float): Standard deviation of red channel intensity
- `std_green` (float): Standard deviation of green channel intensity
- `std_blue` (float): Standard deviation of blue channel intensity
- `label` (int/string): Class label (e.g. `pothole`, `clear`)

Run the training pipeline:
```bash
python train.py your_training_data.csv --output artifacts/custom_pothole_model.joblib
```

---

## 🤝 Backend Integration

The Flask backend integrates with this pipeline asynchronously via `backend/services/ai_bridge.py`:
1. Citizens upload images to `/roads/detect`.
2. The `ai_bridge` spins up a background thread job.
3. The bridge extracts features from the uploaded image and evaluates them using the pothole model loader (`backend/models/RoadModel.py`).
4. The client polls the status using `/roads/detect/<job_id>` until the classification is complete.
