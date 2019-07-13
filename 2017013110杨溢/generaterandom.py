import random
import string
import docx
import numpy as np
from matplotlib import pyplot as plt

class Generaterandom():
    def __init__(self):
        pass

    def dict_generator(self,size,chars=string.ascii_letters + string.digits):#生成随机字典
        dict = {}
        k = ''.join(random.choice(chars) for x in range(self.size))
        v = ''.join(random.sample(string.ascii_letters + string.digits, self.size))
        dict[k] = v
        return dict

    def id_g(self,size,chars=string.ascii_letters + string.digits):#生成随机字符串
        self.size=size
        return ''.join(random.choice(chars) for x in range(self.size))

    def number(self,size=1000):
        self.size=size
        for y in range(1, self.size + 1):
            dict={}
            int_num = random.randint(1, 10000000)#生成int型数字
            dict['int']=int_num
            float_number = random.uniform(0, 10000000)#生成float型数字
            dict['float']=float_number
            string= self.id_g(random.randint(1, 20))#生成字符串
            dict['str']=string
            dic = self.dict_generator(random.randint(1, 20))
            dict['dictionary']=dic
            yield  dict

def save():#保存在txt中
    rd=Generaterandom()
    file = open('./output.txt', 'w')
    for x in rd.number(100000):
        file.write(str(x)+'\n')
    file.close()