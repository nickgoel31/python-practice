#READING DATA IN PANDAS
import pandas as pd

# Read a dataset from a CSV file
df = pd.read_csv('pandas/data.csv')

#Read headers
print(df.columns)

#READ EACH COLUMN (ONLY 5 Values)
print(df[['Name']][:5])

