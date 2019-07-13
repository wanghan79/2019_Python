from dataGenerate import *
#对于随机正整数，画出对17取模后得到的各个数的数量折线图
import matplotlib.pyplot as plt
class IntGenerate(DataGenerate):    #IntGenerate 是 DataGenerate的子类,生成随机整数的绝对值对17取模的结果
    def intgenerate(self):
        for i in range(100000):
            yield abs(self.datagenerateIntFloatStr(1)) % 17   #生成整数
class Plot:
    def __init__(self):
        self.sampleOfIntGenerate = IntGenerate()
        self.intResults = self.sampleOfIntGenerate.intgenerate()
        self.res = []
        for i in range(17):
            self.res.append(0)
    def plotGraph(self):
        for intResult in self.intResults:
            self.res[intResult] += 1
        plt.plot(self.res)
        plt.show()

if __name__ == '__main__':
    pt = Plot()
    pt.plotGraph()
