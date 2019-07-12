import random
import string
#随机生成需包含整型，浮点型，字符型，字典型
class DataGenerate:
    def dgenerate (size=100000):#生成100000个数据
        dict={'Charles':5,'Mark':4,'Bill':7,'Vincent':12,'William':3,'Joseph':7, 'James':8,'Henry':9,'Gary':6,'Martin':23,   	'Malcolm':24,'Joan':14,'Niki':25,'Betty':14,'Linda':14,'Whitney':15,'Lily':17,'Albert':18,'Kevin':19,'Michael':19}#字典
        for i in range(size):
            a = random.randint(1,100000)
            b = random.uniform(1,100000)#从1到100000中随机浮点型
            c = ''.join(random.sample(string.ascii_letters + string.digits,4))#随机4个字符
            d = random.sample(dict.items(),1)#随机选取一个键值对
            x = {
                '整型':a,
                '浮点型':b,
                '字符型':c,
                '字典型':d,
                }
            yield x
    f = open('randomoutput.txt','w')#打开randomoutput文档
    for i in dgenerate():
        r = str(i)
        f.write(r + '\n')#将数据存入
    f.close()#关闭文档
