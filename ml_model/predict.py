"""
ML Model Inference Module
Use trained models to generate predictions and advice
"""
import joblib
import numpy as np
import json
import os

class FinancialMLPredictor:
    def __init__(self):
        self.model_path = "ml_model/models/"
        self.spending_model = None
        self.category_model = None
        self.scaler = None
        self.feature_names = None
        self.load_models()
    
    def load_models(self):
        """Load trained models"""
        try:
            self.spending_model = joblib.load(f"{self.model_path}spending_predictor.pkl")
            self.category_model = joblib.load(f"{self.model_path}category_classifier.pkl")
            self.scaler = joblib.load(f"{self.model_path}scaler.pkl")
            
            with open(f"{self.model_path}feature_names.json", 'r') as f:
                self.feature_names = json.load(f)
            
            print("[ML] Models loaded successfully")
        except FileNotFoundError:
            print("[WARNING] ML models not found. Run 'python ml_model/train.py' first.")
            self.spending_model = None
    
    def prepare_features(self, user_data):
        """Prepare features from user data"""
        # Calculate derived features
        monthly_income = user_data.get('monthly_income', user_data['balance'] * 0.3)
        last_month_spending = user_data.get('last_month_spending', 15000)
        
        savings_rate = (monthly_income - last_month_spending) / monthly_income if monthly_income > 0 else 0
        spending_ratio = last_month_spending / user_data['balance'] if user_data['balance'] > 0 else 0
        goal_progress = user_data['balance'] / user_data['savings_goal'] if user_data['savings_goal'] > 0 else 0
        
        features = {
            'balance': user_data['balance'],
            'monthly_income': monthly_income,
            'age': user_data.get('age', 30),
            'savings_goal': user_data['savings_goal'],
            'last_month_spending': last_month_spending,
            'num_transactions': user_data.get('num_transactions', 20),
            'avg_transaction': user_data.get('avg_transaction', 750),
            'savings_rate': savings_rate,
            'spending_ratio': spending_ratio,
            'goal_progress': goal_progress
        }
        
        # Convert to array in correct order
        feature_array = np.array([[features[name] for name in self.feature_names]])
        return feature_array
    
    def predict_next_month_spending(self, user_data):
        """Predict next month's spending"""
        if not self.spending_model:
            return None
        
        features = self.prepare_features(user_data)
        features_scaled = self.scaler.transform(features)
        prediction = self.spending_model.predict(features_scaled)[0]
        
        return round(prediction, 2)
    
    def classify_spending_behavior(self, user_data):
        """Classify user's spending behavior"""
        if not self.category_model:
            return "Unknown"
        
        features = self.prepare_features(user_data)
        features_scaled = self.scaler.transform(features)
        category = self.category_model.predict(features_scaled)[0]
        
        categories = {0: "Conservative", 1: "Moderate", 2: "Aggressive"}
        return categories.get(category, "Unknown")
    
    def generate_ml_advice(self, user_data, current_spend_amount):
        """Generate ML-powered advice"""
        if not self.spending_model:
            return "Track your expenses regularly for better insights."
        
        predicted_spending = self.predict_next_month_spending(user_data)
        spending_type = self.classify_spending_behavior(user_data)
        
        # Generate contextual advice
        if current_spend_amount > predicted_spending * 0.1:
            advice = f"[WARNING] This expense is higher than your usual pattern. Predicted monthly spending: Rs.{predicted_spending:.0f}"
        elif spending_type == "Aggressive":
            advice = f"[TIP] Your spending pattern is aggressive. Consider saving more. Target: Rs.{user_data['savings_goal']:.0f}"
        elif spending_type == "Conservative":
            advice = f"[GOOD] Great! You're a conservative spender. Keep it up!"
        else:
            advice = f"[INFO] Your spending is moderate. Predicted next month: Rs.{predicted_spending:.0f}"
        
        return advice

# Global instance
ml_predictor = FinancialMLPredictor()
