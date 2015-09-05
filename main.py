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
	g1 = googleSearch("accounting firms auckland")
	print(g1.returnWebsiteList())
	

main()