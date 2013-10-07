import twitter
import time

#app config...
CONSUMER_KEY = 'consumer_key_goes_here'
CONSUMER_SECRET = 'consumer_secret_goes_here'

ACCESS_TOKEN = 'user_access_token_goes_here'
ACCESS_SECRET = 'user_access_secret_goes_here'

"""Connect to twitter using the provided credentials"""
def connect():
    api = twitter.Api(consumer_key = CONSUMER_KEY, consumer_secret = CONSUMER_SECRET,
                      access_token_key = ACCESS_TOKEN, access_token_secret = ACCESS_SECRET)

    #print api.VerifyCredentials()
    return api

"""Upload 'text' as the tweet with the api object returned by connect"""
def upload_tweet(text, api):
    status = api.PostUpdate(text)
    print status


api = connect()

#read the tweets and upload them to twitter...
with open('tweets.txt') as f:
    tweets = f.readlines()
    
for tweet in tweets:
    status = upload_tweet(tweet, api)
    print status, "\n"
    #time.sleep(5)             #a little delay...
