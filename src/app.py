from controller.TweetController import TweetController

class App(object):
	def run(self):
		tweetCtrl = TweetController()
		tweetCtrl.start_stream(['#LIVMUN']);

if __name__ == "__main__":
	app = App()
	app.run()