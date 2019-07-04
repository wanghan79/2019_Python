#由于100000个点太多，图像是铺满了画布的
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

# 选择需要显示的字段
y = data['整型']
z = data['浮点数']


fig = plt.figure()  
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.set_title('Scatter int') 
ax2.set_title('Scatter folat')
ax1.scatter(x,y,c = 'r',marker = 'o')
ax2.scatter(x,z,c = 'b',marker = 's')
# 打印输出
#f=open("out.txt","w")
#for i in table.find():
 #   print(i,file=f)
#f.close()
#print(data1)
plt.show()