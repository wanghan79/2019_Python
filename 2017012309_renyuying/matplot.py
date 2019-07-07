'''
任雨莹
2017012309
matplot可视化显示，散点图
'''
import  matplotlib.pyplot as plt
import  numpy as np
import  pandas as pd
import  pymongo
np.random.seed(0)

#建立MongoDB数据库连接
client = pymongo.MongoClient('localhost',27017)

#连接所需数据库,rand为数据库名
db = client['rand']
table = db['rand']

# 读取数据
data = pd.DataFrame(list(table.find()))

# 选择需要显示的字段
x = data['整数']
y = data['浮点数']
plt.scatter(x, y, c ='b')
plt.show()

