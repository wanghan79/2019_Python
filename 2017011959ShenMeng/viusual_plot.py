#!/usr/bin/python
# -*-coding:UTF-8-*-
"""
姓名：沈萌
学号：2017011959
"""

import matplotlib
import matplotlib.pyplot as plt
from numpy import *
import numpy as np

"""
功能：将visual_data.txt中数据转换为矩阵进行可视化
"""
def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())
    returnMat = zeros((numberOfLines,2))
    classLabelVector = []
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        #用空格分开数据
        listFromLine = line.split(' ')
        returnMat[index,:] = listFromLine[0:2]
        classLabelVector.append(int(float(listFromLine[-1])))
        index += 1
    return returnMat,classLabelVector


datingDataMat,datingLabels=file2matrix('visual_data.txt')
fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(datingDataMat[:,0], datingDataMat[:,1], 0.001*array(datingLabels), 0.001*array(datingLabels))
plt.xlabel('height')
plt.ylabel('weight')
plt.show()
