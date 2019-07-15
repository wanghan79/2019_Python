import matplotlib.pyplot as plt
import numpy as np
import pylab
from pymongo import MongoClient
'''
   @ 2017013212孙浩然
'''

class matplot():
    def scatter():
      myclient = MongoClient("mongodb://localhost:27017/")
      db_name='jesus'
      col_name='holly'
      mydb = myclient[db_name]
      mycol = mydb[col_name]
      x1=[]
      y1=[]
      for x in mycol.find({}, { "int": 1}).limit(50000):
            x1.append(x["int"])
      for y in mycol.find({}, {"int": 1}).limit(50000).skip(50000):
            y1.append(y["int"])
      pylab.scatter(x1, y1,c=y1)
      pylab.show() 


if __name__ == '__main__':
    matplot.scatter()

