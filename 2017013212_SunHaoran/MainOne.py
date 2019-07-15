import matplotlib.pyplot as plt
import numpy as np
from pymongo import MongoClient
from RandomGenera import Generator
from DataMongo import mongodb
from MatplotScat import matplot
'''
   @ 2017013212孙浩然
'''
def themain():
	print("just wait please...")
def ending():
	mongodb.deletes()#清空数据
        

'''
文件运行时显示scatter窗口
'''
if __name__ == '__main__':

 themain()   
 mongodb.store()
 matplot.scatter()

 ending()
