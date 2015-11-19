from DAO import *
import pickle
import re

class Articles:
    def __init__(self):
        self.article_dict = self.load_article_dict()

    def read(self):
        dao = DAO()
        articles = dao.find("topics")
        for article in articles:
            title = article["title"]
            content = article["content"]
            cont = content.encode('utf-8')
            self.article_dict.update({title:cont})

    def save_article_dict(self):
        pickle.dump(self.article_dict, open("article_dict.pkl", "wb"))

    def load_article_dict(self):
        article_dict = pickle.load(open("article_dict.pkl", "rb"))
        return article_dict

    # def alt_read(self):
        # for key, content in a.article_dict.items():
            # cont = content
            # for c in content:
                # try:
                    # print(c, end='')
                # except:
                    # cont.replace(c, ' ')
            # a.article_dict[key] = cont
            
            
class ObtainQuery(Articles):
    def __init__(self):
        self.query_dict = self.get_query()
		
    def get_query(self):
        blank = ''.encode('utf-8')
        content = blank
        dao = DAO()
        while content == blank:
            article = dao.pop('random')
            title = article["title"]
            content = article["content"].encode('utf-8')
        query = {title:content}
        return query
            
        
		




