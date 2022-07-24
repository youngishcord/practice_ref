import pymongo
import json

client = pymongo.MongoClient('localhost', 27017)
print(client)

db = client['test2']

collection = db['test2']


def insert_document(collection, data):
    """ Function to insert a document into a collection and
    return the document's id.
    """
    return collection.insert_one(data).inserted_id

new_show = {
    "_id" : "1",
    "name": "FRIENDS",
    "year": 1994
}
#print(insert_document(collection, new_show))

def find_document(collection, elements, multiple=False):
    """ Function to retrieve single or multiple documents from a provided
    Collection using a dictionary containing a document's elements.
    """
    if multiple:
        results = collection.find(elements)
        return [r for r in results]
    else:
        return collection.find_one(elements)

#print(find_document(collection, {'name': 'FRIENDS'}))

def update_document(collection, query_elements, new_values):
    """ Function to update a single document in a collection.
    """
    collection.update_one(query_elements, {'$set': new_values})

new_show = {
    "name": "FRIENDS",
    "year": 1995
}
#id_ = insert_document(collection, new_show)
#print(id)
#update_document(collection, {'_id': id_}, {'name': 'F.R.I.E.N.D.S'})

def delete_document(collection, query):
    """ Function to delete a single document from a collection.
    """
    collection.delete_one(query)

delete_document(collection, {'name': "FRIENDS"})
'''print(client.list_databases())
for k in client.list_databases():
    print(k)
print(type([i for i in client.list_databases()]))
for j in db.list_collections():
    print(j["name"])'''




'''print(type(new_show))
print(new_show)
new_show = json.dumps(new_show)
print(type(new_show))
print(new_show)

new_show = '"_id" : "1","name": "FRIENDS","year": 1994}'
if new_show[0] == "{":
    try:
        new_show = json.loads(new_show)
    except:
        print("cant deserialize data")
else:
    print("wrong format for deserialization")
print(type(new_show))
print(new_show)'''