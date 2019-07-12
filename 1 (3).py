import json
import pymongo
# 连接MongoDB
client = pymongo.MongoClient(host='localhost', port=27017)
# 指定数据库
db = client.test
# 指定集合
collection = db.randoms
# 导入数据
file = open('test.txt', 'r') 
js = file.read()
dic = json.loads(js)   
file.close() 
# 插入数据
result = collection.insert(dic)
# 查询
result2 = collection.find_one({1: 1})
# 改
condition3 = {1: 1}
randoms3 = collection.find_one(condition3)
randoms3[1] = 25
result = collection.update(condition3, randoms3)
print(result)
# 删除
result = collection.remove({1: 1})
print(result)