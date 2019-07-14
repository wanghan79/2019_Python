from Random_number import Generate
from pymongo import MongoClient
class mongo(Generate):
    def build(self):
        db_name='python_data'
        col_name='sst'
        myclient = MongoClient("mongodb://localhost:27017/")
        mydb=myclient[db_name]
        dblist = myclient.list_database_names()
        if "python_data" in dblist:
          print("exist")
        else:
          print("no exist")
        col=mydb[col_name]
        collist = mydb.list_collection_names()
        if "sst" in collist:
           print("exist")
        else:
           print("no exist")
        for i in range(100000):
          d=Generate().data_crecte()
          col.insert_one(d)
if __name__ == '__main__':
    mongo.build()