from dataGenerate import *
import matplotlib.pyplot as plt

#对于随机正整数，画出对17取模后得到的各个数的数量折线图

class IntGenerate(DataGenerate):    #IntGenerate 是 DataGenerate的子类,生成随机整数的绝对值对17取模的结果
    def intgenerate(self):
        for i in range(100000):
            yield abs(self.datagenerateIntFloatStr(1)) % 17   #生成整数
            
sampleOfIntGenerate = IntGenerate()
intResults = sampleOfIntGenerate.intgenerate()
res = []
for i in range(17):
    res.append(0)
for intResult in intResults:
    res[intResult] += 1
plt.plot(res)
plt.show()

