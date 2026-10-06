# Missing Data Impact Analyzer
# Problem Name:
# Missing Data Sensitivity Test
# Description:
# do two strategies.
# First :
# Drop rows with missing values → calculate mean.
# Fill missing values → calculate mean.
# Compare difference between both strategies.
# Second :
# Drop rows with missing values → calculate Standard Deviation.
# Fill missing values → calculate Standard Deviation.
# Compare difference between both strategies.

import numpy as np
import pandas as pd


def missing_data_impact_analyzer_mean(df):
    """
    Compare mean values after:
    1- Dropping missing rows
    2- Filling missing values with mean (numeric)
    Returns a dictionary with both means and difference
    """

    # create dictionary to store the values

    result = {}

    # Checking if its DataFrame or not
    if not isinstance(df, pd.DataFrame) :
        df = pd.DataFrame(df)

    # lopping on coulmns to know the type of column
    for a in df.columns :

        # Checking the if the type is numeric or not 
        if pd.api.types.is_numeric_dtype(df[a]) :

            # drop the Nan value then calculate the mean
            drop_nan_mean = df[a].dropna().mean()

            # substiute the Nan with mean value then calculate the mean
            fill_nan_mean = df[a].fillna(df[a].mean()).mean()

            result[a] = {
                "drop_nan_mean": drop_nan_mean,
                "fill_nan_mean": fill_nan_mean,
                "difference": fill_nan_mean - drop_nan_mean
            }

    return pd.DataFrame(result)


def missing_data_impact_analyzer_std(df):
    """
    Compare Standard Deviation values after:
    1- Dropping missing rows
    2- Filling missing values with Standard Deviation (numeric)
    Returns a dictionary with both Standard Deviation and difference
    """

    # create dictionary to store the values

    result = {}

    # Checking if its DataFrame or not
    if not isinstance(df, pd.DataFrame) :
        df = pd.DataFrame(df)

    # lopping on coulmns to know the type of column
    for a in df.columns :

        # Checking the if the type is numeric or not 
        if pd.api.types.is_numeric_dtype(df[a]) :

            # drop the Nan value then calculate the Standard Deviation
            drop_nan_std = df[a].dropna().std()

            # substiute the Nan with mean value then calculate the Standard Deviation
            fill_nan_std = df[a].fillna(df[a].mean()).std()

            result[a] = {
                "drop_nan_std": drop_nan_std,
                "fill_nan_std": fill_nan_std,
                "difference": fill_nan_std - drop_nan_std
            }

    return pd.DataFrame(result)



# Create Data

d = {
    'Age': [25, 30, np.nan, 20, 35, 40,np.nan,np.nan,np.nan],# Numeric
    'Salary': [50000, np.nan,20000, 60000, 70000, 50000,np.nan,np.nan,10000] # Numeric
}

df = pd.DataFrame(d)


if __name__ == "__main__":
    print("Dataset before missing data analysis:")
    print(df)

    print("\nMean comparison after drop vs fill:")
    print(missing_data_impact_analyzer_mean(df))

    print("\nStandard Deviation comparison after drop vs fill:")
    print(missing_data_impact_analyzer_std(df))



# output =>    
# Dataset before missing data analysis:
#     Age   Salary
# 0  25.0  50000.0
# 1  30.0      NaN
# 2   NaN  20000.0
# 3  20.0  60000.0
# 4  35.0  70000.0
# 5  40.0  50000.0
# 6   NaN      NaN
# 7   NaN      NaN
# 8   NaN  10000.0

# Mean comparison after drop vs fill:
#                 Age        Salary
# drop_nan_mean  30.0  43333.333333
# fill_nan_mean  30.0  43333.333333
# difference      0.0      0.000000

# Standard Deviation comparison after drop vs fill:
#                    Age        Salary
# drop_nan_std  7.905694  23380.903889
# fill_nan_std  5.590170  18484.227511
# difference   -2.315524  -4896.676378

