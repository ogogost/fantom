import sqlite3
con = sqlite3.connect('test_mp.db')
cursor = con.cursor()
cursor.execute("SELECT COUNT(*) FROM table1")
# cursor.execute("SELECT * FROM table1")
result = cursor.fetchone()
print(result)
print(type(result))
