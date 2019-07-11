import string
import random
from pymongo import MongoClient
import pymongo
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np 


#1.链接本地数据库服务
name = MongoClient('localhost')
#2.链接本地数据库 demo 没有会创建
db = name.xcnhr  #demo数据库名
#3.创建，连接集合
emp = db.mydb #集合名字
emp.remove(None)

def generateRandomNumber(i):
    while i!=0:
        randomInt=random.randint(1,50)
        randomFloat=random.random()
        randomChar=random.choice('hhcsbxiaguosbfhdjfdjfdshfdkjfkjfdfjkfkjhfdskjfdioefiofeiifeiofiiefsiojfseioj')
        randomStr=''.join(random.sample(string.ascii_letters + string.digits,random.randint(1,10)))
        dict={str(randomInt):randomStr}
        tup1=(randomInt,randomFloat,randomChar,randomStr,dict)
        yield tup1
        randomNumber = {
            '整型': randomInt,
            '浮点数':randomFloat,
            '字符': randomChar,
            '字典': dict,
            '字符串':randomStr
        }
        emp.insert_one(randomNumber)
        i= i - 1
    return 'done'
g = generateRandomNumber(100)
f = open("xcnhr.txt", "w", encoding="utf-8")
while True :
    try:
        y = next(g)
        print(y, file = f)
    except StopIteration as e:
        print(e.value)
        break
f.close()
#for i in emp.find():
 # print(i)
 emp = db['mydb']
# 读取数据
y = data['整型']
# 选择需要统计的字段



fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111)
x=np.arange(1,100001) 
ax.scatter(x,y,c='green')
ax.legend('int') 
ax.grid(True)
plt.show()


