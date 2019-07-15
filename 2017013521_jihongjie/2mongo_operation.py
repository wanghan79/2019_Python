#!/usr/bin/python
#-*-coding:UTF-8-*-

import pymongo
import urllib
import threading
from urllib import request

"""
在MongoDB中，定义一个数据库，名为'simon_db'，其中有collection名为'students'
"""

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client['simon_db']
students = db.students

"""
定义一个MongoDB操作的类，实现增删改查，同理，我也在命令行窗口下能实现
"""
class mongo_operation(threading.Thread):
    """
    功能：线程初始化方法
    """
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num

    """
    功能：将random_output.txt的100000条数据存入MongoDB
    """
    def save_into_mongo(filename):
        f = open(filename, 'r')
        lists=f.readlines()
        for l in lists:
            db.students.insert({'simon':l})
            #db.close()
            r=mongo_operation(1)
            r.start()

    """
    功能：查询单条记录
    """
    def find_one(self, table_name, condition=None):
        return self.db.get_collection(table_name).find_one(condition)

    """
    功能：查询多条记录
    """
    def find_all(self, table_name, condition=None):
        return self.db.get_collection(table_name).find(condition)

    """
    功能：查询记录总数
    """
    def count(self, table_name, condition=None):
        return self.db.get_collection(table_name).count(condition)

    """
    功能：插入单条数据
    """
    def insert(self, table_name, data):
        ids = self.db.get_collection(table_name).insert(data)
        return ids

    """
    功能：删除记录
    """
    def remove(self, table_name, condition=None):
        result = self.db.get_collection(table_name).remove(condition)
        if result.get('err') is None:
            return result.get('n', 0)
        # {'ok': 1, 'n': 1}
        else:
            return None


if __name__ == '__main__':
mongo_operation.save_into_mongo('random_output.txt')
