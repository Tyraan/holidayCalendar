import matplotlib
import numpy
import datetime
from pylab import *
import sqlite3


conn = sqlite3.connect("dota2data.db")
cur  = conn.cursor()
peak_online_number = []
average_online_number = []

startdate = datetime.date(2016,9,1)
for i in range(61):
    cur.execute("select * FROM DOTA2 WHERE date='%s'"%(startdate.strftime("%Y-%m-%d")))
    data = cur.fetchall()
    peak_online_number.append(data[-1][2])
    a = []
    for i in data:
        a.append(i[1])
    average_online_number.append(int(sum(a)/len(a)))
    startdate = startdate+datetime.timedelta(days=1)


num_bins = len(peak_online_number)
mu = 100
sigma = 15

peak_online_number_array = numpy.asarray(peak_online_number)
# the histogram of the data
n, bins, patches = plt.hist(peak_online_number_array, num_bins, normed=1, facecolor='red', alpha=0.7)
# add a 'best fit' line
y = mlab.normpdf(bins, mu, sigma)
plt.plot(bins, y, 'r--')
plt.xlabel('时间')
plt.ylabel('最高在线人数')
plt.title(r'dota2 9月10 月在线人数')
# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()










