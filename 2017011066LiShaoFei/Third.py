from matplotlib import pyplot as plt
import pymongo
import pandas as pd
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码

#链接数据库
client = pymongo.MongoClient('localhost',27017)
db = client['flyzer']
flyzertable = db['table']


#查找数据库中表格里的数据并赋值给X与Y
data = pd.DataFrame(list(flyzertable.find()))
x=data['intX']
y=data['intY']


#画出散点图
fig = plt.figure(figsize=(4, 4))
scmap = fig.add_subplot(111)
scmap.scatter(x, y, c='yellow')
scmap.legend('X与Y的关系图')
scmap.grid(True)
plt.show()