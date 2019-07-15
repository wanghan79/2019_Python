import mongoZZJ as mg
import randomZZJ as rd
import matplotlibZZJ as mplt
mg.test()
rd.test()
mplt.test()
"""
将生成的随机数据传入数据库，并将数据库内容保存一份在dataDB.txt中
"""
for data in rd.data_creat():
    mg.insertDB(data)
print('insert finished!')
mg.saveALL()

"""
从数据库中读取数据
"""
for data in mg.loadDB():
    mplt.getValues(data)
print('yvalue is sended')

"""
进行绘图
"""
mplt.plotInit()