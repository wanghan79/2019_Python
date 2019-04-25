import pymongo
import random
import string
from random_num import Generators

class Moveto_db(Generators):
    def __init__(self, size, total):
        super().__init__(size, total)

    def move(self):
        i = 0
        for n in self.random_generator():
            i = i + 1
            # list = []
            dict = {'_id': i, 'content': n}
            # list.append(dict)
            x = self.mycol.insert_one(dict)

    def connect_db(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["SZH_database"]
        self.mycol = mydb["RandomNumbers"]

    def show_col(self):
        for x in self.mycol.find():
            print(x)

    def del_col(self):
        x = self.mycol.delete_many({})

def main():
    moveto_db = Moveto_db(5, 100)
    # 连接数据库
    moveto_db.connect_db()
    # 删除数据表
    moveto_db.del_col()
    # 将数据导入表
    moveto_db.move()
    # 显示导入的数据
    moveto_db.show_col()

if __name__ == '__main__':
    main()