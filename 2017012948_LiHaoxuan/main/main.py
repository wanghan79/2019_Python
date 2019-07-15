from randomD import DataGenerate
import MongoDB
import matplot

if __name__ == '__main__':
    rd = DataGenerate()  # 生成随机数
    DataGenerate.savedate()  # 将数据保存到文件
    MongoDB.insert(rd)  # 将数据插入mogondb
    matplot()  # 绘制数据图像
