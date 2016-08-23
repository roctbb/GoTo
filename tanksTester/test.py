import sqlite3

conn = sqlite3.connect('tanks.sqlite')
c = conn.cursor()
c.execute("SELECT key FROM players")
result = c.fetchall()
for record in result:
    print(record[0])