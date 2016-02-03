from controller.TweetController import TweetController
from flask import Flask, render_template, request, session, Response
import urllib
import jsonstruct

# Creates a Flask server
server = Flask("iscp")

"""
All the routes of the application are defined in this class.
"""
class Router(object):
	@server.route("/start_stream")
	def start_stream():
		"""
		Start a new sentiment analysis with the given keywords. Uses the Twitter stream api.
		"""
		keywords = []
		keywords.append(urllib.unquote(request.args.get('keyword')).decode('utf8'))
		tweetCtrl = TweetController(server)
		tweetCtrl.start_stream(keywords=keywords)
		return "stream started"

	@server.route("/")
	def index():
		"""
		Returns the index.html template
		"""
		return render_template('index.html')

	@server.route("/status")
	def status():
		"""
		Returns the current status of the sentiment analysis (id, status, tweets_analyzed, avg_mood, pos_tweets, 
		neg_tweets, neu_tweets).
		"""
		tweetCtrl = TweetController(server)
		ret = jsonstruct.encode(tweetCtrl.get_status())
		return Response(response=ret, status=200, mimetype="application/json")

	@server.route("/stop_stream")
	def stop_stream():
		"""
		Stop the current sentiment analysis.
		"""
		tweetCtrl = TweetController(server)
		tweetCtrl.stop_stream()
		return "steam stopped"

	def run(self):
		"""
		Start the server.
		"""
		server.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
		server.run(debug=True, threaded=True)