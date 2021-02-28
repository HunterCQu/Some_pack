import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn') 

data = pd.read_csv('time series.csv')
data['Date'] = pd.to_datetime(data['Date'])  # Sorting the date_value by the date
data.sort_values('Date', inplace=True)  # Making sure the plot flow the date not the ground value

date = data['Date']
price = data['Price']

plt.plot_date(date, price, linestyle='-')
plt.gcf().autofmt_xdate()  # Roting the X value of the Xaxis

# Change the date to BB-DD-YY
# date_format = mpl_dates.DateFormatter('%b, %d %y')
# plt.gca().xaxis.set_major_formatter(date_format)


plt.tight_layout()
plt.show()
