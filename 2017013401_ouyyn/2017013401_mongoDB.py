import pymongo

import urllib

import threading

from urllib import request



"""在MongoDB中，定义一个数据库"""



myclient = pymongo.MongoClient("mongodb://localhost:27017/")

db = myclient.test

collection = db['test']



"""定义一个MongoDB操作的类"""

class mongo_operation(threading.Thread):
    

    def __init__(self,num):

        threading.Thread.__init__(self)

        self.num = num



    """将100000条数据存入MongoDB"""

    def save_into_mongo(filename):

        f = open(filename, 'r')

        for i in f.readlines():

            db.students.insert({'test':i})

            r=mongo_operation(i)

            r.start()




    """查询记录总数"""

    def count(self, table, condition=None):

        try:
            
            self.db[table].count(condition)
            
            print('查找成功')
            
        except Exception as e:
            
                print(e)



    """插入单条数据"""

    def insert(self, table, data):

        try:
            
            self.db[table].insert(data)
            
            print('插入成功')
            
        except Exception as e:
            
                print(e)




    "'按条件删除记录'"
    def delete(self, table, condition, one=False):
 
         try:
             
             if one:
                 
                 self.db[table].delete_one(condition)
                 
                 print('删除成功')
                 
             else:
                 
                 result = self.db[table].delete_many(condition)
                 
                 print('删除成功')
                 
                 return result
                
         except Exception as e:
             
             print(e)



if __name__ == '__main__':

    mongo_operation.save_into_mongo('random_output.txt')
    
