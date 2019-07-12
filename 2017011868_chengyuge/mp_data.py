import numpy
import matplotlib
import pymongo
from matplotlib import pyplot as plt
import pylab
class search_db():
    def __init__(self):
        pass;
    def connect_db(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["cyg_database"]
        self.mycol = mydb["RandomNumbers"]   
    def Bar(self):
        y={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
        for x in self.mycol.find({},{"_id":0,"content.int":1}):
            num=int(x["content"]["int"]/10000)
            y[num]=y[num]+1
        x1=[1,3,5,7,9]
        x2=[2,4,6,8]
        y1=[y[1],y[3],y[5],y[7],y[9]]
        y2=[y[2],y[4],y[6],y[8]]
        plt.bar(x1, y1, align='center')
        plt.bar(x2, y2, color='g', align='center')
        plt.title('Bar graph')
        plt.ylabel('Y axis')
        plt.xlabel('X axis')
        plt.show()
    def Scatter(self):
        x1=[]
        y1=[]
        for x in self.mycol.find({}, {"_id": 0, "content.int": 1}).limit(50000):
            x1.append(x["content"]["int"])
        for y in self.mycol.find({}, {"_id": 0, "content.int": 1}).limit(50000).skip(50000):
            y1.append(y["content"]["int"])
        pylab.scatter(x1, y1)
        pylab.show()
def main_3():
    data=search_db()
    data.connect_db()
    data.Bar()
    data.Scatter()
if __name__ == '__main__':
    main_3()