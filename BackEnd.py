import pymongo
from pymongo import MongoClient

cluster = pymongo.MongoClient("mongodb+srv://Benett:_8d2jQhJ7-hX$58@zenclstr.du569.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["ZenClstr"]
collection = db["DataBase"]

post = {"_id": 0, "name": "examplename", "score": 5}

collection.insert_one(post)
