import pymongo
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import random

client = pymongo.MongoClient('localhost',27017)
db = client['hehc']
table = db['mydb']
                             
data = pd.DataFrame(list(table.find()))
                             

y = data['credit_card_number']


                             
fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111)
x = np.arange(1,100001)
ax.scatter(x,y,c='blue')
ax.legend('credit_card_number')
ax.grid(True)
plt.show()
