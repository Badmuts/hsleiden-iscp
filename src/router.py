from controller.TweetController import TweetController
from flask import Flask, render_template, request, session, Response
import urllib.parse
import jsonstruct

server = Flask("iscp")

class Router(object):
	@server.route("/start_stream")
	def start_stream():
		keywords = []
		keywords.append(urllib.parse.unquote(request.args.get('keyword')).decode('utf8'))
		tweetCtrl = TweetController(server)
		tweetCtrl.start_stream(keywords=keywords)
		return "stream started"

	@server.route("/")
	def index():
		return render_template('index.html')

	@server.route("/status")
	def status():
		tweetCtrl = TweetController(server)
		ret = jsonstruct.encode(tweetCtrl.get_status())
		return Response(response=ret, status=200, mimetype="application/json")

	@server.route("/stop_stream")
	def stop_stream():
		tweetCtrl = TweetController(server)
		tweetCtrl.stop_stream()
		return "steam stopped"

	def run(self):
		server.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
		server.run(debug=True, threaded=True)