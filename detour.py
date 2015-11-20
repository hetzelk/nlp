import Wikipedia_API
import cleanrandom


class Detour:
    def __init__(self):
        self.wiki = Wikipedia_API.Wikipedia_API()
        self.cr = cleanrandom.Exponentialsearch()
        self.article = self.cr.repeat()
        self.title = self.article['title'].encode('utf-8')
        self.content = self.article['content'].encode('utf-8')
        # print(self.title.encode('utf-8'), self.content.encode('utf-8'))
        
