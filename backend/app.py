from flask import Flask, render_template, request
import pandas as pd
import os
import pickle

app = Flask(__name__)

# -------------------------------
# PATH CONFIGURATION (IMPORTANT)
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, '..', 'models', 'diabetes_model.pkl')
SCALER_PATH = os.path.join(BASE_DIR, '..', 'models', 'scaler.pkl')

# -------------------------------
# LOAD MODEL & SCALER
# -------------------------------
try:
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)

    with open(SCALER_PATH, 'rb') as f:
        scaler = pickle.load(f)

    print("✅ Model and scaler loaded successfully")

except Exception as e:
    print(f"❌ Error loading model/scaler: {e}")
    model = None
    scaler = None


# -------------------------------
# INPUT VALIDATION FUNCTION
# -------------------------------
def validate_input(form):
    try:
        data = {
            'age': float(form.get('age', 0)),
            'bmi': float(form.get('bmi', 0)),
            'blood_glucose_level': float(form.get('blood_glucose_level', 0)),
            'HbA1c_level': float(form.get('HbA1c_level', 0)),
            'hypertension': int(form.get('hypertension', 0)),
            'heart_disease': int(form.get('heart_disease', 0))
        }

        # Basic validation rules
        if not (1 <= data['age'] <= 120):
            raise ValueError("Age must be between 1 and 120")

        if not (10 <= data['bmi'] <= 50):
            raise ValueError("BMI must be between 10 and 50")

        return data

    except Exception as e:
        raise ValueError(f"Invalid input: {str(e)}")


# -------------------------------
# ROUTES
# -------------------------------
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/methodology')
def methodology():
    return render_template('methodology.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            if model is None or scaler is None:
                raise Exception("Model or scaler not loaded")

            # Validate input
            data = validate_input(request.form)

            # Force exact training feature order
            feature_order = ['age', 'heart_disease', 'hypertension', 'bmi', 'HbA1c_level', 'blood_glucose_level']

            # Convert to DataFrame in exact order
            input_df = pd.DataFrame([[data[col] for col in feature_order]], columns=feature_order)

            # Scale only numeric columns in the same way as training
            numerical_cols = ['age', 'bmi', 'HbA1c_level', 'blood_glucose_level']
            input_df[numerical_cols] = scaler.transform(input_df[numerical_cols])

            # Prediction
            prediction = model.predict(input_df)[0]
            probability = model.predict_proba(input_df)[0][1]

            # Risk classification
            if probability < 0.3:
                risk_level = "Low"
            elif probability < 0.7:
                risk_level = "Medium"
            else:
                risk_level = "High"

            return render_template(
                'results.html',
                prediction=prediction,
                probability=f"{probability * 100:.1f}",
                risk_level=risk_level,
                **data
            )

        except Exception as e:
            print("❌ Prediction Error:", str(e))
            return render_template('predict.html', error=str(e))

    return render_template('predict.html')


# -------------------------------
# MAIN
# -------------------------------
if __name__ == '__main__':
    app.run(debug=True)