import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm

range_a = (0, 10)
range_t = (0, 10)

ax = plt.axes(projection="3d")

x = np.linspace(range_a[0], range_a[1], 10)
y = np.linspace(range_t[0], range_t[1], 10)
x, y = np.meshgrid(x, y)
func = lambda x_1, y_1: x_1**2 + 3*y_1 + 4
z = func(x, y)

ax.plot_surface(x, y, z, cmap=cm.coolwarm)
plt.show()