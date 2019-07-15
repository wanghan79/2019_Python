
import pymongo      
import threading
from pymongo import MongoClient 

client= MongoClient('192.168.122.11', 27017)    #链接数据库主机 
db = client.randomnum                    #连接数据库 
my_set = db.random_set        #使用集合 
class mongo(threading.Thread):   

    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num

    def store("OutputNumber.txt"):      #存入数据           
        f = open("OutputNumber.txt", 'r')
        lines =f.readlines()     
        for line in lines :
            my_set.insert({'randomnum':line})
            r=mongo(1)
            r.start()

    def insert(self):      #添加数据
        int=random.randint(0,9999)
        return my_set.insert(int)
        
    def delete(self):      #删除数据
        return my_set.remove(dict)
    
    def update(self):      #更新数据
        return my_set.update(int,float,str,dict)
    
    def select(self):      #查询全部
        for i in my_set.find():     
            print(i)
        