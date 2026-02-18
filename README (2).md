# 🌦️ Rainfall Prediction Web Application using Machine Learning

This project is an end-to-end Machine Learning application that predicts whether it will rain tomorrow based on weather conditions.  
The trained Machine Learning model is deployed using a Flask web application, allowing users to enter weather parameters and get real-time predictions.

---

## 📌 Project Description

Rainfall prediction plays a vital role in agriculture, irrigation planning, and weather forecasting.  
This project analyzes historical weather data, applies Machine Learning algorithms to identify patterns, and predicts rainfall for the next day.

The project covers the complete ML lifecycle:
- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA)
- Model training and evaluation
- Model selection
- Deployment using Flask

---

## 🎯 Objective

- To analyze historical weather data
- To build a Machine Learning model that predicts rainfall
- To deploy the trained model as a web application
- To provide an easy-to-use interface for users

---

## 📊 Dataset Information

- Dataset: **Weather / Rainfall Dataset**
- Contains weather parameters such as:
  - Temperature
  - Rainfall
  - Humidity
  - Wind information
- Target variable:
  - **RainTomorrow** (Yes / No)

---

## 🧠 Machine Learning Models Used

The following models were trained and evaluated:

- Logistic Regression  
- Random Forest Classifier  

📌 **Final Model Selected:** Random Forest Classifier  
📈 **Accuracy Achieved:** ~85.77%

Random Forest was selected because it performed better and handled non-linear relationships effectively.

---

## 🛠️ Technologies & Tools Used

- **Programming Language:** Python  
- **Libraries:**
  - NumPy
  - Pandas
  - Matplotlib
  - Seaborn
  - Scikit-learn
- **Web Framework:** Flask  
- **IDE / Environment:**
  - Jupyter Notebook
  - Anaconda Navigator  

---

## 🗂️ Project Structure

Rainfall_Prediction_Project/
│
├── data/
│ └── Weather.csv
│
├── notebook/
│ └── rainfall_prediction.ipynb
│
├── model/
│ ├── Rainfall.pkl
│ ├── scaler.pkl
│ ├── encoder.pkl
│ ├── num_imputer.pkl
│ └── cat_imputer.pkl
│
├── app/
│ ├── app.py
│ └── templates/
│ ├── index.html
│ ├── chance.html
│ └── nochance.html
│
└── README.md

---

## 🔄 Project Workflow

1. Data Collection  
2. Exploratory Data Analysis (EDA)  
3. Data Cleaning & Missing Value Handling  
4. Encoding Categorical Variables  
5. Feature Scaling  
6. Train-Test Split  
7. Model Training and Evaluation  
8. Model Selection  
9. Saving Model using Pickle  
10. Flask Application Development  
11. Prediction Result Display  

---
