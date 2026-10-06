# Custom Data Profiling Report
# Problem Name:
# Mini Data Profiling System
# Description:
# Create a function that:
# Takes a DataFrame.
# For each column:
# Detects if numeric or categorical.
# If numeric → print mean, std, min, max.
# If categorical → print number of unique values and top 3 frequent values.
# Output structured summary as a new DataFrame.

import numpy as np
import pandas as pd

def mini_data_profiling_system(df):
    """
    Creates a structured profiling report for a DataFrame.
    """
    x = 0
    lis = []
    if not isinstance(df, pd.DataFrame):
        df = pd.DataFrame(df)

    for x in df.columns :
        if pd.api.types.is_numeric_dtype(df[x]):
            lis.append({
                "Column": x, 
                "Type": "Numeric", 
                "Mean": df[x].mean(), 
                "Std": df[x].std(), 
                "Min": df[x].min(), 
                "Max": df[x].max()
            })
        else:
            lis.append({ 
                "Column": x, 
                "Type": "Categorical", 
                "Unique Values": df[x].nunique(), 
                "Top 3 Frequent": df[x].value_counts().head(3).to_dict() 
                })
    return pd.DataFrame(lis)

np.random.seed(20)

d = {
    'name' : np.random.choice(['Ahmed','Mohammed','Adham','Yasser','Hazem','Omar'],25),
    'age' :  np.random.randint(18,22,25),
    'department' : np.random.choice(['IT','CS','AI','IS'],25),
    'GPA' : np.random.uniform(2,4,25)
}


if __name__ == "__main__":
    print("Dataset before profiling:")
    print(pd.DataFrame(d))

    print("\nDataset Profiling Summary after calculations:")
    test = mini_data_profiling_system(d)
    print(test)


# output =>
# Dataset before profiling:
#         name  age department       GPA
# 0     Yasser   20         IS  2.789686
# 1      Adham   19         AI  2.515949
# 2      Hazem   21         IS  3.164482
# 3      Adham   20         IS  2.323257
# 4   Mohammed   21         IS  3.196268
# 5      Hazem   19         AI  3.651647
# 6     Yasser   19         CS  2.312783
# 7      Adham   21         CS  3.468601
# 8      Ahmed   19         AI  2.817287
# 9      Ahmed   20         IS  3.557376
# 10      Omar   20         AI  3.607941
# 11     Adham   18         IT  3.572143
# 12     Adham   20         AI  3.184574
# 13    Yasser   21         CS  3.328978
# 14    Yasser   20         CS  3.293135
# 15     Ahmed   21         AI  2.851273
# 16      Omar   20         AI  3.027137
# 17     Ahmed   21         AI  3.002516
# 18  Mohammed   19         IS  2.074168
# 19      Omar   19         AI  3.416232
# 20      Omar   19         AI  3.240861
# 21     Adham   18         CS  3.555617
# 22     Adham   21         IT  2.918819
# 23      Omar   18         AI  2.759611
# 24    Yasser   20         AI  2.583784

# Dataset Profiling Summary after calculations:
#        Column         Type  Unique Values  ...       Std        Min        Max
# 0        name  Categorical            6.0  ...       NaN        NaN        NaN
# 1         age      Numeric            NaN  ...  1.011599  18.000000  21.000000
# 2  department  Categorical            4.0  ...       NaN        NaN        NaN
# 3         GPA      Numeric            NaN  ...  0.446582   2.074168   3.651647

# [4 rows x 8 columns]

