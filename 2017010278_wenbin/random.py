import pymongo
import random
from pymongo import MongoClient

a={'鱼类':['青鱼','草鱼','鲤鱼','鲫鱼'],
   '兽类':['虎','狼','象','马','鹿'],
   '鸟类':['鸡','鸭','鹅'],
   '两栖':['青蛙','龟','娃娃鱼','蛇','鳄鱼']
   }
l=list(a.keys())

"""
在mongodb中创建了一个名为'firstpy'的数据库，其中集合叫'dongwu'
"""

client=pymongo.MongoClient('localhost',27017)
dblist=client['firstpy']
dongwu=dblist.dongwu

"""
插入数据
"""
def generaterandom(size):
    while size>0:
        randomint=random.randint(0,100)
        randomfloat=random.random()
        randomchar=random.choice('asdfghjQWERZXC!@#$%^&')
        door=random.choice(l)
        animal=random.choice(a[door])
        temp=(randomint,randomfloat,randomchar,door+'['+animal+']')
        yield temp
        randnum={
            '整数':randomint,
            '浮点数':randomfloat,
            '字符':randomchar,
            '门':door,
            "动物":animal
        }
        dongwu.insert_one(randnum)
        size=size-1
    return 'finish'
if __name__ == '__main__':
    file = open("out.txt", "w")
    for data in generaterandom(100000):
        file.write(str(data)+'\n')
    file.close()

"""
删除数据
"""

def dele(cata,data):
dongwu.delete_one({cata:data})