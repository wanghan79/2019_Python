'''
姓名:王宇婷
学号：2017010886
内容：产生100000个随机数
'''

import random

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