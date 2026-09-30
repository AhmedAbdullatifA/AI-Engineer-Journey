# Problem — Student Grades Analysis

## Requirements

# Using **NumPy only**, build a program to analyze a dataset containing the grades of 10 students across 5 subjects.

### Tasks

# 1. Calculate the average grade for each student.
# 2. Calculate the average grade for each subject.
# 3. Identify the student with the highest average grade.
# 4. Identify the subject with the highest average grade.
# 5. Find all students whose average grade is greater than or equal to 80.
# 6. Find all students whose grades are greater than or equal to 60 in every subject.
# 7. Calculate the overall average grade across all students and subjects.
# 8. Create a new array with the same shape as the original grades array and classify each grade as:

#    `A` → 90 or above
#    `B` → 80–89
#    `C` → 70–79
#    `D` → 60–69
#    `F` → below 60

### Constraints

# Use **NumPy only**.
# Do not use Pandas, SciPy, Statistics, or other Python libraries.
# Do not use `for` or `while` loops.
# Use NumPy operations such as vectorization, boolean indexing, 
# aggregation functions, and the `axis` parameter wherever appropriate.


import numpy as np

grades = np.array([
    [85, 72, 90, 66, 78],
    [91, 88, 76, 95, 89],
    [55, 67, 61, 70, 58],
    [100, 92, 94, 88, 96],
    [73, 81, 69, 77, 85],
    [64, 59, 72, 68, 61],
    [88, 90, 85, 92, 87],
    [79, 75, 83, 71, 80],
    [45, 52, 48, 60, 55],
    [93, 86, 91, 89, 94]
])



# 1. Calculate the average grade for each student.

average_student = np.mean(grades,axis=1)
print("The average grade for each student is :")
print(average_student)

# output => The average grade for each student is :
# [78.2 87.8 62.2 94.  77.  64.8 88.4 77.6 52.  90.6]




# 2. Calculate the average grade for each subject.

average_subject = np.mean(grades,axis=0)
print("The average grade for each subject is :")
print(average_subject)

# output => The average grade for each subject is :
# [77.3 76.2 76.9 77.6 78.3]




# 3. Identify the student with the highest average grade.

top_student_grades = grades[np.argmax(average_student)]
print("The student with the highest average grade is :")
print(top_student_grades)

# output => the student with the highest average grade is :
# [100  92  94  88  96]




# 4. Identify the subject with the highest average grade.

print("The subject with the highest average grade is :")
print(grades[:,np.argmax(average_subject)])

# output => The subject with the highest average grade is :
# [78 89 58 96 85 61 87 80 55 94]




# 5. Find all students whose average grade is greater than or equal to 80.

very_good_student = np.where(average_student >= 80)
print("The sudents whose average grade is greater than or equal to 80 are :")
print(grades[very_good_student[0]])

# output => The sudents whose average grade is greater than or equal to 80 are :
# [[ 91  88  76  95  89]
#  [100  92  94  88  96]
#  [ 88  90  85  92  87]
#  [ 93  86  91  89  94]]




# 6. Find all students whose grades are greater than or equal to 60 in every subject.

pass_students = (grades >= 60).all(axis=1)
print("The students whose grades are greater than or equal to 60 in every subject are :")
print(grades[pass_students])

# output => The students whose grades are greater than or equal to 60 in every subject are :
# [[ 85  72  90  66  78]
#  [ 91  88  76  95  89]
#  [100  92  94  88  96]
#  [ 73  81  69  77  85]
#  [ 88  90  85  92  87]
#  [ 79  75  83  71  80]
#  [ 93  86  91  89  94]]




# 7. Calculate the overall average grade across all students and subjects.

print("The overall average grade across all students and subjects :")
print(np.mean(grades))

# The overall average grade across all students and subjects :
# 77.26




# 8. Create a new array with the same shape as the original grades array and classify each grade as:

#    `A` → 90 or above
#    `B` → 80–89
#    `C` → 70–79
#    `D` → 60–69
#    `F` → below 60

classify_grade = np.where(grades >= 90, 'A', np.where(grades >= 80, 'B', 
np.where(grades >=70, 'C', np.where(grades >=60, 'D','F'))))       
print("The Grades after Classify it :")       
print(classify_grade)


# output => The Grades after Classify it :
# [['B' 'C' 'A' 'D' 'C']
#  ['A' 'B' 'C' 'A' 'B']
#  ['F' 'D' 'D' 'C' 'F']
#  ['A' 'A' 'A' 'B' 'A']
#  ['C' 'B' 'D' 'C' 'B']
#  ['D' 'F' 'C' 'D' 'D']
#  ['B' 'A' 'B' 'A' 'B']
#  ['C' 'C' 'B' 'C' 'B']
#  ['F' 'F' 'F' 'D' 'F']
#  ['A' 'B' 'A' 'B' 'A']]
