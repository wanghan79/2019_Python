# coding=gbk
'''

@author: jianweizhao
'''
from test1111.MongoDB import creat_database
from test1111.drafting import *




def Main():
    while(True):
        print("Welcome!Please select what you want do")
        print("1:生成随机数并存入数据库")
        print("2:生成相关图像")
        print("3.退出")
        select = input("select:")
        print(select)
        if select == '1':
            leave = input("if you want to leave: 1-leave \ 0-continue:")
            if leave == '1':
                continue;
            elif leave == '0':
                name = input("please input dataset's name:")
                site = input("please input site's name")
                creat_database(name,site)  
        elif select == '2':
            while(True):
                print("1:查看整数分布" + "\n" + "2.查看浮点数分布" + "\n" + "3.查看字符串中大小写字母分布" + "\n" + "4.折线图" + "\n" + "5.散点图" + "\n" + "6.离开")
                choose = input("Your choose:")
                if choose == '1':
                    draft_pie_number()
                elif choose == '2':
                    draft_rectilinear()
                elif choose == '3':
                    draft_pie_charcter()
                elif choose == '4':
                    draft_linechart()
                elif choose == '5':
                    draft_scatter()
                elif choose == '6':
                    break;
        elif select == '3':
            print("Thanks")
            exit()

if __name__ == "__main__":
    Main()     
        
