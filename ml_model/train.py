"""
ML Model Training Script for Financial Behavior Prediction
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib
import json

# ============================================
# 1. DATA PREPARATION
# ============================================

def load_data():
    """Load real or synthetic data"""
    import os
    
    # Try to load real dataset first
    if os.path.exists('ml_model/data/UCI_Credit_Card.csv'):
        print("Loading UCI Credit Card dataset...")
        df = pd.read_csv('ml_model/data/UCI_Credit_Card.csv')
        print(f"[OK] Loaded {len(df)} real records")
        
        # Process UCI dataset to match our features
        processed_df = pd.DataFrame({
            'balance': df['LIMIT_BAL'],
            'monthly_income': df['LIMIT_BAL'] * 0.3,
            'age': df['AGE'],
            'savings_goal': df['LIMIT_BAL'] * 0.2,
            'last_month_spending': df['BILL_AMT1'],
            'num_transactions': np.random.randint(10, 50, len(df)),
            'avg_transaction': df['PAY_AMT1'] / np.maximum(np.abs(df['PAY_0']), 1),
            'next_month_spending': df['BILL_AMT2'],
            'spending_category': pd.cut(df['BILL_AMT1'], bins=3, labels=[0, 1, 2])
        })
        
        # Clean data
        processed_df = processed_df.dropna()
        processed_df = processed_df[processed_df['last_month_spending'] > 0]
        processed_df = processed_df[processed_df['next_month_spending'] > 0]
        processed_df = processed_df[processed_df['balance'] > 0]
        
        print(f"[OK] Processed {len(processed_df)} clean records")
        return processed_df
    else:
        print("Real dataset not found. Generating synthetic data...")
        return generate_sample_data()
    """Generate synthetic training data for demonstration"""
    np.random.seed(42)
    n_samples = 1000
    
    data = {
        'balance': np.random.uniform(10000, 100000, n_samples),
        'monthly_income': np.random.uniform(20000, 80000, n_samples),
        'age': np.random.randint(18, 65, n_samples),
        'savings_goal': np.random.uniform(5000, 50000, n_samples),
        'last_month_spending': np.random.uniform(5000, 40000, n_samples),
        'num_transactions': np.random.randint(5, 50, n_samples),
        'avg_transaction': np.random.uniform(100, 5000, n_samples),
        # Target: next month spending
        'next_month_spending': np.random.uniform(5000, 40000, n_samples),
        # Target: spending category (0=Low, 1=Medium, 2=High)
        'spending_category': np.random.randint(0, 3, n_samples)
    }
    
    df = pd.DataFrame(data)
    df.to_csv('ml_model/data/training_data.csv', index=False)
    print("[OK] Sample data generated: ml_model/data/training_data.csv")
    return df

# ============================================
# 2. FEATURE ENGINEERING
# ============================================

def create_features(df):
    """Create additional features"""
    df['savings_rate'] = (df['monthly_income'] - df['last_month_spending']) / df['monthly_income']
    df['spending_ratio'] = df['last_month_spending'] / df['balance']
    df['goal_progress'] = df['balance'] / df['savings_goal']
    return df

# ============================================
# 3. MODEL TRAINING
# ============================================

def train_spending_predictor(df):
    """Train regression model to predict next month spending"""
    features = ['balance', 'monthly_income', 'age', 'savings_goal', 
                'last_month_spending', 'num_transactions', 'avg_transaction',
                'savings_rate', 'spending_ratio', 'goal_progress']
    
    X = df[features]
    y = df['next_month_spending']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # Evaluate
    train_score = model.score(X_train_scaled, y_train)
    test_score = model.score(X_test_scaled, y_test)
    
    print(f"\n[OK] Spending Predictor Model:")
    print(f"  Train R² Score: {train_score:.3f}")
    print(f"  Test R² Score: {test_score:.3f}")
    
    # Save model
    joblib.dump(model, 'ml_model/models/spending_predictor.pkl')
    joblib.dump(scaler, 'ml_model/models/scaler.pkl')
    
    # Save feature names
    with open('ml_model/models/feature_names.json', 'w') as f:
        json.dump(features, f)
    
    return model, scaler

def train_category_classifier(df):
    """Train classifier to categorize spending behavior"""
    features = ['balance', 'monthly_income', 'age', 'savings_goal', 
                'last_month_spending', 'num_transactions', 'avg_transaction',
                'savings_rate', 'spending_ratio', 'goal_progress']
    
    X = df[features]
    y = df['spending_category']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    train_score = model.score(X_train_scaled, y_train)
    test_score = model.score(X_test_scaled, y_test)
    
    print(f"\n[OK] Category Classifier Model:")
    print(f"  Train Accuracy: {train_score:.3f}")
    print(f"  Test Accuracy: {test_score:.3f}")
    
    joblib.dump(model, 'ml_model/models/category_classifier.pkl')
    
    return model

# ============================================
# 4. MAIN TRAINING PIPELINE
# ============================================

def main():
    print("=" * 50)
    print("ML MODEL TRAINING PIPELINE")
    print("=" * 50)
    
    # Step 1: Generate/Load Data
    print("\n[1/4] Loading data...")
    df = load_data()
    
    # Step 2: Feature Engineering
    print("\n[2/4] Creating features...")
    df = create_features(df)
    
    # Step 3: Train Models
    print("\n[3/4] Training models...")
    spending_model, scaler = train_spending_predictor(df)
    category_model = train_category_classifier(df)
    
    # Step 4: Summary
    print("\n[4/4] Training complete!")
    print("\n" + "=" * 50)
    print("SAVED MODELS:")
    print("  - ml_model/models/spending_predictor.pkl")
    print("  - ml_model/models/category_classifier.pkl")
    print("  - ml_model/models/scaler.pkl")
    print("  - ml_model/models/feature_names.json")
    print("=" * 50)

if __name__ == "__main__":
    main()
