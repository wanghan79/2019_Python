import random
import string
import docx
import numpy as np
from matplotlib import pyplot as plt
import pymongo

class Generaterandom():
    def __init__(self):
        pass

    def dict_generator(self,size,chars=string.ascii_letters + string.digits):
        dict = {}
        k = ''.join(random.choice(chars) for x in range(self.size))
        v = ''.join(random.sample(string.ascii_letters + string.digits, self.size))
        dict[k] = v
        return dict

    def id_g(self,size,chars=string.ascii_letters + string.digits):
        self.size=size
        return ''.join(random.choice(chars) for x in range(self.size))

    def number(self,size=1000):
        self.size=size
        for y in range(1, self.size + 1):
            dict={}
            int_num = random.randint(1, 10000000)
            dict['int']=int_num
            float_number = random.uniform(0, 10000000)
            dict['float']=float_number
            string= self.id_g(random.randint(1, 20))
            dict['str']=string
            dic = self.dict_generator(random.randint(1, 20))
            dict['dictionary']=dic
            yield  dict

rd=Generaterandom()
def connect():#链接至mongodb
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["yydatabase"]
    mycol = mydb["random"]
    return mycol

def insert():#将数据保存起来
    mycol=connect()#调用函数
    for x in rd.number(100000):
        mycol.insert_one(x)

def search():
    mycol=connect()
    for x in mycol.find():
        print(x)