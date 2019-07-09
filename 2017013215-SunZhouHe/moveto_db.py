import pymongo
import random
import string
import sys,os
import time
from random_num import Generators
import tkinter.messagebox

class Moveto_db(Generators):
    def __init__(self, size, total):
        super().__init__(size, total)
    #生成数据并导入到数据库
    def move(self):
        i = 0
        # 进度条（获取标准输出）
        _output = sys.stdout
        for n in self.random_generator():
            i = i + 1
            dict = {'_id': i, 'content': n}
            x = self.mycol.insert_one(dict)
            # 输出进度条
            _output.write(f'\rcomplete percent:{i / 1000:.0f}')
        # 将标准输出一次性刷新
        _output.flush()
    #连接数据库
    def connect_db(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["SZH_database"]
        self.mycol = mydb["RandomNumbers"]
    #将数据库中内容存入文本并打开
    def show_col(self):
        file = open('./database.txt', 'w')
        for x in self.mycol.find():
            file.write(str(x) + '\n')
        os.startfile('database.txt')
    #删除数据表
    def del_col(self):
        x = self.mycol.delete_many({})
#主函数
def main_2():
    moveto_db = Moveto_db(5, 100000)
    moveto_db.connect_db()
    moveto_db.del_col()
    moveto_db.move()
    # 对话框
    tkinter.messagebox.showinfo("提示", "数据导入成功！")

def show_data():
    moveto_db = Moveto_db(5, 100000)
    # 连接数据库
    moveto_db.connect_db()
    # 显示数据库内容
    moveto_db.show_col()

if __name__ == '__main__':
    main_2()