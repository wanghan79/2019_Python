import random
import string
class data_generator:
 #随机生成整型
 ans_int=random.randint(0,100000000)
 print(ans_int)

  #随机生成浮点型
 ans_float=random.uniform(0,10000000)
 print(ans_float)

#随机生成字符串
 key=[]
 def getKey():
   key=random.sample(string.ascii_letters,10)
   keys="".join(key)
   return keys
   print(data_generator().getKey())

  #随机生成标点字符串
 dic_sym="".join(random.sample(',./;[]\""''!@#$%^&*()_+-=/',10)).replace(" ","")
 print(dic_sym)

  #随机生成混合型
 def Mulans(count=100000):
   for i in range(count):
    src_digits = string.digits              #数字
    src_uppercase = string.ascii_uppercase  #大写字母 
    src_lowercase = string.ascii_lowercase  #小写字母 
    src_special = string.punctuation  
    
    num = random.sample(src_digits,2) 
    lower = random.sample(src_uppercase,2) 
    upper = random.sample(src_lowercase,2) 
    special = random.sample(src_special,2)  
    other = random.sample(string.ascii_letters+string.digits+string.punctuation,2)
    
    ans_list = num + lower + upper + special + other
    random.shuffle(ans_list)
    ans_str = ''.join(ans_list)
    print(ans_str)
    file = open("Random_ans.txt", "a")
    file.write(str(ans_str)+'\n')
    file.close()
    
 Mulans()

