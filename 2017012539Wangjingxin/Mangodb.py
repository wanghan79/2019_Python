# -*- coding: utf-8 -*-
class DataStorage:
    """Store the data to mongoDB"""

    @staticmethod
    def random_data_storage(mysites, filename):  # 存储size条随机数据
        with open(filename) as file_object:
            for line in file_object:
                mysites.insert_one(eval(line))


import pymongo
