from DAO import *
import pickle
import re

class Articles:
    def __init__(self):
        self.DAO = DAO()
        self.article_dict = {}

    # def read(self):
        # articles = self.DAO.find("topics")
        # for article in articles:
            # title = article["title"]
            # content = article["content"]
            # cont = content.encode('utf-8')
            # self.article_dict.update({title:cont})

    # def save_article_dict(self):
        # pickle.dump(self.article_dict, open("article_dict.pkl", "wb"))

    def load_article_dict(self):
        self.article_dict = pickle.load(open("article_dict.pkl", "rb"))

    def alt_read(self):
        for key, content in a.article_dict.items():
            cont = content
            for c in content:
                try:
                    print(c, end='')
                except:
                    cont.replace(c, ' ')
            a.article_dict[key] = cont
            
a = Articles()
a.load_article_dict()
for value in a.article_dict.values():
    print(value)
		
		




