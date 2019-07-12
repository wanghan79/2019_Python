'''
姓名:王宇婷
学号：2017010886
内容：总结
'''

import random
import pymongo
import numpy as np
import matplotlib.pyplot as plt
#生成随机数
dict = {'type': 'data', 'mount': 10000, 'color': 'black'}
f = open('RandomData.txt', 'w') #即将生成的数据存入此文件
for i in range (0,100000):
    resultList = [];
    a = random.randint(0, 100)
    b = random.random()
    c = random.choice(['I', 'love','python','he','is','handsome'])
    d = random.sample(dict.items(),1)
    resultList.append(a)
    resultList.append(b)
    resultList.append(c)
    resultList.append(d)
    print(resultList)
    r=str(resultList)
    f.write( r + '\n')  # 将数据存入
f.close()
#连接数据库
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

#client = pymongo.MongoClient('localhost', 27017)
#db = client['RandomData']#指定数据库
table = db['RandomData']


# 读取数据
data = pd.DataFrame(list(table.find()))

#显示的数据
N = 1000
x = np.random.randn(N)
y = np.random.randn(N)
plt.scatter(x, y,alpha=0.5,edgecolors= 'white')
plt.show()