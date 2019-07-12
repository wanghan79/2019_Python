import random
import string
import os,sys
import time
import tkinter
import tkinter.messagebox
class Generators():
    def __init__(self,size=5,total=100000):
        self.size=size
        self.total=total
    def int_generator(self):
        t=''
        for i in range(self.size):
            t += str(random.randint(1, 9))
        t=int(t)
        return t
    def float_generator(self):
        t=round(random.uniform(0, 10),self.size)
        return t
    def str_generator(self):
        t=''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], self.size))
        return t
    def dict_generator(self):
        dict={}
        k=random.choice(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'])
        v=''.join(random.sample(string.ascii_letters + string.digits, self.size))
        dict[k]=v
        return dict
    def random_generator(self):
            while(self.total>0):
                self.total=self.total-1
                dict1 = {'int': self.int_generator(), 'float': self.float_generator(), 'str': self.str_generator(),
                        'dict': self.dict_generator()}
                yield dict1
    def print_result(self):
        for n in self.random_generator():
            print(n)
    def write_file(self):
        _output = sys.stdout
        count=0
        file = open('./output.txt', 'w')
        for n in self.random_generator():
            file.write(str(n)+'\n')
            count=count+1
            _output.write(f'\rcomplete percent:{count/1000:.0f}')
        _output.flush()
    def read(self):
        os.startfile('output.txt'）
def main_1():
    generators=Generators(total=100000)
    generators.random_generator()
    generators.write_file()
    tkinter.messagebox.showinfo("提示","生成完毕！")
def read_file():
    generators = Generators(total=100000)
    generators.read()
if __name__ == '__main__':
    main_1()