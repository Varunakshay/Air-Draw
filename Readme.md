# 📱 AirDraw – Air-Written Digit Recognition Using Smartphone Sensors

## ✅ Project Overview
This project recognizes digits **(0–9)** written in the air using smartphone motion sensors.  
It uses:
- **Accelerometer** (AX, AY, AZ)
- **Gyroscope** (GX, GY, GZ)

Data is collected using a **smartphone (iPhone) and phyphox app**, processed, resampled, normalized, and fed into a **CNN + LSTM deep learning model** trained in **Google Colab**.  
The trained model is exported and used locally for predictions and (optionally) a Streamlit demo.

---

## 📂 Dataset Details

### 📌 Data Collection
- Device → **iPhone**
- App → **Phyphox**
- Experiment Used → Raw Sensor / Acceleration + Gyroscope
- Each recording corresponds to **one digit air-written**
- Sampling duration ~ 1–2 seconds
- Exported as **CSV files**

---

### 📁 Dataset Folder Structure
Final dataset structured as:

Dataset/
 ├── digit0/
 │     ├── digit0_sample1.csv
 │     ├── digit0_sample2.csv
 │     └── ...
 ├── digit1/
 │     ├── digit1_sample1.csv
 │     └── ...
 ├── ...
 └── digit9/
       ├── digit9_sample1.csv
       └── ...


Each CSV contains:

Time (s), AX, AY, AZ, GX, GY, GZ

Where:
- Time(s) = timestamp  
- AX/AY/AZ = accelerometer readings  
- GX/GY/GZ = gyroscope readings  

---

## 🧹 Data Preprocessing Steps
For each CSV file:

✔ Selected required columns → AX, AY, AZ, GX, GY, GZ  
✔ Converted values to numeric  
✔ Removed NaN values  
✔ Removed very short recordings (< 30 rows)  
✔ Resampled each signal to fixed length **200 timesteps**  
✔ Stored data as (samples, 200, 6)  
✔ Labels extracted automatically from folder name:

digit0 → 0
digit1 → 1
...
digit9 → 9

---

## 🧠 Model Architecture

### 📌 Why CNN + LSTM?
- **CNN** → learns motion patterns/features  
- **LSTM** → learns temporal sequence behavior  

### Model Used

Conv1D → MaxPooling → Conv1D → MaxPooling → LSTM → Dense

- Optimizer → Adam  
- Loss → Categorical Crossentropy  
- Batch Size → 32  
- Epochs → 25–100 (depending on dataset size)

---

## ☁️ Training in Google Colab

### Steps Followed

1️⃣ Opened Google Colab  
Enabled GPU:
Runtime → Change runtime type → GPU

2️⃣ Uploaded Dataset
Uploaded raw_data.zip
Extracted using:
!unzip raw_data.zip

3️⃣ Installed Libraries
!pip install numpy pandas scipy scikit-learn matplotlib tensorflow

4️⃣ Loaded + Preprocessed Dataset
- Loaded each CSV  
- Cleaned data  
- Resampled to 200 timesteps  
- Label assigned from folder  

5️⃣ Trained CNN + LSTM Model
Observed accuracy and training improvements.

6️⃣ Evaluated Model
Generated:
- Accuracy  
- Loss  
- Classification Report  
- Confusion Matrix  

7️⃣ Saved Trained Model
model.save("airdraw_model.h5")

Downloaded to local machine.

---

## 💾 Using The Trained Model Locally

### 📁 Folder Structure

AirDraw_Project/
├── airdraw_model.h5
├── predict_airdraw.py
├── app.py (optional)
├── raw_data/
│     ├── test_sample.csv
│     └── ...
└── README.md

---

## 🛠 Installation
Run:
pip install numpy pandas scipy scikit-learn tensorflow streamlit

---

## 🧪 Local Prediction (Offline)
A Python script was created to:
- Load trained model  
- Read CSV  
- Preprocess  
- Predict digit  
- Display result  

Run:
python predict_airdraw.py

Output example:
🎯 Predicted Digit: 5

---

## 🖥️ Optional Streamlit Demo
Interactive UI to upload CSV and get prediction.

Run:
streamlit run app.py

Upload → Get prediction instantly 🎯

---

## 🎓 Viva / Presentation Explanation

About Data Collection:
“The dataset was collected using an iPhone and phyphox app. Each CSV represents a digit written in air.”

About Preprocessing:
“Data was cleaned, NaNs removed, resampled to 200 steps, normalized, and converted into 3D time-series format.”

About Model:
“CNN extracts motion features while LSTM learns temporal behavior, making it suitable for gesture recognition.”

About Training:
“Training was done in Google Colab using GPU and the trained model was exported as H5 for deployment.”

About Accuracy:
“Accuracy improves significantly as dataset size increases, which is expected for deep learning models.”

---

## 📊 Recommended Dataset Size vs Accuracy

Samples per Digit → Expected Accuracy:
1–3 → Low  
5–10 → Moderate  
20+ → Good  
50+ → Excellent  

---

## ⚠️ Common Issues & Fixes

NaN / Inf Loss
Cause → missing values  
Fix → drop NaN and normalize

Low Accuracy
Cause → too few samples  
Fix → collect more or apply mild augmentation

Model Not Found
Ensure file exists:
airdraw_model.h5

---

## ✔️ Final Conclusion
This project successfully demonstrates:

- Air-writing digit recognition  
- Real-world IMU data processing  
- Time-series deep learning with CNN + LSTM  
- Cloud-based training  
- Local deployment and optional live demo  

---

## 🙌 Tools & Technologies
- TensorFlow  
- NumPy / Pandas  
- SciPy  
- Scikit-learn  
- Streamlit  
- Google Colab  
- phyphox App  
