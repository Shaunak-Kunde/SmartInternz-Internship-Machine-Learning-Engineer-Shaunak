Garment Worker Productivity Prediction

Hi! I’m Shaunak, and this project focuses on predicting the productivity of garment workers using machine learning. I built this application with a user-friendly web interface, allowing anyone to input work-related factors and instantly see productivity predictions.

Employee Performance Prediction
Project Overview
This is a comprehensive system designed to analyze various data points related to employees' work performance and use machine learning algorithms, specifically XGBoost, to predict and evaluate their future productivity. By incorporating factors such as past performance metrics, training data, feedback, and external factors, the system aims to provide insights that can aid in talent management, resource allocation, and workforce optimization strategies.

Machine Learning Approach
The web application uses a pre-trained machine learning model, which was trained and evaluated in a Jupyter notebook. The project flow is as follows:

User Interaction: The user interacts with a Flask web interface to enter the input features for an employee.

Model Analysis: The entered input is passed to the integrated XGBoost model (gwp.pkl) for prediction.

Prediction Display: The model's prediction is then showcased on the UI, along with a text-based classification ("averagely productive," "medium productive," or "highly productive").

Technical Details (from Jupyter Notebook)
Data Preprocessing:

The date column was converted to a datetime format, and the month was extracted as a new feature.

The department and team columns were handled using a custom MultiColumnLabelEncoder class.

The wip column was dropped from the dataset for model training, as it contained null values.

Model Selection:

Three models were evaluated: LinearRegression, RandomForestRegressor, and XGBRegressor.

The XGBRegressor model showed the best performance and was selected for the final application.

Model Saving: The final XGBoost model was saved to a pickle file named gwp.pkl using the pickle library.

Scenarios
1. Talent Retention
HR departments can use the machine learning predictions to identify high-performing employees at risk of attrition. By analyzing factors contributing to employee turnover and predicting performance trends, HR can implement targeted retention strategies, such as personalized career development plans or incentive programs, to retain top talent.

2. Performance Improvement
Managers and team leaders can leverage the predictions to identify areas where employees may need additional support or training. By understanding performance patterns and potential challenges, managers can provide timely coaching, resources, or skill development opportunities to enhance employee performance and productivity.

3. Resource Allocation
Organizations can optimize resource allocation by using machine learning predictions to match employees with projects or tasks that align with their strengths and capabilities. This ensures efficient utilization of talent, improves project outcomes, and enhances overall organizational performance.

Project Objectives
By completing this project, you will:

Know fundamental concepts and techniques used for machine learning.

Gain a broad understanding about data.

Have knowledge on pre-processing the data/transformation techniques and some visualization concepts.

Setup and Installation
1. Prerequisites
Ensure you have Python installed on your system.

2. Project Files
The project consists of the following files and folders:

app.py: The main Flask application.

gwp.pkl: The pre-trained machine learning model.

templates/: Contains all the HTML files for the web interface.

static/: Contains the CSS files for styling the application.

requirements.txt: Lists all the necessary Python libraries.

3. Install Dependencies
Navigate to the project directory in your terminal and install the required libraries using the requirements.txt file.

pip install -r requirements.txt

4. Run the Application
Start the Flask application by running the app.py file.

python app.py

The application will start on your local server. You can access it by opening your web browser and navigating to http://127.0.0.1:5000.

Usage
Home Page: The starting page provides a general overview of the app.

Predict Page: Navigate to the /predict page.

Enter Data: Fill out the form with the relevant employee information.

Submit: Click "Submit" to get the productivity prediction.

View Result: The result page will display both the numerical prediction and a text-based classification.
