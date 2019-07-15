#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 22:25:48 2019

@author: 王爱玲
"""

import matplotlib.pyplot as plt
import random
# import homework2
def getRandomInt():
    return random.randint(0, 10000)

def getRandonFloat():
    return random.uniform(0, 1000)

def getRandomStr():
    return uuid.uuid1()
    #ran_str=''.join(random.sample(string.ascii_letter+string.digits,16))
    #return ran_str

def getRandomDict():
    node={'number'+str(i):random.randint(1,100) for i in range(5)}
    return node

def dataRandom():
    '''产生随机数据，用tuple存储'''
    for i in range(100000):
        tup=(getRandomInt(),getRandonFloat(),getRandomStr(),getRandomDict())
        #yield tup
        #print(tup)
        return tup
import numpy as np
fig=plt.figure()
ax1=fig.add_subplot(111)
ax1.set_title("scatter Plot")
plt.xlabel('X')
plt.ylabel('Y')
for i in range(1000):
    y=getRandonFloat()
    x=i
    ax1.scatter(x,y,c='r',marker='.')
plt.legend('x1')
plt.show()