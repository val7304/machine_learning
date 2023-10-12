# -*- coding:Utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)
plt.subplot(2, 1, 1)
plt.bar(range(10), [x ** 2 for x in range(10)], color = 'blue')


# plt.subplot(2, 2, 2)
# plt.plot(range(5), color = 'red')


plt.subplot(2, 1, 2)
plt.bar(range(5), range(5), color = 'green')

plt.show()