#LOAD DATA FROM FILE
import numpy as np

filedata = np.genfromtxt('data.txt', delimiter=',')
filedata = filedata.astype('int32')
print(filedata)