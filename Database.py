import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

#dblist = (myclient.list_database_names())
mycollection = mydb["keywords"]
mydictionary = {"keyword": "Java", "url": "https://www.w3schools.com/java/java_encapsulation.asp"}
x = mycollection.insert_one(mydictionary)
print(x.inserted_id)