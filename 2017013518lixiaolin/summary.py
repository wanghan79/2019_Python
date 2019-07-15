# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 16:51:37 2019

@author: ASUS
"""

import random
import string
class Generate:
    def dic(self):
        dict={}
        u=''.join(random.sample(string.ascii_lowercase, 5))
        #返回包含所有小写字母在内的字符串
        v=''.join(random.sample(string.ascii_letters + string.digits, 6))  
        #返回包括所有字母在内的大小写字符串和0-9数字字符串
        dict[u]=v#生成字典
        return dict
    def string(self):
        s=''.join(random.sample(string.ascii_letters,6))
        #生成字符串
        return s
    def data_crecte(self,size=100000):
        data={}
        for i in range(size):
          data["int"]=random.randint(0,2000)
          #生成0-2000的随机整数
          data["float"]=random.uniform(3000,5000)
          data["dic"]=self.dic()
          data["string"]=self.string()
          #生成的字典包含整形，浮点，字符串，字典
          yield data#生成数据
if __name__ == '__main__':
    f = open("output.txt", "w")
    for i in Generate().data_crecte():
       s=str(i)
       f.write(s+'\n')
    f.close()
    import pymongo 
from GenData import DataGenerate  
i=0 
myclient=pymongo.MongoClient("mongodb://localhost:27017") 
mydb=myclient["runoobdb"] 
mycol=mydb["sites"] 
for n in DataGenerate.dgenerate(): 
    i=i+1 
    mydict={'id':i,'content':n} 
    x=mycol.insert_one(mydict) 
    print(x) 
    
import pymongo
import matplotlib.pyplot as plt
import numpy as np
#连接数据库
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb=myclient['python_data']
col=mydb['sst']
x=np.arange(100001,200001)
y=np.loadtxt('output.txt',delimiter=',',usecols=1,unpack=False)
plt.bar(x,y)
plt.show()
