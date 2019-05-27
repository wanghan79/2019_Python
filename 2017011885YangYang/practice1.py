# -*- coding: utf-8 -*-
"""
Created on Wed May 22 18:56:52 2019

@author: apple
"""
import random
stuInfo = {"student"+str(i):random.randint(60,100) for i in range(20)}
print({name:score for name,score in stuInfo.items() if score>90})##生成字典

for i in range(100000):        #生成随机数，浮点类型
    a = random.uniform(10, 30)     #控制随机数的精度round(数值，精度)
    b = random.randint(1, 100)
    c= random.choice(['sdfdfd', 'dfdf', 'sdf','dfjie','fefe','fkeofke','foef','fjijf','iejfi'])
    print(str(round(a,4))+'  '+str(b) +'  ' +str(c) +"  "+ " cat" +str(i) )
    highScore = {}
    for name, score in stuInfo.items():
        if score > 60:
            highScore[name] = score
    print(highScore)
    
