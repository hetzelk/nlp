from gensim.corpora import WikiCorpus, wikicorpus

articles = "enwiki-latest-pages-articles.xml.bz2"

wiki_corpus = WikiCorpus(articles)
wiki_corpus.dictionary.save("wiki_dict.dict")