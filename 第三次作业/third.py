import pymongo
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt 

# 连接数据库
client = pymongo.MongoClient('localhost', 27017)
db = client['RandomNumber']
table = db['myrandom']

# 读取数据
data = pd.DataFrame(list(table.find()))

# 选择需要显示的字段
y = data['int']
z = data['float']

fig = plt.figure()  
ax1 = fig.add_subplot(111)
ax1.set_title('Scatter int') 
ax1.scatter(z,y,c = 'b',marker = 'o')

plt.show()