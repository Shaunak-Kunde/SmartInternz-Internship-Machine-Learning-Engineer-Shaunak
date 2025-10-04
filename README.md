# Employee Performance Prediction using Machine Learning

## Model Building + Application Development + Deployment

A machine learning project that predicts employee productivity using regression models (Linear, Random Forest, XGBoost) and deploys the best-performing model via a Flask web application for real-time insights.

**Author:** Shaunak Kunde

*Master of Engineering in Data Science*

### Internship Context

This project was developed as part of a virtual internship for a Machine Learning Engineer role with **SmartInternz**. It applies machine learning techniques to a practical business challenge: predicting employee productivity and providing actionable insights for workforce management.

## 📋 Project Overview

The Machine Learning Approach for Employee Performance Prediction involves building a comprehensive system that analyzes various employee-related data points to evaluate and forecast performance. By incorporating factors such as past productivity, training data, feedback, and external variables, the system generates predictions that support talent management, resource allocation, and workforce optimization strategies.

### 🎯 Project Objectives

By completing this project, the following outcomes were achieved:

* Gained a deep understanding of fundamental machine learning concepts and techniques.
* Explored and visualized data to uncover insights and patterns.
* Applied essential data preprocessing and feature engineering techniques.
* Built, trained, and evaluated multiple machine learning models to find the best fit.
* Developed and deployed a Flask-based web application for real-time predictions.

## ⚙️ Project Workflow

The project is broken down into four main stages:

#### 1. Data Collection & Preparation

* **Dataset:** `garments_worker_productivity.csv`
* **Preprocessing Steps:**
    * Dropped the `wip` column due to a high number of null values.
    * Converted the `date` column into a datetime object and extracted the `month` as a new feature.
    * Encoded categorical variables (`department`, `team`) using a custom `MultiColumnLabelEncoder` to prepare them for the models.

#### 2. Model Building & Selection

* **Models Tested:**
    1.  Linear Regression
    2.  Random Forest Regressor
    3.  XGBoost Regressor
* **Selected Model:** **XGBoost Regressor** was chosen as the final model due to its superior performance (lower Mean Squared Error and higher R² score).
* The trained XGBoost model was serialized and saved as `gwp.pkl` for deployment in the web application.

#### 3. Application Development

* **Backend:** A **Flask** application (`app.py`) was developed to handle web routes, process user input, and perform model inference.
* **Frontend:** HTML templates (`home.html`, `predict.html`, etc.) were created for user interaction and data entry.
* **Styling:** CSS files were used to create a clean and user-friendly interface.
* **Classification Logic:** The continuous prediction from the model is mapped to distinct categories—**Low, Medium, or High Productivity**—to provide clear, actionable insights.

#### 4. Deployment

* The Flask application was successfully deployed for local use, allowing users to input data via the UI and receive accurate productivity predictions in real time.

## 🏢 Real-World Applications

This model provides valuable insights that can be applied in various business contexts:

* **Talent Retention:** HR departments can use predictions to identify high-performing employees who may be at risk of leaving. This allows for proactive creation of personalized career development plans and incentive programs.
* **Performance Improvement:** Managers can leverage the predictions to pinpoint areas where employees need additional support or training, enabling timely coaching and skill development.
* **Resource Allocation:** The system helps align employees with tasks and projects that best match their strengths, ensuring efficient utilization of talent and improving project outcomes.

## 🚀 How to Run the Project

To run this project locally, please follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/Shaunak-Kunde/SmartInternz-Internship-Machine-Learning-Engineer-Shaunak.git](https://github.com/Shaunak-Kunde/SmartInternz-Internship-Machine-Learning-Engineer-Shaunak.git)
    cd SmartInternz-Internship-Machine-Learning-Engineer-Shaunak
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask Application:**
    ```bash
    python app.py
    ```

5.  Open your web browser and navigate to `http://127.0.0.1:5000`.

## 🎥 Video Demonstration

A video recording demonstrating the live functionality of the web application (`recording of task employee productivity.mp4`) is included in this repository.

## 📂 Repository Structure

.
├── Dataset/
│   └── garments_worker_productivity.csv
├── Flask/
│   ├── app.py
│   ├── static/
│   └── templates/
├── Training FIles/
│   └── Employee Performance Predicition.ipynb
├── .gitattributes
├── Employee Performance Predicition.docx
├── gwp.pkl
├── README.md
├── recording of task employee productivity.mp4
└── requirements.txt
