# Employee Salary Filter
# Problem Name:
# Department Salary Analysis
# Description:
# Given a DataFrame with:
# employee_id
# department
# salary
# Tasks:
# Calculate average salary per department.
# Return employees earning above their department average.     

import numpy as np
import pandas as pd

def department_salary_analysis(df) :
    """
    Calculate average salary per department
    and return employees earning above their department average.
    """
    # Checking if its DataFrame or not
    if not isinstance(df,pd.DataFrame) :
        df = pd.DataFrame(df)

    # Calculate department average salary for each employee
    df["dept_avg_salary"] = df.groupby("department")["salary"].transform("mean")

    # Filter employees earning above department average
    result = df[df["salary"] > df["dept_avg_salary"]]

    return result


np.random.seed(101)

d = {
    'employee_id' : np.arange(1,101),
    'department'  : np.random.choice(["Ai Engineer","Data Analaysis","Full-Stack",
    "Data Engineer","IT Consulat","Cyper Security"],100),
    'salary'      : np.random.randint(10000,50000,100)
}

df = pd.DataFrame(d)

if __name__ == "__main__":
    print("Employees Data before salary analysis:")
    print(df)

    print("\nEmployees earning above their department average:")
    print(department_salary_analysis(df))

# output =>
# 0             1   Data Engineer   38014
# 1             2  Data Analaysis   22228
# 2             3  Cyper Security   26279
# 3             4   Data Engineer   11699
# 4             5  Data Analaysis   46047
# ..          ...             ...     ...
# 95           96     Ai Engineer   43793
# 96           97   Data Engineer   13621
# 97           98     Ai Engineer   48947
# 98           99   Data Engineer   19331
# 99          100  Cyper Security   46709

# [100 rows x 3 columns]

# Employees earning above their department average:
#     employee_id      department  salary  dept_avg_salary
# 0             1   Data Engineer   38014     29728.458333
# 4             5  Data Analaysis   46047     33291.083333
# 6             7     Ai Engineer   49865     34943.200000
# 8             9     Ai Engineer   40339     34943.200000
# 9            10  Cyper Security   36158     33251.769231
# 10           11     IT Consulat   41228     27170.380952
# 12           13     Ai Engineer   40710     34943.200000
# 13           14  Cyper Security   39469     33251.769231
# 14           15     IT Consulat   37797     27170.380952
# 15           16  Cyper Security   47242     33251.769231
# 19           20      Full-Stack   35287     31118.733333
# 20           21     Ai Engineer   49451     34943.200000
# 21           22   Data Engineer   45121     29728.458333
# 23           24   Data Engineer   44435     29728.458333
# 29           30   Data Engineer   32449     29728.458333
# 30           31      Full-Stack   49316     31118.733333
# 35           36  Data Analaysis   38043     33291.083333
# 36           37     Ai Engineer   47677     34943.200000
# 38           39   Data Engineer   41742     29728.458333
# 40           41     IT Consulat   33177     27170.380952
# 41           42      Full-Stack   39821     31118.733333
# 42           43     IT Consulat   46404     27170.380952
# 43           44     Ai Engineer   49041     34943.200000
# 44           45  Data Analaysis   46943     33291.083333
# 47           48     IT Consulat   49731     27170.380952
# 51           52     IT Consulat   46874     27170.380952
# 52           53  Data Analaysis   34766     33291.083333
# 53           54     Ai Engineer   43783     34943.200000
# 54           55   Data Engineer   45962     29728.458333
# 57           58  Cyper Security   39335     33251.769231
# 58           59     Ai Engineer   38226     34943.200000
# 61           62   Data Engineer   40681     29728.458333
# 63           64   Data Engineer   39746     29728.458333
# 66           67     IT Consulat   44653     27170.380952
# 68           69   Data Engineer   32876     29728.458333
# 71           72      Full-Stack   34673     31118.733333
# 73           74  Cyper Security   42976     33251.769231
# 74           75  Data Analaysis   39405     33291.083333
# 76           77  Cyper Security   49487     33251.769231
# 77           78      Full-Stack   44280     31118.733333
# 79           80      Full-Stack   44214     31118.733333
# 80           81     IT Consulat   35389     27170.380952
# 81           82   Data Engineer   38007     29728.458333
# 83           84      Full-Stack   38835     31118.733333
# 86           87     IT Consulat   49368     27170.380952
# 88           89   Data Engineer   44161     29728.458333
# 90           91      Full-Stack   45478     31118.733333
# 92           93  Data Analaysis   40267     33291.083333
# 94           95  Cyper Security   39306     33251.769231
# 95           96     Ai Engineer   43793     34943.200000
# 97           98     Ai Engineer   48947     34943.200000
# 99          100  Cyper Security   46709     33251.769231