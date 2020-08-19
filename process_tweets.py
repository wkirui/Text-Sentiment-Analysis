# load downloaded data from text file
# convert file into a dataframe
# perform text analysis

# import modules
import numpy as np
import pandas as pd
import json
import spacy # for tokenizing tweets
from spacy.lang.en import English
import re
from string import punctuation
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

# tokenize tweets

# filter dataframe
bank_names = bank_comments_df['bank_name'].unique()

# get stop words
stop_words = spacy.lang.en.stop_words.STOP_WORDS
spacy_nlp = English()

# create usernames & links patterns
username_pattern = re.compile('^@[A-Za-z0-9_]{1,15}$')
url_pattern = re.compile(r'^https?:\/\/.*[\r\n]*')

# add some words to punctuation list
punctuation = punctuation + '\n'+'…'+'\n\n'+'rt'+'RT'+' '+'..'+'...'

#  create function to tokenize tweets for each bank
def filter_and_tokenize_tweets_by_bank(bank_names_list):
    # create empty dataframe
    combined_bank_comments_df = pd.DataFrame()
    
    for bank in bank_names_list:
        filtered_df = bank_comments_df[bank_comments_df['bank_name']==bank]
        filtered_bank_comments = [x for x in filtered_df['text'].unique()]

        # create tokens dictionary
        results = []
        for i in filtered_bank_comments:
            sentence_token = spacy_nlp(i)
            token_result = []
            for token in sentence_token:

                # check if token is stop word
                if token.is_stop == False:
                    token_result.append(token)

            results.append(token_result)

        # clean results
        # remove usernames
        cleaned_comment_results = []
        for x in results:
            for i in x:
                if (username_pattern.match(i.text) or url_pattern.match(i.text)):  
                    pass
                else:
                    cleaned_comment_results.append(str.lower(i.text))
                    
        # create word frequency
        word_frequencies = {}
        for word in cleaned_comment_results:
            if word not in punctuation:
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word]+=1

        # create frequency dataframe
        # print(word_frequencies)
        word_freq_df = pd.DataFrame(word_frequencies.items(),columns = ['word','freq'])
        word_freq_df['bank_name'] = bank # add bank name column with bank as value
        word_freq_df = word_freq_df[['bank_name','word','freq']] # reorder columns
        word_freq_df = word_freq_df.sort_values(by='freq',ascending=False).reset_index(drop=True)
        # add results to main dataframe
        combined_bank_comments_df = pd.concat([combined_bank_comments_df,word_freq_df])
    
    # sort main dataframe by word frequency
    combined_bank_comments_df = combined_bank_comments_df.sort_values(by='freq',ascending=False)
    print(combined_bank_comments_df[combined_bank_comments_df['bank_name']!=""][0:20]) # show top words

# apply function on banks
filter_and_tokenize_tweets_by_bank(bank_names)