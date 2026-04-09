from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("models/rf_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array([[data['temperature'], data['vibration'], data['current']]])
    pred = model.predict(features)[0]
    return jsonify({"prediction": int(pred)})

app.run(debug=True)