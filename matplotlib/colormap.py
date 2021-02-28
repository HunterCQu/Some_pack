import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

np.random.seed(20180316)
x = np.random.randn(32, 32)

f, ax2 = plt.subplots(figsize=(6, 6))

sns.heatmap(x, annot=False, ax=ax2, annot_kws={'size': 9, 'weight': 'bold', 'color': 'blue'})

plt.show()
