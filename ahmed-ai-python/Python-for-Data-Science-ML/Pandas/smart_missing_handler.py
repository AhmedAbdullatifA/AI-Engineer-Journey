# Smart Missing Handler
# Problem Name:
# Column-Based Missing Value Strategy
# Description:
# For numeric columns → fill with mean.
# For categorical columns → fill with most frequent value.
# Return cleaned DataFrame.

import numpy as np
import pandas as pd


def smart_missing_handler(df):
    """
    Cleans a DataFrame by filling numeric NaNs with the mean 
    and categorical NaNs with the mode.
    """
    # Checking if its DataFrame or not
    if not isinstance(df , pd.DataFrame) :
        df = pd.DataFrame(df)

    # lopping on coulmns to know the type of column
    for a in df.columns :

        # Checking the type if numeric or not
        if pd.api.types.is_numeric_dtype(df[a]) :

            # substiute the Nan with mean value
            df[a] = df[a].fillna(df[a].mean())

        else :   
            # Checking if there are mode or not , and make sure 
            # the mode is not Nan
            if not df[a].dropna().mode().empty:

                # Substitute the NaN with mode (most frequent value)
                df[a] = df[a].fillna(df[a].mode()[0])

    return df


# Create Data

d = {
    'Age': [25, 30, np.nan, 20, 35, 40,np.nan,np.nan,np.nan],# Numeric
    'City': ['NYC', 'LA','LA' ,np.nan,np.nan, 'NYC', np.nan, 'LA',np.nan], # Categorical
    'Salary': [50000, np.nan,20000, 60000, 70000, 50000,np.nan,np.nan,10000] # Numeric
}

df = pd.DataFrame(d)


if __name__ == "__main__":
    print("Dataset before handling missing values:")
    print(df)

    print("\nDataset after applying Smart Missing Handler:")
    print(smart_missing_handler(df))


# output =>    
# Dataset before handling missing values:
#     Age City   Salary
# 0  25.0  NYC  50000.0
# 1  30.0   LA      NaN
# 2   NaN   LA  20000.0
# 3  20.0  NaN  60000.0
# 4  35.0  NaN  70000.0
# 5  40.0  NYC  50000.0
# 6   NaN  NaN      NaN
# 7   NaN   LA      NaN
# 8   NaN  NaN  10000.0

# Dataset after applying Smart Missing Handler:
#     Age City        Salary
# 0  25.0  NYC  50000.000000
# 1  30.0   LA  43333.333333
# 2  30.0   LA  20000.000000
# 3  20.0   LA  60000.000000
# 4  35.0   LA  70000.000000
# 5  40.0  NYC  50000.000000
# 6  30.0   LA  43333.333333
# 7  30.0   LA  43333.333333
# 8  30.0   LA  10000.000000