from RandomNumber import create_number
from link_data import link_MongoDB
f = open("output_data.txt","w")
for i in range(100000):
    data=create_number()
    print(data)
    data=str(data)
    f.write(data+'\n')
f.close()
link_MongoDB()
import matplotlib.pyplot as plt
file = open('output_data.txt')
i=0
x=[]
y=[]
for line in file:
    x1=line[1:5]
    x.append(int(x1))
    y1=line[7:15]
    y.append(float(y1))
    i=i+1
print(x,y)
plt.figure(figsize=(25, 10), dpi=300)
plt.scatter(x,y,s=3,c='g',marker='o')
plt.savefig('scatter_diagram.jpg')
plt.show()
k1=k2=k3=k4=0
for data in x:
    if data<2000:
        k1 = k1 + 1
    elif 2000<=data<3000:
        k2 = k2 + 1
    elif 3000 <= data < 4000:
        k3 = k3 + 1
    else :
        k4 = k4 + 1
labels='1000<=x<2000','2000<=x<3000','3000<=x<4000','4000<=x<5000'
size =[k1,k2,k3,k4]
print(k1,k2,k3,k4)
explode = (0.1,0.05,0.05,0.1)
plt.figure(figsize=(100,100))
plt.pie(size,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.title("数据分析")
plt.show()

