import router

class App(object):
	def run(self):
		route = router.Router()
		route.run()		

if __name__ == "__main__":
	app = App()
	app.run()