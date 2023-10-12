import matplotlib.pyplot as plt
import numpy as np

t = np.array([1,2,3])

x1, = plt.plot(t**2, t, color="red")
x2, = plt.plot(t**3, t, color="orange")
x3, = plt.plot(t**4, t, color="green")

legend1 = plt.legend((x1,x2, x3), ["<= 30", "<= 50","> 50"], loc="lower right")
plt.gca().add_artist(legend1)

plt.xlabel("x label")
plt.ylabel("y label")
plt.title("multiple legend")

plt.show()