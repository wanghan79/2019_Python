'''
姓名:王宇婷
学号：2017010886
内容：连接mongodb并操作
'''

import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
db = client['RandomData']#指定数据库
collection = db['students']
student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}
#插入数据
result = collection.insert_many([student1, student2])
print(result)
print(result.inserted_ids)
#数据更新
condition = {'name': 'Kevin'}
student = collection.find_one(condition)
student['age'] = 25
result = collection.update(condition, student)
print(result)

def save_to_mongo(ur):
    #如果插入的数据成功，返回True,并打印存储内容：否则返回False
    if db[student].insert(ur):
        print("成功存储到MongoDB",ur)
        return True
    return False