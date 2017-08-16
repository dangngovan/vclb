import commands
import json
import time
import MySQLdb
conn = MySQLdb.connect(host= "10.5.52.33",
                  user="root",
                  passwd="Ngayconang@123",
                  db="quota")
x = conn.cursor()
#x.execute("SELECT *  FROM anooog1")
#x.execute (" INSERT INTO anooog1 VALUES ('%s','%s') ", (188,90))
#row = x.fetchall()

#jdata=json.dumps(data)
livetv_ntl_use =x.execute("select sudung from result  where time in (select max(time) from result group by project) AND project='NTL_CDN';")

print livetv_ntl_use
data = x.fetchall ()
for row in data:
	print row[0]
x.close()
