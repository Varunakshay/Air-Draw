import streamlit as st
import numpy as np
import pandas as pd
from scipy.signal import resample
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model

TIMESTEPS = 200
SENSOR_COLS = ['AX','AY','AZ','GX','GY','GZ']

model = load_model("airdraw_model.h5")
st.title("📱 AirDraw Digit Recognition")
st.write("Upload a motion sensor CSV file to predict the digit")

uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    df = df[SENSOR_COLS]
    df = df.apply(pd.to_numeric, errors="coerce").dropna()

    data = resample(df.values, TIMESTEPS)

    scaler = StandardScaler()
    data = scaler.fit_transform(data)

    data = np.expand_dims(data, axis=0)

    pred = model.predict(data)
    digit = np.argmax(pred)
    confidence = np.max(pred) * 100

    st.success(f"🎯 Predicted Digit: {digit}")
    st.info(f"Confidence: {confidence:.2f}%")

