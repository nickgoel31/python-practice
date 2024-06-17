#READING DATA IN PANDAS
import pandas as pd

# Read a dataset from a CSV file
df = pd.read_csv('pandas/data.csv')

# #Read headers
# print(df.columns)

# #READ EACH COLUMN (ONLY 5 Values)
# print(df[['Name', 'Age']][:5])

# #READ EACH ROW
# print(df.iloc[0])

#INTERATE THRU ROWS
for index,row in df.iterrows():
    print(index,row)

#READ A SPECIFIC LOCATION (R,C)
print(df.iloc[2,1])


