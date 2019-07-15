# -*- coding: utf-8 -*-
import pymongo
import pandas
import random
import string
import numpy as np
import matplotlib.pyplot as pl
def Generate_data(size=100000):
    for i in range(size):
        dic = {}
        data = {}
        data['整型'] = random.randint(0, 100000)
        data['浮点'] = random.uniform(0, 1000)
        data['字符串'] = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        dic["".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))] = "".join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(9))
        data['字典'] = dic
        yield data
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['gaoyl']
mycol = mydb["Gaoyl"]
for data in Generate_data():
    mycol.insert_one(data)
    print(data)
data_db = pandas.DataFrame(list(mycol.find()))
print(data_db)
m = np.arange(0,100000)
n = data_db['整型']
pic = pl.figure(figsize=(35,25))
ax = pic.add_subplot(111)
ax.set_title('整型')
ax.scatter(m,n,marker='x')
pl.show()