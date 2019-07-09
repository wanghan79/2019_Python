import random
import string
import os,sys
import time
import tkinter
import tkinter.messagebox

class Generators():
    #生成的数据长度为5，个数为10w
    def __init__(self,size=5,total=100000):
        self.size=size
        self.total=total
    #整型数生成器
    def int_generator(self):
        t=''
        for i in range(self.size):
            t += str(random.randint(1, 9))
        t=int(t)
        return t
    #浮点型数生成器
    def float_generator(self):
        t=round(random.uniform(0, 10),self.size)
        return t
    #字符串型生成器
    def str_generator(self):
        t=''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], self.size))
        return t
    #字典型生成器
    def dict_generator(self):
        dict={}
        k=random.choice(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'])
        v=''.join(random.sample(string.ascii_letters + string.digits, self.size))
        dict[k]=v
        return dict
    #涵盖整型、浮点型、字符串型、字典型的字典生成器
    def random_generator(self):
            while(self.total>0):
                self.total=self.total-1
                dict1 = {'int': self.int_generator(), 'float': self.float_generator(), 'str': self.str_generator(),
                        'dict': self.dict_generator()}
                yield dict1
    #结果输出
    def print_result(self):
        for n in self.random_generator():
            print(n)
    #数据写入文件
    def write_file(self):
        #进度条（获取标准输出）
        _output = sys.stdout
        count=0
        file = open('./output.txt', 'w')
        for n in self.random_generator():
            #写入一条数据
            file.write(str(n)+'\n')
            count=count+1
            # 输出进度条
            _output.write(f'\rcomplete percent:{count/1000:.0f}')
        # 将标准输出一次性刷新
        _output.flush()
    #打开文件
    def read(self):
        os.startfile('output.txt')
#主函数
def main_1():
    generators=Generators(total=100000)
    generators.random_generator()
    # generators.print_result()
    generators.write_file()
    tkinter.messagebox.showinfo("提示","数据生成完毕！")
def read_file():
    generators = Generators(total=100000)
    generators.read()
if __name__ == '__main__':
    main_1()