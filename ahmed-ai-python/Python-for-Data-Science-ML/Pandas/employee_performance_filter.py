# Multi-Condition Data Filtering
# Problem Name:
# Advanced Employee Performance Filter
# Description:
# Filter employees who:
# Salary > company average
# Work in departments with more than 5 employees
# Have performance score in top 25%
# Return final filtered DataFram

import numpy as np
import pandas as pd

def employee_performance_filter(df):
    """
    Filter employees who: Salary > company average and Work in departments 
    with more than 5 employees and Have performance score in top 25%
    """
    # Checking if its DataFrame or not
    if not isinstance(df,pd.DataFrame):
        df = pd.DataFrame(df)

    # Create column where Salary > company average
    df['company_average'] = df['salary'].mean()

    # Create column to count departments with more than 5 employees
    df['counting_department'] = df.groupby('department')['department'].transform("count")

    # return the result with the condition
    return df[(df['salary'] > df['company_average'])  
              & (df ['counting_department'] > 5)  
              & (df['performance_score'] > df['performance_score'].quantile(0.75)) ]


# to make the random data constant
np.random.seed(101)


# Create Random Data
d = {
    'employee_id' : np.arange(1,51),
    'department'  : np.random.choice(["Ai Engineer","Data Analaysis","Full-Stack",
    "Data Engineer","IT Consulat","Cyper Security"],50),
    'salary'      : np.random.randint(10000,50000,50),
    'performance_score' : np.random.randint(1,10,50)
}

df = pd.DataFrame(d)


if __name__ == "__main__":
    print("Employees Data before performance filtering:")
    print(df)

    print("\nEmployees meeting all performance conditions:")
    print(employee_performance_filter(df))


# output =>
# Employees Data before performance filtering:
#     employee_id      department  salary  performance_score
# 0             1   Data Engineer   14458                  7
# 1             2  Data Analaysis   15260                  6
# 2             3  Cyper Security   19679                  6
# 3             4   Data Engineer   48753                  2
# 4             5  Data Analaysis   18157                  8
# 5             6  Cyper Security   23976                  5
# 6             7     Ai Engineer   13775                  8
# 7             8     IT Consulat   42019                  5
# 8             9     Ai Engineer   28930                  6
# 9            10  Cyper Security   16686                  2
# 10           11     IT Consulat   22787                  7
# 11           12     IT Consulat   36556                  3
# 12           13     Ai Engineer   23927                  7
# 13           14  Cyper Security   13848                  4
# 14           15     IT Consulat   28262                  9
# 15           16  Cyper Security   22119                  2
# 16           17     Ai Engineer   21950                  8
# 17           18  Data Analaysis   12998                  5
# 18           19   Data Engineer   45557                  2
# 19           20      Full-Stack   28093                  9
# 20           21     Ai Engineer   49004                  5
# 21           22   Data Engineer   10907                  1
# 22           23  Cyper Security   26778                  5
# 23           24   Data Engineer   46465                  3
# 24           25   Data Engineer   12467                  6
# 25           26      Full-Stack   39212                  9
# 26           27     IT Consulat   46867                  2
# 27           28     Ai Engineer   31331                  9
# 28           29  Data Analaysis   11327                  5
# 29           30   Data Engineer   21790                  7
# 30           31      Full-Stack   34508                  5
# 31           32     IT Consulat   40917                  4
# 32           33   Data Engineer   43400                  2
# 33           34     Ai Engineer   19139                  5
# 34           35  Data Analaysis   49174                  5
# 35           36  Data Analaysis   14056                  5
# 36           37     Ai Engineer   49141                  3
# 37           38     IT Consulat   38014                  4
# 38           39   Data Engineer   22228                  2
# 39           40   Data Engineer   26279                  8
# 40           41     IT Consulat   11699                  5
# 41           42      Full-Stack   46047                  1
# 42           43     IT Consulat   12274                  7
# 43           44     Ai Engineer   49865                  8
# 44           45  Data Analaysis   19677                  5
# 45           46     IT Consulat   40339                  1
# 46           47      Full-Stack   36158                  8
# 47           48     IT Consulat   41228                  3
# 48           49     Ai Engineer   12021                  8
# 49           50     IT Consulat   40710                  8

# Employees meeting all performance conditions:
#     employee_id   department  salary  performance_score  company_average  counting_department
# 27           28  Ai Engineer   31331                  9         28816.24                   10
# 43           44  Ai Engineer   49865                  8         28816.24                   10
# 49           50  IT Consulat   40710                  8         28816.24                   12                 12     