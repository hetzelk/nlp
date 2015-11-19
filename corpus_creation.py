import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

import pickle
import re
from gensim import corpora, models, similarities
from collections import defaultdict
from nltk.corpus import stopwords
from article_dict import Articles

class Corporalize:
    def __init__(self):
        self.art = Articles()
        self.article_dict = self.get_article_dict()
        print(len(self.article_dict))
        self.article_titles = []
        self.articles= []
        self.get_title_content()
        self.stop_list = self.read_stoplist()
        self.cleaned_articles = self.eliminate_stopwords()
        self.final_articles = self.eliminate_one_words()
        # self.dictionary = self.create_dict_and_save()
        # self.corpus = self.create_corpus_and_save()
    
    # # modify this function when stop list needs to be edited or added to
    # def create_stoplist(self):
        # stop_list = stopwords.words("english")
        # stop_list += ['==', '===', '====','external', 'links', 'search', '=', 'references', 'summary', '-', '.', ',', '', 'introduction', '^']
        # print(stop_list)
        # pickle.dump(stop_list, open('stoplist.pkl', 'wb'))
    
    def read_stoplist(self):
        stop_list = pickle.load(open('stoplist.pkl', 'rb'))
        # stop_list += ['linksedit', 'referencesedit', 'alsoedit', 'readingedit', 'correctnessedit', 'notesedit', 'statesedit', 'compileredit' 'overviewedit', 'architecturesedit', 'historyedit', 'definitionsedit', 'licensingedit', 'developmentedit', 'modeledit', 'toolsedit', 'organizationsedit', 'softwareedit', 'adoptionedit', 'usagedit', 'theoryedit', 'computationedit', 'originedit', 'eraedit', 'basicedit', 'versionsedit', 'otheredit', 'syntaxedit', 'examplesedit', 'featuresedit', 'standardedit']
        return stop_list
       
    def pre_clean(self, article):
        clean_all = ['"', "'", ';']
        text = article.decode('utf-8')
        for i in clean_all:
            text = text.replace(i, ' ')
        return text
        
    def strip_suffix(self, text, suffix):
        if text.endswith(suffix):
            return text[:-len(suffix)]
        return text
    
    def eliminate_stopwords(self):
        cleaned_articles = []
        for artykle in self.articles:
            article = self.pre_clean(artykle)
            art = article.lower().encode('utf-8').split()
            ls = []
            for word in art:
                w = word.decode('utf-8').strip(',.)}{&-(=:!_?').rstrip('s')
                w = self.strip_suffix(w, 'edit')
                if w not in self.stop_list:
                    ls.append(w)
            cleaned_articles.append(ls)
        return cleaned_articles
    
    def eliminate_one_words(self):
        frequency = defaultdict(int)
        for article in self.cleaned_articles:
            for token in article:
                frequency[token] += 1
        final_articles = []
        for article in self.cleaned_articles:
            ls = [token for token in article if frequency[token] > 1]
            final_articles.append(ls)
        return final_articles
        
    def create_dict_and_save(self, fname='softarticles'):
        dictionary = corpora.Dictionary(self.final_articles)
        dictionary.save(fname + '.dict')
        return dictionary
    
    def create_corpus_and_save(self, fname='softarticles'):
        corpus = [self.dictionary.doc2bow(article) for article in self.final_articles]
        corpora.MmCorpus.serialize(fname + '.mm', corpus)
        return corpus
    
    def get_article_dict(self):
        article_dict = self.art.article_dict
        return article_dict
        
    def get_title_content(self):
        for title, content in self.article_dict.items():
            self.article_titles.append(title)
            self.articles.append(content)
            
c = Corporalize()
