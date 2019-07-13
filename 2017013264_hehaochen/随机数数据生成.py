#!/usr/bin/env python
#-*-coding:UTF-8-*-

import random
import string
import decimal


        #定义一个生成随机值的类，随机值包括字典，字符，整型，浮点型


                #生成一个长度为6的字符串（大写字母和数字混合）
def string_generation(size=6,chars=string.ascii_uppercase+string.digits):
                return "".join(random.choice(chars) for _ in range(size))

        
                #生成字典数据包括其他类型随机值                
def dictionary_generation(n=100000):

                for i in range(1,n,1):
                        int_res = random.randint(0,100000)
                        float_res = round(random.uniform(0,1000),2) #保留两位浮点数
                        string_res =string_generation();
                        res = { 'credit_card_number':int_res,'money':float_res,'password':string_res}
                        yield res
        
'''
   测试时 输出到屏幕上
for res in dictionary_generation():
        print(str(res)+'\n')
'''

     #将生成的字典数据输出到文件中
file = open("output.txt","w")
for res in dictionary_generation():
          file.write(str(res)+'\n')
file.close()
