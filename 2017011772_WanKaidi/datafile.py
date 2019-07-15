import numpy as np
import random
import string

def random_list( start, stop, length):
    if length >= 0:
        length = int(length)
        start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
        random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

class dataGenerate:
    def dGen(self, size=1000):
        for i in range(size):
            keys = random_list(0, 100, 1)
            values = random_list(0, 100, 1)
            dictionary = dict(zip(keys, values))
            numx = np.random.randint(0, 1000)
            numy = np.random.randint(0, 1000)
            salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))  # Generate a random string
            data = {'string': salt, 'intX': numx, 'intY': numy, 'float': np.random.uniform(0, 1000000), 'keys': keys, 'values': values}
            yield data

if __name__ == '__main__':
    f = open("output.txt", "w")
    for i in dataGenerate().dGen():
       s=str(i)
       f.write(s+'\n')
    f.close()