import time
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

dn = "postgres"
du = "postgres"
dp = "defender32"
dh = "127.0.0.1"
dbp = "5433"
dt = "table1"

cs = "dbname=%s user=%s password=%s host=%s port=%s" % (dn, du, dp, dh, dbp)

def create_table():
    connection = None
    cursor = None

    try:
        connection = psycopg2.connect(cs)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        sql_create_table = 'DROP TABLE IF EXISTS test2;' \
                           'CREATE UNLOGGED TABLE test2 (id serial PRIMARY KEY, cash int, user_name text)'
        cursor.execute(sql_create_table)
        print("Creating table:{0}")

    except (Exception, Error) as error:
        print("Error", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connection to database is closed")

def select_all():
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(cs)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        sql = 'select * from test2'
        cursor.execute(sql)
        print(cursor.fetchall())
        # for row in cursor:
        #     print(row)
    except (Exception, Error) as error:
        print("Error", error)


def insert_data(v1,v2):
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(cs)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        insertion = ("insert into test (cash,user_name) values (%s,%s)")
        cursor.execute(insertion, (v1,v2))

    except (Exception, Error) as error:
        print("Error", error)

def insert_data2(v1,v2):
    connection = None
    cursor = None
    connection = psycopg2.connect(cs)
    connection.autocommit = False
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    insertion = ("insert into test2 (cash,user_name) values (%s,%s)")
    for i in range(10000):
        cursor.execute(insertion, (v1, v2))
    connection.commit()
    cursor.close()
    connection.close()

def select_name(name):
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(cs)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        cursor.executemany('SELECT * from test2 where user_name=%s', str(name))
        print(cursor.fetchone())

    except (Exception, Error) as error:
        print("Error", error)

t1 = time.time()

select_name(' gaz')

print(time.time() - t1)