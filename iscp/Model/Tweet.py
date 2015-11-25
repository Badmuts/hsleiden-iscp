class Tweet(object):
	tweet = ""
	datetime = 0
	user = ""

	"""docstring for Tweet"""
	def __init__(self, tweet, datetime, user):
		super(Tweet, self).__init__()
		self.tweet = tweet
		self.datetime = datetime
		self.user = user

	def getTweet(self):
		return self.tweet

	def getDate(self):
		return self.datetime

	def getUser(self):
		return self.user
		
	def setTweet(self, tweet):
		self.tweet = tweet

	def setDate(self, date):
		self.datetime = date

	def setUser(self, user):
		self.user = user

	def printTweet(self):
		print(self.getTweet())
		print(self.getDate())
		print(self.getUser())