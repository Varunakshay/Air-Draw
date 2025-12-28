import numpy as np
import pandas as pd
from scipy.signal import resample
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model

MODEL_PATH = "airdraw_model.h5"
CSV_FILE = "raw_data/digit5_sample1.csv"   # change test file here
TIMESTEPS = 200
SENSOR_COLS = ['AX','AY','AZ','GX','GY','GZ']

# load model
model = load_model(MODEL_PATH)
print("Model loaded successfully")

# load csv
df = pd.read_csv(CSV_FILE)
df = df[SENSOR_COLS]
df = df.apply(pd.to_numeric, errors="coerce").dropna()

# resample
data = resample(df.values, TIMESTEPS)

# normalize
scaler = StandardScaler()
data = scaler.fit_transform(data)

# model input shape
data = np.expand_dims(data, axis=0)

# predict
pred = model.predict(data)
digit = np.argmax(pred)

print("🎯 Predicted Digit:", digit)

