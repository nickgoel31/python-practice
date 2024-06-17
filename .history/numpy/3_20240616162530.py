
#INITIALIZING DIFFERENT TYPES OF ARRAYS

import numpy as np

# # Creating a 3D numpy array
# c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(c)

# # Creating a numpy array with zeros
# d = np.zeros((2, 3))
# print(d)

# # Creating a numpy array with ones
# e = np.ones((2, 3), dtype='int32')
# print(e)

# #ANY OTHER NUMBER
# f = np.full((2, 2), 99)
# print(f)

# # Creating a numpy array with random values
# f = np.random.random((2, 3))
# print(f)

# # Creating a numpy array with random values
# g = np.random.rand(4, 2)

# # Creating a numpy array with random values
# h = np.random.randint(4,7, size=(3, 3))

# # Creating a numpy array with random values
# i = np.identity(5)
# print(i)

# # Repeat an array
# arr = np.array([[1, 2, 3]])
# r1 = np.repeat(arr, 3, axis=0)

#EXERCISE
'''
1 1 1 1 1
1 0 0 0 1
1 0 9 0 1
1 0 0 0 1
1 1 1 1 1
'''

a = np.ones((5,5))
print(a)
z = np.zeros((3,3))

#COPYING AN ARRAY