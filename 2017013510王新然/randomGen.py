import string
import random

class Generator:
    def dataGenerate():
        size=100000
        for i in range(size):
            dic = {}
            value=random.randint(1, 10000)
            key=''.join(random.sample(tuple(string.ascii_lowercase + string.digits), 10))
            dic[key]=value
            data=(random.randint(1, 10000),round(random.uniform(1, 1000), 5),
                ''.join(random.sample(tuple(string.ascii_lowercase + string.digits), 10)),dic)
            yield data

if __name__ == '__main__':
    f = open("data.txt", "w")
    for i in Generator.dataGenerate():
        s=str(i)
        f.write(s+'\n')
    f.close()


