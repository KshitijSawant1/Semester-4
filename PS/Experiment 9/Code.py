import pandas as pd

# Sample dataset
data = {
    'Student Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Score': [85, 35, 67, 45, 28]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Trigger function to automatically update Pass/Fail based on Score
def trigger_pass_fail(score):
    return 'Pass' if score >= 40 else 'Fail'

# Applying the trigger using the apply() method
df['Result'] = df['Score'].apply(trigger_pass_fail)

# String Operation: Convert all names to uppercase
df['Student Name'] = df['Student Name'].str.upper()

# Display the modified DataFrame
print("Updated Dataset with Trigger and String Operations:")
print(df)

# Export updated data to a CSV file
df.to_csv('updated_student_scores.csv', index=False)
