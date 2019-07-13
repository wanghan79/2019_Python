import pymongo
from matplotlib import pyplot as plt
import numpy as np

def connect_mongodb():#连接至mongodb
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["tqdb"]
    mycol = mydb["sites"]
    return mycol

def matplot():
    mycol=connect_mongodb()
    num1=num2=num3=num4=0 #计算概率
    for x in mycol.find():
        if(x['int型数']>0 and x['int型数']<=10000):
            num1=num1+1
        if (x['int型数']>10020 and x['int型数']<= 25000):
            num2=num2+1
        if (x['int型数']>25000 and x['int型数']<= 40000):
            num3=num3+1
        if (x['int型数']>40000 and x['int型数']<= 100000):
            num4=num4+1
    print(num1,num2,num3)
    labels = '0~10000', '10020~25000', '25000~40000', '40000~100000'
    sizes = [num1, num2, num3, num4]
    explode = (0, 0.1, 0, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()
