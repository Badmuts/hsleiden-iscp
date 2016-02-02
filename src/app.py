import router
import json

""" Read the config file"""
f = open("config.json")
config = json.loads(f.read())
f.close()

class App(object):
	def run(self):
		route = router.Router()
		route.run()

if __name__ == "__main__":
	app = App()
	app.run()