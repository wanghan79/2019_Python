import pymongo
from First import dataGenerate

#定义数据库
MONGO_URL="localhost"  #本地数据库
MONGO_DB="flyzer"          #定义的数据库名
MONGO_TABLE="table"    #数据库的表名

#链接并创建数据库
client = pymongo.MongoClient(MONGO_URL) #生成一个MongoDB的对象
db = client[MONGO_DB]                   #定义一个db，将数据库的名称传递过来

#定义一个保存函数
def save_to_mongo(ur):
    db[MONGO_TABLE].insert(ur)

#调用上一个文件中的函数并将其实例化传入数据库
MM=dataGenerate()
for i in MM.dGen():
    save_to_mongo(i)  #依次进行存储，并且将前一个Random的数据类型全部改成键值对的形式