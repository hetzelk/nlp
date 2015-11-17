import pymongo
from pymongo import MongoClient

class DAO:
    def __init__(self, collection_type):
        self.client = MongoClient("mongodb://gandalf:fooledeveryone@10.2.20.39")
        self.db = self.client['admin']
        if connection_type == "TEST":
            self.test = self.db['TEST']
        else:
            self.topics = self.db['topics']
    
    def insert_many(self, collection, entries):
        if collection = "TEST":
            ids = self.test.insert_many(entries).inserted_ids
            return ids
        else:
            ids = self.topics.insert_many(entries).inserted_ids
            return ids