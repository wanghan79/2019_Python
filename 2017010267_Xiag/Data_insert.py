from pymongo import MongoClient
from Random  import Creat
client = MongoClient()
#创建数据库
db = client['Xiag']
col = db['Information']
client = MongoClient(host='localhost', port=27017) #端口号默认为27017是数值
m=Creat()
for j in m.random():
     res=col.insert_one(j)