import sys
import sqlite3

tblname = sys.argv[1]
conn = sqlite3.connect('userinfo.db')
cur = conn.cursor()

tok = "SELECT * FROM " + tblname
for row in cur.execute(tok):
    print(row)

cur.close()
conn.close()
