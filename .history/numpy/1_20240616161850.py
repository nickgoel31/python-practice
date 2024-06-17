#INTRODUCTION TO NUMPY
import numpy as np

# # Creating a 1D numpy array
# a = np.array([1, 2, 3, 4, 5])
# print(a)

# # Creating a 2D numpy array
b = np.array([[1, 2, 3], [4, 5, 6]], dtype='int16')
print(b)



# Creating a numpy array with a range of values
g = np.arange(0, 10, 2)
print(g)

# GETTING DIMENSIONS
print(g.ndim)
print("b: ", b.ndim)
# GETTING THE SHAPE OF MATRIX
print(g.shape)
print(b.dtype)
print(b.itemsize)
print(b.size)