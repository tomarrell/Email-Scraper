# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#														  #
#                       Email Scraper 					  #
#														  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This program is provided for educational purposes only. #
# The developer accepts no responsibility for any illegal #
# use of this tool. Licensed under GNU Public License V3. #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Imports
import sys
import requests
from bs4 import BeautifulSoup
from lib.googleSearch import googleSearch
from lib.checkURLThread import checkURLThread

# Helper methods


# Main method
def main():
	print(sys.argv)
	# args = ["law firms", "plumbing auckland"]
	emailList = []
	thread1 = checkURLThread("Thread-1")
	thread2 = checkURLThread("Thread-2")
	for arg in sys.argv[1:]:
	# for arg in args:
		g1 = googleSearch(arg)
		results = g1.getWebsiteList()
		for url in results:
			thread1.insertURL(url)
			thread1.run()

		# thread2.insertURL(url)
		# print("Thread 2 Running")
		# thread2.run()

	print("===================")
	print("=       End       =")
	print("===================")

	# thread1 = checkURLThread("Thread-1")
	# thread2 = checkURLThread("Thread-2")

	# thread1.start()
	# thread2.start()

	# for url in g1.getWebsiteList():
	# 	thread1.insertURL(url)
	# 	thread1.run()

	# thread1.insertURL("www.allangibson.co.nz")
	# thread2.insertURL(g1.returnWebsiteList()[1])

	# thread1.start()

main()