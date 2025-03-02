# Importing the NumPy library
import numpy as np

# Sample dataset of exam scores
exam_scores = [85, 90, 88, 75, 92, 78, 85, 80, 85, 88]

# Applying basic statistical functions
mean_score = np.mean(exam_scores)  # Mean
median_score = np.median(exam_scores)  # Median
std_deviation = np.std(exam_scores)  # Standard Deviation
variance = np.var(exam_scores)  # Variance

# Displaying the results
print("Basic Statistical Analysis of Exam Scores")
print("------------------------------------------------")
print("Mean Score:", mean_score)
print("Median Score:", median_score)
print("Standard Deviation:", std_deviation)
print("Variance:", variance)
print("------------------------------------------------")
