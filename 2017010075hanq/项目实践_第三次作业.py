
import pymongo
import pandas as pd
import numpy as num  
import matplotlib.pyplot as pl 

m = num.arange(1,100001)
client = pymongo.MongoClient('localhost', 27017)
hq = client['random_num']
table = hq['myrandom']

data = pd.DataFrame(list(table.find()))

n = data['整型']


fig = pl.figure()  
ax = fig.add_subplot(111)
ax.set_title('Scatter int') 
ax.scatter(m,n,c = 'g',marker = 'o')
pl.show()