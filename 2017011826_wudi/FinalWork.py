import numpy as np
import random
import string
import pymongo
from matplotlib import pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码

#生成随机列表的函数
def random_list( start, stop, length):
    if length >= 0:
        length = int(length)
        start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
        random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

#生成随机数、字符串和字典的类
class DataCreat:
    def Creat(self, size=100000):
        for i in range(size):
            keys = random_list(0, 1000, 1)
            values = random_list(0, 1000, 1)
            dictionary = dict(zip(keys, values))
            NumberX = np.random.randint(0, 10000)
            NumberY = np.random.randint(0, 10000)
            Str = ''.join(random.sample(string.ascii_letters + string.digits, 12))  # Generate a random string
            data = {'string': Str, 'intX':NumberX,'intY':NumberY, 'float': np.random.uniform(0, 1000000),'key':keys,'value':values}
            yield data

#定义数据库
MONGO_URL="localhost"  #本地数据库
MONGO_DB="mm"          #定义的数据库名
MONGO_TABLE="table"    #数据库的表名

#链接并创建数据库
client = pymongo.MongoClient(MONGO_URL) #生成一个MongoDB的对象
db = client[MONGO_DB]                   #定义一个db，将数据库的名称传递过来

#定义一个保存函数
def save_to_mongo(ur):      #如果插入的数据成功，输出成功存储,并打印存储内容：否则输出存储失败和其值
    if db[MONGO_TABLE].insert(ur):
       print("成功存储到MongoDB",ur)
    else:
        print("存储失败",ur)

#调用上一个文件中的函数并将其实例化传入数据库
m=DataCreat()
for j in m.Creat():
    save_to_mongo(j)  #依次进行存储，并且将前一个Random的数据类型全部改成键值对的形式

#获取数据库的值
wdtable = db['table']
data = pd.DataFrame(list(wdtable.find()))
x=data['intX']
y=data['intY']

#画出散点图
plt.figure()
x1=x[1:1000:10]
y1=y[1:1000:10]
fig = plt.figure(figsize=(10,10))
scmap = fig.add_subplot(111)
scmap.scatter(x, y, c='lightskyblue')
scmap.legend('随机生成X与随机生成Y的关系图')
scmap.grid(True)
plt.show()
plt.savefig("line1.png")

#画出饼图，并统计小于2000的和2000-4000之间的、4000-8000之间、8000-10000之间的
plt.figure()
#调节图形大小，宽，高
plt.figure(figsize=(6,9))
#定义饼状图的标签，标签是列表
labels = [u'0-2000',u'2000-4000',u'4000-8000',u'8000-10000']
#每个标签占多大，会自动去算百分比
NUM=data['intX']
x1=NUM[1:10000:10]
Part4=0
Part1=0
Part2=0
Part3=0
for i in x1:
    if i<2000 and i>0:
        Part1=Part1+1
    elif i<=4000 and i>=2000:
        Part2=Part2+1
    elif i<=8000 and i>4000:
        Part3=Part3+1
    else:
        Part4=Part4+1
Part=[Part1,Part2,Part3,Part4]
#各部分占比重
colors = ['red','yellowgreen','lightskyblue','pink']
patches,text1,text2= plt.pie(Part,
                                labeldistance = 1.1,
                                autopct = '%3.2f%%',
                                labels=labels,
                                colors=colors,
                                shadow = False,
                                startangle = 90,
                                pctdistance = 0.6)
# 设置x，y轴刻度一致，这样饼图才能是圆的
plt.axis('equal')
plt.legend('饼图')
plt.show()
plt.savefig("line2.png")

#折线图
#X轴，Y轴数据
x=data['intX']
y=data['intY']
x1=x[1:1000:10]
y1=y[1:1000:10]
plt.figure(figsize=(8,4)) #创建绘图对象
plt.plot(x1,y1,"b--",linewidth=1)   #在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）
plt.xlabel("X轴随机数据") #X轴标签
plt.ylabel("Y轴随机数据")  #Y轴标签
plt.title("折线图") #图标题
plt.show()  #显示图
plt.savefig("line.png") #保存图