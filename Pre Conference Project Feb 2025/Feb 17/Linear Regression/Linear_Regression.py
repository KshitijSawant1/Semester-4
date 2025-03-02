import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Load the Dataset
file_path = "Data CSV Files/tvmarketing.csv"  # Update with the correct file path
advertising = pd.read_csv(file_path)

# Step 2: Display Dataset Information
print("First 5 Rows:\n", advertising.head())
print("Last 5 Rows:\n", advertising.tail())
print("Dataset Information:")
print(advertising.info())
print("Statistical Summary:")
print(advertising.describe())

# Step 3: Visualizing Data
sns.pairplot(advertising, x_vars=['TV'], y_vars='Sales', size=7, aspect=0.7, kind='scatter')
plt.title("TV vs Sales Scatter Plot")
plt.show()

# Step 4: Prepare Data for Regression
X = advertising['TV'].values.reshape(-1, 1)  # Convert to 2D array
y = advertising['Sales']

# Step 5: Split Data into Training & Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=100)

# Step 6: Train the Model
lr = LinearRegression()
lr.fit(X_train, y_train)

# Step 7: Model Coefficients
print("Intercept:", lr.intercept_)
print("Coefficient:", lr.coef_[0])

# Equation of Regression Line
print(f"y = {lr.intercept_:.3f} + {lr.coef_[0]:.3f} * TV")

# Step 8: Make Predictions
y_pred = lr.predict(X_test)

# Step 9: Visualization of Actual vs Predicted Sales
plt.figure(figsize=(10, 5))
plt.plot(range(len(y_test)), y_test, label="Actual Sales", linestyle="-", color="blue")
plt.plot(range(len(y_pred)), y_pred, label="Predicted Sales", linestyle="dashed", color="red")
plt.legend()
plt.title("Actual vs Predicted Sales")
plt.xlabel("Index")
plt.ylabel("Sales")
plt.show()

# Step 10: Error Analysis
error_terms = y_test - y_pred
sns.histplot(error_terms, bins=30, kde=True, color="blue")
plt.title("Distribution of Error Terms")
plt.xlabel("Error")
plt.ylabel("Frequency")
plt.show()

# Step 11: Model Performance Metrics
mse = mean_squared_error(y_test, y_pred)
r_squared = r2_score(y_test, y_pred)
print('Mean Squared Error:', mse)
print('R² Score:', r_squared)

# Step 12: Regression Line Plot
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Sales')
plt.ylabel('Predicted Sales')
sns.regplot(x=y_test, y=y_pred)
plt.title("Regression Line: Actual vs Predicted Sales")
plt.show()

print("\nModel Training and Evaluation Completed Successfully!")