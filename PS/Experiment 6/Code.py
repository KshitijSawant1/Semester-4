import pandas as pd

# Sample dataset
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [22, 17, 30, 16],
    'email': ['alice@gmail.com', 'bob@gmail.com', 'charlie@gmail.com', 'david@gmail.com'],
    'marks': [85, 45, 78, 92]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# ----------------------------
# Identifier Function: Add unique ID
df['student_id'] = ['SID' + str(i).zfill(3) for i in range(1, len(df)+1)]

# Constraint Function: Filter students age > 18 only
df_valid = df[df['age'] > 18]

print("\nDataset After Adding Identifier and Applying Constraint (Age > 18):")
print(df_valid)
