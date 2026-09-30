# NumPy Exercises
# Q1 : Import NumPy as np
import numpy as np



# Q2 : Create an array of 10 zeros 
arr1 = np.zeros(10)
print(arr1) # => [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]



# Q3 : Create an array of 10 ones
arr2 = np.ones(10)
print(arr2) # => [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]



# Q4 : Create an array of 10 fives
arr3 = np.linspace(5,5,10) 
#OR 
arr3 = np.ones(10) * 5
print(arr3) # => [5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]



# Q4 : Create an array of 10 fives
arr3 = np.linspace(5,5,10)
print(arr3) # => [5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]



# Q5 : Create an array of the integers from 10 to 50
arr4 = np.arange(10,51)
print(arr4) # => [10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 
# 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50]



# Q6 : Create an array of all the even integers from 10 to 50
arr5 = np.arange(10,51)
arr5 = arr5[arr5%2 == 0]
print(arr5) # => [10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50]



# Q7 :  Create a 3x3 matrix with values ranging from 0 to 8
arr6 = np.arange(0,9)
arr6 = arr6.reshape(3,3)
print(arr6) # => 



# Q8 :  Create a 3x3 identity matrix
arr7 = np.eye(3)
print(arr7) # => 
# [[1. 0. 0.]
# [0. 1. 0.]
# [0. 0. 1.]]



# Q9 : Use NumPy to generate a random number between 0 and 1
arr8 = np.random.rand(1)
print(arr8) # => Any array with 1 number < 1 like => [0.7203206]



# Q10 : Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
arr9 = np.random.randn(25)
print(arr9) # =>  Any 25 random numbers from a standard normal distribution like



# Q11 : Create the following matrix:
# [[ 0.01,  0.02,  0.03,  0.04,  0.05,  0.06,  0.07,  0.08,  0.09,  0.1 ],
# [ 0.11,  0.12,  0.13,  0.14,  0.15,  0.16,  0.17,  0.18,  0.19,  0.2 ],
# [ 0.21,  0.22,  0.23,  0.24,  0.25,  0.26,  0.27,  0.28,  0.29,  0.3 ],
# [ 0.31,  0.32,  0.33,  0.34,  0.35,  0.36,  0.37,  0.38,  0.39,  0.4 ],
# [ 0.41,  0.42,  0.43,  0.44,  0.45,  0.46,  0.47,  0.48,  0.49,  0.5 ],
# [ 0.51,  0.52,  0.53,  0.54,  0.55,  0.56,  0.57,  0.58,  0.59,  0.6 ],
# [ 0.61,  0.62,  0.63,  0.64,  0.65,  0.66,  0.67,  0.68,  0.69,  0.7 ],
# [ 0.71,  0.72,  0.73,  0.74,  0.75,  0.76,  0.77,  0.78,  0.79,  0.8 ],
# [ 0.81,  0.82,  0.83,  0.84,  0.85,  0.86,  0.87,  0.88,  0.89,  0.9 ],
# [ 0.91,  0.92,  0.93,  0.94,  0.95,  0.96,  0.97,  0.98,  0.99,  1.  ]]

arr10 = np.arange(1,101).reshape(10,10)
arr10 = arr10/100
print(arr10)



# Q12 : Create an array of 20 linearly spaced points between 0 and 1
arr11 = np.linspace(0,1,20)
print(arr11) # => [0.         0.05263158 0.10526316 0.15789474 0.21052632 0.26315789
#  0.31578947 0.36842105 0.42105263 0.47368421 0.52631579 0.57894737
#  0.63157895 0.68421053 0.73684211 0.78947368 0.84210526 0.89473684
#  0.94736842 1.        ]



# Q13 :Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:
mat = np.arange(1,26).reshape(5,5)

# 1=> give this output 
# [[12, 13, 14, 15],
# [17, 18, 19, 20],
# [22, 23, 24, 25]]
print(mat[2:,1:])

# 2=> give this output 20
print(mat[3,-1])

# 3=> give this output
#[[ 2],
# [ 7],
# [12]]
print(mat[:3,1:2])

# 4=> give this output array([21, 22, 23, 24, 25])
print(mat[-1])

# 5=> give this output 
# [[16, 17, 18, 19, 20],
#[21, 22, 23, 24, 25]]
print(mat[3:])

# 6=>  Get the sum of all the values in mat
print(mat.sum()) #=> 325

# 7=> Get the standard deviation of the values in mat
print(mat.std()) # => 7.211102550927978

# 8=> Get the sum of all the columns in mat
print(mat.sum(axis=0)) 


