import numpy as np


import random
import string

##生成一个长度为 length 的字符串
def randomString():
    length = 8
    return ''.join(random.sample(string.ascii_letters + string.digits, length))

##生成长度为 length 个数据 ， 数据范围在 [start, stop]之间
def randomList(start , stop, length):
    length = int(length)
    if int(start) > int(stop): #当start > stop时交换两个值，保证start < stop
         tmp = start
         start = stop
         stop = tmp
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

class dataGenerate:
    def dGen(self, size=100000):
        for i in range(size):
            numkeys = randomList(0, 100, 10)
            numvalues = randomList(0, 100, 10)
            numdictionary = dict(zip(numkeys, numvalues))
            numint = np.random.randint(0, 100)
            numfloat = np.random.uniform(0, 10000)
            numstring = randomString()

            data = {'string':numstring, 'int':numint, 'float':numfloat, 'dictionary':numdictionary }
            yield data  ##使用yield


if __name__ == '__main__':
    f = open("output.txt", "w")     #打开文件
    num = 1
    for item in dataGenerate().dGen():
        s = str(item)
        f.write('第 {0:10d} 条数据'.format(num) + s +'\n')      #将输出结果输出到 output.text 文件中
        num = num + 1
    f.close()