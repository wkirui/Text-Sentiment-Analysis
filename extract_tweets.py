# Objective: use twitter api to extract tweets

# import modules
import tweepy
from tweepy import OAuthHandler
import pandas as pd
import numpy as np
import jsonpickle
import json
import time

# get access keys from settings file
from settings import consumer_key,consumer_secret,access_token,access_secret


# print(consumer_key,consumer_secret)
# authorize access
oath = OAuthHandler(consumer_key, consumer_secret)
oath.set_access_token(access_token, access_secret)

# create an api
# enable wait when rate limit is reached
twitter_api = tweepy.API(oath, wait_on_rate_limit=True,
                         wait_on_rate_limit_notify=True)

print("Authorization successful!")

# search twitter
# define file to save tweets
filename = "tweets.txt"

# create list of top banks
banks_list = ["KCB Bank", "Equity Bank", "Cooperative Bank", "Family Bank", "Faulu Bank",
              "DTB Bank", "Barclays Bank", "Standard Chartered Bank", "National Bank", "NCBA Bank"]


# define start date
start_date = "2020-01-01"

# counter for search results
total_results = 0

# extract data for the selected banks
def search_and_extract_data_from_bank_tweets(search_list):
    """
    Takes a list of banks to search as argument
    """
    # create counter for total downloads
    total_results = 0

    # open a file to write data
    with open(filename, 'w') as f:

        # search tweets for banks in the list
        # add the results to a json object
        for i in search_list:
            print("Searching twitter for",i)
            for tweet in tweepy.Cursor(twitter_api.search, q=i,
                                        since=start_date,
                                        monitor_rate_limit = True,
                                        wait_on_rate_limit = True,
                                        retry_count = 5,
                                        retry_delay = 5,
                                       geocode = "-1.285796,36.825658,2000km").items():
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) +
                        '\n')
                total_results += 1

        print("Total Tweets downloaded:", total_results)

        f.close()


# apply function on banks list
search_and_extract_data_from_bank_tweets(banks_list)
