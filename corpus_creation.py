import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import corpora, models, similarities
from nltk.corpus import stopwords
from collections import defaultdict
#from article_dict import Article

class Corporalize:
    def __init__(self):
        self.articles = []
        self.cleaned_softarticles = self.eliminate_stopwords()
        self.final_softarticles = self.eliminate_one_words()
        self.dictionary = self.create_dict_and_save()
        self.corpus = self.create_corpus_and_save()
        
    def eliminate_stopwords(self):
        stop_list = stopwords.words("english")
        cleaned_softarticles = []
        for article in self.articles:
            ls = [word for word in article.lower().split() if word not in stop_list]
            cleaned_softarticles.append(ls)
        return cleaned_softarticles
    
    def eliminate_one_words(self):
        frequency = defaultdict(int)
        for article in self.cleaned_softarticles:
            for token in article:
                frequency[token] += 1
        final_softarticles = []
        for article in self.cleaned_softarticles:
            ls = [token for token in article if frequency[token] > 1]
            final_softarticles.append(ls)
        return final_softarticles

    def create_dict_and_save(self, fname='softarticles'):
        dictionary = corpora.Dictionary(final_softarticles)
        dictionary.save(fname + '.dict')
        #print(dictionary.token2id)
        return dictionary
    
    def create_corpus_and_save(self, fname='softarticles'):
        corpus = [dictionary.doc2bow(article) for article in final_softarticles]
        corpora.MmCorpus.serialize(fname + '.mm', corpus)
        return corpus



# #article every line
# software_articles = [

# ]

# article_dict = {article title: article}

# article_titles = []
# article_content = []

