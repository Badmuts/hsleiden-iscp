class Tweet(object):
	tweet = ""
	datetime = ""
	user = ""
	sentiment = ""

	def __init__(self, tweet, datetime, user):
		"""
		Creates a Tweet object containing a tweet.
		"""
		self.tweet = tweet
		self.datetime = datetime
		self.user = user
		self.sentiment = ''

	def getTweet(self):
		"""
		Return the tweet
		"""
		return self.tweet

	def getDate(self):
		"""
		Return the a datetime stamp of the tweet
		"""
		return self.datetime

	def getUser(self):
		"""
		Return user of the tweet
		"""
		return self.user
		
	def setTweet(self, tweet):
		"""
		Set the tweet
		"""
		self.tweet = tweet

	def setDate(self, date):
		"""
		Set the datetime of the tweet
		"""
		self.datetime = date

	def setUser(self, user):
		"""
		Set the user of the tweet
		"""
		self.user = user

	def get_sentiment(self):
		"""
		Get the sentiment of the tweet.
		"""
		return self.sentiment

	def set_sentiment(self, sentiment):
		"""
		Set the sentiment of the tweet (pos, neg, neu).
		"""
		self.sentiment = sentiment

	def printTweet(self):
		"""
		Utility method used to print the tweet
		"""
		print(self.getTweet())
		print(self.getDate())
		print(self.getUser())