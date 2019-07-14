import pymongo
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from pymongo import MongoClient
import random

"""
连接数据库，引入数据
"""
client=pymongo.MongoClient('localhost',27017)
dblist=client['firstpy']
dongwu=dblist.dongwu
data=pd.DataFrame(list(dongwu.find()))

"""
统计整数和浮点数
"""
y=data['整数']
x=data['浮点数']
fig=plt.figure(figsize=(5,5))
ax=fig.add_subplot(111)
plt.xlabel('X')
plt.ylabel('Y')
ax.scatter(x,y,c='green')
ax.legend=('X1')
ax.grid(True)
plt.show()