import pymongo
import pandas as pd
import numpy as np
import matplotlib.pyplot as pl

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['liqi_data']
mycol = mydb["liqi_data"]
data = pd.DataFrame(list(mycol.find()))
m = np.arange(0,100000)
n = data['data_int']
fig = pl.figure(figsize=(40,20))
ax = fig.add_subplot(111)
ax.set_title('Scatter int')
ax.scatter(m,n,marker='o',s=3,alpha=1)
pl.show()
