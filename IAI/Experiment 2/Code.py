# Library Install (if not installed, uncomment and install)
# !pip install pandas matplotlib seaborn

# Object Creation
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import File (Assuming 'data.csv' is present in the working directory)
file_path = "IAI/Experiment 2/Data.csv"

# Read CSV File
df = pd.read_csv(file_path)

# Understand the CSV File
print("Dataset Info:")
df.info()
print("\nFirst 5 rows of dataset:")
print(df.head())

# Handling Missing Values
print("\nMissing Values Before Handling:")
print(df.isnull().sum())

# Filling missing values with mean (for numerical columns)
df.fillna(df.mean(numeric_only=True), inplace=True)  # FIXED

# Read 1st & last 5 lines
print("\nFirst 5 rows after handling missing values:")
print(df.head())
print("\nLast 5 rows after handling missing values:")
print(df.tail())

# Identified Duplicate Data
duplicate_rows = df[df.duplicated()]
print("\nDuplicate Rows:")
print(duplicate_rows)

# Find Null Values
null_values = df.isnull().sum()
print("\nNull Values in Dataset:")
print(null_values)

# Import Data Visualization Object
# Generate heatmap with a lighter color scheme
plt.figure(figsize=(10, 5))
sns.heatmap(df.isnull(), cmap="coolwarm", cbar=False, linewidths=0.5, linecolor="gray")
plt.title("Null Values Heatmap (Lighter Colors)")
plt.show()

