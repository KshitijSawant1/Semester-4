import pandas as pd

# Load the data from a CSV file
# Replace 'your_data.csv' with the actual path to your file
df = pd.read_csv('Experiment 2/Data.csv')

# Specify the column to perform operations on
# Replace 'your_column' with the actual column name in your data
column_name = 'your_column'

# Performing addition operation (adding 5 to each value in the column)
df[column_name] = df[column_name] + 5

# Performing subtraction operation (subtracting 2 from each value in the column)
df[column_name] = df[column_name] - 2

# Display the updated DataFrame
print("Updated DataFrame:")
print(df)

# Save the updated DataFrame to a new CSV file
# Replace 'updated_data.csv' with your desired output file name
df.to_csv('updated_data.csv', index=False)

print("\nThe updated DataFrame has been saved to 'updated_data.csv'")
