
import numpy as np
import random
import string
import pymongo

client = pymongo.MongoClient('localhost', 27017)
mydb = client.Curry
mycollection = mydb.mytext

##生成长度为8的字符串
def randomString():
    length = 8
    return ''.join(random.sample(string.ascii_letters + string.digits, length))

#生成[0,100)以内的整数
def randomInt():
    return np.random.randint(0, 100)

#生成[0, 100)以内的浮点数
def randomFloat():
    return np.random.uniform(0, 100)

#生成长度为10的列表
def randomList():
    length = 5
    random_list =[]
    for i in range(length):
        random_list.append(randomInt())
    return random_list

#随机生成十万条数据， 包括整型，浮点型，字符串型，字典型数据
def randomData():
    length = 100000
    for i in range(length):
        numstring = randomString()
        numint = randomInt()
        numfloat = randomFloat()
        numkeys = randomList()
        numvalues = randomList()


        mycollection.insert({'id': i, 'numstring': numstring, 'numint': numint, 'numfloat': numfloat, 'numkeys': numkeys, 'numvalues':numvalues})
if __name__ == '__main__':
    randomData()