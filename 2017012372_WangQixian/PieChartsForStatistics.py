#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 17:09:10 2019

@author: stefan
"""
import pymongo
import pandas as pd
from matplotlib import pyplot as plt


#链接本地数据库服务
client = pymongo.MongoClient('127.0.0.1', 27017)
#创建
db = client['wqx_db']
#集合
mumbers = db.mumbers
table = mumbers
# 读取数据
data = pd.DataFrame(list(table.find()))
randomInt = data['整型']
a = 0
b = 0
c = 0
d = 0
e = 0
i = 0
while i<100000:
    if 0 < randomInt[i] <= 20:
        a = a + 1
    if 20 < randomInt[i] <= 40:
        b = b + 1
    if 40 < randomInt[i] <= 60:
        c = c + 1
    if 60 < randomInt[i] <= 80:
        d = d + 1
    if 80 < randomInt[i] <= 100:
        e = e + 1
    i = i+1
sizes = [a, b, c, d, e]
# 打印输出
# 调节图形大小，宽，高
plt.figure(figsize=(6, 9))
# 定义饼状图的标签，标签是列表
labels = [u'0-20', u'20-40', u'40-60', u'60-80', u'80-100']
# 每个标签占多大，会自动去算百分比

colors = ['pink', 'yellow', 'blue', 'green', 'red']
# 将某部分爆炸出来， 使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
explode = (0.05, 0, 0)

patches, l_text, p_text = plt.pie(sizes, labels=labels, colors=colors,
                                  labeldistance=1.1, autopct='%3.1f%%', shadow=False,
                                  startangle=90, pctdistance=0.6)

# labeldistance，1.1指1.1倍半径的位置
# autopct，文本格式
# shadow 阴影
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
print(sizes)