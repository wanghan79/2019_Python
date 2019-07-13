import pymongo
from dataGenerate import *

#将随机生成数据中的dict类型数据导入到数据库中
fi = open('result.txt', 'w')
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["randomData"]
mycol = mydb["sites"]
sampleOfDataGenerate = DataGenerate()
mylist = sampleOfDataGenerate.datagenerate()

#插入到数据库
x = mycol.insert_many(mylist)

#查询数据库中的所有数据
for x in mycol.find():
  print(x, file = fi)
