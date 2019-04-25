import random
import string

class Generators():
    def __init__(self,size=5,total=100000):
        self.size=size
        self.total=total
    def int_generator(self):
        t=''
        for i in range(self.size):
            t += str(random.randint(1, 9))
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
                t=random.randint(1, 4)
                if t==1:
                    yield self.int_generator()
                elif t==2:
                    yield self.float_generator()
                elif t==3:
                    yield self.str_generator()
                else :
                    yield self.dict_generator()
    def print_result(self):
        for n in self.random_generator():
            print(n)
def main():
    generators=Generators(total=100000)
    generators.random_generator()
    generators.print_result()

if __name__ == '__main__':
    main()