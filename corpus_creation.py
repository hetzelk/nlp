import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

import pickle
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
        self.article_content = []
        self.get_title_content()
        self.articles = self.get_articles()
        self.stop_list = self.read_stoplist()
        self.cleaned_articles = self.eliminate_stopwords()
        self.final_articles = self.eliminate_one_words()
        print(len(self.final_articles))
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
        stop_list += ['linksedit', 'referencesedit', 'alsoedit', 'readingedit', 'correctnessedit', 'notesedit', 'statesedit'] #'referencesedit', 'alsoedit', 'readingedit', 'correctnessedit', 'notesedit'
        return stop_list
        
    def pre_clean(self, article):
        clean_all = ['"', "'", '?', '!', ';']
        text = article.decode('utf-8')
        for i in clean_all:
            text = text.replace(i, ' ')
        return text
    
    def eliminate_stopwords(self):
        cleaned_articles = []
        for artykle in self.articles:
            article = self.pre_clean(artykle)
            art = article.lower().encode('utf-8').split()
            ls = []
            for word in art:
                w = word.decode('utf-8').strip(',.)][}{&-(=:_').rstrip('s')
                if w not in self.stop_list:
                    ls.append(w.encode('utf-8'))
            # ls = [word for word in art if word not in self.stop_list]
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
        #print(dictionary.token2id)
        return dictionary
    
    def create_corpus_and_save(self, fname='softarticles'):
        corpus = [dictionary.doc2bow(article) for article in self.final_articles]
        corpora.MmCorpus.serialize(fname + '.mm', corpus)
        return corpus
    
    def get_article_dict(self):
        article_dict = self.art.article_dict
        return article_dict
        
    def get_title_content(self):
        for title, content in self.article_dict.items():
            self.article_titles.append(title)
            self.article_content.append(content)
            
    def get_articles(self):
        articles = []
        for content in self.article_dict.values():
            articles.append(content)
        return articles

c = Corporalize()
# #article every line
# software_articles = [

# ]

# article_dict = {article title: article}

# article_titles = []
# article_content = []


