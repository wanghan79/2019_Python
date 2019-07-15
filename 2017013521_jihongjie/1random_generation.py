#!/usr/bin/python
#-*-coding:UTF-8-*-

import string
import random
import uuid

"""
定义一个数据生成的类，实现各数据类型数据生成，最后以字典存入.txt
"""

class data_generator:
        
    """
    功能：随机生成范围为1~100001的不重复的整数，记为'stu_number'
    """
    def int_generator(self):
        return random.sample(range(1,100001),1)

    '''
    功能：随机生成指定范围的精度为2位小数的浮点数，记为'height'
    '''
    def float_generator_height(self):
        if(random.random()*100+120) < 250:
            return round(random.random()*100+120,2)
    '''
    功能：随机生成指定范围的精度为4位小数的浮点数，记为'weight'
    '''
    def float_generator_weight(self):
        if (random.random()*150) < 200:
            return round(random.random()*100,4)
        
    '''
    功能：随机生成长度为6，由大写字母和数字组成的字符串，记为'password'
    '''
    def str_generator(self,string_length=6):
        random = str(uuid.uuid4())
        random = random.upper()
        random = random.replace("-", "")
        return random[0:string_length]

    '''
    功能：随机生成100000个字典数据
    '''
    def dic_generator(self,n = 100000):
        for i in range(n):
            int_data = self.int_generator()
            height_data = self.float_generator_height()
            weight_data = self.float_generator_weight()
            string_data = self.str_generator()
            data = {'stu_number':int_data,'height':height_data,'weight':weight_data,'password':string_data}
            yield data



if __name__ == '__main__':
    '''
    创建一个文件，将数据写入文件
    '''
    file = open("random_output.txt", "w")
    for data in data_generator().dic_generator():
        file.write(str(data)+'\n')
file.close()
