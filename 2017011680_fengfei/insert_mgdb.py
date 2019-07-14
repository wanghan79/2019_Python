import pymongo
from firstcode import CreateNumber
def insert_mongo():
    cn = CreateNumber()
    myclient = pymongo.MongoClient('localhost', 27017)
    mydb = myclient["mydb"]
    mycol = mydb["number"]
    mycol.delete_many({ })
    # f = open('F:/python/test/test.txt','w')
    for j in cn.ReturnRes(100000):
        x = mycol.insert_one(j)  # 将产生的数据存入monggodb
    return