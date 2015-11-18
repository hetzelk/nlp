from DAO import *
import pymongo 
from pymongo import MongoClient
from bson.json_util import dumps


class Articles:
	def __init__(self):
		self.DAO = DAO()
		self.article_dict = {}

	def read(self):
		articles = self.DAO.find("topics")
		json_articles = dumps(articles) 
		
		for article in json_articles:
			title = article["title"]
			content = article["content"]
			self.article_dict.update({title:content})
		
		




