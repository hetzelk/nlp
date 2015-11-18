import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import corpora, models, similarities

class Similarity:
    def __init__(self, dictpath='softarticles.dict', corpuspath='softarticles.mm'):
        self.dictionary = corpora.Dictionary.load('{}'.format(dictpath))
        self.corpus = corpora.MmCorpus('{}'.format(corpuspath))
        self.index = self.initialize_query_structure()
        
    def initialize_query_structure(self):
        index = similarities.MatrixSimilarity(lsi[self.corpus])
        return index