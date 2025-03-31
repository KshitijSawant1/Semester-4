Here is the complete write-up for:

---

## 🧪 **Experiment 7 – Python Data Manipulation: Modifying, Updating, and String Operations on Project Datasets**

---

### 🎯 **Learning Objective**
Students should be able to:
- Understand how to modify and update data using Python.
- Perform string operations such as uppercase, lowercase, replacement, and formatting on dataset values.

---

### 🛠️ **Tools Used**
- Python
- Pandas Library
- Jupyter Notebook / Google Colab / VS Code

---

### 📚 **Theory**

Sure! Here's an **enhanced and detailed theory section** for **Experiment 7 – Python Data Manipulation: Modifying, Updating, and String Operations on Project Datasets**:

---

## 📚 **Theory**

### 🔹 What is Data Manipulation?

**Data manipulation** is the process of changing data to make it organized, structured, and ready for analysis or presentation. It is a core part of data preprocessing, especially in data science and machine learning projects.

#### ✅ Key Data Manipulation Operations in Python:
1. **Loading and Viewing Data**  
   - Using `pandas.read_csv()` to load data  
   - Using `.head()`, `.tail()`, and `.info()` to view and understand datasets

2. **Accessing and Modifying Data**
   - Accessing columns and rows using `df['column']` or `df.loc[]`
   - Modifying column values based on conditions (e.g., `df[df['age'] > 18]`)
   - Adding new columns using computed or derived data

3. **Updating Values**
   - Direct value assignment: `df.at[index, 'column'] = new_value`
   - Updating using logic/conditions with `.apply()` or `.loc[]`

4. **Removing or Replacing Data**
   - `df.drop()` to remove rows or columns  
   - `df.replace()` to replace specific values  
   - `df.fillna()` to handle missing values

---

### 🔹 What are String Operations?

When working with **textual (string) data** in datasets, string operations help clean, format, or extract information from text columns.

#### ✅ Common String Functions in Python (Pandas `.str` Accessor):
| Function             | Description                                  | Example                                  |
|----------------------|----------------------------------------------|------------------------------------------|
| `.str.upper()`       | Converts all characters to uppercase         | `'kshitij' → 'KSHITIJ'`                  |
| `.str.lower()`       | Converts all characters to lowercase         | `'MUMBAI' → 'mumbai'`                    |
| `.str.title()`       | Capitalizes the first letter of each word    | `'john doe' → 'John Doe'`               |
| `.str.strip()`       | Removes leading and trailing whitespace      | `'  hello  ' → 'hello'`                  |
| `.str.replace(a,b)`  | Replaces `a` with `b` in string              | `'data science' → 'data_science'`        |
| `.str.contains()`    | Checks if string contains a substring        | `'abc'.contains('b') → True`             |
| `.str.len()`         | Returns length of each string in the column  | `'apple' → 5`                            |

---

### 🔹 Importance in Real-World Projects

- **Standardizing names, locations, emails**, etc., in customer databases
- **Correcting misspelled or inconsistent entries** (e.g., `‘Mum’`, `‘Mumbai’`, `‘mumbai’`)
- **Creating derived fields** like `Full Name`, `Address`, `Tags`, etc.
- Preprocessing textual data for NLP and machine learning models

---

### 🔹 Example Scenario

Imagine a dataset where the **names** are in lowercase and **cities** are inconsistently capitalized:

| Name     | City        |
|----------|-------------|
| alice    | Mumbai      |
| bob      | mumbai      |
| charlie  | DELHI       |

Using string operations:
- Convert all names to title case → `Alice`, `Bob`, `Charlie`
- Convert all cities to uppercase → `MUMBAI`, `DELHI`

---

Would you like a visual table or diagram added for a report too?

### 🧑‍💻 **Code & Output**

```python
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
```

---

### ✅ **Output**

```
Original Dataset:
      Name      City  Age
0   alice    mumbai   22
1     bob     delhi   25
2  charlie     pune   24
3   david  bangalore  23

Modified Dataset:
      Name       City  Age                 Info
0   Alice     MUMBAI   23     Alice from MUMBAI
1     Bob      DELHI   26       Bob from DELHI
2  Charlie       PUNE   25   Charlie from PUNE
3   David  BANGALORE   24  David from BANGALORE
```

---

### ✅ **Learning Outcomes**

- **LO7.1:** Define and apply basic data manipulation and string operations on datasets.
- **LO7.2:** Learn the steps to apply operations like `.str.upper()`, direct value updates, and conditional modifications.

---

### 📘 **Course Outcomes**
After completing this experiment, students will be able to:
- Modify data for analysis.
- Apply transformations using string functions effectively in Python using Pandas.

---

### 📝 **Conclusion**
Data manipulation and string operations are essential for cleaning and preparing datasets for analysis or visualization. Python makes it simple using the Pandas library, enabling efficient and readable transformations.

---

Would you like a DOCX or PDF version of this report?