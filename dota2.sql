DROP TABLE if EXISTS DOTA2;
CREATE TABLE DOTA2(

              id integer primary key autoincrement,
              currentNumber int NOT NULL,
              peakNumber int NOT NULL,
              date varchar(20) NOT NULL,
              time varchar(20) NOT Null
);
