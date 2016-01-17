from controller.TweetController import TweetController
from flask import Flask
import json
import time

server = Flask("iscp")

class Router(object):
	@server.route("/")
	def hello():
		tweetCtrl = TweetController()
		tweetCtrl.start_stream(keywords=["#LIVMUN"])
		return "Good game, retrieved tweets for 10 seconds"

	def run(self):
		server.run(debug=True)