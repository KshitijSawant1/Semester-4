# Library Installation (uncomment if needed)
# !pip install pandas matplotlib seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File Path (change as per your environment)
file_path = "IAI/Experiment 2/Data.csv"

# Load Dataset
df = pd.read_csv(file_path)
df_before = df.copy()  # For comparison

# ===============================
# Dataset Overview
# ===============================
print("Dataset Info:")
df.info()

print("\nFirst 5 Rows:")
print(df.head())

# ===============================
# Null Values - Before Handling
# ===============================
print("\nMissing Values Before Handling:")
print(df_before.isnull().sum())

# ===============================
# Data Cleaning
# ===============================
df.fillna(df.mean(numeric_only=True), inplace=True)

# ===============================
# Null Values - After Handling
# ===============================
print("\nMissing Values After Handling:")
print(df.isnull().sum())

# ===============================
# First and Last 5 Rows (After Handling)
# ===============================
print("\nFirst 5 Rows After Handling:")
print(df.head())

print("\nLast 5 Rows After Handling:")
print(df.tail())

# ===============================
# Duplicate Detection
# ===============================
duplicate_rows = df[df.duplicated()]
print("\nDuplicate Rows:")
print(duplicate_rows)

# ===============================
# Heatmaps: Before & After
# ===============================
fig, axs = plt.subplots(1, 2, figsize=(18, 6))

sns.heatmap(df_before.isnull(), cmap="YlOrRd", cbar=False, linewidths=0.5, linecolor="gray", ax=axs[0])
axs[0].set_title("Null Values Heatmap - Before Handling")

sns.heatmap(df.isnull(), cmap="BuGn", cbar=False, linewidths=0.5, linecolor="gray", ax=axs[1])
axs[1].set_title("Null Values Heatmap - After Handling")

plt.tight_layout()
plt.show()
