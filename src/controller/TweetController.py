from model.Tweet import Tweet
import tweepy
import os
import json
from service.Listener import Listener

CONSUMER_KEY 		= os.environ['CONSUMER_KEY']
CONSUMER_SECRET 	= os.environ['CONSUMER_SECRET']
ACCESS_TOKEN 		= os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

class TweetController(object):

	def __init__(self):
		self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		self.auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
		self.api = tweepy.API(self.auth, parser=tweepy.parsers.JSONParser())

	def get_tweets(self):
		pub_tweets = self.api.home_timeline()
		f = open(os.path.dirname(__file__)  + "/../tweets.json", "w")
		f.write(json.dumps(pub_tweets))

	def start_stream(self, keywords):
		self.tweet_listener = Listener()
		self.stream = tweepy.Stream(auth = self.auth, listener=self.tweet_listener)
		self.stream.filter(track=keywords, async=True)

	def list_tweets(self):
		f = open(os.path.dirname(__file__)  + "/../tweets.json")
		return f.read()

	def stop_stream(self):
		self.stream.disconnect()
