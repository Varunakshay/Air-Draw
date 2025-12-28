# AirDraw: Digit Recognition Using Smartphone Sensors

## Overview
This project recognizes digits (0–9) written in the air using smartphone motion sensors.

## Data Collection
- Device: iPhone
- Sensors: Accelerometer, Gyroscope
- App: phyphox
- Format: CSV files

## Preprocessing
- Resampling to 200 timesteps
- Feature normalization
- Label extraction from filename

## Model
- 1D CNN for feature extraction
- LSTM for temporal modeling
- Softmax output for 10 classes

## How to Run
1. Install dependencies
2. Place CSV files in raw_data/
3. Run `train_airdraw.py`
4. Run `predict_airdraw.py` or `streamlit run app.py`

## Results
Achieved good accuracy on real sensor data with clear class separation.

