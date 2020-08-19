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

# clean up data
# add bank names column
bank_comments_df['bank_name'] = np.where(bank_comments_df['text'].str.contains('Equity Bank',case=False),"Equity Bank",'')
bank_comments_df['bank_name'] = np.where(bank_comments_df['text'].str.contains('KCB',case=False),"KCB Bank",bank_comments_df['bank_name'])
bank_comments_df['bank_name'] = np.where(bank_comments_df['text'].str.contains('Cooperative Bank',case=False),"Cooperative Bank",bank_comments_df['bank_name'])
bank_comments_df['bank_name'] = np.where(bank_comments_df['text'].str.contains('Family Bank',case=False),"Family Bank",bank_comments_df['bank_name'])
bank_comments_df['bank_name'] = np.where(bank_comments_df['text'].str.contains('Faulu Bank',case=False),"Faulu Bank",bank_comments_df['bank_name'])
bank_comments_df['bank_name'] = np.where(bank_comments_df['text'].str.contains('DTB Bank',case=False),"DTB Bank",bank_comments_df['bank_name'])
bank_comments_df['bank_name'] = np.where(bank_comments_df['text'].str.contains('Barclays Bank',case=False),"Barclays Bank",bank_comments_df['bank_name'])
bank_comments_df['bank_name'] = np.where(bank_comments_df['text'].str.contains('Standard Chartered Bank',case=False),"Standard Chartered",bank_comments_df['bank_name'])
bank_comments_df['bank_name'] = np.where(bank_comments_df['text'].str.contains('NCBA Bank',case=False),"NCBA Bank",bank_comments_df['bank_name'])
bank_comments_df['bank_name'] = np.where(bank_comments_df['text'].str.contains('National Bank',case=False),"National Bank",bank_comments_df['bank_name'])

# generate summary
bank_tweets_summary = bank_comments_df.groupby('bank_name')['id'].count().rename('total_tweets').reset_index()
print(bank_tweets_summary)