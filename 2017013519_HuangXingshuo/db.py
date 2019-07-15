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

dblist = myclient.list_database_names()

#由于MongoDB的惰性创建特性，需要插入后再判断是否已创建

if "randomData" in dblist:  #判断randomData数据库是否存在
  print("数据库已存在！")
collist = mydb. list_collection_names()
if "sites" in collist:   # 判断 sites 集合是否存在
  print("集合已存在！")
#查询数据库中的所有数据
for x in mycol.find():
  print(x, file = fi)
