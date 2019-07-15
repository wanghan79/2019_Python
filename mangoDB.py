import pymongo
import random
client = pymongo.MongoClient('mongodb')
db = myclient.list

from pymongo import MongoClient
db = myclient.test  
my_set = db.test_set
with open('ans.txt', 'r') as f:
    for line in f.readlines():    
        ans.insert({ 'ans':1})

********************************
增
********************************
use tblorders;
 
db.tblorders.insert( {sfbshfi" } );
db.tblorders.insert( { "4089902"} );
db.tblorders.find();
********************************
删
********************************
#删除满足该条件的一行
db.tblorders.update({ "id": 1 }, { $unset: {"naje" : 1} }) ;
********************************
改 
********************************
#将所有ocpyang更新为Atalas 
db.tblorders.update({ name: "ocpyang" }, { $set: {name: "Atalas"} },false,true) ;
 
********************************
查
********************************

#方法1
db.tblorders.find();
 
#方法2
db.tblorders.find({"kiki"});
 
#方法3
db.tblorders.find({"kiki"}).limit(1);
 
#方法4
db.tblorders.find({"kiki"}).forEach(printjson);
