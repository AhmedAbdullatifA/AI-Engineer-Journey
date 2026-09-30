# This project demonstrates how to perform feature standardization
# on a dataset using NumPy only, without using any explicit loops.

# Each column represents a feature and is normalized using the
# standard score (z-score) formula:

#     X_norm = (X - mean) / std

# The implementation relies on NumPy vectorization and broadcasting
# for efficient computation, which is a common preprocessing step
# in machine learning pipelines.

import numpy as np

def normalize_dataset(data):
    """
    Standardizes each feature (column) in the dataset using z-score normalization.
    """
    mean = data.mean(axis=0)
    std = data.std(axis=0)

    safe = np.where(std == 0, 1, std)
    
    normalized = (data - mean) / safe
    
    return normalized

data = np.array([
    [10, 200],
    [20, 300],
    [30, 400]
])
print(normalize_dataset(data)) 
# => output 
# [[-1.22474487 -1.22474487]
#  [ 0.          0.        ]
#  [ 1.22474487  1.22474487]]