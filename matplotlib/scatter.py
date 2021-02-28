import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

x = [5, 7, 9, 15, 7, 4, 1, 9, 15, 100]
y = [7, 5, 7, 1, 10, 2, 4, 8, 5, 80]
colors = [7, 5, 6, 7, 8, 2, 1, 9, 5, 4]
sizes = [10, 20, 90, 12, 16, 17, 22, 25, 30, 50]

plt.scatter(x, y, s=sizes, c=colors, cmap='autumn', edgecolors='black', linewidths=1, alpha=0.75)

plt.xscale('log') #
plt.yscale('log') #

cbar = plt.colorbar()
cbar.set_label('Like/ Dislike Ration')
cbar.set_label('Satisfaction')
plt.show()
