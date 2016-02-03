import re
"""
Class used to analyze a Tweet. This is a basic sentiment analysis.
"""
class Analyser(object):
	""" 
	Lists containing positive, negative and neutral words.
	"""
	positive_words = ["cool", "awesome", "great", "incredible", "wow", "amazing", "good", "happy", "goal", "right", "love", "loved", "more", "perfect", "best", "won", "win", "epic", "congrats", "better", "biggest", "remarkable", "will", "does", "like", "heaven", "haha", "hahaha", "lol", "laugh", "laughing"]
	negative_words = ["not", "bad", "lousy", "worthless", "wtf", "angry", "mad", "missed", "miss", "wrong", "hate", "hated", "less", "lost", "worst", "smallest", "atrocious", "horrifyingly", "poor", "horrifying", "rubbish", "shagged", "doesn't", "won't", "fraud", "doubt", "doubts", "dead", "die", "hell", "cruel", "criminal", "shooting"]
	neutral_words  = ["ok", "okay", "oke", "hmm", "mmh", "absolutely", "only", "maybe"]

	def __init__(self):
		pass

	def analyse(self, tweet):
		"""
		Recieves a Tweet object and does a sentiment analyses by checking if a word exists in the positive, negative or
		neutral list. 

		When a word is positive it adds 0.6 to the total score. 
		When a word is negative it substracts 0.5 from the total score.

		It eventualy sets the sentiment of the tweet.
		"""
		processed_text = self.process_text(tweet.getTweet())
		score = 0
		for word in processed_text:
			if word in self.positive_words:
				score += 0.6
			if word in self.negative_words:
				score -= 0.5
		if score <= -0.5:
			tweet.set_sentiment("neg")
		elif score >= 0.5:
			tweet.set_sentiment("pos")
		else:
			tweet.set_sentiment("neu")

	def process_text(self, text):
		""" 
		Processes text from the Tweet. Sets it to lower case. Rewrites links. Rewrites mentions to other users. Removes
		white space. Removes hashtags.
		"""
		text = text.lower()
		# Remove links
		text = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http://[^\s]+))','URL',text)
		# Remove mentions
		text = re.sub('@[^\s]+','MENTION',text)
		# Remove white spaces
		text = re.sub('[\s]+', ' ', text)
		# Remove hashtag from words
		text = re.sub(r'#([^\s]+)', r'\1', text)

		#trim 
		text = text.strip('\'"')
		# Split text to array
		text = text.split()
		return text

