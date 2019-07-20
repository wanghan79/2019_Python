# 导入相关模块
import pymongo
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib as mpl

# 连接数据库
client = pymongo.MongoClient('localhost', 12345)
db = client['maojitian']
table = db['data']
# 读取数据
data = pd.DataFrame(list(table.find()))
print(data)
#用matplotlib来画出箱型图
list1=[]
list1=data['doublenumber']
count=0;
count1=0;
count2=0;
for item in list1:
    if float(item)>=6.7:
        count=count+1;
    if float(item)<6.7 and float(item)>=3.3:
        count1=count1+1;
    if float(item)<3.3:
        count2=count2+1;
name_list = ['low 3.3', 'between', 'high  6.7']
num_list = [count2,count1,count]
plt.barh(range(len(num_list)), num_list, tick_label=name_list)
plt.show()