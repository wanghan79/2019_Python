import numpy as np
import random
import string
import  math

def random_list( start, stop, length):
    if length >= 0:
        length = int(length)
        start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
        random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

class DataCreat:
    def Creat(self, size=100000):
        for i in range(size):
            keys = random_list(0, 1000, 10)
            values = random_list(0, 1000, 10)
            dictionary = dict(zip(keys, values))
            Number = np.random.randint(0, 1000)
            Str = ''.join(random.sample(string.ascii_letters + string.digits, 12))  # Generate a random string
            data = {'string': Str, 'int':Number, 'float': np.random.uniform(0, 1000000),'dictionary':dictionary}
            yield data

if __name__ == '__main__':
    f = open("output.txt", "w")
    for i in DataCreat().Creat():
       S=str(i)
       f.write(S+'\n')
    f.close()