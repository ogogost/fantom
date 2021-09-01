from sqlite3 import Error

def sql_table(con):
    cursor = con.cursor()
    try:
        cursor.execute("DROP TABLE IF EXISTS employees ")
        cursor.execute("CREATE TABLE employees(id INTEGER NOT NULL PRIMARY KEY, name TEXT, surname TEXT)")
        con.commit()
        print('table is created')
    except Error as e:
        print(e)


def show_sql_table():
    cursor = con.cursor()
    try:
        cursor.execute("SELECT * FROM employees")
        result = cursor.fetchall()
        print(result)
    except Error as e:
        print(e)


def insert_sql_table(con, data):

    try:
        cursor = con.cursor()
        sql = "INSERT INTO employees (name, surname) VALUES (?, ?)"
        cursor.execute(sql, data)
        con.commit()
    except Error as e:
        print(e)


def get_line_from_table(con, data):
    cursor = con.cursor()
    if data == 'all':
        sql = "SELECT * FROM employees"
        cursor.execute(sql)
        print(cursor.fetchall())
    else:
        try:
            sql = f"SELECT * FROM employees WHERE id={data}"
            cursor.execute(sql)
            rows = cursor.fetchall()
            con.commit()
            return rows
        except Error as e:
            print(e)

