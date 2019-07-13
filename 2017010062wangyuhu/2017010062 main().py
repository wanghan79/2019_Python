# -*- coding: utf-8 -*-
import pymongo
from data_generation import DataGeneration
from data_to_mongoDB import DataStorage
from data_visualization import DataVisualization

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["random_data"]
dblist = myclient.list_database_names()
mysites = mydb["mysites"]


DG = DataGeneration()
DS = DataStorage()
DV = DataVisualization()

DG.data_generation('output.txt', 100000)  # 生成100000条随机数据并存入output.txt
DS.random_data_storage(mysites, 'output.txt')  # 从output.txt中读取数据并存入mongoDB

data = list(mysites.find())
batch_size = 50  # 为方便显示选取前50个数据
x, y1, y2 = [], [], []
for i in range(batch_size):
    x.append(data[i]['_id'])
    y1.append(data[i]['random_int'])
    y2.append(data[i]['random_float'])

# 可视化图像绘制
DV.draw_plot(x, y1, y2, 'random_int')
DV.draw_plot(x, y1, y2, 'random_float')
DV.draw_plot(x, y1, y2, 'both')
DV.draw_bar(x, y1, y2, 'random_int', 'vertical')
DV.draw_bar(x, y1, y2, 'random_int', 'horizontal')
DV.draw_bar(x, y1, y2, 'random_float', 'vertical')
DV.draw_bar(x, y1, y2, 'random_float', 'horizontal')
DV.draw_pie(data, batch_size)
DV.draw_hist(y1, y2, 'random_int')
DV.draw_hist(y1, y2, 'random_float')
DV.draw_scatter(x, y1, y2, 'random_int')
DV.draw_scatter(x, y1, y2, 'random_float')
