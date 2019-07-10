import pymongo
import matplotlib.pyplot as plt
import numpy as np

''' 
功能：画散点图，各点为每条数据的整数部分
作者：高晓雨2017012834
日期：2019年7月
'''

#连接数据库
myclient=pymongo.MongoClient("mongodb://localhost:27017")
mydb=myclient["runoobdb"]
mycol=mydb["sites"]

x=np.arange(1,100001)
y=np.loadtxt('data.txt',delimiter=',',usecols=1,unpack=False)
plt.scatter(x,y,marker='o',s=1,alpha=0.5)
plt.show()