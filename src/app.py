from controller.TweetController import TweetController

class App(object):
	def run(self):
		tweetCtrl = TweetController()
		tweetCtrl.get_tweets();

if __name__ == "__main__":
	app = App()
	app.run()