#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 17:06:18 2019

@author: stefan
"""

#生成100000条数据，并输出到out.txt中
import random

x={'中国':['习近平','毛泽东','周恩来','朱德','江泽民'],
   '美国':['华盛顿','奥巴马','克林顿','华莱士'],
   '日本':['苍老师','小泽玛利亚','大桥未久','吉泽明步','秦泽多摩雄'],
   '韩国':['金正恩','李敏镐','BigBang','朴泰桓']}
s=list(x.keys())


def CreateRandomNumber(i):
    while i!=0:
        country = random.choice(s)
        famous = random.choice(x[country])
        randomInt = random.randint(0, 100)
        randomFloat = random.uniform(0,100)
        randomChar = random.choice('q%#F$*AS)_w(DG@er^!+t&yH~-=')
        trip = (randomInt, randomFloat, randomChar,country + ": [" + famous + "]")
        yield trip
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