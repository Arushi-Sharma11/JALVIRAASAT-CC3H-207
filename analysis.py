import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
import warnings
warnings.filterwarnings('ignore')

# Load data
df = pd.read_csv('ml_model/data/UCI_Credit_Card.csv')

print("="*80)
print("DATA OVERVIEW")
print("="*80)
print(f"\nDataset Shape: {df.shape}")
print(f"\nColumn Names:\n{df.columns.tolist()}")
print(f"\nFirst 5 rows:\n{df.head()}")
print(f"\nData Types:\n{df.dtypes}")
print(f"\nBasic Statistics:\n{df.describe()}")

print("\n" + "="*80)
print("DATA CLEANING")
print("="*80)
print(f"\nMissing Values:\n{df.isnull().sum()}")
print(f"\nDuplicate Rows: {df.duplicated().sum()}")

# Check for outliers in key columns
print(f"\nOutliers Detection (values outside reasonable ranges):")
print(f"SEX (should be 1 or 2): {df[~df['SEX'].isin([1,2])].shape[0]} outliers")
print(f"EDUCATION (should be 1-4): {df[~df['EDUCATION'].isin([1,2,3,4])].shape[0]} outliers")
print(f"MARRIAGE (should be 1-3): {df[~df['MARRIAGE'].isin([1,2,3])].shape[0]} outliers")

# Clean data
df_clean = df.copy()
df_clean = df_clean[df_clean['SEX'].isin([1,2])]
df_clean = df_clean[df_clean['EDUCATION'].isin([1,2,3,4])]
df_clean = df_clean[df_clean['MARRIAGE'].isin([1,2,3])]
print(f"\nCleaned Dataset Shape: {df_clean.shape}")

print("\n" + "="*80)
print("EXPLORATORY DATA ANALYSIS")
print("="*80)
print(f"\nTarget Variable Distribution:")
print(df_clean['default.payment.next.month'].value_counts())
print(f"\nDefault Rate: {df_clean['default.payment.next.month'].mean()*100:.2f}%")

print(f"\nAge Distribution:")
print(df_clean['AGE'].describe())

print(f"\nCredit Limit Distribution:")
print(df_clean['LIMIT_BAL'].describe())

# Visualizations
fig, axes = plt.subplots(3, 3, figsize=(15, 12))
fig.suptitle('Credit Card Dataset Analysis', fontsize=16)

# Target distribution
axes[0,0].bar(['No Default', 'Default'], df_clean['default.payment.next.month'].value_counts().values)
axes[0,0].set_title('Default Distribution')
axes[0,0].set_ylabel('Count')

# Age distribution
axes[0,1].hist(df_clean['AGE'], bins=30, edgecolor='black')
axes[0,1].set_title('Age Distribution')
axes[0,1].set_xlabel('Age')

# Credit limit distribution
axes[0,2].hist(df_clean['LIMIT_BAL'], bins=30, edgecolor='black')
axes[0,2].set_title('Credit Limit Distribution')
axes[0,2].set_xlabel('Credit Limit')

# Sex distribution
axes[1,0].bar(['Male', 'Female'], df_clean['SEX'].value_counts().sort_index().values)
axes[1,0].set_title('Gender Distribution')

# Education distribution
axes[1,1].bar(['Grad', 'Univ', 'High', 'Other'], df_clean['EDUCATION'].value_counts().sort_index().values)
axes[1,1].set_title('Education Distribution')

# Marriage distribution
axes[1,2].bar(['Married', 'Single', 'Other'], df_clean['MARRIAGE'].value_counts().sort_index().values)
axes[1,2].set_title('Marriage Status')

# Default by gender
default_by_sex = df_clean.groupby('SEX')['default.payment.next.month'].mean()
axes[2,0].bar(['Male', 'Female'], default_by_sex.values)
axes[2,0].set_title('Default Rate by Gender')
axes[2,0].set_ylabel('Default Rate')

# Default by education
default_by_edu = df_clean.groupby('EDUCATION')['default.payment.next.month'].mean()
axes[2,1].bar(['Grad', 'Univ', 'High', 'Other'], default_by_edu.values)
axes[2,1].set_title('Default Rate by Education')

# Default by age group
df_clean['age_group'] = pd.cut(df_clean['AGE'], bins=[20,30,40,50,60,80], labels=['20-30','30-40','40-50','50-60','60+'])
default_by_age = df_clean.groupby('age_group')['default.payment.next.month'].mean()
axes[2,2].bar(default_by_age.index, default_by_age.values)
axes[2,2].set_title('Default Rate by Age Group')

plt.tight_layout()
plt.savefig('eda_visualizations.png', dpi=300, bbox_inches='tight')
print("\n[OK] Visualizations saved as 'eda_visualizations.png'")

# Correlation heatmap
plt.figure(figsize=(14, 10))
corr = df_clean.drop(['ID', 'age_group'], axis=1).corr()
sns.heatmap(corr, cmap='coolwarm', center=0, annot=False, fmt='.2f')
plt.title('Feature Correlation Heatmap')
plt.tight_layout()
plt.savefig('correlation_heatmap.png', dpi=300, bbox_inches='tight')
print("[OK] Correlation heatmap saved as 'correlation_heatmap.png'")

print("\n" + "="*80)
print("MACHINE LEARNING MODEL")
print("="*80)

# Prepare features
X = df_clean.drop(['ID', 'default.payment.next.month', 'age_group'], axis=1)
y = df_clean['default.payment.next.month']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(f"\nTraining set: {X_train.shape}, Test set: {X_test.shape}")

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model 1: Logistic Regression
print("\n--- Logistic Regression ---")
lr = LogisticRegression(max_iter=1000, random_state=42)
lr.fit(X_train_scaled, y_train)
lr_pred = lr.predict(X_test_scaled)
lr_prob = lr.predict_proba(X_test_scaled)[:,1]
print(f"Accuracy: {lr.score(X_test_scaled, y_test):.4f}")
print(f"ROC-AUC: {roc_auc_score(y_test, lr_prob):.4f}")
print("\nClassification Report:")
print(classification_report(y_test, lr_pred))

# Model 2: Random Forest
print("\n--- Random Forest ---")
rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_prob = rf.predict_proba(X_test)[:,1]
print(f"Accuracy: {rf.score(X_test, y_test):.4f}")
print(f"ROC-AUC: {roc_auc_score(y_test, rf_prob):.4f}")
print("\nClassification Report:")
print(classification_report(y_test, rf_pred))

# Feature importance
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': rf.feature_importances_
}).sort_values('importance', ascending=False)
print("\nTop 10 Important Features:")
print(feature_importance.head(10))

# Visualization: Model comparison
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# ROC curves
fpr_lr, tpr_lr, _ = roc_curve(y_test, lr_prob)
fpr_rf, tpr_rf, _ = roc_curve(y_test, rf_prob)
axes[0].plot(fpr_lr, tpr_lr, label=f'Logistic Regression (AUC={roc_auc_score(y_test, lr_prob):.3f})')
axes[0].plot(fpr_rf, tpr_rf, label=f'Random Forest (AUC={roc_auc_score(y_test, rf_prob):.3f})')
axes[0].plot([0,1], [0,1], 'k--', label='Random')
axes[0].set_xlabel('False Positive Rate')
axes[0].set_ylabel('True Positive Rate')
axes[0].set_title('ROC Curves')
axes[0].legend()

# Confusion matrix - Random Forest
cm = confusion_matrix(y_test, rf_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[1])
axes[1].set_title('Confusion Matrix (Random Forest)')
axes[1].set_xlabel('Predicted')
axes[1].set_ylabel('Actual')

# Feature importance
top_features = feature_importance.head(10)
axes[2].barh(top_features['feature'], top_features['importance'])
axes[2].set_xlabel('Importance')
axes[2].set_title('Top 10 Feature Importance')
axes[2].invert_yaxis()

plt.tight_layout()
plt.savefig('model_results.png', dpi=300, bbox_inches='tight')
print("\n[OK] Model results saved as 'model_results.png'")

print("\n" + "="*80)
print("SUMMARY")
print("="*80)
print(f"[OK] Dataset analyzed: {df_clean.shape[0]} records, {df_clean.shape[1]} features")
print(f"[OK] Default rate: {df_clean['default.payment.next.month'].mean()*100:.2f}%")
print(f"[OK] Best model: Random Forest with ROC-AUC = {roc_auc_score(y_test, rf_prob):.4f}")
print(f"[OK] Generated 3 visualization files")
print("\nAnalysis complete!")
