import pymongo       #导入相关的包
from Generate import dataGenerate

# 连接数据库
client = pymongo.MongoClient('localhost', 12345)
db = client['maojitian']
table = db['data']

#定义一个保存函数
def save_to_mongo(ur):
    db[data].insert(ur)

#调用上一个文件中的函数并将其实例化传入数据库
m=dataGenerate()
for j in m.dGen():
    save_to_mongo(j)  #依次进行存储，并且将前一个Random的数据类型全部改成键值对的形式
