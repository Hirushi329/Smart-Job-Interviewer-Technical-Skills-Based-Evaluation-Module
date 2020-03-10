import pymongo

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["myDB"]

mycollection = mydb["questions"]
mydictionary = { "technicalskill": "java", "question": "What are OOP concepts?" }

x = mycollection.insert_one(mydictionary)