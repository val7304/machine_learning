import matplotlib.pyplot as plt
import numpy as np
# print(plt.style.available)

# ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 
# 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 
# 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 
# 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 
# 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 
# 'tableau-colorblind10']

x = np.linspace(0,2,10)  
y = x**2                    #tableau qui est le carré de x
print(x)


plt.figure(figsize=(12, 8))
plt.plot(x, y, label='quadratique')
plt.plot(x, x**3, label='cubique')

plt.title('Figure 1')
# axe des absyss
plt.xlabel('axe X')
# axe ordonné
plt.ylabel('axe Y')
# legend - prends des labels définis
plt.legend()
plt.show()
plt.savefig('nomdelafigure.png')

# afficher une autre figure, il faut juste recommencer le cycle
# plt.figure()
# plt.plot(5,10,15)
# plt.plot(10,20,15)
# plt.show()
