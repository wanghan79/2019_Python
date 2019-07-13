from dataGenerate import *
from db import *
from graphShow import *

#从数据库中导出dict，画出把dict的各个value的绝对值对17取模后得到的各个数的数量的折线图

class DBPlot(Plot):
    def __init__(self): #重写构造方法
        self.intResults = []
        self.res = []
        for i in range(17):
            self.res.append(0)
        for x in mycol.find():
          for y in list(x.values()):
            if type(y) == type(1):
                self.intResults.append(abs(y)%17)

mainpt = DBPlot()
mainpt.plotGraph()
