import numpy as np
import matplotlib.pyplot as plt

range = (0, 10)

x = np.linspace(range[0], range[1], 10)
func = lambda x: x**2 + 5
y = func(x)

plt.style.use("seaborn-v0_8-whitegrid")
plt.plot(x, y, label="$ f(x) = x^2 + 5 $")
plt.legend(loc="center left")
plt.show()