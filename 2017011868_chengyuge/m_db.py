import pymongo
import random
import string
import sys,os
import time
from random_num import Generators
import tkinter.messagebox
class m_db(Generators):
    def __init__(self, size, total):
        super().__init__(size, total)
    def move(self):
        i = 0
        _output = sys.stdout
        for n in self.random_generator():
            i = i + 1
            dict = {'_id': i, 'content': n}
            x = self.mycol.insert_one(dict)
            _output.write(f'\rcomplete percent:{i / 1000:.0f}')
        _output.flush()
    def connect_db(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["cyg_database"]
        self.mycol = mydb["RandomNumbers"]
    def show_col(self):
        file = open('./database.txt', 'w')
        for x in self.mycol.find():
            file.write(str(x) + '\n')
        os.startfile('database.txt')
    def del_col(self):
        x = self.mycol.delete_many({})
def main_2():
    M_db = m_db(5, 100000)
    M_db.connect_db()
    M_db.del_col()
    M_db.move()
    tkinter.messagebox.showinfo("提示", "数据导入成功！")
def show_data():
    M_db = m_db(5, 100000)
    M_db.connect_db()
    # 显示数据库内容
    M_db.show_col()
if __name__ == '__main__':
    main_2()