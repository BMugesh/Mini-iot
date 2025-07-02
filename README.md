# 🍌 Banana Ripeness Detection using IoT + ML

A smart agricultural solution to detect whether bananas are **artificially ripened** (e.g., calcium carbide or ethylene gas) or **naturally ripened** using IoT sensors and machine learning.

---

## 🎯 Objective

Many fruits, especially bananas, are artificially ripened using chemicals, which may have health risks. This project uses environmental data + sensor readings to determine the **ripening method**.

---

## 🧠 Tech Stack

- 🛠️ Hardware: Arduino UNO, DHT11 (humidity & temperature), MQ-3 (ethylene gas), Color sensor (TCS3200), Load Cell (optional)
- 🧪 Data: Sensor readings + Labeling (Natural or Artificial)
- 🧠 ML Model: Random Forest / SVM classifier
- 🌐 Web: Flask dashboard
- 📊 Visualization: Plotly, Matplotlib

---

## 🗂️ Project Structure

- `hardware/` → Arduino setup, sensor wiring, CSV logs
- `ml_model/` → ML training, models, datasets
- `app/` → Flask web app to upload readings and get results

---

## 🚀 How to Run

### 1. Arduino Setup

- Connect:
  - DHT11 for temp/humidity
  - MQ-3 for gas
  - TCS3200 for banana color
- Upload `ArduinoCode.ino` to your Arduino

### 2. Collect Data

- Run Arduino and log values to `sensor_data.csv`
- Label manually: `natural` or `artificial`

### 3. Train ML Model

```bash
cd ml_model/
jupyter notebook train_model.ipynb
