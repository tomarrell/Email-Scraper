import threading
import re
import requests
import sys
from bs4 import BeautifulSoup

# Thread class
class checkURLThread(threading.Thread):

	def __init__(self, threadID):
		threading.Thread.__init__(self)
		self.threadID 	= threadID
		self.url 		= ""
		self.returnList = []
		# self.callback 	= callback

	def run(self):
		emailRE = "[\w+-]+(?:\.[\w+-]+)*@[\w+-]+(?:\.[\w+-]+)*(?:\.[a-zA-Z]{2,4})"
		contactURL = None
		if self.url:
			website = self.getWebsite()
			if website:
				emails = re.findall(emailRE, website)
				print("Found " + str(len(emails)) + (" emails" if len(emails) > 1 else " email"))
				for email in emails:
					self.saveToFile("data/emails.txt", "\n" + email)
				soup = BeautifulSoup(website, 'html.parser')
				for anchor in soup.find_all("a"):
					# print(anchor.get("href") == None)
					if anchor.get("href") and "contact" in anchor.get("href"):
						contactURL = anchor.get("href")
						break
				website = None
				if contactURL:
					if "/" in self.url:
						self.url = self.url.split("/")[0]
					website = self.getWebsite(contactURL)
					if website:
						emails = re.findall(emailRE, website)
						print("Found " + str(len(emails)) + (" emails" if len(emails) > 1 else " email"))
						if len(emails) == 0:
							self.saveToFile("data/emails.txt", "\n" + "info@" + self.url.replace("www.", ""))
						for email in emails:
							self.saveToFile("data/emails.txt", "\n" + email)
				self.url = ""
				return True
		else:
			return False

	def getWebsite(self, custom=False):
		if custom:
			if "http" in custom:
				print("Getting website " + custom)
				try:
					website = requests.get(custom, verify=False, timeout=4).text
				except:
					print("Error getting website: " + custom)
					website = False
				return website
			else:
				print("Getting website " + "http://" + self.url + custom)
				try:
					website = requests.get("http://" + self.url + custom, verify=False).text
				except:
					print("Error getting website: " + "http://" + self.url + custom)
					website = False
				return website
		else:
			print("Getting website " + "http://" + self.url)
			try:
				website = requests.get("http://" + self.url, verify=False, timeout=4).text
			except:
				print("Error getting website: " + "http://" + self.url)
				website = False
			return website

	def insertURL(self, url):
		self.url = url

	def saveToFile(self, filename, data):
		f = open(filename, 'a')
		f.write(data)
		f.close()
