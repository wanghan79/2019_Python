#!/usr/bin/env python

import random
import string
import decimal
from pymongo import MongoClient

name = MongoClient('localhost')
db = name.hehc
#if "hehc" in dblist:
#    print("数据库已存在")
emp = db.mydb
emp.remove(None)

def string_generation(size=6,chars=string.ascii_uppercase+string.digits):
                return "".join(random.choice(chars) for _ in range(size))

                      
def dictionary_generation(n=100000):

                for i in range(1,n,1):
                        int_res = random.randint(0,100000)
                        float_res = round(random.uniform(0,1000),2) #保留两位浮点数
                        string_res =string_generation();
                        res = { 'credit_card_number':int_res,'money':float_res,'password':string_res}
                        yield res
                        emp.insert_one(res)
file = open("output.txt","w")
for res in dictionary_generation():
          file.write(str(res)+'\n')
file.close()
