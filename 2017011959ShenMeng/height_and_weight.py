#!/usr/bin/python
#-*-coding:UTF-8-*-
"""
姓名：沈萌
学号：2017011959
"""


import ast

filename = 'random_output.txt'
'''
实现将random_output.txt中height和weight的值取出来存入新的名为visual_data.txt文件中以备之后的可视化操作
'''
def save_list(filename):
    result = []
    file = open(filename)
    for line in file:
        dict = ast.literal_eval(line)
        result = tuple(dict.values())
        yield result



if __name__ == '__main__':
    newfile = open('visual_data.txt','w')
    for result in save_list(filename):
        final_result1 = result[1]
        final_result2 = result[2]
        newfile.write(str(final_result1)+' '+str(final_result2)+'\n')
    newfile.close()
