# Step 1: Import Required Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

# Step 2: Load the Dataset
dataset = pd.read_csv('Data CSV Files/Iris.csv')  # Update the path if needed
print("Dataset Loaded Successfully.")

# Step 3: Display Dataset Summary
print("\nDataset Description:\n", dataset.describe())

# Step 4: Encode Target Variable ('Species')
label_encoder = LabelEncoder()
dataset['encoded'] = label_encoder.fit_transform(dataset['Species'])
print("\nUnique Species Classes:", list(dataset['Species'].unique()))
print("Encoded Classes:", list(dataset['encoded'].unique()))

# Step 5: Define Features and Target Variable
X = dataset.iloc[:, [1, 2, 3, 4]].values  # SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm
y = dataset.iloc[:, 6].values  # Encoded Target Variable

# Step 6: Split Dataset into Training and Testing Set
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=0)
print("\nDataset Split into Training and Testing Sets.")

# Step 7: Standardize Features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
print("\nFeatures Standardized.")

# Step 8: Initialize Logistic Regression Model
classifier = LogisticRegression()

# Step 9: Hyperparameter Tuning using GridSearchCV
parameter_grid = {
    'penalty': ['l2'],  # Only 'l2' is valid for 'lbfgs' solver
    'C': [1, 2, 3, 4, 5, 6, 10, 20, 30, 40, 50],
    'max_iter': [100, 200, 300]
}

classifier_regressor = GridSearchCV(classifier, param_grid=parameter_grid, scoring='accuracy', cv=5)
classifier_regressor.fit(X_train, y_train)

# Step 10: Train the Best Model
best_classifier = classifier_regressor.best_estimator_
best_classifier.fit(X_train, y_train)
print("\nModel Trained with Best Hyperparameters.")

# Step 11: Make Predictions
y_pred = best_classifier.predict(X_test)

# Step 12: Evaluate Model Performance
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nBest Hyperparameters:", classifier_regressor.best_params_)
print("\nModel Accuracy:", accuracy_score(y_test, y_pred))

# Step 13: Visualizing Model Performance
plt.figure(figsize=(6, 4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, cmap="Blues", fmt="d", xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_)
plt.xlabel('Predicted Label')
plt.ylabel('Actual Label')
plt.title('Confusion Matrix Heatmap')
plt.show()