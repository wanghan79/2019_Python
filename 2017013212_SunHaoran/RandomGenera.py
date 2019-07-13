import random
import string
'''
   @ 2017013212孙浩然
'''
class Generator:

  '''    
    四种数据生成
  '''      
  def Dgenerate(self):
    g={}
    g["int"]=random.randint(0,100000)  #生成int
    g["float"]=random.uniform(0,100000)#生成float
    g["string"]=self.string()          #调用生成string
    g["dict"]=self.dict()              #调用生成dict
    return g
    #string生成   
  def string(self):
    s=''.join(random.sample(string.ascii_letters,4))
    return s 
    #dict生成    
  def dict(self):
    di={}
    key=''.join(random.sample(string.ascii_lowercase, 7))
    val=''.join(random.sample(string.ascii_letters + string.digits, 8))        
    di[key]=val
    return di      

  '''
    文件运行时打印100000数据
  '''
if __name__ == '__main__':
    f = open("outputdata.txt", "w")
    for i in range(100000):
       o=Generator().Dgenerate()
       
       print(o)
       s=str(o)
       f.write(s+'\n')
    f.close()
