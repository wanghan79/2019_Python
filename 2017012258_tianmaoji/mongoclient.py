import pymongo
#连接数据库
mongoClient=pymongo.MongoClient('localhost',12345)
# 格式：mongoClient.库名  如果该库存在表示使用该库，如果该库不存在表示创建该库
client = pymongo.MongoClient('localhost', 12345)
db = client['maojitian']
table = db['data']
user=[{'name':'MaojiTian','age':22,'sex':'男'},{'name':'Tom','age':34,'sex':'男'}]
data.student.insert(user) #插入一条记录
#data.student.remove({'name':'MaojiTian'})    #删除一条记录
#mongoClient.close()   #关闭连接