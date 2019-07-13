# -*- coding: utf-8 -*-

'''
姓名:杨洋
学号：2017011885
'''



import numpy as np
import matplotlib.pyplot as plt
import pymongo

#coding:utf-8

client = pymongo.MongoClient('localhost', 27017)
db = client['RandomData']#指定数据库
table = db['RandomData']

# 读取数据
data = pd.DataFrame(list(table.find()))

#显示的数据
N = 1000
x = np.random.randn(N)
y = np.random.randn(N)
plt.scatter(x, y,alpha=0.5,edgecolors= 'white')
plt.show()