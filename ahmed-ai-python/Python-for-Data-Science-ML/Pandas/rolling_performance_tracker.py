# Rolling Performance Indicator
# Problem Name:
# Rolling Performance Tracker
# Description:
# Given a time-series:
# Compute rolling 3-period average.
# Detect anomalies where value > 2× rolling mean.
# Return anomaly indices.

import numpy as np
import pandas as pd
def rolling_performance_tracker(s):
    """
    Compute rolling 3-period average then Detect anomalies 
    where value > 2×rolling mean then Return anomaly indices.
    """
    # Checking if its Sreia or not
    if not isinstance(s,pd.Series) :
        s = pd.Series(s)
    # Compute rolling 3-period average.
    d =s.rolling(window=3).mean()
    # Compare original values with 2*rolling mean then return the indices
    return s[s > 2 * d].index

# Generate 50 random integers between 10 and 50

np.random.seed(42)

times = np.random.randint(10,100000,1000)
ind = np.arange(1,1001)

s = pd.Series(times , index = ind)


if __name__ == "__main__" :
    print("Time-Series Data before rolling analysis:")
    print(s)

    print("\nAnomaly Indices (where value > 2× rolling mean):")
    print(rolling_performance_tracker(s).to_list())

    
# output => 
# Time-Series Data before rolling analysis:
# 1       15805
# 2         870
# 3       76830
# 4       54896
# 5        6275
#         ...  
# 996     81459
# 997     60014
# 998     62991
# 999     84669
# 1000    54563
# Length: 1000, dtype: int32

# Anomaly Indices (where value > 2× rolling mean):
# [3, 31, 43, 48, 78, 116, 121, 191, 257, 268, 295, 306, 335, 349, 368, 376, 406, 441, 468, 483, 487, 
#  558,572, 579, 633, 642, 647, 663, 684, 702, 744, 749, 793, 796, 805, 820, 838, 894, 925, 951, 961, 984, 989]     

