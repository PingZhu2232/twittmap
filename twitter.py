import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import oauth2
import json


ckey = 
csecret = 
atoken = 
asecret = 

tweets = []
# file name that you want to open is the second argument
save_file = open('Twitter.json', 'a')

        
class listener (StreamListener):
    
    def __init__(self):
        self.num_tweets = 0
        
        self.save_file = tweets
    
    def on_data(self, data):
        print(data)
        
#        self.save_file.append(json.loads(data))
#        save_file.write(str(data))
        tweets.append(json.loads(data))

        self.num_tweets += 1
        if self.num_tweets < 100:
            return True
        else:
            return False
        
    def on_error(self, status):
        print(status)
        
save_file.write(str(tweets))

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitts = twitterStream.filter(track=["a",'the',"for","Python", "to", "in","cloud"])

