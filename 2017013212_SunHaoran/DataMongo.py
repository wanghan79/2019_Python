from pymongo import MongoClient
from RandomGenera import Generator
'''
   @ 2017013212孙浩然
'''
class mongodb(Generator):
    '''
     创建DB并导入
    '''  
    def store():
      myclient = MongoClient("mongodb://localhost:27017/")
      db_name='jesus'
      col_name='holly'
      mydb = myclient[db_name]
      mycol = mydb[col_name]
      dblist = myclient.list_database_names()
      if "jesus" in dblist:    #检测判断数据库exsitence
       print("DB ensured(ﾟДﾟ*)ﾉ")
       collist = mydb. list_collection_names()

     
      for i in range(100000):  #导入100000数据
          d=Generator().Dgenerate()
          mycol.insert_one(d)
    '''
     清除全部数据功能
    '''  
    def deletes():
      myclient = MongoClient("mongodb://localhost:27017/")
      mydb = myclient["jesus"]
      mycol = mydb["holly"]
      x = mycol.delete_many({})
      mycol.drop()
      print(x.deleted_count, "has been deleted")  
    '''
    文件运行时导入100000数据
    '''     
if __name__ == '__main__':
       mongodb.store()
