from chai import Chai
from iscp.Model.Tweet import Tweet

class TestTweet(Chai):
	
	def test_tweet(self):
		tweet = Tweet("Karel appel?", 1448432850, "@karelappel")
		self.assert_equals(tweet.getTweet(), "Karel appel?")
		self.assert_equals(tweet.getDate(), 1448432850)
		self.assert_equals(tweet.getUser(), "@karelappel")

if __name__ == '__main__':
    import unittest2
    unittest2.main()

