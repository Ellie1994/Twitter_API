from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

################################################
import re

REPLACE_NO_SPACE = re.compile("(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])")
REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")
################################################
# there may be problems with ascii char in python 2
# The ascii() function is only available in Python 3
# Use the repr() function, which does exactly what ascii() does in Python 3

import string # get rid of non ascii char

c_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
c_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

a_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
a_s_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# you can use if __name__ == "__main__" for importing your tokens and keys
# more info about the __name__ attribute here --> https://thepythonguru.com/what-is-if-__name__-__main__/

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)

        tweet = all_data["text"]
        tweet = ascii(all_data["text"])
        tweet.encode("ascii", errors="ignore").decode()
        
        printable = set(string.printable)
        filter(lambda x: x in printable, tweet)

        print((tweet))

        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(c_key, c_secret)
auth.set_access_token(a_token, a_s_token)

twitter_stream = Stream(auth, listener())
twitter_stream.filter(track=["Tesla"]) # the tracking word or alternatively -->
# --> import sys
# --> twitter_stream.filter(track=sys.argv[1]) # for typing in a terminal 

# use ctrl + s to stop and ctrl + q to continue
