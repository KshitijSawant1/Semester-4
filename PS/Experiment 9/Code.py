import pandas as pd

# Sample DataFrame
data = {
    "Customer_ID": [101, 102, 103, 104],
    "Name": ["alice ", "Bob", "CHARLIE", "dave"],
    "Email": ["alice@example.com", "bob@Example.com", "charlie@example", "dave@example.com"],
    "Status": ["new", "inactive", "active", "new"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Define a trigger: if email doesn't contain ".com", mark status as 'invalid email'
df.loc[~df['Email'].str.endswith('.com'), 'Status'] = 'invalid email'

# String Operations
df['Name'] = df['Name'].str.strip().str.title()   # Clean spaces and capitalize
df['Email'] = df['Email'].str.lower()             # Normalize emails to lowercase

# Output
print("\nModified Data After Trigger and String Functions:")
print(df)
