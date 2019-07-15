#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 21:57:28 2019

@author: 王爱玲
"""
from pymongo import MongoClient
import random
import pymongo
##循环写入（以字典的方式一条一条插入）

#链接本地数据库服务
client = pymongo.MongoClient('127.0.0.1', 27017)
#创建数据库名为text
db=client.test
db=client['test']
#集合
p=db.persons
p=db['persons']

def getRandomInt():
    return random.randint(0, 10000)

def getRandonFloat():
    return random.uniform(0, 1000)

def getRandomStr():
    return uuid.uuid1()
    #ran_str=''.join(random.sample(string.ascii_letter+string.digits,16))
    #return ran_str

def getRandomDict():
    node={'number'+str(i):random.randint(1,100) for i in range(5)}
    return node

def dataRandom():
    '''产生随机数据，用tuple存储'''
    for i in range(100000):
        tup=(getRandomInt(),getRandonFloat(),getRandomStr(),getRandomDict())
        #yield tup
        #print(tup)
        return tup
"""
将数据写进Mongodb中
"""
for i in range(10000):
    person={'id':i,'data':dataRandom()}
    result=p.insert_one(person)
    print(result)

"""
查询数据
"""

res=p.find_one({'id':10})
print(res)



"""
统计数据
"""
count=p.find().count()
"""
排序
"""
res=p.find().sort('id',pymongo.ASCENDING)
"""
删除数据
"""
result=p.remove({'id':10})
result.delete_count

