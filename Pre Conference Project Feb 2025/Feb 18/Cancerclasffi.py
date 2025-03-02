# Step 1: Import Required Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, accuracy_score
from imblearn.over_sampling import SMOTE
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# Step 2: Load the Breast Cancer Dataset from UCI Repository
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data"
columns = ['id', 'diagnosis'] + [f'feature_{i}' for i in range(1, 31)]
data = pd.read_csv(url, header=None, names=columns)

# Step 3: Drop the 'id' column as it is not needed
data.drop(columns=['id'], inplace=True)

# Step 4: Save the dataset to a CSV file (optional)
data.to_csv('breast_cancer_wisconsin.csv', index=False)

# Step 5: Check the class distribution
print("Class distribution:\n", data['diagnosis'].value_counts())

# Step 6: Encode the Diagnosis Column ('M' = 1, 'B' = 0)
label_encoder = LabelEncoder()
data['diagnosis'] = label_encoder.fit_transform(data['diagnosis'])  # M -> 1, B -> 0

# Step 7: Define Features and Target Variable
X = data.drop(columns=['diagnosis'])
y = data['diagnosis']

# Step 8: Split the dataset into Training and Testing Sets (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 9: Normalize the Feature Data Using StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 10: Handle Class Imbalance using SMOTE (Synthetic Minority Oversampling Technique)
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

print("Resampled Data Shape:", X_train_resampled.shape, y_train_resampled.shape)

# Step 11: Build a Neural Network Model using TensorFlow/Keras
model = Sequential()
model.add(Dense(64, activation='relu', input_dim=X_train_resampled.shape[1]))
model.add(Dropout(0.5))  # Dropout to prevent overfitting
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))  # Sigmoid activation for binary classification

# Step 12: Compile the Model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Step 13: Train the Model
history = model.fit(X_train_resampled, y_train_resampled, epochs=20, batch_size=32, validation_split=0.2)

# Step 14: Display the Model Summary
model.summary()

# Step 15: Evaluate Model Performance
y_pred = (model.predict(X_test) > 0.5).astype("int32")

# Step 16: Display Classification Report and Accuracy Score
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("Model Accuracy:", accuracy_score(y_test, y_pred))
