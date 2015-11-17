import pymongo
from pymongo import MongoClient

class DAO:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.database
        self.wiki_corpus = self.db.wiki_corpus
    
    ## Takes list of objects
    def insert_many(self, entries):
        ids = self.wiki_corpus.insert_many(entries).inserted_ids
        return ids