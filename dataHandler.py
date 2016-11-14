import matplotlib
import numpy
import datetime
from pylab import *
import sqlite3



conn = sqlite3.connect("dota2data.db")
cur  = conn.cursor()
cur.execute("select * from DOTA2")
peak_online_number = ()







