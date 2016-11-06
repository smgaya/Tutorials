from matplotlib import pyplot as plt
from matplotlib import style

style.use("ggplot")

x1 = [5, 6, 7, 8, 8]
y1 = [9, 4, 1, 3, 7]
x2 = [1, 3, 5, 7, 9]
y2 = [6, 2, 8, 4, 2]

plt.plot(x1, y1, linewidth=2, label="Line 01")
plt.plot(x2, y2, linewidth=2, label="Line 02")
plt.title("Random Graph")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.grid(True, color="k")
plt.show()
