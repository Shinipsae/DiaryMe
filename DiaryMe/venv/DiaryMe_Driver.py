import os
import pymysql

conn = pymysql.connect(
    user='root',
    passwd='mysql',
    host='127.0.0.1',
    db='diaryme',
    charset='utf8'
)

cursor = conn.cursor()
sql = "select * from member"
cursor.execute(sql)

rows = cursor.fetchall()
# fetchone()은 한 줄, fetchmany(n)은 n줄
print(rows)
conn.close()
