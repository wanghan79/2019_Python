#将随机生成的数据存储到数据库中
import random
from pymongo import MongoClient

#1.链接本地数据库服务
name = MongoClient('localhost')
#2.链接本地数据库，没有会创建
db = name.random_number   #数据库名
#3.创建，连接集合
emp = db.province_city  #集合名字
emp.remove(None)
x={'辽宁省':['沈阳','鞍山','大连','营口','铁岭'],
   '山东省':['济南','青岛','临沂','淄博'],
   '湖南省':['长沙','衡阳','湘潭','邵阳','岳阳','株洲'],
   '江西省':['南昌','九江','上饶','景德镇']}
s=list(x.keys())
def generateRandomNumber(i):
    while i!=0:
        province = random.choice(s)
        city = random.choice(x[province])
        randomInt = random.randint(0, 100)
        randomFloat = random.random()
        randomChar = random.choice('qwertyASDFGH~!@#$%^&*()_+-=')
        tup1 = (randomInt, randomFloat, randomChar,province + ": [" + city + "]")
        yield tup1
        randomNumber = {
            '整型': randomInt,
            '浮点数':randomFloat,
            '字符': randomChar,
            '省': province,
            '市' : city
        }
        emp.insert_one(randomNumber)
        i= i - 1
    return 'done'
g = generateRandomNumber(100000)
f = open("out.txt", "w", encoding="utf-8")
while True :
    try:
        y = next(g)
        print(y, file = f)
    except StopIteration as e:
        print(e.value)
        break
f.close()
