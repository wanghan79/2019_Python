#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 17:09:10 2019

@author: stefan
"""
import pymongo
import random
"""
在MongoDB中，定义一个数据库，名为'wqx_db'，其中有collection名为numbers，把数据存到数据库中
"""
#链接本地数据库服务
client = pymongo.MongoClient('127.0.0.1', 27017)
#创建
db = client['wqx_db']
#集合
mumbers = db.mumbers

x={'中国':['习近平','毛泽东','周恩来','朱德','江泽民'],
   '美国':['华盛顿','奥巴马','克林顿','华莱士'],
   '日本':['苍老师','小泽玛利亚','大桥未久','吉泽明步','秦泽多摩雄'],
   '韩国':['金正恩','李敏镐','BigBang','朴泰桓']}
s=list(x.keys())

def CreateRandomNumber(i):
    while i!=0:
        randomInt = random.randint(0, 100)
        randomFloat = random.uniform(0,100)
        randomChar = random.choice('q%#F$*AS)_w(DG@er^!+t&yH~-=')
        country = random.choice(s)
        famous = random.choice(x[country])
        trip = (randomInt, randomFloat, randomChar,country + ": [" + famous + "]")
        yield trip
        randomNumber = {
            '整型': randomInt,
            '浮点数':randomFloat,
            '字符': randomChar,
            '国家': country,
            '著名人物' : famous
        }
        mumbers.insert_one(randomNumber)
        i = i - 1
    return 'done'
g = CreateRandomNumber(100000)
f = open("out.txt", "w", encoding="utf-8")
while True :
    try:
        y = next(g)
        print(y, file = f)
    except StopIteration as exit:
        print(exit.value)
        break
f.close()
