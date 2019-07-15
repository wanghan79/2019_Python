from matplotlib import pyplot as plt
from search_mgdb import search_string1
from search_mgdb import search_int1
from search_mgdb import search_float1
from search_mgdb import search_strlen1
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
def draw_bar1():
    #画条形图
    x = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    y1= search_string1()
    y =[y1["6"],y1["7"],y1["8"],y1["9"],y1["10"],y1["11"],y1["12"],y1["13"],y1["14"],y1["15"]]
    # x = [5, 8, 10]
    # y = [12, 16, 6]
    plt.bar(x, y, align='center')
    plt.title('The lenth of string')
    plt.ylabel('Y value')
    plt.xlabel('X value')
    #plt.show()
    plt.savefig("D:out1.png")
    return
def draw_scater1():
    x = search_int1()#取生成的整数
    y = search_float1()#取生成的浮点数
    plt.scatter(x,y,s=20,marker='p')#由生成的浮点数和整数画散点图
    plt.title('Scatter')
    plt.ylabel('Y value')
    plt.xlabel('X value')
    # plt.show()
    plt.savefig("D:out2.png")
    return