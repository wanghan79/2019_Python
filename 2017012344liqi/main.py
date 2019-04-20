#-*-coding:utf-8-*-
#代码运行环境python3.6
from Create import Generate
f = open("output.txt", "w")#以写的形式打开文件
for i in Generate.Ggenerate_text(100000):
    f.write(str(i) + "\n")#将随机生成的数据写入文件
f.close()  # 关闭文件