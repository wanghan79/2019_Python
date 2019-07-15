import pymongo
mongoClient=pymongo.MongoClient('localhost',12345)
# 格式：mongoClient.库名  如果该库存在表示使用该库，如果该库不存在表示创建该库
school=mongoClient.school
user=[{'name':'LinfengChen','age':21,'sex':'男'},{'name':'jack','age':30,'sex':'男'}]
#school.student.insert(user) #插入一条记录
#school.student.remove({'name':'LinfengChen'})    #删除一条记录
#mongoClient.close()   #关闭连接