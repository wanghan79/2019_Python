"""
将生成的数据制成散点图
    董昱辰
    2019.7.13
"""

import matplotlib.pyplot as plt
import homework1
# import homework2
import numpy as np
fig=plt.figure()
ax1=fig.add_subplot(111)
ax1.set_title("scatter Plot")
plt.xlabel('X')
plt.ylabel('Y')
for i in range(1000):
    y=homework1.getRandonFloat()
    x=i
    ax1.scatter(x,y,c='r',marker='.')
plt.legend('x1')
plt.show()