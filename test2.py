import sqlite3
from sqlite3 import Error

data_base_path = 'test.db'

def sql_connection():
    try:
        con = sqlite3.connect(data_base_path)
        print('Connection is established:', data_base_path)
    except Error:
        print('Error')
    finally:
        con.close()

def sql_table():
    try:
        con = sqlite3.connect(data_base_path)
        cursorObj = con.cursor()
        cursorObj.execute("CREATE TABLE employees(id INTEGER NOT NULL PRIMARY KEY, name, salary real, department, position, hireDate)")
        con.commit()
    except Error:
        print('Error')

def show_sql_table():
    try:
        con = sqlite3.connect(data_base_path)
        cursorObj = con.cursor()
        cursorObj.execute("SELECT * FROM employees")
        result = cursorObj.fetchall()
        print(result)
    except Error as e:
        print(e)

def insert_sql_table(data):
    try:
        con = sqlite3.connect(data_base_path)
        cursorObj = con.cursor()
        v = [('Jhon', '10000', 'xxx', 'member', '%s'), (data)]
        cursorObj.executemany("INSERT INTO employees VALUES(?,?,?,?,?)", v)
        con.commit()
        # con.close()
    except Error as e:
        print(e)

# sql_connection()
sql_table()
insert_sql_table('231gfd')
# insert_sql_table('sdfsdf')
# insert_sql_table('fgdfgfdg')
show_sql_table()
