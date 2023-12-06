import numpy as np
import matplotlib.pyplot as plt

range = (0, 14)

x = np.linspace(range[0], range[1], 14)
func = lambda x: 7*x - 5*(x**2)
y = func(x)

plt.style.use("seaborn-v0_8-whitegrid")
plt.plot(x, y, label="$ f(x) = 7x - 5x^2 $")
plt.legend(loc="center left")
plt.show()