import matplotlib.pyplot as plt
from connect_to_mongodb import db


def plot():
    # 数据可视化
    plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
    label = ['0-25', '25-50', '50-75', '75-100']
    explode = [0.1, 0, 0, 0]
    value = [db.count({'value': {'$gte': i, '$lt': (i+1)*25}}) for i in range(0, 4)]
    plt.pie(value, explode=explode, labels=label, autopct='%1.1f%%')  # 绘制饼图
    plt.title('0-100区间分布饼图')  # 绘制标题
    plt.savefig('./0-100区间分布饼图')  # 保存图片
    plt.show()

