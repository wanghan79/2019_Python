import string
import random
from pymongo import MongoClient

#1.链接本地数据库服务
name = MongoClient('localhost')
#2.链接本地数据库 demo 没有会创建
db = name.xcnhr  #demo数据库名
#3.创建，连接集合
emp = db.mydb #集合名字
emp.remove(None)

def generateRandomNumber(i):
    while i!=0:
        randomInt=random.randint(1,100000)
        randomFloat=random.random()
        randomChar=random.choice('hhcsbxiaguosbfhdjfdjfdshfdkjfkjfdfjkfkjhfdskjfdioefiofeiifeiofiiefsiojfseioj')
        randomStr=''.join(random.sample(string.ascii_letters + string.digits,random.randint(1,10)))
        dict={str(randomInt):randomStr}
        tup1=(randomInt,randomFloat,randomChar,randomStr,dict)
        yield tup1
        randomNumber = {
            '整型': randomInt,
            '浮点数':randomFloat,
            '字符': randomChar,
            '字典': dict,
            '字符串':randomStr
        }
        emp.insert_one(randomNumber)
        i= i - 1
    return 'done'
g = generateRandomNumber(100000)
f = open("xcnhr.txt", "w", encoding="utf-8")
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
 