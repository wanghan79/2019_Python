import numpy as np
import pymongo
import random
import pandas as pd
import matplotlib.pyplot as plt

#连接MongoDB
client = pymongo.MongoClient()
db = client['my_db']
table = db['my_collection']

class Matplot:
        #取整张表的数据
        data = pd.DataFrame(list(table.find()))
        x = data['整型'] # 产生x坐标
        y = data['浮点型'] # 产生y坐标
        area = np.pi * (15 * np.random.rand(50))**2  # 点的半径范围:0~15 
        # 绘制散点图,点的形状为星星
        plt.scatter(x, y, s=area, alpha=0.5, marker='*')
        plt.show()

