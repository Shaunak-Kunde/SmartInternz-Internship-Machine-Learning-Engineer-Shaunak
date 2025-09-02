# app.py

from flask import Flask, render_template, request
import numpy as np
import pickle
import os

app = Flask(__name__)

# This path will now work as gwp.pkl is in the same folder as app.py
model = pickle.load(open("gwp.pkl", "rb"))

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/predict")
def home1():
    return render_template('predict.html')

@app.route("/submit")
def home2():
    return render_template('submit.html')

@app.route("/predict", methods=["GET", "POST"])
def predict_route():
    if request.method == "POST":
        try:
            # Get the input values from the form
            quarter = request.form['quarter']
            department = request.form['department']
            day = request.form['day']
            
            # Numeric inputs
            team = float(request.form['team'])
            targeted_productivity = float(request.form['targeted_productivity'])
            smv = float(request.form['smv'])
            wip = float(request.form['wip'])
            over_time = float(request.form['over_time'])
            incentive = float(request.form['incentive'])
            idle_time = float(request.form['idle_time'])
            idle_men = float(request.form['idle_men'])
            no_of_style_change = float(request.form['no_of_style_change'])
            no_of_workers = float(request.form['no_of_workers'])

            # --- One-Hot Encoding for Categorical Features ---
            
            # Order of one-hot encoded features is critical and must match the model's training data.
            # This order is a common one if you used pandas.get_dummies() during training.
            
            # Department
            dept_sewing = 1 if department == 'sewing' else 0
            dept_finishing = 1 if department == 'finishing' else 0
            
            # Quarter
            q_q1 = 1 if quarter == 'Quarter1' else 0
            q_q2 = 1 if quarter == 'Quarter2' else 0
            q_q3 = 1 if quarter == 'Quarter3' else 0
            q_q4 = 1 if quarter == 'Quarter4' else 0

            # Day
            day_friday = 1 if day == 'Friday' else 0
            day_monday = 1 if day == 'Monday' else 0
            day_saturday = 1 if day == 'Saturday' else 0
            day_sunday = 1 if day == 'Sunday' else 0
            day_thursday = 1 if day == 'Thursday' else 0
            day_tuesday = 1 if day == 'Tuesday' else 0
            day_wednesday = 1 if day == 'Wednesday' else 0

            # Assemble the final feature list in the EXACT order your model expects
            features = [[
                dept_finishing,
                dept_sewing,
                q_q1,
                q_q2,
                q_q3,
                q_q4,
                day_friday,
                day_monday,
                day_saturday,
                day_sunday,
                day_thursday,
                day_tuesday,
                day_wednesday,
                team,
                targeted_productivity,
                smv,
                wip,
                over_time,
                incentive,
                idle_time,
                idle_men,
                no_of_style_change,
                no_of_workers
            ]]
            
            # Run prediction on the input features
            prediction = model.predict(features)[0]

            # Classify productivity based on the prediction value
            if prediction <= 0.3:
                text = 'The employee is averagely productive.'
            elif prediction > 0.3 and prediction <= 0.8:
                text = 'The employee is medium productive.'
            else:
                text = 'The employee is highly productive.'
            
            return render_template("submit.html", prediction_text=text)
            
        except Exception as e:
            error_message = f"An error occurred: {e}. Please check your input."
            return render_template("predict.html", error=error_message)

    return render_template("predict.html")

if __name__ == "__main__":
    app.run(debug=True)
