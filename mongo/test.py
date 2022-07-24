import pymongo
import json



client = pymongo.MongoClient('localhost', 27017)
print(client)

db = client['test2']

collection = db['test2']

print(db.name)