import requests
import wikipedia
from urllib import parse

class Wikipedia_API():
    def __init__(self):
        self.endpoint = "http://en.wikipedia.org/w/api.php"
        self.constructors = "&format=json&action=query&prop=revisions&rvprop=content"
            
    def get_article_info(self, title, auto_suggest = True, redirect = True, topic_match_length = 250):
        try:
            title = str(title)
            revisions = self.get_article_revisions(title)
            page = wikipedia.page(title = title, auto_suggest = auto_suggest, redirect = redirect)
            page_info = {
                'url': page.url,
                'content': page.content,
                'summary': page.summary,
                'links': page.links,
                'json': self.get_article_json(title),
            }
            return page_info
        except Exception as e:
            print("Type: {} | Error: {}".format(type(e), e))
            
    def get_random_pages(self, num):
        title_list = wikipedia.random(num = num)
        page_list = [wikipedia.page(title = page) for page in page_list]
        return [(page.title, page.url) for page in page_list]
        
    def get_article_json(self, title):
        title = parse.quote_plus(title)
        response = requests.get(self.endpoint + "?titles={}".format(title) + self.constructors)
        return response.json()
            
print (Wikipedia_API().get_random_pages(60))
