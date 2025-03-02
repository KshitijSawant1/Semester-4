import pandas as pd

# Load the Iris Flower Dataset
iris_data = pd.read_csv('IAI/Experiment 3/Iris Flower Dataset.csv')

# Create Data Frame Info
print("Iris Flower Dataset Info:\n")
print(iris_data.info())

# Filtering: Select flowers where petal_length > 4.5
filtered_iris = iris_data[iris_data['petal_length'] > 4.5]
print("\nFiltered Flowers with Petal Length > 4.5:\n", filtered_iris)

# Apply Function: Calculate Sepal Area (sepal_length * sepal_width)
iris_data['SepalArea'] = iris_data.apply(
    lambda row: row['sepal_length'] * row['sepal_width'], axis=1
)
print("\nIris Dataset with Sepal Area:\n", iris_data.head())
