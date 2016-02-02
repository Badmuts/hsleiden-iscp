import tweepy
import os
import json
from model.Tweet import Tweet 
import jsonstruct
import sqlite3

class Listener(tweepy.StreamListener):	

	def __init__(self, app, save_location = "/../../tweets.json"):
		super(Listener, self).__init__()
		self.save_location = save_location
		self.count = 0
		self.tweets = []
		self.app = app
		self.conn = sqlite3.connect(os.path.dirname(__file__)  + "/../../iscp.db", check_same_thread=False)

	def on_status(self, status):
		if self.get_status() == "active":
			print("Tweet recieved")
			self.tweets.append(self.create_tweet(status))
			self.count += 1
			self.save_count()
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
		# for tweet in self.tweets:
		f.write(jsonstruct.encode(self.tweets))
		f.close()

	def get_status(self):
		cursor = self.conn.cursor()
		cursor.execute("SELECT status FROM stream_status WHERE id = 1")
		result = cursor.fetchall()
		return str(result[0][0])

	def save_count(self):
		cursor = self.conn.cursor()
		cursor.execute("UPDATE stream_status SET tweets_retrieved=? WHERE id = 1", (self.count,))
		self.conn.commit()
