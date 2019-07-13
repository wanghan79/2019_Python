#!/usr/bin/env python

import random
import string
import decimal
from pymongo import MongoClient
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


name = MongoClient('localhost')
db = name.hehc
emp = db.mydb
emp.remove(None)

def string_generation(size=6,chars=string.ascii_uppercase+string.digits):
                return "".join(random.choice(chars) for _ in range(size))

                      
def dictionary_generation(n=100000):

                for i in range(n):
                        int_res = random.randint(0,100000)
                        float_res = round(random.uniform(0,1000),2) #保留两位浮点数
                        string_res =string_generation();
                        res = { 'credit_card_number':int_res,'money':float_res,'password':string_res}
                        yield res
                        emp.insert_one(res)
file = open("output.txt","w", encoding="utf-8")
for res in dictionary_generation():
          file.write(str(res)+'\n')
file.close()

  # 连接数据库
client = pymongo.MongoClient('localhost',27017)
db = client['hehc']
table = db['mydb']
                             
 # 读取数据
data = pd.DataFrame(list(table.find()))
                             
#选择需要统计的字段
y = data['credit_card_number']


                             
fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111)
x = np.arange(0,100000)
ax.scatter(x,y,c='blue')
ax.legend('credit_card_number')
ax.grid(True)
plt.show()
