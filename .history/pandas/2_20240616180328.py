#LOADING DATA INTO PANDAS

import pandas as pd
from IPython.display import display

# Read a dataset from a CSV file
data = pd.read_csv('pandas/data.csv')

print(data.head(3))
