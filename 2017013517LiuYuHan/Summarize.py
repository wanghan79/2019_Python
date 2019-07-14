import pymongo
import random
import string
import numpy as np
import pymongo
import pandas as pd
import matplotlib.pyplot as plt
#连接数据库
client = pymongo.MongoClient()
db = client['my_db']
collection = db['my_collection']
table = db['my_collection']
class Summarize:
    #随机生成需包含整型，浮点型，字符型，字典型
    def dgenerate (size=100000):
        dict={'Charles':5,'Mark':4,'Bill':7,'Vincent':12,'William':3}
        for i in range(size):
            a = random.randint(1,100)#从1到100000中随机整型
            b = random.uniform(5,10)#从1到100000中随机浮点型
            c = ''.join(random.sample(string.ascii_letters + string.digits,4))#随机4个字符
            d = random.sample(dict.items(),1)#随机选取一个键值对
            x = {
                '整型':a,
                '浮点型':b,
                '字符型':c,
                '字典型':d
                }
            yield x
    #将数据插入数据库，按条插入
    for i in dgenerate():
        r = dict(i)
        collection.insert_one(r)
    results = collection.find({'字典型':[('Bill', 7)]})
    f = open('NumberFromMongodb.txt','w')
    #print(results)
    for i in results:  
        r=str(i)
        f.write(r + '\n')
        print(i)
    f.close()
    #取整张表的数据
    data = pd.DataFrame(list(table.find()))
    x = data['整型'] # 产生x坐标
    y = data['浮点型'] # 产生y坐标
    area = np.pi * (15 * np.random.rand(50))**2  # 点的半径范围:0~15 
    # 绘制散点图,点的形状为星星
    plt.scatter(x, y, s=area, alpha=0.5, marker='*')
    plt.show()