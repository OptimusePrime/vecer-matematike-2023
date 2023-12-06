import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm

range_a = (0, 10)
range_t = (0, 60)

ax = plt.axes(projection="3d")

a = np.linspace(range_a[0], range_a[1], 60)
t = np.linspace(range_t[0], range_t[1], 60)
a, t = np.meshgrid(a, t)
func = lambda a_1, t_1: (a_1*t_1**2)/2
s = func(a, t)

ax.plot_surface(a, t, s, cmap=cm.coolwarm)
plt.show()