#导入相关的库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

"""折线图"""
np.random.seed(100)#随机数种子
#输入相关数据
df = pd.DataFrame(np.random.randint(-10, 10, (10, 3)), index=pd.date_range("1/1/2000", periods=10), columns=list("ABC"))
df = df.cumsum()
df.head()
df.plot()#默认情况下画图
df.plot(x="A", y="C")#指定x轴和y轴

"""柱状图"""
df.plot(kind="bar")
df.plot(kind="barh")#转换方向
df.plot(kind="bar", x="A", y=["B", "C"])#指定x轴和y轴
df.plot(kind="bar", stacked=True)#生成堆叠条形图

"""直方图"""
df.plot(kind="hist")
df.plot(kind="hist", bins=5)#改变参数

"""箱线图"""
df.plot(kind="box")

"""区域图"""
df.abs().plot(kind="area")
df.plot(kind="area", stacked=False)#生成不堆积的区域图

"""散点图"""
df.plot(kind="scatter", x="A", y="B")
df.plot(kind="scatter", x="A", y="B", c="C")#生成带颜色的散点图
ax = df.plot(kind="scatter", x="A", y="B", color="blue")#在单个轴上绘制多个列组
df.plot(kind="scatter", x="C", y="B", color="green", ax=ax)

"""饼图"""
a = df.A[:5]
a.abs().plot.pie(subplots=True, figsize=(4, 4))
a.abs().plot.pie(subplots=True, figsize=(4, 4), autopct="%.2f")#自动计算比例

"""六边形容器图"""
df = pd.DataFrame(np.random.randn(1000, 2), columns=["A", "B"])
df["B"] = df["B"] + np.arange(1000)
df.plot(kind="hexbin", x="A", y="B", gridsize=10)
df.plot(kind="hexbin", x="A", y="B", gridsize=20)#改变参数gridsize


