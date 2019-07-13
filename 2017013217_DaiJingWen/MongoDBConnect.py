#将随机生成的数据存储到表中
import random
from pymongo import MongoClient

#1.链接本地数据库服务
name = MongoClient('localhost',27017)
#2.链接本地数据库,没有会创建
db = name.random_number   #数据库名
#3.创建，连接集合
emp = db.t_country_city  #集合名
emp.remove(None)
x={'中国':['北京','上海','广州','台湾','香港','澳门','重庆'],
   '美国':['华盛顿','纽约','洛杉矶','金州','夏威夷'],
   '英国':['曼彻斯特','伦敦','德比郡','利物浦','牛津','剑桥'],
   '德国':['慕尼黑','柏林','斯图加特','美因兹']}
s=list(x.keys())
def RandomNumber(i):
    while i!=0:
        country = random.choice(s)
        city = random.choice(x[country])
        randomInt = random.randint(0, 100)
        randomFloat = random.random()
        randomChar = random.choice('qwertyASDFGH~!@#$%^&*()_+-=')
        tup1 = (randomInt, randomFloat, randomChar,country + ": [" + city + "]")
        yield tup1
        randomNumber = {
            '整型': randomInt,
            '浮点数':randomFloat,
            '字符': randomChar,
            '省': country,
            '市' : city
        }
        emp.insert_one(randomNumber)
        i= i - 1
    return 'done'
r = RandomNumber(100000)
f = open("out.txt", "w", encoding="utf-8")
while True :
    try:
        y = next(r)
        print(y, file = f)
    except StopIteration as e:
        print(e.value)
        break
f.close()
