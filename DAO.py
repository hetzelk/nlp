import pymongo
from pymongo import MongoClient

class DAO:
    def __init__(self):
        self.connection = MongoClient("10.2.20.39:27017")
        self.handle = self.connection['admin']
        self.handle.authenticate("gandalf", "fooledeverybody")
    
    def insert_one(self, entry):
        id = self.handle['TEST'].insert_one(entry).inserted_id
        return id