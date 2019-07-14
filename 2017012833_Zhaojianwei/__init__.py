from _ctypes import sizeof
from _operator import index
a = [15,26,83,46,50,65,72,81,99,10];
def __found_number( b):
    for index in range(len(a)):
        print("i = ",a[index])
        if a[index] == b:
            return index
        elif a[index]!=b:
            index = -1
    return index 
def __found_number2(c):
    for index, it in enumerate(a):
        print("it =",it)
        if it == c:
            return index
        elif it != c: 
            index = -1
    return index   
    
 
if __name__ == "__main__":
   g = __found_number(51)
   h = __found_number2(50)
   print("kkk",g,h)     
    