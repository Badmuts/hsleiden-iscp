import tweepy
import os
import json
from model.Tweet import Tweet 

class Listener(tweepy.StreamListener):	

	def __init__(self, save_location = "/../tweets.json"):
		super(Listener, self).__init__()
		self.save_location = save_location
		self.count = 0
		self.tweets = []

	def on_status(self, status):
		if self.count <= 10:
			self.tweets.append(self.create_tweet(status))
			self.count += 1
			return True
		self.save_tweets()
		return False

	def on_disconnect(self, notice):
		"""Called when twitter sends a disconnect notice
		Disconnect codes are listed here:
		https://dev.twitter.com/docs/streaming-apis/messages#Disconnect_messages_disconnect
		"""
		self.save_tweets()
		return

	def create_tweet(self, status):
		return Tweet(status.text.encode("utf8"), str(status.created_at), status.user.screen_name)

	def save_tweets(self):
		f = open(os.path.dirname(__file__) + self.save_location, "w")
		for tweet in self.tweets:
			f.write(json.dumps(tweet.__dict__))
		f.close()
