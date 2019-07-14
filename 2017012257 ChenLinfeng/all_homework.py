# encoding:utf-8
import random
import time
import pymongo
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib as mpl
client=pymongo.MongoClient('localhost',12345)
mydb=client.linfengchen
mycollection=mydb.text

dataCount= 200000    #定义需要产生的数据总数
def genRandomIntnumber():            #产生随机整数的函数
    return random.randint(0, 10)     #产生0-10之间的随机整数

def genRandomFloatnumber():          #产生随机浮点数
    return random.uniform(1, 10)      #浮点数的范围是0-10

def genRandomString():              #产生随机的字符串
    return random.choice(['apple', 'pear', 'peach', 'orange', 'lemon'])  #从其中选取一个作为返回值

def genRandomDict():                #产生随机的字典
    x = {'河北省': ['石家庄', '唐山', '秦皇岛', '承德'],          #给定一些字典对应的键值对
         '山东省': ['济南', '青岛', '临沂', '淄博'],
         '湖南省': ['长沙', '衡阳', '湘潭', '邵阳', '岳阳', '株洲'],
         '江西省': ['南昌', '九江', '上饶', '景德镇']}
    s = list(x.keys())                                               # 省列表
    province = random.choice(s)                                      # 随机选一个省
    city = random.choice(x[province] )                               # 随机选一城市
    return province+':'+city


def FunGenerate(fileName, dataCount):                      #定义函数，调用相应的函数产生
    outputfile = open(fileName, 'w')
    i = 0
    while i < dataCount:
        intNumber=genRandomIntnumber()
        floatNumber=genRandomFloatnumber()
        String=genRandomString()
        Dict=genRandomDict()
        mLine = "%i %d %f %s %s\n" % (i + 1,intNumber,floatNumber,String,Dict)
        outputfile.write(mLine)
        i += 1
    outputfile.close()

# 打开需要存入的文件, 并将数据存入到数据库
with open('db_test.txt', 'r') as f:
    for line in f.readlines():
        items = line.strip('\r').strip('\n').split(' ')
        # 添加到数据库
        mycollection.insert_one({'ID':items[0], 'intnumber': items[1], 'doublenumber': items[2], 'string': items[3],'dict':items[4]})
# 查询数据库中自己导入的记录并输出
for s in mycollection.find():
    print(s)

if __name__ == "__main__":
    random.seed()
    start = time.time()
    FunGenerate('db_test.txt', dataCount)
    end = time.time()
    print('use times:%d' % (end - start))
    print('congratulation,you finish the work.')
'''
    # 连接数据库
    client = pymongo.MongoClient('localhost', 12345)
    db = client['linfengchen']
    table = db['text']
    # 读取数据
    data = pd.DataFrame(list(table.find()))
    print(data)
    # 用matplotlib来画出箱型图
    list1 = []
    list1 = data['doublenumber']
    count = 0;
    count1 = 0;
    count2 = 0;
    for item in list1:
        if float(item) >= 6.7:
            count = count + 1;
        if float(item) < 6.7 and float(item) >= 3.3:
            count1 = count1 + 1;
        if float(item) < 3.3:
            count2 = count2 + 1;
    # print(count)
    # print(count1)
    # print(count2)
    mpl.rcParams["font.sans-serif"] = ["SimHei"]
    mpl.rcParams["axes.unicode_minus"] = False
    labels = 'high than 6.7', 'between', 'low than 3.3'
    fracs = [count, count1, count2]
    explode = [0, 0.1, 0]  # 0.1 凸出这部分，
    plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
    # autopct ，show percet
    plt.pie(x=fracs, labels=labels, explode=explode, autopct='%3.1f %%', shadow=True, labeldistance=1.1, startangle=90,
            pctdistance=0.6)

    labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
    autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
    shadow，饼是否有阴影
    startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
    pctdistance，百分比的text离圆心的距离
    patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本
    '''
'''
    plt.title("产生随机数各段百分比")
    plt.show()
    '''