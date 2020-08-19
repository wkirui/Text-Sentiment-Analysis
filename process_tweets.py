# load downloaded data from text file
# convert file into a dataframe
# perform text analysis

# import modules
import numpy as np
import pandas as pd
import json

# load data

json_data = []

filename = 'tweets.txt'

with open(filename,'r') as f:
    for line in f:
        json_data.append(json.loads(line))
        
    f.close()

# convert json file to dataframe
bank_comments_df = pd.DataFrame(json_data)
print(bank_comments_df.info())

#
