#100000个点太多
#此处截图部分
# 导入相关模块
import pymongo
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt 

x = np.arange(1,100001)
# 连接数据库
client = pymongo.MongoClient('localhost', 27017)
db = client['random_number']
table = db['myrandom']

# 读取数据
data = pd.DataFrame(list(table.find()))
y = data['整型']
z = data['浮点数']


fig = plt.figure()  
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.set_title('Scatter int') 
ax2.set_title('Scatter folat')
ax1.scatter(x,y,c = 'g',marker = 'o')
ax2.scatter(x,z,c = 'b',marker = 'x')
plt.show()
)