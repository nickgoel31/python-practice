#LOADING DATA INTO PANDAS

import pandas as pd

# Read a dataset from a CSV file
data = pd.read_csv('pandas/data.csv')

print(data.head(3))
print(data.tail(3))
