from corpus_creation import MrClean
from similarity_query import Query

class Compare:
    def __init__(self):
        self.cleaned = MrClean()
        self.query = Query(self.cleaned)
        self.query_title = self.query.query_title
        self.top = self.top_ten()
        
    def display_results(self):
        print(self.query.score_dict)
    
    def top_ten(self):
        ten = sorted(self.query.score_dict.items(), key=lambda x:float(x[1]), reverse=True)
        # print(ten)
        # titles = self.query.article_titles
        # top_tuple = [i, s for i, s in ten]
        return ten[:10]
        
if __name__=="__main__":
    compare = Compare()
    print(compare.query_title)
    print(compare.top)