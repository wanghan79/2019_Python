# 导入相关模块
import pymongo
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib as mpl

# 连接数据库
client = pymongo.MongoClient('localhost', 12345)
db = client['linfengchen']
table = db['text']
# 读取数据
data = pd.DataFrame(list(table.find()))
list1=[]
list1=data['intnumber']
#print(list1)
count=0;
count1=0;
count2=0;
for item in list1:
    if int(item)>=7:
        count=count+1;
    if int(item)<7 and int(item)>=3:
        count1=count1+1;
    if int(item)<3:
        count2=count2+1;
#print(count)
#print(count1)
#print(count2)
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
labels = 'high than 7', 'between', 'low than 3'
fracs = [count,count1,count2]
explode = [0, 0.1, 0.2]  # 0.1 凸出这部分，
plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
# autopct ，show percet
plt.pie(x=fracs, labels=labels, explode=explode, autopct='%3.1f %%', shadow=True, labeldistance=1.1, startangle=90, pctdistance=0.6  )
'''
labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
shadow，饼是否有阴影
startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
pctdistance，百分比的text离圆心的距离
patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本
'''
plt.title("产生随机数各段百分比")
plt.show()