#STATISTICS IN NUMPY
import numpy as np

stats = np.array([[1,2,3],[4,5,6]])
# print(stats)

# print(np.min(stats))
# print(np.max(stats))

print(np.min(stats, axis=2))

# print(np.sum(stats, axis=0))

