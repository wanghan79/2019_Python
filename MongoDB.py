
import pymongo
from test1111.Generate_Data import Generate_Data


 
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['runoobdb']#datasets name
mycol = mydb["sites2"]#datasets sets
 
#mydict = { "name": "Google", "alexa": "1", "url": "https://www.google.com" }

G = Generate_Data
for i in range (100000):
    a = G.data_Generate(1,int,float,str,dict,n = 10)
    #print(a)
    #items = a.strip(',').strip('\n').split('')
    mycol.insert_one({'Int':a[0],'float':a[1],'str':a[2],'dict':a[3]})
    


#x = mycol.insert_many(a)
 
#print(x.inserted_id)
