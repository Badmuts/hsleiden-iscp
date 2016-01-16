from model.Tweet import Tweet
import tweepy
import os
import json

CONSUMER_KEY 		= os.environ['CONSUMER_KEY']
CONSUMER_SECRET 	= os.environ['CONSUMER_SECRET']
ACCESS_TOKEN 		= os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

if CONSUMER_KEY == "":
	print("ERROR: Please set your CONSUMER_KEY as env variable")

if CONSUMER_SECRET == "":
	print("ERROR: Please set your CONSUMER_SECRET as env variable")

if ACCESS_TOKEN == "":
	print("ERROR: Please set your ACCESS_TOKEN as env variable")

if ACCESS_TOKEN_SECRET == "":
	print("ERROR: Please set your ACCESS_TOKEN_SECRET as env variable")

class TweetController(object):

	def __init__(self):
		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
		self.api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

	def get_tweets(self):
		pub_tweets = self.api.home_timeline()
		f = open(os.path.dirname(__file__)  + "/../tweets.json", "w")
		f.write(json.dumps(pub_tweets))
