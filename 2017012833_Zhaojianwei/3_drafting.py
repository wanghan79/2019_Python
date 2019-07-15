'''
Created on 

@author: jianweizhao
'''
import matplotlib.pyplot as plt
from prompt_toolkit.layout.utils import explode_text_fragments
import pymongo
from tensorflow.python.framework.test_ops import attr_enum_list
import numpy as np
#from curses.ascii import islower, isupper

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['runoobdb']#datasets name
mycol = mydb["sites3"]
def draft_pie_number():
    a = b = c = d = e = 0
    labels = '0<num<=200','200<num<=400','400<num<=600','600<num<=800','800<num<=1000'
    for item in mycol.find({},{"_id":0,"Int":1}):
        if 0<item['Int']<=200:
            a = a + 1
        elif 200<item['Int']<=400:
            b = b + 1
        elif 400<item['Int']<=600:
            c = c + 1
        elif 600<item['Int']<=800:
            d = d + 1
        elif 800<item['Int']<=1000:
            e = e + 1
    size = a,b,c,d,e
    colors = 'lightgreen','gold','lightskyblue','lightcoral','red'
    explode = 0,0,0,0,0
    plt.pie(size, explode = explode, labels = labels, colors = colors, autopct = '%1.1f%%', shadow = True, startangle = 50)
    plt.axis('equal')
    plt.show()

def draft_rectilinear():
    name_list = ['0~0.25','0.25~0.5','0.5~0.75','0.75~1.0']
    a_num = b_num = c_num = d_num = 0
    for item in mycol.find({},{"_id":0,"float":1}):
        if 0.0<item['float']<=0.25:
            a_num = a_num + 1
        elif 0.25<item['float']<=0.5:
            b_num = b_num + 1
        elif 0.5<item['float']<=0.75:
            c_num = c_num + 1
        elif 0.75<item['float']<=1.0:
            d_num = d_num + 1
    #print(a_num,b_num,c_num,d_num)
    num_list = [a_num,b_num,c_num,d_num]
    rects = plt.bar(range(len(num_list)),num_list,color = 'rgby')
    
    index = [0,1,2,3]
    index = [float(i) + 0.4 for i in index]
    plt.ylim(ymax = 26000,ymin = 0)
    plt.xticks(index,name_list)
    plt.ylabel("All number")
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2,height,str(height),ha = 'center',va = 'bottom')
    plt.show()

def draft_pie_charcter():
    low_f  = low_s = upper_f = upper_s = 0
    labels = 'lowercase_a-m','lowercase_m-z','uppercase_A-N','uppercase_M-Z'
    for item in mycol.find({},{"_id":0,"str":1}):
        str = item['str']
        for i in str:
            if i >= 'a' and i <= 'm':
                low_f += 1
            elif i >= 'n' and i <= 'z':
                low_s += 1
            elif i >= 'A' and i <= 'M':
                upper_f += 1
            elif i >= 'N' and i <= 'Z':
                upper_s += 1
    size2 = low_f,low_s,upper_f,upper_s
    colors = 'lightgreen','gold','lightskyblue','lightcoral'
    explode = 0,0,0,0
    plt.pie(size2, explode = explode, labels = labels, colors = colors, autopct = '%1.1f%%', shadow = True, startangle = 50)
    plt.axis('equal')
    plt.show()


def draft_linechart():
    int_label = []
    float_label = []
    flag = 0
    for item in mycol.find({},{"_id":0,"Int":1,"float":1}):
        flag += 1
        if flag >= 50000 and flag <= 50100:
            int_label.append(item['Int'])
            float_label.append(item['float'])
            int_label.sort(key=None, reverse=False)
            float_label.sort(key=None, reverse=False)
    plt.figure(figsize=(8,4))
    plt.plot(int_label,float_label,"b--",linewidth=1)
    plt.xlabel("Int")
    plt.ylabel("Float")
    plt.title("locateion")
    plt.show()


def draft_scatter():
    int_label = []
    float_label = []
    flag = 0
    for item in mycol.find({},{"_id":0,"Int":1,"float":1}):
        flag += 1
        if flag >= 40000 and flag <= 41000:
            int_label.append(item['Int'])
            float_label.append(item['float'])
    n = len(int_label)
    x2 = np.random.uniform(0,1000, n)
    y2 = np.array([0.5] * n)
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.set_title('Result Analysis')
    ax1.set_xlabel('Int') 
    ax1.set_ylabel('Float')
    ax1.scatter(int_label, float_label, s=10, c='k', marker='.')
    ax1.plot(x2, y2, c='b', ls='--')
    plt.xlim(xmax=1000, xmin=0)
    plt.show()
    
if __name__ == "__main__":
    draft_pie_number()
    draft_rectilinear()
    draft_pie_charcter()
    draft_linechart()
    draft_scatter()


    
