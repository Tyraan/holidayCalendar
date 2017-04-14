import matplotlib
import numpy
import datetime
import pylab as pl
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

x = list(range(len(peak_online_number)))
pl.plot(x,peak_online_number)
pl.xlabel("")

pl.show()








