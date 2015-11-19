from corpus_creation import MrClean
from similarity_query import Query

class Compare:
    def __init__(self):
        self.cleaned = MrClean()
        self.query = Query(self.cleaned)
        
    def display_results(self):
        print(self.query.score_dict)
        
if __name__=="__main__":
    compare = Compare()
    compare.display_results()