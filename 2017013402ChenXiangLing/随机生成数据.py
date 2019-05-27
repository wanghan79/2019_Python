import random

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
for i in range (0,100000):
    resultList = [];
    a=random.random()
    b=random.randint(1, 10)
    c=random.choice(['剪刀', '石头', '布','I','love','python'])
    d = random.sample(dict.items(),1)
    resultList.append(a)
    resultList.append(b)
    resultList.append(c)
    resultList.append(d)
    print(resultList)\

