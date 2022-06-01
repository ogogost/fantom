import sqlite3 as sl

# import uuid
# print(uuid.uuid4().hex)
# from datetime import datetime, date, time
# print(datetime.today())

con = sl.connect('test.db')
cursor = con.cursor()
cursor.execute("SELECT * FROM TABLE_OF_ORDERS")

tupl = cursor.fetchall()
a = '\n'.join(map(str, tupl))
print(a)

