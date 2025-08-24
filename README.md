Garment Worker Productivity Prediction

Hi! I’m Shaunak, and this project focuses on predicting the productivity of garment workers using machine learning. I built this application with a user-friendly web interface, allowing anyone to input work-related factors and instantly see productivity predictions.

How the Project Works

Here’s the flow I designed for the application:

User Input: You provide key details about a garment worker’s performance via the web interface.

Model Analysis: The backend receives your input and feeds it into a pre-trained machine learning model.

Prediction: The model processes the data and gives a productivity prediction, which is immediately displayed for you.

Project Structure

I organized the project to keep things simple and easy to navigate:

Dataset/: Contains the garments_worker_productivity.csv dataset I used to train the model.

Training Files/: Includes my Jupyter Notebook Employee_Prediction.ipynb and the saved model gwp.pkl.

Flask/: Houses the web app code:

templates/: HTML files for the UI (home.html, about.html, predict.html, submit.html).

app.py: Python script managing the web server, model loading, and predictions.

gwp.pkl: The trained machine learning model ready to use.

What I Did in This Project
1. Data Collection & Pre-processing

Collected the garments_worker_productivity.csv dataset.

Cleaned the data to handle missing or null values.

Processed columns like date, department, quarter, and day to make them suitable for the model, including converting categorical data into numerical formats.

2. Model Building

Set up libraries like xgboost, scikit-learn, and numpy.

Split the dataset into training and testing sets, and trained an XGBoost model.

Evaluated the model’s performance to ensure accuracy.

Saved the final trained model as gwp.pkl so it could be easily loaded in the web app.

3. Application Development

Designed HTML pages for the homepage, about page, and prediction form.

Built the Flask backend to:

Serve the HTML templates.

Load the saved model (gwp.pkl).

Process user input and make predictions.

Display the results in a clear, readable format.

Running the Application

To try it out on your own machine:

Clone the Repository

git clone <repository_url>


Install Required Libraries

pip install flask numpy xgboost scikit-learn


Go to the Flask Directory

cd Project/Flask


Run the Web Application

python app.py
