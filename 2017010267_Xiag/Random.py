import random
import string
class Creat():
    def random(self):
        for i in range(1,100000):
                randomInt=random.randint(556, 102582)  # 随机整数
                randomFloat=random.random()*10  # 浮点数
                randomStr=''.join(random.sample(string.ascii_letters + string.digits,random.randint(1,10)))  # 字符串
                dict={str(randomInt):randomStr}  # 随机字典
                #tup1=(randomInt,randomFloat,randomChar,randomStr,dict)
                Person = {
                    'Int': randomInt,
                    'Float': randomFloat,
                    'Dict': dict,
                    'String': randomStr
                }
                yield Person
m=Creat()
if __name__ == '__main__':
    f = open("homework1.txt", "w")
    for i in m.random():

        s = str(i)
        f.write(s + '\n')
    f.close()