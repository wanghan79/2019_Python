import random
import string
import docx

class randomdata():
    def __init__(self):
        pass

    def id_g(self,size,chars=string.ascii_letters + string.digits):
        self.size=size
        return ''.join(random.choice(chars) for x in range(self.size))

    def number(self,size=1000):
        self.size=size
        for y in range(1, self.size + 1):
            int_num = random.randint(1, 10000000)
            float_number = random.uniform(0, 10000000)
            string= self.id_g(random.randint(1, 20))
            dic = {}
            b = random.randint(1, 5)
            c = 0
            while (c < b):
                d = random.randint(1, 3)
                e = random.randint(1, 3)
                if (d == 1):
                    h = random.randint(0, 10000000)
                    key = h
                elif (d == 2):
                    h = random.uniform(0, 10000000)
                    key = h
                else:
                    h = self.id_g(random.randint(1, 20))
                    key = h
                if (e == 1):
                    h = random.randint(1, 10000000)
                    value = h
                elif (e == 2):
                    h = random.uniform(0, 10000000)
                    value = h
                else :
                    h = self.id_g(random.randint(1, 20))
                    value = h
                dic[key] = value
                c = c + 1
            tuple=(int_num,float_number,string,dic)
            yield  tuple

rd=randomdata()
doc=docx.Document()

for x in rd.number(10000):
    x=str(x)
    doc.add_paragraph(x)
doc.save('data.docx')