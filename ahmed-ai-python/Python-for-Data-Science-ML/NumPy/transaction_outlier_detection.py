# Problem — Transaction Outlier Detection

## Requirements

# Using **NumPy only**, build a program to analyze financial transaction data collected over 12 days, with 6 transactions recorded per day.

### Tasks

# 1. Calculate the average transaction value for each day.

# 2. Calculate the average value of each transaction position across all days.

# 3. Detect outliers using the following rule:

#    `|x - mean| > 2 * standard_deviation`

# 4. Create a Boolean mask identifying the positions of all detected outliers.

# 5. Extract all outlier values from the dataset.

# 6. Calculate the mean of all non-outlier values.

# 7. Replace every outlier with the mean of the non-outlier values.

# 8. Store the cleaned dataset in a new array named `cleaned_transactions`.

# 9. Recalculate the average transaction value for each day after cleaning.

# 10. Compare the daily averages before and after cleaning.

# 11. Identify the day with the largest decrease in its average transaction value.

# 12. Calculate the percentage change in the average of each day using:

# `percentage_change = ((old_average - new_average) / old_average) * 100`

# 13. Create the final cleaned array without using loops:

#  Outliers must be replaced with their cleaned values.
#  Non-outlier values must remain unchanged.
#  The final array must have the same shape as the original dataset.

# ### Constraints

#  Use **NumPy only**.
#  Do not use Pandas, SciPy, Statistics, or other Python libraries.
#  Do not use `for` or `while` loops.
#  Use vectorized NumPy operations.
#  Use Boolean masking and NumPy aggregation functions where appropriate.
#  The entire solution should be implemented without explicit iteration.


import numpy as np


transactions = np.array([

    [120, 135, 150, 142, 128, 131],
    [110, 115, 108, 120, 117, 113],
    [500, 130, 125, 140, 135, 128],
    [145, 152, 149, 155, 148, 151],
    [90,  95,  88,  92,  87,  91],
    [160, 158, 162, 165, 159, 161],
    [130, 128, 135, 132, 129, 131],
    [140, 145, 142, 138, 141, 143],
    [75,  80,  72, 78,  76,  74],
    [155, 150, 148, 152, 149, 151],
    [100, 105, 98,  102, 97,  101],
    [135, 132, 138, 500, 140, 136]
    
])




# 1. Calculate the average transaction value for each day.

average_transaction_day = transactions.mean(axis=1)
print("The average transaction value for each day is :")
print(average_transaction_day)

# output => The average transaction value for each day is :
# [134.33333333 113.83333333 193.         150.          90.5
#  160.83333333 130.83333333 141.5         75.83333333 150.83333333
#  100.5        196.83333333]




# 2. Calculate the average value of each transaction position across all days.

print("The average value of each transaction position across all days is :")
print(transactions.mean(axis=0))

# output => The average value of each transaction position across all days is :
# [155.         127.08333333 126.25       159.66666667 125.5
#  125.91666667]




# 3. Detect outliers using the following rule:

#    `|x - mean| > 2 * standard_deviation`

mean = transactions.mean()
std = transactions.std()



# 4. Create a Boolean mask identifying the positions of all detected outliers.

outlier_mask = abs(transactions-mean) > 2*std
print("The Boolean mask is :")
print(outlier_mask)

# output => The Boolean mask is :
# [[False False False False False False]
#  [False False False False False False]
#  [ True False False False False False]
#  [False False False False False False]
#  [False False False False False False]
#  [False False False False False False]
#  [False False False False False False]
#  [False False False False False False]
#  [False False False False False False]
#  [False False False False False False]
#  [False False False False False False]
#  [False False False  True False False]]



# 5. Extract all outlier values from the dataset.

outlier_mask = abs(transactions-mean) > 2*std
print("The all outlier values from the dataset are :")
print(transactions[outlier_mask])

# output => The all outlier values from the dataset are :
# [500 500]



# 6. Calculate the mean of all non-outlier values.

mean_of_non_outlier = transactions[~outlier_mask ].mean() # outlier_mask == False  == ~outlier_mask
print("The mean of all non-outlier values is :")
print(mean_of_non_outlier)

# output => The mean of all non-outlier values is :
# 126.18571428571428



# 7. Replace every outlier with the mean of the non-outlier values.
# 8. Store the cleaned dataset in a new array named `cleaned_transactions`.
cleaned_transactions = np.where(outlier_mask, mean_of_non_outlier,transactions)
print("The array after Replace every outlier with the mean of the non-outlier values is :")
print(cleaned_transactions)

# output => The array after Replace every outlier with the mean of the non-outlier values is :
# [[120.         135.         150.         142.         128.
#   131.        ]
#  [110.         115.         108.         120.         117.
#   113.        ]
#  [126.18571429 130.         125.         140.         135.
#   128.        ]
#  [145.         152.         149.         155.         148.
#   151.        ]
#  [ 90.          95.          88.          92.          87.
#    91.        ]
#  [160.         158.         162.         165.         159.
#   161.        ]
#  [130.         128.         135.         132.         129.
#   131.        ]
#  [140.         145.         142.         138.         141.
#   143.        ]
#  [ 75.          80.          72.          78.          76.
#    74.        ]
#  [155.         150.         148.         152.         149.
#   151.        ]
#  [100.         105.          98.         102.          97.
#   101.        ]
#  [135.         132.         138.         126.18571429 140.
#   136.        ]]



# 9. Recalculate the average transaction value for each day after cleaning.

print("The average transaction value for each day after cleaning is :")
print(cleaned_transactions.mean(axis=1))

# output => The average transaction value for each day after cleaning is :
# [134.33333333 113.83333333 130.69761905 150.          90.5
#  160.83333333 130.83333333 141.5         75.83333333 150.83333333
#  100.5        134.53095238]



# 10. Compare the daily averages before and after cleaning.

print("The compare between daily averages before and after cleaning is :")
print(f"The daily averages before cleaning : {transactions.mean(axis=1)}")
print(f"The daily averages after cleaning : {cleaned_transactions.mean(axis=1)}")

# output => The diffrence between daily averages before and after cleaning is :
# The daily averages before cleaning : [134.33333333 113.83333333 193.         150.          90.5
#  160.83333333 130.83333333 141.5         75.83333333 150.83333333
#  100.5        196.83333333]
# The daily averages after cleaning : [134.33333333 113.83333333 130.69761905 150.          90.5
#  160.83333333 130.83333333 141.5         75.83333333 150.83333333
#  100.5        134.53095238]



# 11. Identify the day with the largest decrease in its average transaction value.

print("The day with the largest decrease in its average transaction value :")
print(np.argmax(transactions.mean(axis=1)-cleaned_transactions.mean(axis=1)) + 1)


# output => 3



# 12. Calculate the percentage change in the average of each day using:

# `percentage_change = ((old_average - new_average) / old_average) * 100`

print("The percentage change in the average of each day using: :")
print(((transactions.mean(axis=1)-cleaned_transactions.mean(axis=1))/transactions.mean(axis=1))*100)


# output => [ 0.          0.         32.2810264   0.          0.          0.
#   0.          0.          0.          0.          0.         31.65235273]



# 13. Create the final cleaned array without using loops:

#  Outliers must be replaced with their cleaned values.
#  Non-outlier values must remain unchanged.
#  The final array must have the same shape as the original dataset.

print("The final cleaned array is:")
print(cleaned_transactions)


# output => The final cleaned array is:
# [[120.         135.         150.         142.         128.
#   131.        ]
#  [110.         115.         108.         120.         117.
#   113.        ]
#  [126.18571429 130.         125.         140.         135.
#   128.        ]
#  [145.         152.         149.         155.         148.
#   151.        ]
#  [ 90.          95.          88.          92.          87.
#    91.        ]
#  [160.         158.         162.         165.         159.
#   161.        ]
#  [130.         128.         135.         132.         129.
#   131.        ]
#  [140.         145.         142.         138.         141.
#   143.        ]
#  [ 75.          80.          72.          78.          76.
#    74.        ]
#  [155.         150.         148.         152.         149.
#   151.        ]
#  [100.         105.          98.         102.          97.
#   101.        ]
#  [135.         132.         138.         126.18571429 140.
#   136.        ]]



