# -*- coding: utf-8 -*-
import pymongo
import pandas
import numpy as np
import matplotlib.pyplot as pl
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['gaoyl']
mycol = mydb["Gaoyl"]
data = pandas.DataFrame(list(mycol.find()))
print(data)
m = np.arange(0,100000)
n = data['整型']
pic = pl.figure(figsize=(35,25))
ax = pic.add_subplot(111)
ax.set_title('整型')
ax.scatter(m,n,marker='x')
pl.show()
