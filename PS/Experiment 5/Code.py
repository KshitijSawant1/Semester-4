import pandas as pd

# Import data from a CSV file
df = pd.read_csv('PS/Experiment 5/Data.csv')

# Display the first few rows of the DataFrame
print("Original Data:")
print(df.head())

# Export DataFrame to a CSV file
df.to_csv('exported_data.csv', index=False)

# Renaming columns (alias for better readability)
df.rename(columns={'name': 'student_name', 'score': 'exam_score'}, inplace=True)

# Creating aliases for values in the 'student_name' column
df['student_name'] = df['student_name'].replace({'John': 'Johnny', 'Alice': 'Alicia'})

# Display modified data
print("\nModified Data:")
print(df.head())
