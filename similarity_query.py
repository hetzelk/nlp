import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import corpora, models, similarities

class Similarity:
    def __init__(self, dictpath='softarticles.dict', corpuspath='softarticles.mm'):
        self.dictionary = self.load_corp_dict(dictpath)
        self.corpus = self.load_corpus(corpuspath)
        self.lsi = self.load_lsi() #self.create_lsi()
        self.index = self.load_index() #self.initialize_query_structure('sftarticle')
        
    def initialize_query_structure(self, fname):
        index = similarities.MatrixSimilarity(self.lsi[self.corpus])
        index.save(fname + '.index')
        return index
        
    def load_corpus(self, corpuspath):
        corpus = corpora.MmCorpus('{}'.format(corpuspath))
        return corpus
        
    def load_corp_dict(self, dictpath):
        dict = corpora.Dictionary.load('{}'.format(dictpath))
        return dict
        
    def create_lsi(self):
        lsi = models.LsiModel(self.corpus, id2word=self.dictionary, num_topics=50)
        lsi.save('sftartlsi')
        return lsi
        
    def load_index(self):
        index = pickle.load(open('sftarticle.index', 'rb')
        return index
        
    def load_lsi(self):
        lsi = pickle.load(open('sftartlsi.projection', 'rb'))
        return lsi
        
s = Similarity()
# for key, value in s.dictionary.token2id.items():
    # print('key: {}, value: {}'.format(key.encode('utf-8'), value))
