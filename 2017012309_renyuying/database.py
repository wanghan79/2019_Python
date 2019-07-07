'''
任雨莹
2017012309
数据库存取
'''
import random
import string
#coding=utf-8
from pymongo import MongoClient
#建立MongoDB数据库连接
client = MongoClient('localhost',27017)

#连接所需数据库,rand为数据库名
db = client.rand

#连接所用集合，也就是我们通常所说的表，rand为表名
collection = db.rand
collection.remove(None)
#向集合中插入数据
def Random():
    row = 0
    while row < 1000:
        column = 0
        while column < 100:
            # 产生0到100000随机整数
            integer = random.randint(0, 100000)
            # 产生0到100随机浮点数
            f = random.uniform(0, 100)
            # 产生随机字典
            dict1 = {random.choice(string.ascii_letters): random.sample(string.ascii_letters + string.digits, 3)}
            # 产生随机字符串
            str1 = ''.join(random.sample(string.ascii_letters + string.digits, 3))
            tuple = (integer, f, dict1, str1)
            yield tuple
            randNum = {
                '整数': integer,
                '浮点数': f,
                '字典': dict1,
                '字符串': str1
            }
            collection.insert_one(randNum)
            column += 1
        row += 1
    return 'done'
g = Random()
f = open("out.txt", "w", encoding="utf-8")
while True :
    try:
        y = next(g)
        print(y, file = f)
    except StopIteration as e:
        print(e.value)
        break
f.close()