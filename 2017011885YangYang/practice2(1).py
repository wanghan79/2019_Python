""" 
@author:杨洋

 """ 

import pymongo  
import random
client = pymongo.MongoClient(host='localhost', port=27017) 
db = client['my_db']
collection = db['my_collection']
count = 0
while (count < 9999):
        a = random.uniform(10, 30)     #控制随机数的精度round(数值，精度)
        b = random.randint(1, 100)
        c= random.choice(['sdfdfd', 'dfdf', 'sdf','dfjie','fefe','fkeofke','foef','fjijf','iejfi']) 
        stuInfo = {"student"+str(i):random.randint(60,100) for i in range(1)}
        randomNumber = {
                        'num':count,
                        'int': a,
                        'float':b,
                        'string': c,
                        'dict': stuInfo
                    }
        result = collection.insert_one(randomNumber)     #插入
        count = count + 1
results = collection.find({'string': 'dfdf'})  #查询符合条件的数据
print(results)  
for result in results:  
    print(result) 

 
