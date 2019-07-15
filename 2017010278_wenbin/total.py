import pymongo
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import random
from pymongo import MongoClient

a={'鱼类':['青鱼','草鱼','鲤鱼','鲫鱼'],
   '兽类':['虎','狼','象','马','鹿'],
   '鸟类':['鸡','鸭','鹅'],
   '两栖':['青蛙','龟','娃娃鱼','蛇','鳄鱼']
   }
l=list(a.keys())

client=pymongo.MongoClient('localhost',27017)#连接数据库
dblist=client['firstpy']#数据库名
dongwu=dblist.dongwu#集合名

def generaterandom(size):
    while size>0:
        randomint=random.randint(0,100)
        randomfloat=random.random()
        randomchar=random.choice('asdfghjQWERZXC!@#$%^&')
        door=random.choice(l)
        animal=random.choice(a[door])
        temp=(randomint,randomfloat,randomchar,door+'['+animal+']')
        yield temp
        randnum={
            '整数':randomint,
            '浮点数':randomfloat,
            '字符':randomchar,
            '门':door,
            "动物":animal
        }
        dongwu.insert_one(randnum)
        size=size-1
if __name__ == '__main__':
    file = open("out.txt", "w")
    for data in generaterandom(100000):
        file.write(str(data)+'\n')
    file.close()

data=pd.DataFrame(list(dongwu.find()))
y=data['整数']
x=data['浮点数']
fig=plt.figure(figsize=(5,5))
ax=fig.add_subplot(111)
plt.xlabel('X')
plt.ylabel('Y')
ax.scatter(x,y,c='green')
ax.legend=('x1')
ax.grid(True)
plt.show()