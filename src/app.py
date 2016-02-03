import router
import json

"""
Read the config file and save it to the config variable.
"""
f = open("config.json")
config = json.loads(f.read())
f.close()

class App(object):
	"""
	Create a new Router and start the server.
	"""
	def run(self):
		route = router.Router()
		route.run()

if __name__ == "__main__":
	"""
	Create a new App and run it.
	"""
	app = App()
	app.run()