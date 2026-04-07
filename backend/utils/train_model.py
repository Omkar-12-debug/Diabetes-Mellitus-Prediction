"""
Train diabetes prediction model.

Run this file separately to generate:
- models/diabetes_model.pkl
- models/scaler.pkl
"""

import pandas as pd
import os
import pickle

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Get base directory (backend/utils/)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define paths relative to project
DATASET_PATH = os.path.join(BASE_DIR, '..', '..', 'dataset', 'diabetes_prediction_dataset.csv')
MODEL_DIR = os.path.join(BASE_DIR, '..', '..', 'models')

# Ensure model directory exists
os.makedirs(MODEL_DIR, exist_ok=True)

print("Dataset Path:", DATASET_PATH)

# Load dataset
df = pd.read_csv(DATASET_PATH)
print(f"Total entries loaded: {len(df)}")

# Drop rows with missing target
df = df.dropna(subset=['diabetes'])

# Encode categorical/binary columns
for col in ['heart_disease', 'hypertension', 'diabetes']:
    if df[col].dtype == 'object':
        df[col] = LabelEncoder().fit_transform(df[col])

# Scale numeric columns
num_cols = ['age', 'bmi', 'HbA1c_level', 'blood_glucose_level']
scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

# Features & target
X = df[['age', 'heart_disease', 'hypertension', 'bmi', 'HbA1c_level', 'blood_glucose_level']]
y = df['diabetes']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Models
models = {
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Naive Bayes': GaussianNB(),
    'Random Forest': RandomForestClassifier(random_state=42)
}

best_model_name = None
best_model = None
best_accuracy = 0

print("\nModel Evaluation:")
for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)
    prec = precision_score(y_test, preds)
    rec = recall_score(y_test, preds)
    f1 = f1_score(y_test, preds)

    print(f"\n{name}:")
    print(f"  Accuracy : {acc * 100:.2f}%")
    print(f"  Precision: {prec * 100:.2f}%")
    print(f"  Recall   : {rec * 100:.2f}%")
    print(f"  F1 Score : {f1 * 100:.2f}%")

    if acc > best_accuracy:
        best_accuracy = acc
        best_model_name = name
        best_model = model

print(f"\nBest model: {best_model_name} ({best_accuracy * 100:.2f}%)")

# Save model
model_path = os.path.join(MODEL_DIR, 'diabetes_model.pkl')
with open(model_path, 'wb') as f:
    pickle.dump(best_model, f)

# Save scaler
scaler_path = os.path.join(MODEL_DIR, 'scaler.pkl')
with open(scaler_path, 'wb') as f:
    pickle.dump(scaler, f)

print("Model saved at:", model_path)
print("Scaler saved at:", scaler_path)