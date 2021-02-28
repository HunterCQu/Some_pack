from matplotlib import pyplot as plt
import numpy as np

plt.xkcd()

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
x_indexes = np.arange(len(ages_x))
width = 0.25

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65988, 70003, 70000, 71496, 75370, 83640]
# plt.plot(ages_x, py_dev_y, label='Python')
plt.bar(x_indexes - width, py_dev_y, width=width, label='Python')

js_dev_y = [55555, 88555, 58585, 88885, 22289, 76838, 70003, 71035, 71496, 75370, 96963]
# plt.plot(ages_x, js_dev_y, label='JavaScript')
plt.bar(x_indexes, js_dev_y, width=width, label='JavaScript')

dev_y = [75757, 65652, 14141, 25252, 78789, 34345, 52525, 42435, 25985, 12345, 56321]
# plt.plot(ages_x, dev_y, color='#444444', linestyle='--', label='All Devs')
plt.bar(x_indexes + width, dev_y, width=width, color='#444444', label='All Devs')

plt.xlabel('Ages')
plt.ylabel('Median Salary ($)')
plt.title('Median Salary by Age')

plt.legend()
plt.xticks(ticks=x_indexes, labels=ages_x) #
plt.tight_layout()
plt.savefig('plot.jpg')
plt.show()
