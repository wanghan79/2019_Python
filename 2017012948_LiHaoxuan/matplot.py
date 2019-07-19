import pymongo
from matplotlib import pyplot as plt

"""
MongoDB connect、delete、insert
"""


def connect_mongodb(self):  # 连接mongodb数据库
    myClient = pymongo.MongoClient("mongodb://localhost:27017/")
    myDb = myClient["mgdb"]
    myCol = myDb["sites"]
    return myCol


def matplot():
    mycol = connect_mongodb()
    num1 = num2 = num3 = num4 = 0  # 计算概率
    for x in mycol.find():
        if (x['int型数'] > 0 and x['int型数'] <= 10000):
            num1 = num1 + 1
        if (x['int型数'] > 10000 and x['int型数'] <= 25000):
            num2 = num2 + 1
        if (x['int型数'] > 25000 and x['int型数'] <= 40000):
            num3 = num3 + 1
        if (x['int型数'] > 40000):
            num4 = num4 + 1
    print(num1, num2, num3, num4)
    labels = '0~10000', '10000~25000', '25000~40000', '40000以上'
    sizes = [num1, num2, num3, num4]
    explode = (0, 0.1, 0, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()
