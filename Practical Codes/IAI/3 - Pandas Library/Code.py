import pandas as pd
# Load the Student Classification Dataset
student_data = pd.read_csv('Practical Codes/IAI/3 - Pandas Library/Data.csv')

# Creating a sample DataFrame for Exam Scores (to join)
exam_scores = pd.DataFrame({
    'Id': [1, 2, 3, 4, 5],
    'Exam_Score': [85, 78, 90, 88, 92]
})

# Merging: Merge student data with exam scores on 'Id'
merged_data = pd.merge(student_data, exam_scores, on='Id', how='left')
print("\nMerged Dataset:\n", merged_data.head())

# Sorting: Sort by Exam Score descending
sorted_data = merged_data.sort_values(by='Exam_Score', ascending=False)
print("\nSorted by Exam Score:\n", sorted_data)

# Pivot Table: Average Exam Score by High School Type
pivot_table = merged_data.pivot_table(
    values='Exam_Score', index='High_School_Type', aggfunc='mean'
)
print("\nPivot Table - Average Exam Score by High School Type:\n", pivot_table)

# Indexing: Set 'Id' as the index
indexed_data = merged_data.set_index('Id')
print("\nIndexed Dataset:\n", indexed_data.head())
