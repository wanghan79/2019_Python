# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:54:39 2019

@author: ASUS
"""

import pymongo
import matplotlib.pyplot as plt
import numpy as np

''' 
2017013518
author: lixiaolin
'''

#连接数据库
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb=myclient['python_data']
col=mydb['sst']

x=np.arange(100001,200001)
y=np.loadtxt('output.txt',delimiter=',',usecols=1,unpack=False)
plt.bar(x,y)
plt.show()
