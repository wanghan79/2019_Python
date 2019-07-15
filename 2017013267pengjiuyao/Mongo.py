import pymongo
from Generate import DataGenerate

def mongoc():
 i=0
 myclient=pymongo.MongoClient("mongodb://localhost:27017")
 mydb=myclient["runoobdb"]
 mycol=mydb["sites"]
 for n in DataGenerate.dgenerate():
    i=i+1
    mydict={'id':i,'content':n}
    x=mycol.insert_one(mydict)
 print(x)

