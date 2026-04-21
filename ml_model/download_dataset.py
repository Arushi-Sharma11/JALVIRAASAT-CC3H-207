"""
Download and prepare UCI Credit Card Default Dataset
"""
import pandas as pd
import numpy as np

def download_and_prepare_data():
    """
    Download UCI Credit Card dataset and prepare for training
    """
    print("Downloading UCI Credit Card Default Dataset...")
    
    # Download from UCI repository
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00350/default%20of%20credit%20card%20clients.xls"
    
    try:
        df = pd.read_excel(url, header=1)
        print(f"✓ Downloaded {len(df)} records")
        
        # Rename columns for clarity
        df.columns = ['ID', 'LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE',
                      'PAY_0', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6',
                      'BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6',
                      'PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6',
                      'default']
        
        # Create features for our model
        processed_df = pd.DataFrame({
            'balance': df['LIMIT_BAL'],
            'monthly_income': df['LIMIT_BAL'] * 0.3,  # Estimate
            'age': df['AGE'],
            'savings_goal': df['LIMIT_BAL'] * 0.2,
            'last_month_spending': df['BILL_AMT1'],
            'num_transactions': np.random.randint(10, 50, len(df)),
            'avg_transaction': df['PAY_AMT1'] / np.maximum(df['PAY_0'], 1),
            'next_month_spending': df['BILL_AMT2'],  # Target
            'spending_category': pd.cut(df['BILL_AMT1'], bins=3, labels=[0, 1, 2])
        })
        
        # Clean data
        processed_df = processed_df.dropna()
        processed_df = processed_df[processed_df['last_month_spending'] > 0]
        processed_df = processed_df[processed_df['next_month_spending'] > 0]
        
        # Save
        processed_df.to_csv('ml_model/data/uci_credit_card.csv', index=False)
        print(f"✓ Saved {len(processed_df)} clean records to ml_model/data/uci_credit_card.csv")
        
        return processed_df
        
    except Exception as e:
        print(f"Error downloading: {e}")
        print("\nAlternative: Download manually from:")
        print("https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients")
        return None

if __name__ == "__main__":
    download_and_prepare_data()
