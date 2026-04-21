# ML Models Directory

## 📁 About This Folder

This folder contains trained machine learning models for the Financial Intelligence App.

**Note**: Model files (`.pkl`) are **NOT** tracked in Git due to their large size (100+ MB).

---

## 🚀 How to Generate Models

### Step 1: Ensure Dataset is Available
```bash
# Check if dataset exists
ls ml_model/data/UCI_Credit_Card.csv
```

### Step 2: Train Models
```bash
# Navigate to ml_model directory
cd ml_model

# Run training script
python train.py
```

### Step 3: Verify Models Created
```bash
# Check models folder
ls models/

# You should see:
# - spending_predictor.pkl
# - category_classifier.pkl
# - scaler.pkl
# - feature_names.json
```

---

## 📦 Model Files

### 1. `spending_predictor.pkl`
- **Type**: Random Forest Regressor
- **Purpose**: Predict next month's spending
- **Size**: ~176 MB
- **Accuracy**: High (trained on 30K records)

### 2. `category_classifier.pkl`
- **Type**: Logistic Regression
- **Purpose**: Classify spending behavior (Conservative/Moderate/Aggressive)
- **Size**: ~50 MB
- **Accuracy**: 80.98%

### 3. `scaler.pkl`
- **Type**: StandardScaler
- **Purpose**: Feature normalization
- **Size**: ~10 KB

### 4. `feature_names.json`
- **Type**: JSON file
- **Purpose**: Store feature names for model input
- **Size**: ~1 KB

---

## 🔧 Training Configuration

### Dataset
- **Source**: UCI Credit Card Default Dataset
- **Records**: 30,000 customers
- **Features**: 23 financial indicators
- **Target**: Default payment prediction

### Models
```python
# Random Forest
RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

# Logistic Regression
LogisticRegression(
    max_iter=1000,
    random_state=42
)
```

---

## 📊 Model Performance

### Random Forest (Best Model)
- **Accuracy**: 81.10%
- **ROC-AUC**: 0.7592
- **Precision**: 64%
- **Recall**: 36%
- **F1-Score**: 0.46

### Logistic Regression
- **Accuracy**: 80.98%
- **ROC-AUC**: 0.7244
- **Precision**: 72%
- **Recall**: 24%
- **F1-Score**: 0.36

---

## 🚨 Important Notes

### Why Models Are Not in Git
- **Size**: Models exceed GitHub's 100 MB file limit
- **Solution**: Generate locally or use Git LFS
- **Alternative**: Download pre-trained models from release

### Git LFS (Optional)
If you want to track models in Git:
```bash
# Install Git LFS
git lfs install

# Track .pkl files
git lfs track "*.pkl"

# Add and commit
git add .gitattributes
git add ml_model/models/*.pkl
git commit -m "Add ML models with Git LFS"
git push
```

---

## 🔄 Regenerating Models

### When to Retrain
- New data available
- Model performance degrades
- Feature engineering changes
- Hyperparameter tuning

### Quick Retrain
```bash
# Delete old models
rm ml_model/models/*.pkl

# Retrain
cd ml_model
python train.py

# Verify
ls models/
```

---

## 📝 Model Usage

### In Backend (main.py)
```python
from ml_model.predict import ml_predictor

# Generate advice
advice = ml_predictor.generate_ml_advice(user_data, amount)

# Predict spending
prediction = ml_predictor.predict_next_month_spending(user_data)

# Classify behavior
category = ml_predictor.classify_spending_behavior(user_data)
```

---

## 🐛 Troubleshooting

### Issue: Models Not Found
```bash
# Error: FileNotFoundError: ml_model/models/spending_predictor.pkl

# Solution: Train models
cd ml_model
python train.py
```

### Issue: Training Fails
```bash
# Error: Dataset not found

# Solution: Check dataset path
ls ml_model/data/UCI_Credit_Card.csv

# If missing, download dataset
python ml_model/download_dataset.py
```

### Issue: Import Error
```bash
# Error: ModuleNotFoundError: No module named 'sklearn'

# Solution: Install dependencies
pip install -r requirements.txt
```

---

## 📦 Pre-trained Models (Alternative)

If you don't want to train models locally:

### Option 1: Download from Release
```bash
# Download from GitHub Releases
# (Add release with pre-trained models)
```

### Option 2: Use Cloud Storage
```bash
# Download from Google Drive / Dropbox
# (Share link with pre-trained models)
```

### Option 3: Use Smaller Models
```bash
# Train with fewer estimators
# Edit train.py:
# n_estimators=10 (instead of 100)
```

---

## 🎯 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Train models
cd ml_model
python train.py

# 3. Verify models
ls models/

# 4. Run backend
cd ..
uvicorn main:app --reload

# 5. Test ML predictions
# Models will be loaded automatically
```

---

## 📊 Model Metrics

### Training Time
- Random Forest: ~2-3 minutes
- Logistic Regression: ~30 seconds
- Total: ~3-4 minutes

### Model Sizes
- spending_predictor.pkl: ~176 MB
- category_classifier.pkl: ~50 MB
- scaler.pkl: ~10 KB
- feature_names.json: ~1 KB
- **Total**: ~226 MB

---

## 🔐 Security Note

- Models contain no sensitive data
- Only statistical patterns learned
- Safe to share publicly
- No PII or credentials

---

## 📞 Need Help?

- Check `ml_model/train.py` for training code
- Check `ml_model/predict.py` for inference code
- See `ANALYSIS_REPORT.md` for model details
- Open GitHub issue for support

---

**Models are ready to use once trained! 🚀**
