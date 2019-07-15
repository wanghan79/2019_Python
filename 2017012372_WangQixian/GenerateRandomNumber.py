#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 17:08:17 2019

@author: stefan
"""

#生成随机数据100000条在txt文件中显示，存储到MongoDB中并且统计了整型数据，绘制成饼状图
import random
import pymongo
from matplotlib import pyplot as plt
import numpy as np

#链接本地数据库服务
client = pymongo.MongoClient('127.0.0.1', 27017)
#创建
db = client['wqx_db']
#集合
mumbers = db.mumbers
table = mumbers
#emp.delete_one(None)
x={'中国':['习近平','毛泽东','周恩来','朱德','江泽民'],
   '美国':['华盛顿','奥巴马','克林顿','华莱士'],
   '日本':['苍老师','小泽玛利亚','大桥未久','吉泽明步','秦泽多摩雄'],
   '韩国':['金正恩','李敏镐','BigBang','朴泰桓']}
s=list(x.keys())

a = 0
b = 0
c = 0
d = 0
e = 0

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
        
        global a
        global b
        global c
        global d
        global e
        
        if 0 < randomInt <= 20:
             a = a+1
        if 20 < randomInt <= 40:
            b = b+1
        if 40 < randomInt <= 60:
            c = c+1
        if 60 < randomInt <= 80:
            d = d+1
        if 80 < randomInt <= 100:
            e = e+1
        sizes = [a,b,c,d,e]
        #将生成的数据通过增加语句存到数据库里
        mumbers.insert_one(randomNumber)

        i = i-1
    # 调节图形大小，宽，高
    plt.figure(figsize=(6, 9))
    # 定义饼状图的标签，标签是列表
    labels = [u'0-20', u'20-40', u'40-60', u'60-80', u'80-100']
    # 每个标签占多大，会自动去算百分比

    colors = ['pink', 'yellow', 'blue', 'green', 'red']
    # 将某部分爆炸出来， 使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
    explode = (0.01, 1, 0)

    patches, l_text, p_text = plt.pie(sizes, labels=labels, colors=colors,
                                      labeldistance=1.1, autopct='%3.1f%%', shadow=False,
                                      startangle=90, pctdistance=0.6)

    # labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
    # autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
    # shadow，饼是否有阴影
    # startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
    # pctdistance，百分比的text离圆心的距离
    # patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本

    # 改变文本的大小
    # 方法是把每一个text遍历。调用set_size方法设置它的属性
    for t in l_text:
        t.set_size = (30)
    for t in p_text:
        t.set_size = (20)
    # 设置x，y轴刻度一致，这样饼图才能是圆的
    plt.axis('equal')
    plt.legend()
    plt.show()

    return sizes
g = CreateRandomNumber(100000)


f = open("out.txt", "w", encoding="utf-8")
while True :
    try:
        y = next(g)
        print(y, file = f)
    except StopIteration as e:
        print(e.value)
        break
f.close()
