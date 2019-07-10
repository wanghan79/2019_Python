import pymongo
from GenData import DataGenerate
'''
功能：创建数据库
作者：高晓雨2017012834
日期：2019年7月
'''
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