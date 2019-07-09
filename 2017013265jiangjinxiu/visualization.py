# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 09:35:01 2019

@author: hp
"""
import matplotlib.pyplot as plt
import numpy as np
from pymongo import MongoClient
#from run_mongo import build
#绘制的是饼图，10万数据中int分成4段。小于500，大于400小于1000，大于1000小于1500，大于1500小于2000
class matplot():
    def picture():
        k1=k2=k3=k4=0
        myclient = MongoClient("mongodb://localhost:27017/")
        mydb=myclient['python_data']
        col=mydb['sst']
        for x in col.find({},{ "int": 1 }):
            #print(x)
            if x["int"]<500:
                k1=k1+1
            elif  500<=x["int"]<1000:
                k2=k2+1
            elif  1000<=x["int"]<1500:
                k3=k3+1
            else:
                k4=k4+1
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'x<500', '500<=x<1000', '1000<=x<1500', 'x>=1500'
        sizes = [k1, k2, k3, k4]
        explode = (0.1,0.05, 0.05, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
        
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.5f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        
        plt.show()
if __name__ == '__main__':
    matplot.picture()
    