🏠 House Price Prediction using Linear Regression
📌 Project Overview

This project is part of Artificial Intelligence & Machine Learning – Task 1 assigned by Maincrafts.
The objective is to build and evaluate a Linear Regression model to predict house prices using the California Housing dataset, while demonstrating the complete machine learning workflow.

🎯 Objectives

Understand the end-to-end Machine Learning pipeline

Perform Exploratory Data Analysis (EDA)

Train and evaluate a Linear Regression model

Analyze model performance using standard regression metrics

Save the trained model and predict on new inputs

📊 Dataset

Name: California Housing Dataset

Source: scikit-learn built-in dataset

Records: 20,640

Features: 8 numerical features

Target Variable: MedHouseVal (Median house value)

🛠️ Technologies Used

Programming Language: Python

Libraries:

pandas

numpy

matplotlib

seaborn

scikit-learn

Environment: Jupyter Notebook

🔍 Project Workflow

Data loading and inspection

Exploratory Data Analysis (EDA)

Feature-target separation

Train-test split

Model training using Linear Regression

Model evaluation (MAE, RMSE, R²)

Residual analysis

Model persistence using pickle

Prediction on new inputs using a script

📈 Model Evaluation Metrics

MAE (Mean Absolute Error)

RMSE (Root Mean Squared Error)

R² Score (Coefficient of Determination)

These metrics help assess prediction accuracy and model reliability.
📂 Project Structure
├── task1_ml_linear_regression.ipynb
├── house_price_linear_model.pkl
├── predict_house_price.py
├── README.md

▶️ How to Run the Project
1️⃣ Install Required Libraries
pip install pandas numpy matplotlib seaborn scikit-learn

2️⃣ Run the Jupyter Notebook
jupyter notebook task1_ml_linear_regression.ipynb

3️⃣ Predict on New Inputs (Optional)
python predict_house_price.py


Follow the prompts to enter feature values.

📌 Results Summary

The Linear Regression model explains approximately 60% of the variance in house prices.

Median Income (MedInc) is the most influential feature.

Residual analysis indicates a reasonable model fit.

🚀 Future Improvements

Feature scaling and normalization

Polynomial regression

Regularization techniques (Ridge, Lasso)

Advanced models like Random Forest and Gradient Boosting

🏢 Organization

This project was completed as part of an AI & ML task provided by Maincrafts.
