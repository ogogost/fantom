import sqlite3

con = sqlite3.connect('test_mp.db')
cursor = con.cursor()
cursor.execute("select * from table1")
result = cursor.fetchone()
print(result)
