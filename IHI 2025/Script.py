import pandas as pd
from datetime import datetime

# Load the CSV file
csv_file = "Mission Launches.csv"
data = pd.read_csv(csv_file)

# Function to reformat the date
def reformat_date(date_str):
    try:
        if date_str.lower() == 'none':  # Exclude invalid date values
            return None
        dt_obj = datetime.strptime(date_str, "%a %b %d, %Y %H:%M %Z")
        return dt_obj.strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        print(f"Skipping invalid date: {date_str}")
        return None

# Escape single quotes in text fields
def escape_single_quotes(value):
    if isinstance(value, str):
        return value.replace("'", "''")
    return value

# Reformat the date column and escape text fields
data["Date"] = data["Date"].apply(reformat_date)
text_columns = ["Organisation", "Location", "Detail", "Rocket_Status", "Mission_Status"]
for column in text_columns:
    data[column] = data[column].apply(escape_single_quotes)

# Replace NaN values in the 'Price' column with NULL
data["Price"] = data["Price"].apply(lambda x: "NULL" if pd.isna(x) else x)

# Filter out rows with invalid dates
filtered_data = data.dropna(subset=["Date"])

# Generate SQL statements
table_name = "SpaceMissions"
sql_statements = []

for _, row in filtered_data.iterrows():
    sql = f"""
    INSERT INTO {table_name} (Organisation, Location, Date, Detail, Rocket_Status, Price, Mission_Status)
    VALUES (
        '{row['Organisation']}',
        '{row['Location']}',
        '{row['Date']}',
        '{row['Detail']}',
        '{row['Rocket_Status']}',
        {row['Price']},
        '{row['Mission_Status']}'
    );
    """
    sql_statements.append(sql.strip())

# Write the SQL statements to a file
output_file = "filtered_insert_statements.sql"
with open(output_file, "w") as file:
    file.write("\n".join(sql_statements))

print(f"SQL insert statements have been written to {output_file}, excluding invalid rows.")
