import matplotlib.pyplot as plt

x_value = range(1, 1001)
y_value = [x**2 for x in x_value]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.scatter(x_value, y_value, s=10)

# 设置图题并给每个坐标轴打上标签
ax.set_title("Square Number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Number", fontsize=14)

# 设置每个坐标轴的范围
ax.axis([0, 1100, 0, 1_100_000])
"""
ax.ticklabel_format(style='plain')#anyway, 这行代码的作用是不使用科学计数法
"""
plt.show()