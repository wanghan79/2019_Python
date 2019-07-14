import pymongo
import matplotlib.pyplot as plt
import numpy as np


#连接数据库
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["database"]
mycol = mydb["RandomNumbers"]

x=np.arange(1,100001)
y=np.loadtxt('data.txt',delimiter=',',usecols=1,unpack=False)
plt.scatter(x,y,marker='o',s=1,alpha=0.5)
plt.show()
