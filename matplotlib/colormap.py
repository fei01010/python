import matplotlib.pyplot as plt

x_value = range(1, 1001)
y_value = [x**2 for x in x_value]
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, s=10)

# 设置图题并给每一个坐标轴打上标签
ax.set_title("Square Number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Number",fontsize=14)

# 设置刻度标记的样式
ax.tick_params(labelsize=14)

plt.show()

"""
要了解 pyplot 中所有的颜色映射，请访问 Matplotlib 主页并单
击 Documentation。在 Learning resources 部分找到 Tutorials 并单击其中
的 Introductory tutorials, 向下滚动到 Colors, 再单击 Choosing
Colormaps in Matplotlib。
"""