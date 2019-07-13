import string
import random
from pymongo import MongoClient

#1.链接本地数据库服务
name = MongoClient('localhost')
#2.链接本地数据库 demo 没有会创建
db = name.mapx#demo数据库名
#3.创建，连接集合
emp = db.pxm #集合名字
emp.remove(None)
def generateRandomNumber(i):
    while i!=0:
        Int=random.randint(1,100000)
        Float=random.random()
        Char=random.choice('ud7hfji8jkgikgjksdjgshjgdsgjgdsjjkdkdgsjkgdsgdjdsghgdsgdjskjdgsjkdgkgd')
        Str=''.join(random.sample(string.ascii_letters + string.digits,random.randint(1,10)))
        dict={str(Int):Str}
        lop=(Int,Float,Char,Str,dict)
        yield lop
        randomNumber = {
            '整型': Int,
            '浮点数':Float,
            '字符': Char,
            '字典': dict,
            '字符串':Str
        }
        emp.insert_one(randomNumber)
        i= i - 1
    return 'done'
g = generateRandomNumber(100000)
f = open("mpx.txt", "w", encoding="utf-8")
while True :
    try:
        y = next(g)
        print(y, file = f)
    except StopIteration as e:
        print(e.value)
        break
f.close()
#for i in emp.find():
 # print(i)