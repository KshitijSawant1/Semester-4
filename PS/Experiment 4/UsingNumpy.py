import numpy as np

# Sample dataset
data = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

# Calculating the quantile at 0.5 (median)
median = np.quantile(data, 0.5)
print("Median (Quantile at 0.5):", median)

# Calculating the 25th and 75th percentiles
percentile_25 = np.percentile(data, 25)
percentile_75 = np.percentile(data, 75)

print("25th Percentile:", percentile_25)
print("75th Percentile:", percentile_75)
