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
	emailList = []
	g1 = googleSearch("accounting firms auckland")

	thread1 = checkURLThread("Thread-1")
	thread2 = checkURLThread("Thread-2")

	thread1.start()
	thread2.start()

	for url in g1.getWebsiteList():
		thread1.insertURL(url)
		thread1.run()


	# thread1.insertURL("www.allangibson.co.nz")
	# thread2.insertURL(g1.returnWebsiteList()[1])

	# thread1.start()


main()