#!/usr/bin/python
# -*-coding:UTF-8-*-
"""
姓名：沈萌
学号：2017011959
"""

import pymongo
import os
import re
import bar
import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import threading
import colorsys

"""
数据库初始化：
在MongoDB中，定义一个数据库，名为‘simon_db’，其中有collection名为students
"""
client = pymongo.MongoClient('127.0.0.1', 27017)
db = client['simon_db']
collection = db['students']

"""
定义一个可视化的类，实现从mongodb中取出数据分别进行散点图可视化和饼图可视化
"""
class visual():

    """
    功能：取出mongodb中height和weight进行散点图可视化
    """
    def scatter_plot_visual():
        plt.figure(figsize = (6,6))
        i = 0
        for x in collection.find({},{"_id":0,"simon":1}):
            i += 1
            plt.scatter((eval(x['simon']))['weight'], (eval(x['simon']))['height'])
            plt.xlabel('weight')
            plt.ylabel('heightix')
            #if i == 100000: 取部分，因为我电脑跑不了100000条这样的二维数据...T_T...
            if i == 5000:
                plt.show()
                break

    """
    功能：取出mongodb中height进行饼图可视化
    """
    def pie_plot_visual():
        plt.figure(figsize = (6,6))
        plt.axes(aspect = 'equal')
        plt.rcParams['font.sans-serif']
        '''
        定义饼图的标签
        '''
        height1 = 0
        height2 = 0
        height3 = 0
        label = ['身高120-150','身高151-180','身高181-220']
        i = 0
        for x in collection.find({},{"_id":0,"simon":1}):
            i += 1
            if (((eval(x['simon']))['height'] >= 120.00) & ((eval(x['simon']))['height'] <= 150.00)):
                height1 += 1
            elif (((eval(x['simon']))['height'] >= 151.00) &((eval(x['simon']))['height'] <=180.00)):
                height2 += 1
            else:
                height3 += 1

            if(i == 100000):
                break

        sizes = [height1, height2, height3]
        colors = ['green', 'blue', 'red']
        explode = (0.05, 0.05, 0.05)
        plt.pie(sizes, explode = explode, labels = label, colors = colors, autopct = '%1.1f%%', startangle = 50)

        plt.axis('equal')
        plt.show()




if __name__ == '__main__':
    visual.scatter_plot_visual()
    visual.pie_plot_visual()

