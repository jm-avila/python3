from pymongo import MongoClient
import datetime
# MongoClient(host = localhost, port=27017)
myClient = MongoClient()

# by accesing the client the db is created.
db = myClient["my-db"]

# by accesing the db collections are created.
exampleDb = db.example

current_date = datetime.datetime.now()
exampleItem = {"name": "example", "age": 00, "hobbies": ["coding"], "date": current_date.now()}
print("exampleItem", exampleItem)

exampleItemId = exampleDb.insert_one(exampleItem).inserted_id

print("exampleItemId", exampleItemId)

exampleItemList = [{"name": "example2", "age": 1, "hobbies": ["coding","coding"]}, {"name": "example3", "age": 1, "hobbies": ["coding","coding"]}]

exampleItemsIds = exampleDb.insert_many(exampleItemList).inserted_ids

print("exampleItemsIds", exampleItemsIds)

itemsCount = exampleDb.find().count()
print("itemsCount", itemsCount)

itemsAge0Count = exampleDb.find({"age": 0}).count()
print("itemsAge0Count", itemsAge0Count)

example3Count = exampleDb.find({"age": 1, "name": "example3"}).count()
print("example3Count", example3Count)