import numpy as np
import matplotlib.pyplot as plt

values = np.array([2,5,3,6,4,7,1])   
idx = np.array(list('abcdefg')) 
clrs = ['grey' if (x < max(values)) else 'red' for x in values ]
plt.bar(idx, values, color=clrs, width=0.4)
plt.show()