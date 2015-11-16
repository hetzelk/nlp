import pymongo
from pymongo import MongoClient

class Database:
    def __init__(self):
        self.db = None
        self.fc = None
        self.setup()
        
    def setup(self):
        client = MongoClient()
        self.db = client.nlp
        self.fc = self.db.fav1
        
    def insert_entry(self, entry):
        self.fc.insert_one(entry).inserted_id
