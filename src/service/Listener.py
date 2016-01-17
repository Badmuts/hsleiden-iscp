from __future__ import print_function
import tweepy
import os
import json


class Listener(tweepy.StreamListener):	

	def __init__(self, save_location = "/../tweets.json"):
		super(Listener, self).__init__()
		self.save_location = save_location
		self.count = 0
		self.f = open(os.path.dirname(__file__) + self.save_location, "w")
		self.f.write("[")

	def on_status(self, status):
		if self.count <= 1000:
			self.f.write("{\"tweet\":{\"text\": \"" + status.text.encode("utf8") + "\"}},")
			print("TWEETS RETRIEVED:" + str(self.count), end="\r")
			self.count += 1
			return True
		self.f.write("]")
		self.f.close()
		print("")
		return False
