##########################写入mongodb 数据库######################
###########################python操作mongodb数据库
"""
将生成的数据写进MongoDB中

    董昱辰
"""
from pymongo import MongoClient
import homework1
import pymongo
##循环写入（以字典的方式一条一条插入）

client=pymongo.MongoClient(host='127.0.0.1',port=27017)
db=client.test
db=client['test']
p=db.persons
p=db['persons']
"""
将数据写进Mongodb中
"""
for i in range(10000):
    person={'id':i,'data':homework1.dataRandom()}
    result=p.insert_one(person)
    print(result)

"""
查询数据
"""
"""
res=p.find_one({'id':10})
print(res)
"""


"""
统计数据
count=p.find().count()

排序

res=p.find().sort('id',pymongo.ASCENDING)


删除数据

result=p.remove({'id':10})
result.delete_count
"""