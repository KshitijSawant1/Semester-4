import pandas as pd

# Sample dataset
data = {
    'Name': ['alice', 'bob', 'charlie', 'david'],
    'City': ['mumbai', 'delhi', 'pune', 'bangalore'],
    'Age': [22, 25, 24, 23]
}

# Creating a DataFrame
df = pd.DataFrame(data)
print("Original Dataset:\n", df)

# -------- Modifying values in a column -------- #
# Capitalize all names
df['Name'] = df['Name'].str.title()

# -------- Updating values directly -------- #
# Increase age by 1 year for all
df['Age'] = df['Age'] + 1

# -------- String Operations -------- #
# Convert city names to uppercase
df['City'] = df['City'].str.upper()

# Add a new column with custom string formatting
df['Info'] = df['Name'] + ' from ' + df['City']

print("\nModified Dataset:\n", df)
