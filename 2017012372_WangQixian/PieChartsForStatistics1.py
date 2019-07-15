#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 08:49:52 2019

@author: stefan
"""


  
from matplotlib import pyplot as plt
import pymongo
import pandas as pd
import numpy
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码

#链接本地数据库服务
client = pymongo.MongoClient('127.0.0.1', 27017)
#创建
db = client['wqx_db']
#集合
mumbers = db.mumbers
table = mumbers
class Matplot:
        #取数据
        data = pd.DataFrame(list(table.find()))
        x = data['整型'] # 产生x坐标
        y = data['浮点数'] # 产生y坐标
        area = numpy.pi * (5 * numpy.random.rand(50))**2  # 点的半径范围:0~5 
        # 绘制散点图
        plt.scatter(x, y, s=area, alpha=0.3, marker='o')
        plt.show()