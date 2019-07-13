import pymongo
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np 
import random

# 连接数据库
client = pymongo.MongoClient('localhost', 27017)
db = client['xcnhr']
table = db['mydb']
# 读取数据
data = pd.DataFrame(list(table.find()))
# 选择需要统计的字段
y = data['整型']



fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111)
x=np.arange(1,100001) 
ax.scatter(x,y,c='green')
ax.legend('int') 
ax.grid(True)
plt.show()