from config import*

import string,random
    
class randomGenerate:
    
    "'生成列表'"
    
def create_list():
    
    tmp=string.ascii_letters +string.digits
    
    "生成1—10长度的字符串"
    
    value=''.join(random.sample(tmp,random.randint(1,10)))
    
    list=[]
    
    list.append(value)
    
    return list
    

"在字典中分别插入整数、浮点数、列表"

def get_dic():
    
    k=100000
    
    count=0
    
    while count <= k:

        data1=create_list()
        
        data={'data1':data1,'data2':random.randint(100,200),'data3':random.random()}
        
        yield data

        count += 1
        

if __name__ == '__main__':

    "创建文件，把数据写入文件"

output = open("random_output.txt","w")

for res in get_dic():

    output.write(str(res)+'\n')

output.close()

