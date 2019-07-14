import numbers
import random
import string
import pymongo

from builtins import range
from random import randint

from filecmp import dircmp
class Generate_Data :
    '''
    Generating Random numbers
    '''
    def data_Generate (self,*args,n,size = 100000):
        for times in range(0,size):
            for types in range(len(args)):
                #print(args[types])
                if args[types] == int:
                    fir = randint(0,1000)
                    #print(fir)
                    continue
                if args[types] == float:
                    sec = random.random()
                    continue
                if args[types] == str:
                    a = string.ascii_letters
                    thir = ''
                    for l in range(n):
                        thir += random.choice(a)
                    continue
                if args[types] == dict:
                    b = string.digits
                    a = string.ascii_letters
                    c = ''.join((random.choice(a)) for j in range(5))
                    d = ''.join((random.choice(b)) for i in range(3))
                    list = [( c,d )]
                    four = dict(list) 
                    continue
            tp = (fir,sec,thir,four)
            return tp
            #print (tp)       
    
                
        
if __name__ == "__main__":
    G = Generate_Data  
    G.data_Generate(1,int,float,str,dict,n = 10)
    #print(p)
    
    
    
    
    
    
    