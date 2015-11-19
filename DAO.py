import pymongo
from pymongo import MongoClient
from keys import keys

class DAO:
    def __init__(self):
        self.connection = MongoClient(keys['SERVER'])
        self.handle = self.connection[keys['DATABASE']]
        self.handle.authenticate(keys['USER_NAME'], keys['PASSWORD'])
    
    def insert_one(self, entry):
        id = self.handle[keys['COLLECTIONS'][2]].insert_one(entry).inserted_id
        return id
    
    def find(self, collection, key):
        cursor = self.handle[collection].find()
        return [item[key] for item in cursor]