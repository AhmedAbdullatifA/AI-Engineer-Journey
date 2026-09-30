# This project implements Min-Max feature scaling from scratch using NumPy only.

# Each column in the dataset represents a feature, and each row represents a data sample.
# The goal is to scale all features to a range between 0 and 1 using the Min-Max
# normalization formula:

#     X_scaled = (X - X_min) / (X_max - X_min)

# The implementation avoids explicit loops and relies entirely on NumPy vectorization
# and broadcasting for efficient computation.

# Special care is taken to handle edge cases where a feature has no variance
# (i.e., X_max == X_min). In such cases, the entire feature column is set to zero
# to prevent division by zero and ensure numerical stability.

# This preprocessing step is commonly used in machine learning pipelines and mirrors
# the behavior of standard libraries such as scikit-learn.

import numpy as np

def min_max_scale(data):

    """
    This project implements Min-Max feature scaling from scratch using NumPy only.
    """
    Min = data.min(axis = 0)
    Max = data.max(axis = 0)

    safe = np.where(Max - Min == 0, 1, Max - Min)

    scaled = (data - Min) / safe

    return scaled

data = np.array([
    [5, 10, 100],
    [5, 20, 200],
    [5, 30, 300]
])
print(min_max_scale(data))
# output 
# [[0.  0.  0. ]
#  [0.  0.5 0.5]
#  [0.  1.  1. ]]