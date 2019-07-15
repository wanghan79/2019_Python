import string
import random
import pymongo
import matplotlib.pyplot as plt
import numpy as np

#生成随机数
class Generator:
    def dataGenerate():
        size=100000
        for i in range(size):
            dic = {}
            value=random.randint(1, 10000)
            key=''.join(random.sample(tuple(string.ascii_lowercase + string.digits), 10))
            dic[key]=value
            data=(random.randint(1, 10000),round(random.uniform(1, 1000), 5),
                ''.join(random.sample(tuple(string.ascii_lowercase + string.digits), 10)),dic)
            yield data

          
generator=Generator

f = open("data.txt", "w")
for i in generator.dataGenerate():
    s=str(i)
    f.write(s+'\n')
f.close()

#连接数据库   
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["database"]
mycol = mydb["randomNumbers"]

x =mycol.delete_many({})
i=0
for n in generator.dataGenerate():
    i=i+1
    mydict={'_id':i,'content':n}
    x=mycol.insert_one(mydict)

#绘图
x=np.arange(1,100001)
y=np.loadtxt('data.txt',delimiter=',',usecols=1,unpack=False)
plt.scatter(x,y,marker='o',s=1,alpha=0.5)
plt.show()
