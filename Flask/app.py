from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('gwp.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            quarter = request.form['quarter']
            department = request.form['department']
            day = request.form['day']
            team = request.form['team']
            targeted_productivity = request.form['targeted_productivity']
            smv = request.form['smv']
            wip = request.form['wip']
            over_time = request.form['over_time']
            incentive = request.form['incentive']
            idle_time = request.form['idle_time']
            idle_men = request.form['idle_men']
            no_of_style_change = request.form['no_of_style_change']
            no_of_workers = request.form['no_of_workers']

            total = [[int(quarter), int(department), int(day), int(team), float(targeted_productivity),
                      float(smv), float(wip) if wip else 0, int(over_time), int(incentive), float(idle_time), int(idle_men),
                      int(no_of_style_change), float(no_of_workers)]]

            prediction = model.predict(total)[0]

            # Classify productivity based on the prediction value
            if prediction <= 0.3:
                text = 'The employee is averagely productive.'
            elif prediction > 0.3 and prediction <= 0.8:
                text = 'The employee is medium productive.'
            else:
                text = 'The employee is highly productive.'

            return render_template('submit.html', predicted_value=prediction, text=text)

        except (ValueError, KeyError) as e:
            return f"An error occurred: Missing or invalid data. Details: {e}", 400

    return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)
