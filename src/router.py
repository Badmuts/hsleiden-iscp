from controller.TweetController import TweetController
from flask import Flask, render_template

server = Flask("iscp")

class Router(object):
	@server.route("/")
	def hello():
		tweetCtrl = TweetController()
		tweetCtrl.start_stream(keywords=["#LIVMUN"])
		return "Good game, retrieved tweets for 10 seconds"

	@server.route("/kaas")
	def kaas():
		return render_template('index.html')

	def run(self):
		server.run(debug=True)