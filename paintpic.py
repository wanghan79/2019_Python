import seaborn as sb
# 先计算出df中col列中的值的出现次数，再绘制柱状图
sb.countplot(df['col']
#散点图
sb.jointplot(x='col1',y='col2',data=df)
# 直方图
sb.distplot(df['col'], bins=10)
