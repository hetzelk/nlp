import logging
from gensim import corpora, models, similarities
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from nltk.corpus import stopwords
from collections import defaultdict

# #article every line
# software_articles = [

# ]




stop_list = stopwords.words("english")
cleaned_softarticles = []
for article in software_articles:
    ls = [word for word in article.lower().split() if word not in stop_list]
    cleaned_softarticles.append(ls)
    
frequency = defaultdict(int)
for article in cleaned_softarticles:
    for token in article:
        frequency[token] += 1

final_softarticles = []
for article in cleaned_softarticles:
    ls = [token for token in article if frequency[token] > 1]
    final_softarticles.append(ls)

dictionary = corpora.Dictionary(final_softarticles)
dictionary.save('softarticles.dict')
#print(dictionary.token2id)

corpus = [dictionary.doc2bow(article) for article in final_softarticles]
corpora.MmCorpus.serialize('softarticles.mm', corpus)





# article_dict = {article title: article}

# article_titles = []
# article_content = []


