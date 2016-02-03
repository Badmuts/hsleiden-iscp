import tweepy
import os
import json
from model.Tweet import Tweet 
import jsonstruct
import sqlite3
from service.Analyser import Analyser

class Listener(tweepy.StreamListener):	

	def __init__(self, app, save_location = "/../../tweets.json"):
		super(Listener, self).__init__()
		self.save_location = save_location
		self.count = 0
		self.tweets = []
		self.app = app
		self.conn = sqlite3.connect(os.path.dirname(__file__)  + "/../../iscp.db", check_same_thread=False)
		self.analyser = Analyser()
		print("Listener created")

	def on_status(self, status):
		print("Tweet recieved")
		if self.get_status() == "active":
			self.count += 1
			tweet = self.create_tweet(status)
			self.analyser.analyse(tweet)
			self.tweets.append(tweet)
			self.save_avg_mood()
			self.save_count()
			return True
		self.save_tweets()
		return False

	def on_disconnect(self, notice):
		"""Called when twitter sends a disconnect notice
		Disconnect codes are listed here:
		https://dev.twitter.com/docs/streaming-apis/messages#Disconnect_messages_disconnect
		"""
		print("disconnected")
		self.save_tweets()
		return

	def on_error(self, status_code):
		print(str(status_code))

	def create_tweet(self, status):
		return Tweet(status.text.encode("utf8"), str(status.created_at), status.user.screen_name)

	def save_tweets(self):
		print("Saving tweets to tweets.json")
		f = open(os.path.dirname(__file__) + self.save_location, "w")
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

	def save_avg_mood(self):
		pos_tweets = 0
		neg_tweets = 0
		neu_tweets = 0
		mood = ''
		for tweet in self.tweets:
			if tweet.get_sentiment() == 'pos':
				pos_tweets = pos_tweets + 1
			elif tweet.get_sentiment() == 'neg':
				neg_tweets = neg_tweets + 1
			else:
				neu_tweets = neu_tweets + 1
		if pos_tweets > neg_tweets and pos_tweets > neu_tweets:
			mood = 'pos'
		elif neg_tweets > pos_tweets and neg_tweets > neu_tweets:
			mood = 'neg'
		else:
			mood = 'neu'
		self.save_sent_count(pos_tweets, neg_tweets, neu_tweets)
		self.save_mood(mood);

	def save_mood(self, mood):
		cursor = self.conn.cursor()
		cursor.execute("UPDATE stream_status SET avg_mood=? WHERE id = 1", (mood,))
		self.conn.commit()

	def save_sent_count(self, pos, neg, neu):
		cursor = self.conn.cursor()
		cursor.execute("UPDATE stream_status SET pos_tweets=?, neg_tweets=?, neu_tweets=? WHERE id = 1", (pos, neg, neu))
		self.conn.commit()