import threading

# Thread class
class checkURLThread(threading.Thread):
	def __init__(self, threadID, URL):
		threading.Thread.__init__(self)
		self.threadID 	= threadID
		self.URL 		= URL
	def run(self):
		print(self.threadID, self.URL)