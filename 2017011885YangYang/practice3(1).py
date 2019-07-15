"""
@author:杨洋
"""
import numpy as np
import pymongo
import pandas as pd
import matplotlib.pyplot as plt
client = pymongo.MongoClient(host='localhost', port=27017) #连接MongoDB
db = client['my_db']
table = db['my_collection']

class Matplot:
        #取数据
        data = pd.DataFrame(list(table.find()))
        x = data['int'] # 产生x坐标
        y = data['float'] # 产生y坐标
        area = np.pi * (5 * np.random.rand(50))**2  # 点的半径范围:0~5 
        # 绘制散点图,点的形状为圆圈
        plt.scatter(x, y, s=area, alpha=0.3, marker='o')
        plt.show()
