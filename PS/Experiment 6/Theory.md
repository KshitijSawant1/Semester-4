Here's a complete write-up for **Experiment 6 – Constraint Function & Identifier Function on Dataset Using Python**:

---

## 🧪 **Experiment 6 – Applying Constraint & Identifier Functions on Dataset**

---

### 🎯 **Learning Objective**
Students should be able to:
- Understand how to apply **constraint functions** on dataset fields to ensure data validity.
- Apply **identifier functions** to uniquely identify or track entries in a dataset.

---

### 🛠️ **Tools**
- **Python**
- **Pandas** (for DataFrame operations)
- Jupyter Notebook / PyCharm / VS Code / Google Colab

---

### 📚 **Theory**

#### 🔹 What is a **Constraint Function**?
A **Constraint Function** enforces certain rules or conditions on data columns to ensure consistency and validity.

**Example:**
- Ensuring age is greater than 18.
- Ensuring salary is non-negative.

```python
df[df['age'] > 18]
```

---

#### 🔹 What is an **Identifier Function**?
An **Identifier Function** helps in uniquely identifying records in a dataset. It often includes:
- Adding a unique ID column.
- Using fields like Email or Roll Number as unique identifiers.

**Example:**
```python
df['student_id'] = range(1, len(df)+1)
```

---

### 🧑‍💻 **Code & Output**

```python
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
```

---

### ✅ **Output**

```
Original Dataset:
      name  age             email  marks
0    Alice   22    alice@gmail.com     85
1      Bob   17      bob@gmail.com     45
2  Charlie   30  charlie@gmail.com     78
3    David   16    david@gmail.com     92

Dataset After Adding Identifier and Applying Constraint (Age > 18):
      name  age             email  marks student_id
0    Alice   22    alice@gmail.com     85     SID001
2  Charlie   30  charlie@gmail.com     78     SID003
```

---

### 🧠 **Learning Outcomes**

- 🔸 **LO6.1:** You learned what constraint and identifier functions are and how they apply to datasets.
- 🔸 **LO6.2:** You understood how to use pandas in Python to add identifiers and enforce data constraints.

---

### 🎓 **Course Outcomes**
Upon completion, students will be able to:
- Use Python to validate data using constraints.
- Uniquely identify records using identifiers in real-world datasets.

---

### 📝 **Conclusion**
This experiment shows how we can **automate data validation** and **uniquely identify entries** in any dataset using Python. Such techniques are crucial in real-world data preprocessing and cleaning.

---

Would you like the same in **DOC/PDF format**, or want to add graphs or charts as well?