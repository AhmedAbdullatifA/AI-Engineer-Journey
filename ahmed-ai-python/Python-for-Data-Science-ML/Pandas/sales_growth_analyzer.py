# Sales Growth Analyzer
# Problem Name:
# Monthly Sales Growth Calculator
# Description:
# Given a Pandas Series of monthly sales:
# Calculate month-over-month growth percentage.
# Identify the month with highest growth.
# Identify months with negative growth.

import pandas as pd
import numpy as np

def sales_growth_analyzer(s):
    """
    function Calculate month-over-month growth percentage and 
    Identify the month with highest growth.
    Identify months with negative growth.
    """
    if not isinstance(s, pd.Series):
        s = pd.Series(s)
    # pct_change() gives percentage change between rows.
    growth = s.pct_change() *100

    # determine the month with highest growth. 
    highest_growth = growth.idxmax()

    # determine months with negative growth.
    negative_growth = growth[growth < 0]

    return {
        "monthly_growth_percent": growth,
        "highest_growth_month": growth.idxmax(),
        "negative_growth_months": growth[growth < 0]
    }


np.random.seed(42) #  => reproducibility

# Create 12 months of random sales between 10k and 100k
months = np.arange(1,13)
sales = np.random.randint(10000, 100000,12)

# Put into a Series
sales_series = pd.Series(sales, index=months, name="Sales")
print(sales_series)

if __name__ == "__main__":
    print("Monthly Sales Data before growth analysis:")
    print(sales_series)

    print("\nSales Growth Analysis Results:")
    print(sales_growth_analyzer(sales_series))

# output =>
# 1     25795
# 2     10860
# 3     86820
# 4     64886
# 5     16265
# 6     92386
# 7     47194
# 8     97498
# 9     54131
# 10    70263
# 11    26023
# 12    51090
# Name: Sales, dtype: int32
# Monthly Sales Data before growth analysis:
# 1     25795
# 2     10860
# 3     86820
# 4     64886
# 5     16265
# 6     92386
# 7     47194
# 8     97498
# 9     54131
# 10    70263
# 11    26023
# 12    51090
# Name: Sales, dtype: int32

# Sales Growth Analysis Results:
# {'monthly_growth_percent': 1            NaN
# 2     -57.898818
# 3     699.447514
# 4     -25.263764
# 5     -74.932959
# 6     468.004919
# 7     -48.916503
# 8     106.589821
# 9     -44.479887
# 10     29.801777
# 11    -62.963437
# 12     96.326327
# Name: Sales, dtype: float64, 'highest_growth_month': np.int64(3), 'negative_growth_months': 2    -57.898818
# 4    -25.263764
# 5    -74.932959
# 7    -48.916503
# 9    -44.479887
# 11   -62.963437
# Name: Sales, dtype: float64}