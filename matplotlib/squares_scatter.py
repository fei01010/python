import matplotlib.pyplot as plt

x_value = [1, 2, 3, 4, 5]
y_value = [1, 4, 9, 16, 25]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.scatter(x_value, y_value, s=100)

# 设置图题并给坐标轴打上标签
ax.set_title("Square Number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Number", fontsize=14)

# 设置刻度标记的样式
ax.tick_params(labelsize=14)

plt.show()