import pymongo
import random
import string
client = pymongo.MongoClient()
db = client['my_db']
collection = db['my_collection']
class DataAccess:
    def dgenerate (size=10000):
        dict={'Charles':5,'Mark':4,'Bill':7,'Vincent':12,'William':3,'Joseph':7, 'James':8,'Henry':9,'Gary':6,'Martin':23,
              'Malcolm':24,'Joan':14,'Niki':25,'Betty':14,'Linda':14,'Whitney':15,'Lily':17,'Albert':18,'Kevin':19,'Michael':19}
        for i in range(size):
            a = random.randint(1,100000)#从1到100000中随机整型
            b = random.uniform(1,100000)#从1到100000中随机浮点型
            c = ''.join(random.sample(string.ascii_letters + string.digits,4))#随机4个字符
            d = random.sample(dict.items(),1)#随机选取一个键值对
            x = {
                'ZhengXing':a,
                'FuDian':b,
                'ZiFu':c,
                'ZiDian':d
                }
            yield x
    for i in dgenerate():
        r = dict(i)
        collection.insert_one(r)#插入每条数据
    results = collection.find({'ZiDian':[('Bill', 7)]})#查找符合条件的数据
    f = open('NumberFromMongodb.txt','w')#打开文档
    #print(results)
    for i in results:  
        r=str(i)
        f.write(r + '\n')#将符合条件的数据取出到NumberFromMongodb.txt文档中
        print(i)#并且打印出来
    f.close()#关闭文档