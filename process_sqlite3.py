from multiProc import Process
import time
import sqlite3
from multiProc import Pool

con = sqlite3.connect('test_mp.db')
cursor = con.cursor()
cursor.execute("DROP TABLE IF EXISTS table1")
cursor.execute("CREATE TABLE table1(id INTEGER PRIMARY KEY, name TEXT, surname TEXT)")

time1 = time.time()

def myfunc():
    con = sqlite3.connect('test_mp.db')
    cursor = con.cursor()
    sql = "INSERT INTO table1 (name, surname) VALUES (?,?)"

    for i in range(10):
        data = [('test'),('dkfjdf')]
        cursor.execute(sql, data)

    con.commit()

def myfunc2():
    con = sqlite3.connect('test_mp.db')
    cursor = con.cursor()
    sql = "INSERT INTO table1 (name, surname) VALUES (?,?)"

    for i in range(10):
        data = [('cxvxc'),('dskfhdskf')]
        cursor.execute(sql, data)

    con.commit()

def del_function():
    con = sqlite3.connect('test_mp.db')
    cursor = con.cursor()
    while True:
        sql_count = "SELECT COUNT(*) FROM table1"
        sql_del_1 = "DELETE * FROM table1 WHERE id=(SELECT max(id) FROM table1)"

        cursor.execute(sql_count)
        count = cursor.fetchall()[0]
        if count > 0:
            cursor.execute(sql_del_1)
            con.commit()
        else:
            print('Database is empty')
            break




if __name__ == "__main__":
    proc = Process(target=myfunc)
    proc2 = Process(target=del_function)
    cursor.execute("INSERT INTO table1 (name, surname) VALUES (?,?)", ("dfdfdf","dfdfsdf"))
    pool = Pool(processes= 2)
    pool.apply_async(myfunc)
    pool.apply_async(del_function)
    pool.close()
    pool.join()

    time2 = time.time()
    print(time2 - time1)
    cursor.execute("SELECT COUNT(*) FROM table1")
    result = cursor.fetchone()
    print(result)
    print(type(result))
