"""
生成随机数据100000组

    董昱辰
    2019.7.13
"""


import random
import uuid
import string
#from __future__ import print_function
import numpy as np
'''产生随机数元组，包括int，float，string，dict类型数据'''
def getRandomInt():
    return random.randint(0, 10000)

def getRandonFloat():
    return random.uniform(0, 1000)

def getRandomStr():
    return uuid.uuid1()
    #ran_str=''.join(random.sample(string.ascii_letter+string.digits,16))
    #return ran_str

def getRandomDict():
    node={'number'+str(i):random.randint(1,100) for i in range(5)}
    return node

def dataRandom():
    '''产生随机数据，用tuple存储'''
    for i in range(100000):
        tup=(getRandomInt(),getRandonFloat(),getRandomStr(),getRandomDict())
        #yield tup
        #print(tup)
        return tup

#dataRandom()
"""
将数据写进txt中的程序
    txt=dataRandom()
    with open("user.txt","a") as f:
        f.write(txt)
    print(txt)
"""