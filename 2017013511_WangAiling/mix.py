#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 22:27:26 2019

@author: 王爱玲
"""

import random
import uuid
import pymongo
import matplotlib.pyplot as plt
import numpy as np
import string
#链接本地数据库服务
client = pymongo.MongoClient('127.0.0.1', 27017)
#创建数据库名为text
db=client.test
db=client['test']
#集合person
p=db.persons
p=db['persons']
'''产生随机数元组，包括int，float，string，dict类型数据'''
def getRandomInt():
    return random.randint(0, 10000)

def getRandonFloat():
    return random.uniform(0, 1000)

def getRandomStr():
    return uuid.uuid1()

def getRandomDict():
    node={'number'+str(i):random.randint(1,100) for i in range(5)}
    return node

def dataRandom():
    '''产生随机数据，用tuple存储'''
    for i in range(100000):
        tup=(getRandomInt(),getRandonFloat(),getRandomStr(),getRandomDict())
        return tup


"""
将数据写进Mongodb中
"""
for i in range(10000):
    person={'id':i,'data':dataRandom()}
    result=p.insert_one(person)
    print(result)

"""将生成的数据打印成散点图"""
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title("scatter Plot")
plt.xlabel('X')
plt.ylabel('Y')
for i in range(1000):
    y = getRandonFloat()
    x = i
    ax1.scatter(x, y, c='r', marker='.')
plt.legend('x1')
plt.show()