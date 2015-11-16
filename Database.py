import pymongo
from pymongo import MongoClient
import gridfs

class Database:
    def __init__(self):
        self.db = None
        self.fc = None
        self.setup()
        
    def setup(self):
        client = MongoClient()
        self.db = client.candidate_db
        self.fc = self.db.fav1
        
    def insert_entry(self, entry):
        entry_id = self.cc.insert_one(entry).inserted_id
    # return entry_id