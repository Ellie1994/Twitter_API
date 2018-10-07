# prints out the latest tweets from the timeline of the account bound to your Twitter API 
# sign in --> https://developer.twitter.com/ 

import tweepy
from tweepy import OAuthHandler
import json

consumer_key = 'xxxxxxxxxxxxxxxxxxxxxx' 
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(5):
    print(status.text)
