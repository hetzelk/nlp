import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import corpora, models, similarities

class Similarity:
    def __init__(self, dictpath='softarticles.dict', corpuspath='softarticles.mm'):
        self.dictionary = self.load_corp_dict(dictpath)
        self.corpus = self.load_corpus(corpuspath)
        # self.index = self.initialize_query_structure()
        
    def initialize_query_structure(self, fname):
        index = similarities.MatrixSimilarity(lsi[self.corpus])
        index.save(fname + '.index')
        return index
        
    def load_corpus(self, corpuspath):
        corpus = corpora.MmCorpus('{}'.format(corpuspath))
        return corpus
        
    def load_corp_dict(self, dictpath):
        dict = corpora.Dictionary.load('{}'.format(dictpath))
        return dict
s = Similarity()
# for key, value in s.dictionary.token2id.items():
    # print('key: {}, value: {}'.format(key.encode('utf-8'), value))
print('\n\n\n\n\n')
print(s.corpus)