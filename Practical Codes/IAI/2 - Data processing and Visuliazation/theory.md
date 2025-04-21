Here's a **detailed line-by-line explanation** of the Python code you've provided, which performs **data analysis and visualization** using `pandas`, `matplotlib`, and `seaborn`.

---

## 🧠 Objective:

To clean and visualize a dataset (`Data.csv`) by:

- Checking for missing values
- Filling missing data
- Detecting duplicates
- Displaying heatmaps before and after cleaning

---

## 🔍 Code Explanation

```python
# Library Installation (uncomment if needed)
# !pip install pandas matplotlib seaborn
```

- If these libraries are not already installed, you can uncomment and run this line in a notebook or terminal.

---

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

- Imports libraries:
  - `pandas` for data manipulation.
  - `matplotlib.pyplot` and `seaborn` for plotting heatmaps.

---

```python
# File Path (change as per your environment)
file_path = "IAI/Experiment 2/Data.csv"
```

- Stores the path of your CSV file.

---

```python
# Load Dataset
df = pd.read_csv(file_path)
df_before = df.copy()  # For comparison
```

- Reads the CSV file into a DataFrame `df`.
- Creates a copy `df_before` to retain the **original state before cleaning**, which is useful for comparing heatmaps.

---

```python
# ===============================
# Dataset Overview
# ===============================
print("Dataset Info:")
df.info()
```

- Prints info like:
  - Column names
  - Non-null counts
  - Data types
  - Memory usage

---

```python
print("\nFirst 5 Rows:")
print(df.head())
```

- Displays the **first 5 records** of the dataset.

---

```python
# ===============================
# Null Values - Before Handling
# ===============================
print("\nMissing Values Before Handling:")
print(df_before.isnull().sum())
```

- Shows the number of **missing values per column** in the original dataset (`df_before`).

---

```python
# ===============================
# Data Cleaning
# ===============================
df.fillna(df.mean(numeric_only=True), inplace=True)
```

- Replaces missing values in **numeric columns only** (`Age`, `Income` in this case) with their **column means**.
- Non-numeric columns like `Name` or `City` are **ignored** during this operation.

---

```python
# ===============================
# Null Values - After Handling
# ===============================
print("\nMissing Values After Handling:")
print(df.isnull().sum())
```

- Prints the **remaining null values** in the cleaned DataFrame `df`.

---

```python
# ===============================
# First and Last 5 Rows (After Handling)
# ===============================
print("\nFirst 5 Rows After Handling:")
print(df.head())

print("\nLast 5 Rows After Handling:")
print(df.tail())
```

- Displays the **top 5** and **bottom 5** records **after** missing value treatment.

---

```python
# ===============================
# Duplicate Detection
# ===============================
duplicate_rows = df[df.duplicated()]
print("\nDuplicate Rows:")
print(duplicate_rows)
```

- Checks for duplicate rows.
- If any are found, they are printed.

---

```python
# ===============================
# Heatmaps: Before & After
# ===============================
fig, axs = plt.subplots(1, 2, figsize=(18, 6))
```

- Creates **2 side-by-side subplots** for visual comparison.

---

```python
sns.heatmap(df_before.isnull(), cmap="YlOrRd", cbar=False, linewidths=0.5, linecolor="gray", ax=axs[0])
axs[0].set_title("Null Values Heatmap - Before Handling")
```

- Heatmap shows **missing values before** cleaning.
- Color map: Yellow to Red (indicating severity).

---

```python
sns.heatmap(df.isnull(), cmap="BuGn", cbar=False, linewidths=0.5, linecolor="gray", ax=axs[1])
axs[1].set_title("Null Values Heatmap - After Handling")
```

- Heatmap shows **missing values after** cleaning.
- Color map: Blue to Green (fresher/cleaner look).

---

```python
plt.tight_layout()
plt.show()
```

- Adjusts spacing and displays the two heatmaps neatly.

---

## 🧾 Sample `Data.csv` Record (Based on your input):

| ID  | Name | Age  | Income  | City     |
| --- | ---- | ---- | ------- | -------- |
| 101 | John | 25.0 | 50000.0 | New York |

You can expand this file with more rows, some of which may have missing values (`NaN`) in `Age` or `Income` to test the heatmap.

---

## ✅ Output Summary:

- **Before Cleaning:** Red/yellow squares show missing values.
- **After Cleaning:** Heatmap becomes clean (green/blue).
- **Duplicates:** Detected (if any).
- **Head/Tail:** Shows progress from raw to clean data.

Would you like me to help generate a sample `Data.csv` with missing values and duplicates for practice?
