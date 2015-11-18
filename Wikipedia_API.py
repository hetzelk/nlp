import requests
import wikipedia
from urllib import parse

class Wikipedia_API():
    def __init__(self):
        self.endpoint = "http://en.wikipedia.org/w/api.php"
        self.article_constructor = "&format=json&action=query&prop=revisions&rvprop=content"
        self.random_constructor = "&action=query&list=random&rnredirect=true&format=json"
            
    def get_article_info(self, title, auto_suggest = True, redirect = True, topic_match_length = 250):
        try:
            title = str(title)
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
        
    def get_article_json(self, title):
        title = parse.quote_plus(title)
        response = requests.get(self.endpoint + "?titles={}".format(title) + self.article_constructor)
        return response.json()
        
    def get_random_articles(self, num):
        response = requests.get(self.endpoint + "?rnlimit={}".format(str(num)) + self.random_constructor)
        article_titles = [article['title'] for article in response.json()['query']['random']]
        url_list = []
        for title in article_titles:
            try:
                print (title)
                page = wikipedia.page(title = title)
                url_list.append((page.url, page.title))
            except wikipedia.exceptions.DisambiguationError:
                pass
            except wikipedia.exceptions.PageError:
                pass
            except:
                pass
                
        return url_list
print(Wikipedia_API().get_random_articles(100))
