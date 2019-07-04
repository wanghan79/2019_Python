#随机生成整型、浮点型、字符串、字典
#导入MongoDB
#统计整型数据的分布情况
import string
import random
from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

#1.链接本地数据库服务
name = MongoClient('localhost')
#2.链接本地数据库 demo 没有会创建
db = name.number   #demo数据库名
#3.创建，连接集合
emp = db.random  #集合名字
emp.remove(None)

def Random(i):
    cout=0
    while i!=0:
        cout+=1
        num=random.randint(1,10)
        ran_str =  ''.join(random.sample(string.ascii_letters + string.digits,num))
        unif=random.uniform(1,10)
        rand=random.randint(1,100000)
        key=random.choice(string.ascii_letters)
        dict1={key:unif}
        dict2={key:rand}
        dict3={key:ran_str}
        cout1=(str(cout)+':')
        tup1 = (cout1,ran_str,unif,rand,dict1,dict2,dict3)
        yield tup1
        randomNumber = {
            '序号':cout,
            '整型': rand,
            '浮点数':unif,
            '字符': ran_str,
            '字典1': dict1,
            '字典2':dict2,
            '字典3':dict3
        }
        emp.insert_one(randomNumber)
        i= i - 1
    return 'done'
g = Random(100000)
f = open("out.txt", "w", encoding="utf-8")
while True :
    try:
        y = next(g)
        print(y, file = f)
    except StopIteration as e:
        print(e.value)
        break
f.close()
#绘图 柱状图（整型范围数量）
x=np.arange(1,100001)
data = pd.DataFrame(list(emp.find()))
y=data['整型']
#print(y)
fig = plt.figure()
#plt.scatter(x,y,c='r',marker='s')
#plt.show()
a_0=0
a_1=0
a_2=0
a_3=0
a_4=0
a_5=0
a_6=0
a_7=0
a_8=0
a_9=0
for i in y:
    if 0<=i<10000:
        a_0+=1
    if 10000<=i<20000:
        a_1+=1
    if 20000<=i<30000:
        a_2+=1
    if 30000<=i<40000:
        a_3+=1
    if 40000<=i<50000:
        a_4+=1
    if 50000<=i<60000:
        a_5+=1
    if 60000<=i<70000:
        a_6+=1
    if 70000<=i<80000:
        a_7+=1
    if 80000<=i<90000:
        a_8+=1
    if 90000<=i<100000:
        a_9+=1
X=[0,1,2,3,4,5,6,7,8,9]
Y=[a_0,a_1,a_2,a_3,a_4,a_5,a_6,a_7,a_8,a_9]
plt.bar(X,Y,0.4,color="red")
plt.xlabel("distribution/ten thousand")
plt.ylabel("number")
plt.title("Integer random number distribution")
plt.grid=True
plt.show()
