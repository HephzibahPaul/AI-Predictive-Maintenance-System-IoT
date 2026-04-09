import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 🔹 LOAD MODEL
# -------------------------------
model = joblib.load("models/rf_model.pkl")

# -------------------------------
# 🔹 TITLE
# -------------------------------
st.title("🔧 Predictive Maintenance Dashboard")

# -------------------------------
# 🔹 SECTION 1: PREDICTION + LIVE GRAPH
# -------------------------------
st.header("📊 Predict Machine Failure")

temp = st.slider("Temperature", 30, 120)
vib = st.slider("Vibration", 0, 10)
curr = st.slider("Current", 0, 20)

predict_btn = st.button("Predict")

if predict_btn:
    pred = model.predict([[temp, vib, curr]])[0]

    # 🔥 Rule-based override (fix imbalance issue)
    if temp > 100 or vib > 7 or curr > 15:
        pred = 1

    # 🔹 SHOW RESULT
    if pred == 1:
        st.error("⚠️ Failure Likely")
    else:
        st.success("✅ Machine Healthy")

    # 🔹 LIVE PREDICTION GRAPH
    st.subheader("⚡ Live Prediction Graph")

    labels = ["Normal", "Failure"]
    values = [1 - pred, pred]

    fig3, ax3 = plt.subplots()
    ax3.bar(labels, values)
    ax3.set_title("Current Prediction")

    st.pyplot(fig3)

# -------------------------------
# 🔹 SECTION 2: SENSOR VISUALIZATION
# -------------------------------
st.header("📈 Sensor Data Visualization")

data = pd.read_csv("data/time_series_data.csv")

fig, ax = plt.subplots()
ax.plot(data["temperature"], label="Temperature")
ax.plot(data["vibration"], label="Vibration")
ax.plot(data["current"], label="Current")

ax.set_title("Sensor Trends Over Time")
ax.legend()

st.pyplot(fig)

# -------------------------------
# 🔹 SECTION 3: FAILURE DISTRIBUTION
# -------------------------------
st.header("📊 Failure Distribution (Dataset)")

st.info("This graph shows dataset distribution (not live prediction)")

failure_counts = data["failure"].value_counts()

normal_count = failure_counts.get(0, 0)
failure_count = failure_counts.get(1, 0)

fig2, ax2 = plt.subplots()
ax2.bar(["Normal", "Failure"], [normal_count, failure_count])
ax2.set_title("Failure vs Normal Count")

st.pyplot(fig2)

# -------------------------------
# 🔹 SECTION 4: MODEL PERFORMANCE
# -------------------------------
st.header("📊 Model Performance")

try:
    st.subheader("Confusion Matrix")
    st.image("images/confusion_matrix.png")

    st.subheader("Accuracy Graph")
    st.image("images/accuracy.png")

except:
    st.warning("Run main.py to generate performance graphs")

# -------------------------------
# 🔹 FOOTER
# -------------------------------
st.markdown("---")
st.markdown("✅ Built with ML + LSTM for Predictive Maintenance")