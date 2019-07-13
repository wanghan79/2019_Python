from random_data import *
from mogondb import *
from matplot import *

if __name__ == '__main__':#调用函数完成所有功能
    rd = randomdata()#生成随机数
    savedate()#将数据保存至docx
    insert(rd)#将数据插入mogondb
    print_data()#将数据在控制台输入
    matplot()#绘制数据图像
