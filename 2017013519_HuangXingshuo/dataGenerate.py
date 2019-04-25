"""
author : 黄星朔

"""
import random
f = open('result.txt', 'w')
class DataGenerate:
    '''随机生成包含int、float、str、dict的多维数据'''
    def __init__(self):
        self.dataChoices = [1, 2, 3, 4]    #分别代表四种数据类型
        self.p = 0
        self.chars = []               #可以选取的字符集合
        for i in range(ord('a'), ord('z')):
            self.chars.append(chr(i))
        for i in range(ord('A'), ord('Z')):
            self.chars.append(chr(i))
        for i in range(ord('0'), ord('9')):
            self.chars.append(chr(i))
        self.num = 0
    def datagenerateIntFloatStr(self, x):       #生成生成器函数中的int，float和string类型元素
        if x == 1:
            return random.randint(-1000000000, 1000000000)
        elif x == 2:
            return random.uniform(-1000000000, 1000000000)
        elif x == 3:
            str = ''
            strSize = random.randint(1, 16)
            for j in range(strSize):
                str += random.choice(self.chars)
            return str

    def datagenerate(self):         #生成器函数
        for i in range(100000):
            x = random.choice(self.dataChoices)
            self.num += 1
            if x == 1:
                print(self.num, 'int :', end = " ", file = f)
            elif x == 2:
                print(self.num, 'float :', end = " ", file = f)
            elif x == 3:
                print(self.num, 'str :', end = " ", file = f)
            elif x == 4:
                print(self.num, 'dict :', end = " ", file = f)
            if x < 4:
                yield self.datagenerateIntFloatStr(x)
            else:                   #生成字典类型元素
                d = dict()
                dictSize = random.randint(1, 10)
                for j in range(dictSize):
                    keyTypeOfj = random.choice(self.dataChoices[0:3])
                    valueTypeOfj = random.choice(self.dataChoices[0:3])
                    keyOfj = self.datagenerateIntFloatStr(keyTypeOfj)
                    valueOfj = self.datagenerateIntFloatStr(valueTypeOfj)
                    d[keyOfj] = valueOfj
                yield d


def main():
    sampleOfDataGenerate = DataGenerate()
    results = sampleOfDataGenerate.datagenerate()
    for result in results:
        print(result, file = f);
    f.close()
main()
