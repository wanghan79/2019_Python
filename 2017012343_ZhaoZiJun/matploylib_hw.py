import matplotlib.pyplot as plt
import numpy as np
"""
简单画了三个函数图像，分别是y=x  y=1/x  y=x^3
"""
x_values = np.arange(0.,3.,0.05)
plt.plot(x_values,x_values,'r',x_values,x_values**3,'g',
         x_values,x_values**(-1),'y')
#plt.plot(input_values,squares,linewidth=5)
plt.title('y=x  y=1/x  y=x^3',fontsize=24)
plt.xlabel('value',fontsize=14)
plt.ylabel('square of value',fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.show()

