# -*- coding: utf-8 -*-
"""
@author:杨洋
"""

import random
import pymongo 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

stuInfo = {"student"+str(i):random.randint(60,100) for i in range(20)}


for i in range(100000):        #生成随机数，浮点类型
    a = random.uniform(10, 30)     #控制随机数的精度round(数值，精度)
    b = random.randint(1, 100)
    c= random.choice(['sdfdfd', 'dfdf', 'sdf','dfjie','fefe','fkeofke','foef','fjijf','iejfi'])
    print(str(round(a,4))+'  '+str(b) +'  ' +str(c) +"  "+ " cat" +str(i) )
    stuInfo = {"student"+str(i):random.randint(60,100) for i in range(2)}
    print({name:score for name,score in stuInfo.items() })##生成字典


client = pymongo.MongoClient(host='localhost', port=27017) 
db = client['my_db']
collection = db['my_collection']
count = 0
while (count < 9999):
        a = random.uniform(10, 30)     #控制随机数的精度round(数值，精度)
        b = random.randint(1, 100)
        c= random.choice(['sdfdfd', 'dfdf', 'sdf','dfjie','fefe','fkeofke','foef','fjijf','iejfi']) 
        stuInfo = {"student"+str(i):random.randint(60,100) for i in range(1)}
        randomNumber = {
                        'num':count,
                        'int': a,
                        'float':b,
                        'string': c,
                        'dict': stuInfo
                    }
        result = collection.insert_one(randomNumber)     #插入
        count = count + 1
results = collection.find({'string': 'dfdf'})  #查询符合条件的数据
print(results)  
for result in results:  
    print(result) 


class Matplot:
        #取数据
        data = pd.DataFrame(list(table.find()))
        x = data['int'] # 产生x坐标
        y = data['float'] # 产生y坐标
        area = np.pi * (5 * np.random.rand(50))**2  # 点的半径范围:0~5 
        # 绘制散点图,点的形状为圈圈
        plt.scatter(x, y, s=area, alpha=0.3, marker='o')
        plt.show()