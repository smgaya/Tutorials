# Thomas Reaney
# Electronic & Computer Engineering Student
# National University of Ireland Galway

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use("ggplot")

x, y = np.loadtxt("matplotlib.csv", unpack=True, delimiter=",")

print(x)
print(y)

plt.plot(x, y)
plt.title("CSV Data Graph")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid(True, color="k")
plt.show()
