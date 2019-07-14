import pymongo
from insert_mgdb import insert_mongo
def search_string1():
    insert_mongo()
    myclient = pymongo.MongoClient('localhost', 27017)
    mydb = myclient["mydb"]
    mycol = mydb["number"]
    dic = {'6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0}  # 存字符串长度的字典
    for j in mycol.find({}, {"_id": 0, "string": 1}):
        dic[str(len(j['string']))] = dic[str(len(j['string']))] + 1  # 统计字符串长度的数量
    return dic
def search_int1():
    insert_mongo()
    myclient = pymongo.MongoClient('localhost', 27017)
    mydb = myclient["mydb"]
    mycol = mydb["number"]
    list1 = []
    for i in mycol.find({}, {"_id": 0, "int": 1}):
        list1.append(i["int"])
    return list1
def search_float1():
    insert_mongo()
    myclient = pymongo.MongoClient('localhost', 27017)
    mydb = myclient["mydb"]
    mycol = mydb["number"]
    list1 = []
    for i in mycol.find({}, {"_id": 0, "float": 1}):
        list1.append(i["float"])
    return list1
def search_strlen1():
    insert_mongo()
    myclient = pymongo.MongoClient('localhost', 27017)
    mydb = myclient["mydb"]
    mycol = mydb["number"]
    list1 = []
    for j in mycol.find({}, {"_id": 0, "string": 1}):
        list1.append(str(len(j['string'])))
    return list1