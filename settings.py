# create environment settings
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

# get access keys
# keys are stored in a '.env' file
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_secret = os.getenv('ACCESS_SECRET')

# get email credential
mail_username = os.getenv('MAIL_USERNAME')
mail_password = os.getenv('MAIL_PASSWORD')
mail_recipient = os.getenv('MAIL_RECIPIENT')
mail_sender = os.getenv('MAIL_SENDER')