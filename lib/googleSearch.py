import sys
import requests
from bs4 import BeautifulSoup

# Google Search Class
class googleSearch():

	def __init__(self, query):
		self.query 			= "http://google.com/search?q=" + "+".join(query.split()) + "&num=100&start="
		self.page 			= 1
		# self.content 		= requests.get(self.query).text
		self.websiteList 	= self.returnWebsiteList(0) + self.returnWebsiteList(100) + self.returnWebsiteList(200)

	def getWebsiteList(self):
		return self.websiteList

	def cleanURL(self, url):
		return url.replace("https://", "").replace("http://", "")

	def returnWebsiteList(self, startResult):
		# PRODUCTION CODE
		# storeURL = []
		## Parse raw HTML into BeautifulSoup object
		# soup = BeautifulSoup(self.content, 'html.parser')

		storeURL = []
		# Return Google raw HTML
		rawPageData = open('data/google.txt', 'r').read()
		# Parse raw HTML into BeautifulSoup object
		soup = BeautifulSoup(rawPageData, 'html.parser')

		# Loop over cite tags in HTML
		for cite in soup.find_all("cite"):
			# Extract text from cite tags
			text = self.cleanURL(cite.text)
			if "..." in text:
				storeURL.append(text.split("/")[0])
			else:
				storeURL.append(text)
		return storeURL