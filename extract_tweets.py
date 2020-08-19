# Objective: use twitter api to extract tweets

# Get Access tokens
# load_ext dotenv
# dotenv

# import modules
import os
import tweepy
from tweepy import OAuthHandler
import pandas as pd
import numpy as np
import jsonpickle
import time
# get access
# keys are stored in a '.env' file
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret= os.getenv('CONSUMER_SECRET')
access_token =  os.getenv('ACCESS_TOKEN')
access_secret =  os.getenv('ACCESS_SECRET')

# authorize access
oath = OAuthHandler(consumer_key,consumer_secret)
oath.set_access_token(access_token,access_secret)

# create an api
# enable wait when rate limit is reached
twitter_api = tweepy.API(oath,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
print("Executed successfully!")