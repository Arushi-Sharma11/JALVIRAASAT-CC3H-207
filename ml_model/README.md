# ML Model Training Guide

## 📁 Project Structure

```
ml_model/
├── data/               # Training datasets
├── models/             # Saved trained models
├── notebooks/          # Jupyter notebooks for experimentation
├── train.py           # Model training script
└── predict.py         # Inference module
```

## 🚀 Quick Start

### 1. Install ML Dependencies

```bash
pip install scikit-learn pandas numpy joblib
```

### 2. Train Models

```bash
python ml_model/train.py
```

This will:
- Generate sample training data (or use your own CSV)
- Train 2 models:
  - **Spending Predictor** (Regression) - Predicts next month spending
  - **Category Classifier** (Classification) - Classifies spending behavior
- Save models to `ml_model/models/`

### 3. Use Models in Backend

The models are automatically loaded in `main.py` via `ml_model/predict.py`

## 📊 Models Trained

### 1. Spending Predictor (Random Forest Regressor)
**Purpose:** Predict user's next month spending

**Features:**
- balance
- monthly_income
- age
- savings_goal
- last_month_spending
- num_transactions
- avg_transaction
- savings_rate (derived)
- spending_ratio (derived)
- goal_progress (derived)

**Output:** Predicted spending amount (₹)

### 2. Category Classifier (Random Forest Classifier)
**Purpose:** Classify spending behavior

**Categories:**
- 0 = Conservative (Low spender)
- 1 = Moderate (Average spender)
- 2 = Aggressive (High spender)

## 🔧 Customize Training

### Use Your Own Data

Replace `generate_sample_data()` in `train.py` with:

```python
def load_real_data():
    df = pd.read_csv('ml_model/data/your_data.csv')
    return df
```

Your CSV should have columns:
```
balance, monthly_income, age, savings_goal, last_month_spending, 
num_transactions, avg_transaction, next_month_spending, spending_category
```

### Tune Hyperparameters

In `train.py`, modify:

```python
model = RandomForestRegressor(
    n_estimators=200,      # More trees
    max_depth=15,          # Deeper trees
    min_samples_split=5,   # Minimum samples to split
    random_state=42
)
```

## 📈 Model Performance

After training, you'll see:

```
✓ Spending Predictor Model:
  Train R² Score: 0.XXX
  Test R² Score: 0.XXX

✓ Category Classifier Model:
  Train Accuracy: 0.XXX
  Test Accuracy: 0.XXX
```

**Good scores:**
- R² > 0.7 (Regression)
- Accuracy > 0.8 (Classification)

## 🧪 Test Predictions

```python
from ml_model.predict import ml_predictor

user_data = {
    'balance': 45280,
    'savings_goal': 10000,
    'monthly_income': 30000,
    'last_month_spending': 15000,
    'age': 28,
    'num_transactions': 25,
    'avg_transaction': 600
}

# Predict next month spending
prediction = ml_predictor.predict_next_month_spending(user_data)
print(f"Predicted spending: ₹{prediction}")

# Classify behavior
category = ml_predictor.classify_spending_behavior(user_data)
print(f"Spending type: {category}")

# Get advice
advice = ml_predictor.generate_ml_advice(user_data, current_spend_amount=500)
print(f"Advice: {advice}")
```

## 🔄 Retrain Models

As you collect more real user data:

1. Export transactions from database:
```python
import sqlite3
import pandas as pd

conn = sqlite3.connect('finance_app.db')
df = pd.read_sql_query("SELECT * FROM transactions", conn)
df.to_csv('ml_model/data/real_transactions.csv')
```

2. Preprocess and retrain:
```bash
python ml_model/train.py
```

3. Restart backend to load new models

## 🎯 Advanced: Add More Models

### Anomaly Detection (Fraud Detection)
```python
from sklearn.ensemble import IsolationForest

model = IsolationForest(contamination=0.1)
model.fit(X_train)
```

### Time Series Forecasting
```python
from statsmodels.tsa.arima.model import ARIMA

model = ARIMA(spending_history, order=(1,1,1))
model.fit()
```

### Deep Learning (Neural Networks)
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([
    Dense(64, activation='relu', input_shape=(10,)),
    Dense(32, activation='relu'),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')
```

## 📝 Notes

- Models are trained on **synthetic data** by default
- For production, collect **real user data** for 3-6 months
- Retrain models **monthly** for best accuracy
- Monitor model performance with A/B testing
