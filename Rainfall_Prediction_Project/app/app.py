from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model and scaler
model = pickle.load(open('../model/Rainfall.pkl', 'rb'))
scaler = pickle.load(open('../model/scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get values from form
    min_temp = float(request.form['MinTemp'])
    max_temp = float(request.form['MaxTemp'])
    rainfall = float(request.form['Rainfall'])
    humidity = float(request.form['Humidity3pm'])

    # Prepare data for prediction
    data = np.array([[min_temp, max_temp, rainfall, humidity]])
    data = scaler.transform(data)

    # Make prediction
    prediction = model.predict(data)[0]

    if prediction == 1:
        return render_template('chance.html')
    else:
        return render_template('nochance.html')

if __name__ == '__main__':
    app.run(debug=True)
