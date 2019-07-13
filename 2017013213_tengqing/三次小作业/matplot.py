import random
import string
import docx
import numpy as np
from matplotlib import pyplot as plt
import pymongo


class randomdata():
    def __init__(self):
        pass

    def id_g(self,size,chars=string.ascii_letters + string.digits):
        self.size=size
        return ''.join(random.choice(chars) for x in range(self.size))

    def number(self,size=1000):
        self.size=size
        for y in range(1, self.size + 1):
            dict={}
            int_num = random.randint(1, 10000000)
            dict['int型数']=int_num
            float_number = random.uniform(0, 10000000)
            dict['float型数']=float_number
            string= self.id_g(random.randint(1, 20))
            dict['字符串']=string
            dic = {}
            b = random.randint(1, 5)
            c = 0
            while (c < b):
                d = random.randint(1, 3)
                e = random.randint(1, 3)
                if (d == 1):
                    h = random.randint(0, 10000000)
                    key = h
                elif (d == 2):
                    h = random.uniform(0, 10000000)
                    key = h
                else:
                    h = self.id_g(random.randint(1, 20))
                    key = h
                if (e == 1):
                    h = random.randint(1, 10000000)
                    value = h
                elif (e == 2):
                    h = random.uniform(0, 10000000)
                    value = h
                else :
                    h = self.id_g(random.randint(1, 20))
                    value = h
                dic[key] = value
                c = c + 1
            dict['字典']=dic
            yield  dict

rd=randomdata()
doc=docx.Document()
numberint=[]
for x in rd.number(10000):
    x=str(x)
    doc.add_paragraph(x)
doc.save('data.docx')

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["tqdb"]
mycol = mydb["sites"]
for x in rd.number(100000):
    mycol.insert_one(x)
for x in mycol.find():
    print(x)

num1=num2=num3=num4=0 #计算概率
for x in mycol.find():
    if (x['int型数'] > 0 and x['int型数'] <= 10000):
        num1 = num1 + 1
    if (x['int型数'] > 10020 and x['int型数'] <= 25000):
        num2 = num2 + 1
    if (x['int型数'] > 25000 and x['int型数'] <= 40000):
        num3 = num3 + 1
    if (x['int型数'] > 40000 and x['int型数'] <= 100000):
        num4 = num4 + 1
print(num1, num2, num3, num4)
labels = '0~10000', '10020~25000', '25000~40000', '40000~100000'
sizes = [num1, num2, num3, num4]
explode = (0, 0.1, 0, 0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.show()