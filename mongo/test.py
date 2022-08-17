import pymongo
import json



client = pymongo.MongoClient('localhost', 27017)
#print(client)
try:
    client.server_info()
except Exception as ex:
    print(ex)
db = client['test2']

#print(db)

collection = db['test2']

#print(collection)