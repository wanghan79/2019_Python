import numpy as np  
import matplotlib.pyplot as plt  
#产生测试数据  
x, y = np.random.rand(2, 300)
fig = plt.figure()  
ax1 = fig.add_subplot(111)
#设置横纵坐标
plt.xlabel('Y')
plt.ylabel('X')
#画散点图 
ax1.scatter(x,y,c = 'r',marker = 's')
#设置图标位置 
ax1.legend('X',loc=1, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)
plt.show()