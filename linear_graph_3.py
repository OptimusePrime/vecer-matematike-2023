import numpy as np
import matplotlib.pyplot as plt

range = (1, 6)

x = np.linspace(range[0], range[1], 6)
func = lambda t: 75*t
y = func(x)

plt.style.use("seaborn-v0_8-whitegrid")
plt.plot(x, y, label="$ s(t) = (75 km/h)t $")
plt.xlabel("t [h]")
plt.ylabel("s [km]")
plt.legend(loc="center left")
plt.show()