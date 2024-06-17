#MATHEMATICS IN NUMPY
import numpy as np

a = np.array([1, 2, 3, 4])
# print(a)

# print(a+2)
# print(a-2)
# print(a*2)
# print(a/2)

b = np.array([1,0,1,0])

# print(a+b)

# print(a**2)

# #Take the sin
# print(np.sin(a))

# #Take the cosine
# print(np.cos(a))

# print(np.tan(a))


#LINEAR ALGEBRA
a = np.ones((2,3))
b= np.full((3,2), 2)

print(a)
print(b)

#Matrix multiplication
print(np.matmul(a,b))

#Find the determinant
c = np.identity(3)
print(np.linalg.det(c))



