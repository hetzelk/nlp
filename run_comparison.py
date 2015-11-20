from corpus_creation import MrClean
from similarity_query import Query

class Compare:
    def __init__(self):
        self.cleaned = MrClean()
        self.query = Query(self.cleaned)
        self.query_title = self.query.query_title
        self.top, self.all = self.top_ten()
        
    def display_results(self):
        print(self.query.score_dict)
    
    def top_ten(self):
        ten = sorted(self.query.score_dict.items(), key=lambda x:float(x[1]), reverse=True)
        return ten[:10], ten