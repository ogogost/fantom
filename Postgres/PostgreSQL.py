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


def postgres_version():
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(cs)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        print("Information about PostgreSQL server")
        print(connection.get_dsn_parameters(), '\n')
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You connected to ", record, "\n")

    except (Exception, Error) as error:
        print("Error", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connection to database is closed")


def create_database():
    connection = None
    cursor = None

    try:
        connection = psycopg2.connect(cs)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        query = """create database postgres_db"""
        cursor.execute(query)
        # print("Creating database:" + str(result))
        # record = cursor.fetchone()
        # print("You connected to ", record, "\n")

    except (Exception, Error) as error:
        print("Error", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connection to database is closed")


def create_table():
    connection = None
    cursor = None

    try:
        connection = psycopg2.connect(cs)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        sql_create_table = 'CREATE TABLE table_of_clients (id int PRIMARY KEY, users text, password text, cash int, stock int)'
        cursor.execute(sql_create_table)
        print("Creating table:{0}")

    except (Exception, Error) as error:
        print("Error", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connection to database is closed")

def insert_data(v1,v2):
    # self.data = data
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(cs)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        insertion = ("insert into test (cash,user_name) values (%s,%s)")
        cursor.executemany(insertion, (v1,v2))
        # print("")

    except (Exception, Error) as error:
        print("Error", error)

def select_all():
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(cs)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        sql = 'select * from test'
        cursor.execute(sql)
        print(cursor.fetchall())
        # for row in cursor:
        #     print(row)
    except (Exception, Error) as error:
        print("Error", error)

postgres_version()