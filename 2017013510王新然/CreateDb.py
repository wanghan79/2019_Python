import pymongo
from randomGen import Generator

#连接数据库
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["database"]
mycol = mydb["RandomNumbers"]

x =mycol.delete_many({})
i=0
for n in Generator.dataGenerate():
    i=i+1
    mydict={'_id':i,'content':n}
    x=mycol.insert_one(mydict)


file = open('database.txt', 'w')
for x in mycol.find():
    file.write(str(x) + '\n')

