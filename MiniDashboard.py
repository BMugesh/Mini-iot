from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load('../ml_model/ripeness_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        temp = float(request.form['temp'])
        humidity = float(request.form['humidity'])
        gas = float(request.form['gas'])
        color = float(request.form['color'])
        features = [[temp, humidity, gas, color]]
        prediction = model.predict(features)[0]
        result = "Artificial ⚠️" if prediction else "Natural 🍌"
        return render_template('dashboard.html', result=result)
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
