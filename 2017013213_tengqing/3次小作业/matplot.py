from pylab import *

subplot(1,2,1)#同时展示两张图片
n = 1024
X = np.linspace(-np.pi,np.pi,n,endpoint=True)
Y = np.sin(2*X)
plot (X, Y+1, color='green', alpha=1.00)
plot (X, Y-1, color='black', alpha=1.00)
show()

subplot(1,2,2)
n = 512
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
scatter(X,Y)
show()