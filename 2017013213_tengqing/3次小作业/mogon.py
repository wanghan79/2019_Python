import pymongo


class Mongo:
    def connect_mongodb(self):#连接mongodb数据库
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["tqdb"]
        mycol = mydb["sites"]
        return mycol

    def delete(self):#删除数据
        mycol=self.connect_mongodb()
        mycol.delete_many({})#删除全部数据

    def insert(self,data):#将数据插入到mogondb中
        mycol=data.connect_mongodb()
        mycol.insert_one(data)

    def print_data(self):#将数据输出
        mycol = self.connect_mongodb().mycol
        for x in mycol.find():
            print(x)

if __name__ == '__main__':
    data={'tq',12344}
    mg=Mongo();
    mg.insert(data)#插入数据
    mg.print_data()
    mg.delete()