# -*- coding: utf-8 -*-
import random
import string
import pymongo
def Generate_data(size=100000):
    for i in range(size):
        dic = {}
        data = {}
        data['整型'] = random.randint(0, 100000)
        data['浮点'] = random.uniform(0, 1000)
        data['字符串'] = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        dic["".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))] = "".join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(9))
        data['字典'] = dic
        yield data
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['gaoyl']
mycol = mydb["Gaoyl"]
for data in Generate_data():
    mycol.insert_one(data)
    print(data)
