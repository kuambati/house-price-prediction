# house-price-prediction
1. Introduction
Accurate house price prediction is an important real-world problem in economics and urban planning. In this project, a Linear Regression model is developed to predict median house prices using the California Housing dataset.
The objective of this task is not only to achieve good prediction accuracy but also to understand the complete machine learning lifecycle, including data loading, exploratory data analysis (EDA), model training, evaluation, and interpretation of results.
Linear Regression is chosen as a baseline model due to its simplicity, interpretability, and efficiency, making it suitable for understanding fundamental regression concepts.
2. Dataset Description
The dataset used in this project is the California Housing dataset, provided by the scikit-learn library. It is derived from the 1990 California census data.
Dataset Characteristics:
•	Number of instances: 20,640
•	Number of features: 8
•	Target variable: MedHouseVal (Median house value in hundreds of thousands of dollars)
Features:
•	MedInc – Median income in the district
•	HouseAge – Median house age
•	AveRooms – Average number of rooms per household
•	AveBedrms – Average number of bedrooms per household
•	Population – Population of the district
•	AveOccup – Average occupancy per household
•	Latitude – Latitude of the district
•	Longitude – Longitude of the district
All features are numerical, and no missing values were found in the dataset, making preprocessing straightforward.
3. Exploratory Data Analysis (EDA)
Exploratory Data Analysis was conducted to understand the structure, distribution, and relationships within the data.
Key Observations:
•	The dataset is clean and well-structured with no null values.
•	Summary statistics reveal varying scales across features.
•	Correlation analysis shows that Median Income (MedInc) has the strongest positive correlation with median house prices.
•	Geographic features (Latitude and Longitude) also influence house prices, indicating regional pricing trends.
A correlation heatmap was used to visually inspect linear relationships between features and the target variable.
 
Fig 1: Correlation heatmap to understand linear relationships between features and the target variable
4. Data Preparation
The dataset was divided into:
•	Features (X): All input variables
•	Target (y): Median house value
To evaluate the model fairly, the data was split into:
•	Training set: 80%
•	Testing set: 20%
A fixed random_state was used to ensure reproducibility of results.
5. Model Selection and Training
A Linear Regression model was trained using the training dataset. The model learns a linear relationship between the input features and the target variable by estimating coefficients that minimize the error between predicted and actual values.
Linear Regression is suitable here because:
•	It provides a strong baseline for regression problems.
•	The coefficients are easy to interpret.
•	It helps identify how each feature contributes to house prices.
6. Model Evaluation
The trained model was evaluated on the test dataset using standard regression metrics:
Evaluation Metrics:
•	MAE (Mean Absolute Error): Measures average absolute prediction error
•	RMSE (Root Mean Squared Error): Penalizes larger errors more strongly
•	R² Score: Measures the proportion of variance explained by the model
Results:
Metric	Value (Approx.)
MAE	0.53
RMSE	0.73
R² Score	0.60
The R² score of approximately 0.60 indicates that the model explains about 60% of the variance in house prices, which is reasonable for a simple linear model on real-world data. An Actual vs Predicted plot shows that predictions generally follow the ideal diagonal line, with some spread due to model limitations.
 
Fig 2 : A plot that shows actual vs predicted house prices
7. Residual Analysis
Residual analysis was performed to assess model assumptions and error behavior.
Observations:
•	The residual distribution is approximately bell-shaped, indicating near-normal error distribution.
•	The residuals vs predicted values plot shows no strong systematic pattern.
•	Errors appear randomly distributed around zero, suggesting the model does not suffer from severe bias.
 
Fig 3: Residual Distribution of the Linear Regression Model

8. Conclusion
This project successfully demonstrates the end-to-end machine learning workflow using a Linear Regression model for house price prediction.
Key Takeaways:
•	Linear Regression provides a strong and interpretable baseline.
•	Median income is the most influential feature for predicting house prices.
•	The model achieves reasonable performance despite its simplicity.
9. Future Improvements
To further improve model performance, the following enhancements can be explored:
•	Feature scaling and normalization
•	Polynomial regression to capture non-linear relationships
•	Regularization techniques such as Ridge and Lasso
•	Advanced models like Random Forest, Gradient Boosting, or XGBoost

