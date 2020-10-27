import sqlite3
import sys

conn = sqlite3.connect('userinfo.db')
cur = conn.cursor()

thing = "shabnam@cse.iitb.ac.in"

cmd = "SELECT id, name, email, password, opassword FROM users INNER JOIN org ON org.oname=users.orgname WHERE users.email=?"
for row in cur.execute(cmd,(thing,)):
    print(row)

cur.close()
conn.close()
