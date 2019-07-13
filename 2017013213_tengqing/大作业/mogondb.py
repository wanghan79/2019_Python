import pymongo
from random_data import *

def connect_mongodb():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["tqdb"]
    mycol = mydb["sites"]
    return mycol

def delete():
    mycol=connect_mongodb()
    mycol.delete_many({})

def insert(data):#将数据插入到mogondb中
    rd=data
    mycol=connect_mongodb()
    for x in rd.number(100000):
        mycol.insert_one(x)

def print_data():#将数据输出
    mycol = connect_mongodb().mycol
    for x in mycol.find():
        print(x)

