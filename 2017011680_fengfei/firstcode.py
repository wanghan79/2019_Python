import random
import string
class CreateNumber(object):
    #def __init__(self):
    def ReturnInt(self):
        start = random.randint(0,100)
        end = random.randint(100,200)
        return random.randint(start,end)
    def ReturnFloat(self):
        start = random.randint(0, 100)
        end = random.randint(100, 200)
        return random.uniform(start,end)
    def ReturnStr(self,chars = string.ascii_letters + string.digits):
        size = random.randint(6,15)
        return ''.join(random.sample(string.ascii_letters + string.digits,size))
    def ReturnDct(self):
        Ksize = random.randint(6,15)
        ValueSize = random.randint(6,15)
        key = ''.join(random.sample(string.ascii_letters + string.digits,Ksize))
        value = ''.join(random.sample(string.ascii_letters + string.digits,ValueSize))
        Dect={key:value}
        return Dect
    def ReturnRes(self,Size):
         for i in range(1,Size):
            dect = {'id': i, 'int': self.ReturnInt(),'float': self.ReturnFloat(),'string': self.ReturnStr(), 'dic': self.ReturnDct()}
            yield dect
