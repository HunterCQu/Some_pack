import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('linedata.csv')
ages = data['Age']
pop = data['Pop']
salary = data['Salary']

plt.plot(ages, pop, color='#444444', linestyle='-', label='Pop')
plt.plot(ages, salary, color='#333333', linestyle='-.', label='Salary')

# # Filling the Area between 'pop' and 'overall_median'
# overall_median = 10
# plt.fill_between(ages, pop, overall_median, where=(pop > overall_median), interpolate=True, color='red',
#                  alpha=0.25)
# plt.fill_between(ages, pop, overall_median, where=(pop <= overall_median), interpolate=True, color='green',
#                  alpha=0.25)

# Filling the Area between 'pop' and 'salary'
plt.fill_between(ages, pop, salary, where=(pop > salary), interpolate=True, color='red', alpha=0.25,
                 label='Pop higher than Salary')
plt.fill_between(ages, pop, salary, where=(pop <= salary), interpolate=True, color='green', alpha=0.25,
                 label='Salary higher than Pop')
plt.legend()
plt.title("A Chart")
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
