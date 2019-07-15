import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 制作数据
from numpy import array
from numpy.random import normal

def getData():
    heights=[]
    weights=[]
    books=[]
    N=100000
    for i in range(N):
        while True:
            #身高服从均值为172，标准差为6的正态分布
            height=normal(172,6)
            if 0<height:
                break
        while True:
            #体重由身高作为自变量的线性回归模型产生，误差服从标准正态分布
            weight=(height-80)*0.7+normal(0,1)
            if 0<weight:
                break
        while True:
            #借阅量服从均值为20，标准差为5的正态分布
            number=normal(20,5)
            if 0<=number and number<=50:
                book='E' if number<10 else ('D' if number<15 else ('C' if number<20 else ('B' if number<25 else 'A')))
                break
        heights.append(height)
        weights.append(weight)
        books.append(book)
   return array(heights),array(weights),array(books)
heights,weights,books=getData()

from matplotlib import pyplot

#绘制柱状图
def drawBar(books):
    xticks=['A','B','C','D','E']
    bookGroup={}
    #对每一类借阅量进行频数统计
    for book in books:
        bookGroup[book]=bookGroup.get(book,0)+1
    #创建柱状图
    pyplot.bar(range(5),[bookGroup.get(xtick,0) for xtick in xticks],align='center') 
    #设置柱的文字说明
    pyplot.xticks(range(5),xticks)
    pyplot.xlabel("Types of Students")
    pyplot.ylabel("Frequency")
    pyplot.title("Numbers of Books Students Read")
    #绘图
    pyplot.show()
drawBar(books)

#绘制饼形图
def drawPie(books):
    labels=['A','B','C','D','E']
    bookGroup={}
    for book in books:
        bookGroup[book]=bookGroup.get(book,0)+1
    pyplot.pie([bookGroup.get(label,0) for label in labels],labels=labels,autopct='%1.1f%%')
    pyplot.title("Number of Books Students Read")
    pyplot.show()
drawPie(books)

#绘制直方图
def drawHist(heights):
    pyplot.hist(heights,100)
    pyplot.xlabel('Heights')
    pyplot.ylabel('Frequency')
    pyplot.title('Height of Students')
    pyplot.show()
drawHist(heights)

#绘制累积曲线
def drawCumulativaHist(heights):
    pyplot.hist(heights,20,normed=True,histtype='step',cumulative=True)
    pyplot.xlabel('Heights')
    pyplot.ylabel('Frequency')
    pyplot.title('Heights of Students')
    pyplot.show()
drawCumulativaHist(heights)

#绘制散点图
def drawScatter(heights,weights):
    pyplot.scatter(heights,weights)
    pyplot.xlabel('Heights')
    pyplot.ylabel('Weight')
    pyplot.title('Heights & Weight of Students')
    pyplot.show()
drawScatter(heights,weights)

#绘制箱型图
def drawBox(heights):
    pyplot.boxplot([heights],labels=['Heights'])
    pyplot.title('Heights of Students')
    pyplot.show()
drawBox(heights)
