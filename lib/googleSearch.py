import sys
import requests
from bs4 import BeautifulSoup

# Google Search Class
class googleSearch():

	def __init__(self, query):
		self.query 			= "http://google.com/search?q=" + "+".join(query.split()) + "&num=100"
		self.page 			= 1
		# self.content 		= requests.get(self.query).text
		self.websiteList 	= self.returnWebsiteList()

	def websiteList(self):
		return self.websiteList

	def returnWebsiteList(self):
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
			text = cite.text.replace("https://", "").replace("http://", "")
			if "..." in cite.text:
				storeURL.append(cite.text.split("/")[0])
			else:
				storeURL.append(cite.text)
		return storeURL