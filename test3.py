import sqlite3
from sqlite3 import Error
import time

data_base_path = 'TEST_1.db'
time1 = time.time()



def sql_connection():
    try:
        con = sqlite3.connect(data_base_path)
        print('Connection is established:', data_base_path)
    except Error as e:
        print(e)
    finally:
        con.close()


def sql_table():
    try:
        con = sqlite3.connect(data_base_path)
        cursor = con.cursor()
        cursor.execute("DROP TABLE IF EXISTS employees ")
        cursor.execute("CREATE TABLE employees(id INTEGER NOT NULL PRIMARY KEY, name TEXT)")
        con.commit()
        con.close()
    except Error as e:
        print(e)


def show_sql_table():
    try:
        con = sqlite3.connect(data_base_path)
        cursor = con.cursor()
        cursor.execute("SELECT * FROM employees")
        result = cursor.fetchall()
        print(result)
        con.close()
    except Error as e:
        print(e)


def insert_sql_table(data):

    try:
        sql = "INSERT INTO employees (name) VALUES (?)"
        # data = [data]
        # print(data)
        con = sqlite3.connect(data_base_path)
        cursor = con.cursor()
        cursor.execute(sql, (data,))
        con.commit()
        con.close()
    except Error as e:
        print(e)


sql_connection()
sql_table()
# insert_sql_table('example')

for i in range(1000):
    insert_sql_table('example')

show_sql_table()
time2 = time.time()
print(time2 - time1)
