# Thomas Reaney
# Electronic & Computer Engineering Student
# National University of Ireland Galway

from matplotlib import pyplot as plt
from matplotlib import style

style.use("ggplot")

x1 = [2, 4, 6, 8, 10]
y1 = [9, 4, 1, 3, 7]
x2 = [1, 3, 5, 7, 9]
y2 = [6, 2, 8, 4, 2]

# plt.scatter(x1, y1, color="red", linewidth=2, label="Line 01")
# plt.scatter(x2, y2, color="green", linewidth=2, label="Line 02")
plt.bar(x1, y1, color="red", linewidth=2, label="Line 01", align="center")
plt.bar(x2, y2, color="green", linewidth=2, label="Line 02", align="center")
plt.title("Random Graph")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.grid(True, color="k")
plt.show()
