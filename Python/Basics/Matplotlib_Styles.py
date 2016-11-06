from matplotlib import pyplot as plt
from matplotlib import style

style.use("ggplot")

x = [5, 6, 7, 8, 8]
y = [9, 4, 1, 3, 7]

plt.plot(x, y)
plt.title("Random Graph")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()
