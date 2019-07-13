import random
f = open('result.txt', 'w')

'''随机生成包含int、float、str、dict的多维数据'''
class DataGenerate:
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
        if x == 1:      #generate int
            return random.randint(-1000000000, 1000000000)
        elif x == 2:    #generate float
            return random.uniform(-1000000000, 1000000000)
        elif x == 3:    #generate string
            str = ''
            strSize = random.randint(6, 10)
            for j in range(strSize):
                str += random.choice(self.chars)
            return str

    def datagenerate(self):         #生成器函数
        for i in range(100000):
            #在本文件中需生成前三种
            #在db.py中调用时只生成dict
            if __name__ == "__main__":
                for x in [1, 2, 3]:
                    yield self.datagenerateIntFloatStr(x)
            #生成字典类型元素
            d = dict()
            dictSize = random.randint(3, 6)
            for j in range(dictSize):
                keyOfj = self.datagenerateIntFloatStr(3)
                valueOfj = self.datagenerateIntFloatStr(1)
                d[keyOfj] = valueOfj
            yield d

if __name__ == "__main__" :
    sampleOfDataGenerate = DataGenerate()
    results = sampleOfDataGenerate.datagenerate()
    num = 0
    #输出到文件，每行有一个int，一个float，一个string和一个dict
    for result in results:
            print(result, file = f, end = '    ')
            num = num + 1
            if num % 4 == 0:
                print("", file = f)
    f.close()
