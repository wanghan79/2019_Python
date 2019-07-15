# -*- coding: utf-8 -*-
import random
import string
def Generate_data(size=100000):
    for i in range(size):
        dic = {}
        data = {}
        data['整型'] = random.randint(0, 100000)
        data['浮点'] = random.uniform(0, 1000)
        data['字符串'] = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        dic["".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))] = "".join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(9))
        data['字典'] = dic
        yield data
f = open("gaoyl_data.txt", "w")
for i in Generate_data():
    f.write(str(i) + "\n")
f.close()