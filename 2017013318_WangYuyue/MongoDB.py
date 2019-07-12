#!/usr/bin/python3
import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
dblist = myclient.list_database_names()
# dblist = myclient.database_names() 
if "runoobdb" in dblist:
  print("数据库已存在！")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]
  

"""把txt文件写入MongoDB"""
from pymongo import MongoClient
db = myclient.test  
# 使用 ans集合，没有则自动创建
ans = db.ans
# 打开ans文件，将数据存入到数据库
my_set = db.test_set
with open('ans.txt', 'r') as f:
    for line in f.readlines():    
        # 分割信息
        items = line.strip('\n')   
        # 添加到数据库
        ans.insert({ 'ans':1})
        
        
"""查询数据"""
for i in my_set.find():
    print(i)
#查询ans=uhb13j3ub的数据
for i in my_set.find({"ans":"uhb13j3ub"}):
    print(i)
print(my_set.find_one({"ans":"uhb13j3ub"}))
            

"""添加数据"""
mydict=[{"ans":"uhb13j3ub"}]  
x = mycol.insert_one(mydict)
print(x)


"""修改数据"""
myquery={ "ans": "uhb13j3ub" } #查询条件
newvalues={ "$set": { "ans": "uhb13j3u5" } } #update的对象和一些更新的操作符
mycol.update_one(myquery, newvalues)
for x in mycol.find():
  print(x)



"""删除数据"""
myquery = { "name": {"$regex": "^u"} #删除条件：删除开头为u的ans 
x=mycol.delete_many(myquery)
for x in mycol.find():
  print(x)

