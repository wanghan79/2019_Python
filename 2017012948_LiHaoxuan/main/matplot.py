import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123456)  # 设置随机种子

fig, ax = plt.subplots()
for color in ['tab:red', 'tab:blue', 'tab:green']:
    n = 750
    x, y = np.random.rand(2, n)
    scale = 200.0 * np.random.rand(n)
    ax.scatter(x, y, c=color, s=scale, label=color,
               alpha=0.9, edgecolors='none')  # 设置范围、标签、透明度和边界颜色

ax.legend()
ax.grid(False)  # 取消网格

plt.show()