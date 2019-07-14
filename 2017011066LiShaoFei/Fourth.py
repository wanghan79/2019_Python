import numpy as np
import random
import string
import pymongo
from matplotlib import pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif']=['SimHei']      #防止中文乱码

def random_list( start, stop, length):
    if length >= 0:
        length = int(length)
        start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
        random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

class dataGenerate:
    def dGen(self, size=1000):
        for i in range(size):
            keys = random_list(0, 100, 1)
            values = random_list(0, 100, 1)
            dictionary = dict(zip(keys, values))
            numx = np.random.randint(0, 1000)
            numy = np.random.randint(0, 1000)
            salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))  # Generate a random string
            data = {'string': salt, 'intX': numx, 'intY': numy, 'float': np.random.uniform(0, 1000000), 'keys': keys, 'values': values}
            yield data

#定义数据库
MONGO_URL="localhost"       #本地数据库
MONGO_DB="flyzer"           #定义的数据库名
MONGO_TABLE="table"         #数据库的表名

#链接并创建数据库
client = pymongo.MongoClient(MONGO_URL) #生成一个MongoDB的对象
db = client[MONGO_DB]
#定义一个db，将数据库的名称传递过来


def save_to_mongo(ur):
    db[MONGO_TABLE].insert(ur)

#调用上一个文件中的函数并将其实例化传入数据库
m=dataGenerate()
for j in m.dGen():
    save_to_mongo(j)    #依次进行存储，并且将前一个Random的数据类型全部改成键值对的形式

flyzertable = db['table']
#查找数据库中表格里的数据并赋值给X与Y
data = pd.DataFrame(list(flyzertable.find()))
x=data['intX']
y=data['intY']


#画出散点图
fig = plt.figure(figsize=(4, 4))
scmap = fig.add_subplot(111)
scmap.scatter(x, y, c='blue')
scmap.legend('X与Y的关系图')
scmap.grid(True)
plt.show()
plt.savefig("Scatter.png")


#画出饼图，并统计小于2000的和2000-4000之间的、4000-8000之间、8000-10000之间的
plt.figure()
#调节图形大小，宽，高
plt.figure(figsize=(6,9))
#定义饼状图的标签，标签是列表
labels = [u'0-200',u'200-400',u'400-700',u'700-1000']
#每个标签占多大，会自动去算百分比
NUM=data['intX']
x1=NUM[1:1000:10]
Part1=0
Part2=0
Part3=0
Part4=0
for i in x1:
    if i<200 and i>0:
        Part1=Part1+1
    elif i<=400 and i>=200:
        Part2=Part2+1
    elif i<=700 and i>400:
        Part3=Part3+1
    else:
        Part4=Part4+1
Part=[Part1,Part2,Part3,Part4]
#各部分占比重

colors = ['red','yellow','blue','pink']
patches,text1,text2= plt.pie(Part,
                                labeldistance = 1.1,
                                autopct = '%3.3f%%',
                                labels=labels,
                                colors=colors,
                                shadow = False,
                                startangle = 90,
                                pctdistance = 0.6)
# 设置x，y轴刻度一致，这样饼图才能是圆的
plt.axis('equal')
plt.legend('饼图')
plt.show()
plt.savefig("pie.png")
