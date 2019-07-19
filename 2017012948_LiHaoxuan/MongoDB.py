import pymongo


class MongoDB:
    """
    MongoDB connect、delete、insert
    """

    def connect_mongodb(self):  # 连接mongodb数据库
        myClient = pymongo.MongoClient("mongodb://localhost:27017/")
        myDb = myClient["mgdb"]
        myCol = myDb["sites"]
        return myCol

    def delete(self):  # 删除数据
        myCol = MongoDB.connect_mongodb()
        myCol.delete_many({})

    def insert(data):  # 将数据插入到mogondb中
        myCol = MongoDB.connect_mongodb()
        myCol.insert_one(data)
