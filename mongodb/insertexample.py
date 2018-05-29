"""Mongo Insert Model"""
from pymongo import MongoClient
from pymongo.results import InsertManyResult

class InsertExample:

    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.dbName = self.client.inventory
        print(self.client.database_names())

    def insertOneRecord(self):
        record = self.dbName.inventory.insert_one({"item": "canvas",
                                                   "qty": 100,
                                                   "tags": ["cotton"],
                                                   "size": {"h": 28, "w": 35.5, "uom": "cm"}})

        print(record.inserted_id)
        print(self.dbName.inventory.find({"item":"canvas"}))

    def colseConnection(self):
        self.client.close()
    
    def insertManyRecords(self):
        mayResult = self.dbName.inventory.insert_many([{"item": "canvas",
                                                     "qty": 100,
                                                     "tags": ["cotton"],
                                                     "size": {"h": 28, "w": 35.5, "uom": "cm"}},
                                                    {"item": "toy",
                                                     "qty": 20,
                                                     "tags": ["cotton"],
                                                     "size": {"h": 10, "w": 15.5, "uom": "cm"}},
                                                    {"item": "statue",
                                                     "qty": 60,
                                                     "tags": ["mud"],
                                                     "size": {"h": 28, "w": 35.5, "uom": "cm"}}])
        print(mayResult.inserted_ids)

    def printResults(self):
        cursor = self.dbName.inventory.find({})

        for result in cursor:
            print(result)


if __name__ == '__main__':
    insertExmpl = InsertExample()
    insertExmpl.insertOneRecord()
    insertExmpl.colseConnection()
    insertExmpl.insertManyRecords()
    insertExmpl.printResults()