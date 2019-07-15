import pymongo
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import random

# 连接数据库
client = pymongo.MongoClient('localhost', 27017)
db = client['Xiag']
table = db['Information']
data = pd.DataFrame(list(table.find()))
y = data['Int']

fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111)
x=np.arange(1,100001)
ax.scatter(x,y,c='blue')
ax.legend('整形数的可视化')
ax.grid(True)
plt.show()