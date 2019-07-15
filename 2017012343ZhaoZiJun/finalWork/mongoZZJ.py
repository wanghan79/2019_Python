import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
#创建数据库和集合
dblist = myclient.list_database_names()
mydb = myclient["zzjDB"]
mycol = mydb["zzjST"]
#因为在本地跑程序时，多次运行导致数据库混乱，故每次清空集合 zzjST
mycol.delete_many({})
def insertDB(data):
    """
    将一个具有四个value值的字典的数据传入数据库中，无返回值
    """
    value1 = data['data_int']
    value2 = data['data_float']
    value3 = data['data_string']
    value4 = data['data_dictionary']
    mydict={"int":value1,"float":value2,"string":value3,"dictionary":value4}
    x = mycol.insert_one(mydict)
#    print('insert succeeded!')
#	print(x)
#	print(x.inserted_id)

def loadDB():
    """
    传入一个参数，在数据库的name中寻找匹配值，并将其对应的value值yield出来
    """
    for x in mycol.find():
        yield x
            
def saveALL():
    """
    将当前数据库集合中的内容存储到文件dataDB.txt
    """
    output = open("dataDB.txt","w")
    for x in mycol.find({},{ "_id": 1, "int": 1, "float": 1,
                             "string": 1, "dictionary": 1 }):
        output.write(str(x)+'\n')
    output.close()
            
def test():
    """
    测试import是否成功
    """
    print("import mongoZZJ succeeded")