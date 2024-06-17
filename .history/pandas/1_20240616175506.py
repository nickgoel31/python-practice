#INTRODUCTION TO PANDAS

import pandas as pd
import IPython

# Create a simple dataset of people
data = {'Name': ["John", "Anna", "Peter", "Linda"], 
        'Location' : ["New York", "Paris", "Berlin", "London"],
        'Age' : [24, 13, 53, 33]
       }

data_pandas = pd.DataFrame(data)

display(data_pandas)