# the code analyses the degree of how positive or negativ the given tweet with an input-word is.

import tweepy
from textblob import TextBlob
# TextBlob is a Natural Language Processing library

# you can use if __name__ == "__main__" for importing your tokens and keys
# more info about the __name__ attribute here --> https://thepythonguru.com/what-is-if-__name__-__main__/

consumer_key = 	"xxxxxxxxxxxxxxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

access_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_token_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("Trump")

# The sentiment property returns a tuple of the form Sentiment (polarity, subjectivity). 
# The polarity score is a float within the range [-1.0, 1.0]. 
# The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
