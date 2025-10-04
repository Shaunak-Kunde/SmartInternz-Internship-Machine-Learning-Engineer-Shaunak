## Employee Performance Prediction using Machine Learning (Model Building + Application Development + Deployment)

## A machine learning project that predicts employee productivity using regression models (Linear, Random Forest, XGBoost) and deploys the best-performing model via a Flask web application for real-time insights.

Author:
Shaunak Kunde
Master of Engineering in Data Science

Internship Context

This project was developed as part of a virtual internship for a Machine Learning Engineer role with SmartInternz. It applies machine learning techniques to a practical business challenge: predicting employee productivity and providing actionable insights for workforce management.

# Project Overview

The Machine Learning Approach for Employee Performance Prediction involves building a comprehensive system that analyzes employee-related data points to evaluate and forecast performance. By incorporating factors such as past productivity, training data, feedback, and external variables, the system generates predictions that support:

Talent management

Resource allocation

Workforce optimization strategies

# Real-World Applications
1. Talent Retention

HR departments can use predictions to identify high-performing employees who may be at risk of leaving. By analyzing turnover factors and performance trends, HR can design personalized career development plans and incentive programs to retain top talent.

2. Performance Improvement

Managers and team leaders can leverage predictions to pinpoint areas where employees need additional support or training. This enables timely coaching, skill development, and resource allocation, ultimately boosting performance and productivity.

3. Resource Allocation

Machine learning predictions can align employees with tasks and projects that best match their strengths. This ensures efficient utilization of talent, improves project outcomes, and enhances overall organizational performance.

# Project Objectives

By completing this project, the following outcomes were achieved:

Gained understanding of fundamental machine learning concepts and techniques.

Explored and visualized data to uncover insights.

Applied essential data preprocessing and transformation techniques.

Built, trained, and evaluated multiple machine learning models.

Developed and deployed a Flask-based web application for real-time predictions.

## Project Workflow
# 1. Data Collection & Preparation

Dataset used: garments_worker_productivity.csv

Preprocessing steps included:

Dropping the wip column due to null values.

Converting the date column into a datetime object and extracting the month feature.

Encoding categorical variables (department, team) using a custom MultiColumnLabelEncoder.

# 2. Model Building & Selection

Models tested:

Linear Regression

Random Forest Regressor

XGBoost Regressor

# XGBoost Regressor was selected as the final model due to its superior performance (lower MSE, higher R²).

The trained model was serialized as gwp.pkl for deployment.

# 3. Application Development

# Backend: Flask (app.py) — handles routes, logic, and model inference.

# Frontend: HTML pages (home.html, about.html, predict.html, submit.html) for user interaction.

# Styling: CSS files for a clean and user-friendly interface.

# Classification Logic: Predictions mapped to categories — Low, Medium, or High Productivity — for actionable insights.

# 4. Deployment

The application was successfully deployed locally.

# A video demostrating the working of the web application is also attached in the repository.

Users can input data via the UI and receive accurate productivity predictions in real time.
