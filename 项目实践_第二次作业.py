import string
import random
from pymongo import MongoClient

#1.链接本地数据库服务
name = MongoClient('localhost')
#2.链接本地数据库 demo 没有会创建
db = name.random_number   #demo数据库名
#3.创建，连接集合
emp = db.myrandom  #集合名字
emp.remove(None)

def Random(i):
    cout=0
    while i!=0:
        cout+=1
        num=random.randint(1,10)
        ran_str =  ''.join(random.sample(string.ascii_letters + string.digits,num))
        unif=random.uniform(1,10)
        rand=random.randint(1,100)
        key=random.choice(string.ascii_letters)
        dict1={key:unif}
        dict2={key:rand}
        dict3={key:ran_str}
        cout1=(str(cout)+':')
        tup1 = (cout1,ran_str,unif,rand,dict1,dict2,dict3)
        yield tup1
        randomNumber = {
            '序号':cout,
            '整型': rand,
            '浮点数':unif,
            '字符': ran_str,
            '字典1': dict1,
            '字典2':dict2,
            '字典3':dict3
        }
        emp.insert_one(randomNumber)
        i= i - 1
    return 'done'
g = Random(100000)
f = open("out.txt", "w", encoding="utf-8")
while True :
    try:
        y = next(g)
        print(y, file = f)
    except StopIteration as e:
        print(e.value)
        break
f.close()