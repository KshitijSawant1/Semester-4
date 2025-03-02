import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1) Create Object:
print("Creating a Pandas DataFrame object...")

# 2) Import path:
path = '/Users/kshitijksawant/Programs/Python PS Sem 4 TCET/Experiment 2/Data2.1.csv'  # Replace with the path to your CSV file

# 3) Read CSV File:
df = pd.read_csv(path)

# 4) Read 1st 5 Lines:
print("First 5 lines of the dataset:")
print(df.head())

# 5) Read Last 5 Lines:
print("Last 5 lines of the dataset:")
print(df.tail())

# 6) Information:
print("Information about the dataset:")
print(df.info())

# 7) Describe:
print("Statistical summary of the dataset:")
print(df.describe())

# 8) Find Null Values:
print("Checking for null values in the dataset:")
print(df.isnull().sum())

# 9) Import Data Visualization Command:
sns.histplot(df['your_column'], kde=True)  # Histogram of 'your_column'
plt.title("Distribution of 'Column Data'")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()
