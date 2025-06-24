from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd  # 👈 Import pandas

app = Flask(__name__)

# Load the trained model pipeline (includes encoder + regressor)
with open('insurance_model.pkl', 'rb') as f:
    model = pickle.load(f)

print("✅ Model loaded successfully.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    print("📥 Received data:", data)

    # Format input as a DataFrame with correct column names
    input_df = pd.DataFrame([{
        'sex': data['sex'],
        'smoker': data['smoker'],
        'region': data['region'],
        'age': data['age'],
        'bmi': data['bmi'],
        'children': data['children']
    }])

    print("🔄 DataFrame for prediction:\n", input_df)

    try:
        prediction = model.predict(input_df)[0]
        print("✅ Prediction:", prediction)
        return jsonify({'prediction': float(prediction)})
    except Exception as e:
        print("❌ Error during prediction:", str(e))
        return jsonify({'error': 'Prediction failed. Check server logs.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
