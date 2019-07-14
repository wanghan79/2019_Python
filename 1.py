import random
import json
# 字典
dic = {}
# 生成随机
for i in range(100000):
    dic[i]=random.randint(0,9)
# 保存
js = json.dumps(dic)   
file = open('test.txt', 'w')  
file.write(js)  
file.close()