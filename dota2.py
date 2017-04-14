#Tyraan T  
# 2016/8/21

from bs4 import BeautifulSoup
import requests
import datetime

url = "http://store.steampowered.com/stats"
headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, sdch",
    "Accept-Language":"en-US,en;q=0.8",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
}

req=requests.get(url,timeout=50)
if req.status_code and req.status_code==200:
  soup = BeautifulSoup(req.content,"html.parser")
  span = soup.find_all(name='span',attrs="currentServers",limit=2)
  currentNumber,peakNumber =span[0],span[1]
  if currentNumber.string.replace(',','').isdigit():
    currentNumber=int(currentNumber.string.replace(',',''))
    peakNumber  = int(peakNumber.string.replace(',',''))
    now = datetime.datetime.now().strftime("%H:%M")  
    date = datetime.datetime.now().strftime("%Y-%m-%d")


#savedata
if now:
    import sqlite3
    conn = sqlite3.connect('dota2data.db')
    cur = conn.cursor()  
    cur.execute("""CREATE TABLE if not exists DOTA2 (
              id integer primary key autoincrement,
              currentNumber int NOT NULL,
              peakNumber int NOT NULL,
              date varchar(20) NOT NULL,
              time varchar(20) NOT Null
               );""")
    sql = "INSERT INTO DOTA2 (currentNumber,peakNumber,date,time) VALUES ( %d ,%d,'%s','%s')"%(currentNumber,peakNumber,date,now)
    cur.execute(sql)
    cur.execute("select * from DOTA2 ")
    for i in cur.fetchall():
    	print(i)
    conn.commit()
    print("data inserted %d ,%d ,%s"%(currentNumber,peakNumber,now))
    conn.close()
 

