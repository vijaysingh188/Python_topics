import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["Ecommerce"]

collection = db["Sales"]

document = [{"name": "vj", "age": 32},{"name": "Divya", "age": 20}]

collection.insert_many(document)

# collection.update_many({"name": "vj"}, {"$set": {"age": 25}})

# collection.delete_one({"name": "vj"})

print("=====done====")
client.close()
