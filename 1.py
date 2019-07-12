import pymongo
from GenData import DataGenerate
i=0
myclient=pymongo.MongoClient("mongodb://localhost:27017")
mydb=myclient["runoobdb"]
mycol=mydb["sites"]
for n in DataGenerate.dgenerate():
    i=i+1
    mydict={'id':i,'content':n}
    x=mycol.insert_one(mydict)
print(x)

'''
class mongo:
    def dbConnect(self,clientName='client'):
        clientName=pymongo.MongoClient(host='localhost',port=27017)
    def dbSelect(self,clientName='client',dbName='testDB'):
        pass
'''