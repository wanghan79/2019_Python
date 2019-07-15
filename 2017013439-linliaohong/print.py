import pymongo
import matplotlib.pyplot as plt
import numpy as np
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]
x = np.arange(1, 100001)
y = np.loadtxt('data.txt', delimiter=',', usecols=1, unpack=False)
plt.scatter(x, y, marker='o', s=1, alpha=0.5)
plt.savefig('scatter.png')
plt.show()