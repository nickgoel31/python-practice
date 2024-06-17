#ACCESSING/CHANGING SPECIFIC ELEMENTS, ROWS, COLUMNS, ETC.
import numpy as np

# # Creating a 1D numpy array
a = np.array([[1, 2, 3, 4, 5], [4,5,43,56,7]])
print(a)

#GET A SPECIFIC ELEMENT [row,col]
print(a[1][2])

#Fet a specific row
print(a[0, :])

#Get a specific column
print(a[:, 2])

#[startindex:endindex:stepsize]
print(a[0,1:])