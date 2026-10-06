# Dataset Summary Analyzer
# Problem Name:
# Dataset Quick Summary Tool
# Description:
# Create a Pandas script that:
# Loads a CSV file.
# Prints:
# Number of rows and columns
# Data types of each column
# Number of missing values per column
# Basic statistics for numerical columns

import pandas as pd
import numpy as np

def quick_summary(file):
    """
    Docstring for quick_summary
    
    : function descripe and get information about the file 
    """
    df = pd.read_csv(file)

    print(" Dataset Summary")

    print(f"Number of rows is : {df.shape[0]} and columns is  :{df.shape[1]}")

    print(f"Data types of each column are : \n{df.dtypes}")   

    print(f"Number of missing values per column is :  \n{df.isnull().sum()}")

    print(f"Basic statistics for numerical columns is : \n{df.describe()}")


# Data to write

np.random.seed(20)

df = {
    "customer_id": np.arange(1, 51),
    "region": np.random.choice(["Cairo","Giza","Alex","Helwan","Maddi"],50),
    "amount": np.random.randint(1000, 10000, 50)
}

df = pd.DataFrame(df)

# Writing to CSV
df.to_csv("customers.csv", index=False)

if __name__ == "__main__" :
    print("Customers Data before writing to CSV:")
    print(df)

    print("\nDataset Summary after calculations:")
    quick_summary("customers.csv")


# output =>
# Customers Data before writing to CSV:
#     customer_id  region  amount
# 0             1  Helwan    9011
# 1             2    Alex    1264
# 2             3   Maddi    1262
# 3             4    Alex    9730
# 4             5    Giza    5946
# 5             6   Maddi    4150
# 6             7  Helwan    3465
# 7             8    Alex    1725
# 8             9   Cairo    8794
# 9            10   Cairo    7952
# 10           11    Alex    6930
# 11           12    Alex    4900
# 12           13  Helwan    1980
# 13           14  Helwan    4195
# 14           15   Cairo    1158
# 15           16   Cairo    8972
# 16           17    Giza    2672
# 17           18    Alex    7320
# 18           19    Alex    1816
# 19           20  Helwan    8933
# 20           21    Alex    5873
# 21           22    Giza    7332
# 22           23  Helwan    3711
# 23           24    Alex    3612
# 24           25  Helwan    4918
# 25           26  Helwan    8135
# 26           27    Giza    8734
# 27           28   Cairo    2225
# 28           29    Alex    4558
# 29           30  Helwan    4306
# 30           31  Helwan    5311
# 31           32    Alex    1777
# 32           33  Helwan    8950
# 33           34    Giza    3872
# 34           35   Cairo    3490
# 35           36  Helwan    2359
# 36           37   Cairo    6810
# 37           38    Alex    7782
# 38           39    Alex    7380
# 39           40  Helwan    6701
# 40           41  Helwan    9066
# 41           42   Cairo    3711
# 42           43    Alex    6221
# 43           44    Giza    2781
# 44           45    Alex    6372
# 45           46  Helwan    7006
# 46           47    Alex    2269
# 47           48    Giza    9386
# 48           49   Maddi    1655
# 49           50   Maddi    8361

# Dataset Summary after calculations:
#  Dataset Summary
# Number of rows is : 50 and columns is  :3
# Data types of each column are : 
# customer_id     int64
# region         object
# amount          int64
# dtype: object
# Number of missing values per column is :  
# customer_id    0
# region         0
# amount         0
# dtype: int64
# Basic statistics for numerical columns is : 
#        customer_id       amount
# count     50.00000    50.000000
# mean      25.50000  5336.780000
# std       14.57738  2698.469031
# min        1.00000  1158.000000
# 25%       13.25000  2952.000000
# 50%       25.50000  5114.500000
# 75%       37.75000  7681.500000
# max       50.00000  9730.000000
