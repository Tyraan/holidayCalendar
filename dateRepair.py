#__author__ = Tyraan
#__date__ = 2016/11/9

import datetime
import sqlite3


#read data

conn = sqlite3.connect("dota2data.db")
cur1  =conn.cursor()
cur2  =conn.cursor()
cur1.execute("UPDATE DOTA2 set date='2016-11-09' WHERE date='1996'")
cur1.execute("select * from DOTA2")
print("cur1 selected")

wrong_time_zone = ['00:20','00:50',
                   '01:20','01:50',
                   '02:20','02:50',
                   '03:20','03:50',
                   '04:20','04:50',
                   '05:20','05:50',
                   '06:20','06:50',
                   '07:20','07:50']


data = cur1.fetchone()
while data[3] != '2016-11-10':
    #if the date data in table is wrong timezone
    if data[4] in wrong_time_zone:
        currentdateobj = datetime.datetime.strptime(data[3], "%Y-%m-%d").date()
        currentdateobj+datetime.timedelta(days=1)
        correct_date = (currentdateobj+datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        sql = "UPDATE DOTA2 SET date='%s' WHERE id=%d"%(correct_date,data[0])
        cur2.execute(sql)
  
    data=cur1.fetchone()
    print("id = %d"%(data[0],))

conn.commit()
conn.close()