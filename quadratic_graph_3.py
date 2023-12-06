import numpy as np
import matplotlib.pyplot as plt

range = (0, 14)

x = np.linspace(range[0], range[1], 14)
func = lambda t: 1 / 2 * 2.5 * (t ** 2)
y = func(x)

plt.style.use("seaborn-v0_8-whitegrid")
plt.plot(x, y, label=r"$ s(t) = \frac{1}{2}(2.5 m/s)t^2 $")
plt.legend(loc="center left")
plt.show()