import matplotlib.pyplot as plt

import numpy as np

from pymongo import MongoClient

#from run_mongo import build

#绘制的是饼图，10万数据中int分成4段。小于25，大于25小于50，大于50小于75，大于75小于100

class matplot():

    def picture():

        k1=k2=k3=k4=0

        myclient = MongoClient("mongodb://localhost:27017/")

        mydb=myclient['python_data']

        col=mydb['sst']

        for x in col.find({},{ "int": 1 }):

            #print(x)

            if x["int"]<25:

                k1=k1+1

            elif  25<=x["int"]<50:

                k2=k2+1

            elif  50<=x["int"]<75:

                k3=k3+1

            else:

                k4=k4+1

        # Pie chart, where the slices will be ordered and plotted counter-clockwise:

        labels = 'x<25', '25<=x<50', '50<=x<75', 'x>=75'

        sizes = [k1, k2, k3, k4]

        explode = (0.1,0.05, 0.05, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')



        fig1, ax1 = plt.subplots()

        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.5f%%',

                shadow=True, startangle=90)

        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.



        plt.show()

if __name__ == '__main__':

    matplot.picture()
