# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 17:15:01 2019

@author: hp
"""

# -*- coding: utf-8 -*-  
"""
Created on Sun Apr 14 17:06:13 2019

@author: hp
"""
#生成随机数
import random
import string
class Generate:
    def dic(self):
        dict={}
        k=''.join(random.sample(string.ascii_lowercase, 5))
        v=''.join(random.sample(string.ascii_letters + string.digits, 6))        
        dict[k]=v#生成字典
        return dict
    def string(self):
        s=''.join(random.sample(string.ascii_letters,6))
        #生成字符串
        return s
    def data_crecte(self):
          data={}
          data["int"]=random.randint(0,2000)
          data["float"]=random.uniform(3000,5000)
          data["string"]=self.string()
          data["dic"]=self.dic()
          #生成的字典包含整形，浮点，字符串，字典
         # yield data
          return data
if __name__ == '__main__':
    f = open("output1.txt", "w")
    for i in range(100000):
       d=Generate().data_crecte()#生成的随机数存入txt
       print(d)
       s=str(d)
       f.write(s+'\n')
    f.close()