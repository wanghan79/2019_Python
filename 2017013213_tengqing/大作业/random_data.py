import random
import string
import docx

class randomdata():#随机数生成器
    def __init__(self):
        pass

    def id_g(self,size,chars=string.ascii_letters + string.digits):#生成随机长度字符串的函数
        self.size=size
        return ''.join(random.choice(chars) for x in range(self.size))

    def number(self,size=1000):
        self.size=size
        for y in range(1, self.size + 1):
            dict={}
            int_num = random.randint(1, 10000000)
            dict['int型数']=int_num#随机生成int型整数
            float_number = random.uniform(0, 10000000)
            dict['float型数']=float_number#随机生成浮点数
            string= self.id_g(random.randint(1, 20))#生成长度随机字符串
            dict['字符串']=string
            dic = {}#生成随机字典，其中内容也随机生成
            b = random.randint(1, 5)#选择生成字典内容个数
            c = 0
            while (c < b):
                d = random.randint(1, 3)
                e = random.randint(1, 3)
                if (d == 1):
                    h = random.randint(0, 10000000)
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
                key=str(key)
                dic[key] = value
                c = c + 1
            dict['字典']=dic
            yield  dict

def savedate():#将data保存至docx中
    rd=randomdata()
    doc=docx.Document()
    for x in rd.number(100000):
        x=str(x)
        doc.add_paragraph(x)
    doc.save('data.docx')

