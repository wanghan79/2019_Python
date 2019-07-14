import matplotlib.pyplot as plt
from pymongo import MongoClient
class matplot():
    def picture(self):
        k1 = k2 = k3 = k4 = 0
        myclient = MongoClient("mongodb://localhost:27017/")
        mydb = myclient['python_data']
        col = mydb['sst']
        for x in col.find({}, {"int": 1}):
            # print(x)
            if x["int"] < 500:
                k1 = k1 + 1
            elif 500 <= x["int"] < 1000:
                k2 = k2 + 1
            elif 1000 <= x["int"] < 1500:
                k3 = k3 + 1
            else:
                k4 = k4 + 1

        labels = 'x<500', '500<=x<1000', '1000<=x<1500', 'x>=1500'
        sizes = [k1, k2, k3, k4]
        explode = (0.1, 0.05, 0.05, 0.1)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.5f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')

        plt.show()


if __name__ == '__main__':
    matplot.picture()