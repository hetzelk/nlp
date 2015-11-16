import requests
import wikipedia
import json
import re
from urllib import parse

class Constructor():
    def __init__(self):
        self.endpoint = "http://en.wikipedia.org/w/api.php"
        self.constructors = "&format=json&action=query&prop=revisions&rvprop=content"
        
    ## MAIN COMMANDS
    
    def get_article_info(self, title, auto_suggest = True, redirect = True, topic_match_length = 250):
        try:
            title = str(title)
            revisions = self.get_article_revisions(title)
            page = wikipedia.page(title = title, auto_suggest = auto_suggest, redirect = redirect)
            page_info = {
            'content': page.content,
            'url': page.url
            'summary': page.summary,
            'links': page.links,
            'sections': page.sections,
            'json': self.get_article_json(title),
            'related_topics': self.get_related_topics(revisions, topic_match_length)
            }
            return page_info
        except Exception as e:
            print("Type: {} | Error: {}".format(type(e), e))
            
    def get_random_pages(self, num):
        title_list = wikipedia.random(num = num)
        page_list = [wikipedia.page(title = page) for page in page_list]
        return [(page.title, page.url) for page in page_list]
            
    ## SUPPLEMENTARY METHODS
            
    def get_article_json(self, title):
        title = parse.quote_plus(title)
        response = requests.get(self.endpoint + "?titles={}".format(title) + self.constructors)
        return response.json()
        
    def get_article_revisions(self, title):
        try:
            json = self.get_article_json(title.lower())
            page = json['query']['pages']
            key = list(page)[0]
            revisions = page[key]['revisions'][0]['*']
            return revisions
        except Exception as e:
            print("Type: {} | Error: {}".format(type(e), e))
        
    def get_related_topics(self, revisions, match_length):
        try:
            match_length = int(match_length)
            regx = re.compile("\[\[.*\]\]", re.IGNORECASE)
            matches = re.findall(regx, revisions)
            return [match for match in matches if len(match) <= match_length]
        except Exception as e:
            print("Type: {} | Error: {}".format(type(e), e))