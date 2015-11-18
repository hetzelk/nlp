from DAO import *
import pymongo 
from pymongo import MongoClient



class Articles:
	def __init__(self):
		self.DAO = DAO()
		self.article_dict = {}

	def read(self):
		articles = self.DAO.find("topics",)
		for article in articles:
			title = article["title"]
			content = article["content"]
			self.article_dict.update({title:content})

		
		




