import string
import random
import pymongo
from GenData import DataGenerate
import matplotlib.pyplot as plt
import numpy as np

'''
   功能：三次作业总结
   作者：高晓雨2017012834
   日期：2019年7月
'''

class DataGenerate:
    def dgenerate(size=100000):
        for i in range(size):
            dic = {}
            value=random.randint(1, 10000)
            key=''.join(random.sample(tuple(string.ascii_lowercase + string.digits), 10))
            dic[key]=value
            data=(random.randint(1, 10000),round(random.uniform(1, 1000), 5),
                ''.join(random.sample(tuple(string.ascii_lowercase + string.digits), 10)),dic)
            yield data
if __name__ == '__main__':
    f = open("data.txt", "w")
    for i in DataGenerate.dgenerate():
        s=str(i)
        f.write(s+'\n')
    f.close()

i=0
myclient=pymongo.MongoClient("mongodb://localhost:27017")
mydb=myclient["runoobdb"]
mycol=mydb["sites"]
for n in DataGenerate.dgenerate():
    i=i+1
    mydict={'id':i,'content':n}
    x=mycol.insert_one(mydict)

x=np.arange(1,100001)
y=np.loadtxt('data.txt',delimiter=',',usecols=1,unpack=False)
plt.scatter(x,y,marker='o',s=1,alpha=0.5)
plt.show()



