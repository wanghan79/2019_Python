import ast

import matplotlib

import matplotlib.pyplot as plt

from numpy import *

import numpy as np


filename = 'random_output.txt'




"""功能：将data.txt中数据转换为进行可视化"""

x = np.arange(1,100001)

y = np.loadtxt('random_output.txt',delimiter = ',',usecols = 1,unpack = False)

plt.scatter(x,y,marker='o',s=1,alpha=0.5,color='red')

plt.show()
