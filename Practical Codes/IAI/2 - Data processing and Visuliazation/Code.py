# !pip install pandas matplotlib seaborn

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File Path
file_path = "Practical Codes/IAI/2 - Data processing and Visuliazation/Data.csv"

# Read CSV File
df = pd.read_csv(file_path)

# Make a copy for comparison
df_before = df.copy()

# ===============================
# Subplot: Heatmap Before & After
# ===============================
fig, axs = plt.subplots(1, 2, figsize=(18, 6))

# Heatmap Before
sns.heatmap(df_before.isnull(), cmap="YlOrRd", cbar=False, linewidths=0.5, linecolor="gray", ax=axs[0])
axs[0].set_title("Null Values Heatmap - Before Handling")

# Handle Missing Values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Heatmap After
sns.heatmap(df.isnull(), cmap="BuGn", cbar=False, linewidths=0.5, linecolor="gray", ax=axs[1])
axs[1].set_title("Null Values Heatmap - After Handling")

plt.tight_layout()
plt.show()

# ===============================
# Dataset Analysis
# ===============================
print("\nMissing Values Before Handling:")
print(df_before.isnull().sum())

print("\nMissing Values After Handling:")
print(df.isnull().sum())

# Optional: Check Duplicates
duplicate_rows = df[df.duplicated()]
print("\nDuplicate Rows:")
print(duplicate_rows)
