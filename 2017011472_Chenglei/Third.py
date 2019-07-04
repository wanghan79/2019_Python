#从数据库中取数据并统计成饼图
import pymongo
import pandas as pd
import matplotlib as mpl

mpl.use('Agg')

from matplotlib import pyplot as plt

# 连接数据库
client = pymongo.MongoClient('localhost', 27017)
db = client['Curry']
table = db['mytext']

# 读取数据
data = pd.DataFrame(list(table.find()))
# 选择需要统计的字段
numint = data['numint']
cnt_a = 0 #表示0~20的数的个数
cnt_b = 0 #表示20~40的数的个数
cnt_c = 0 #表示40~60的数的个数
cnt_d = 0 #表示60~80的数的个数
cnt_e = 0 #表示80~100的数的个数
i = 0
while i < 100000:
    if 0  < numint[i] <= 20:
        cnt_a = cnt_a + 1
    if 20 < numint[i] <= 40:
        cnt_b = cnt_b + 1
    if 40 < numint[i] <= 60:
        cnt_c = cnt_c + 1
    if 60 < numint[i] <= 80:
        cnt_d = cnt_d + 1
    if 80 < numint[i] <= 100:
        cnt_e = cnt_e + 1
    i = i+1
sizes = [cnt_a, cnt_b, cnt_c, cnt_d, cnt_e]
# 打印输出
# 调节图形大小，宽，高
plt.figure(figsize=(6, 9))
# 定义饼状图的标签，标签是列表
labels = [u'0到20之间的数', u'20到40之间的数', u'40到60之间的数', u'60到80之间的数', u'80到100之间的数']
# 每个标签占多大，会自动去算百分比

colors = ['red', 'yellow', 'lightskyblue', 'green', 'pink']
# 将某部分爆露出来， 使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
explode = (0.05, 0, 0)

patches, l_text, p_text = plt.pie(sizes, labels=labels, colors=colors,
                                  labeldistance=1.1, autopct='%3.1f%%', shadow=False,
                                  startangle=90, pctdistance=0.6)

# labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
# autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
# shadow，饼是否有阴影
# startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
# pctdistance，百分比的text离圆心的距离
# patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本

# 改变文本的大小
# 方法是把每一个text遍历。调用set_size方法设置它的属性
for t in l_text:
    t.set_size = (30)
for t in p_text:
    t.set_size = (20)
# 设置x，y轴刻度一致，这样饼图才能是圆的
plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文乱码
plt.axis('equal')
plt.legend()
plt.show()
print(sizes)