dn = "postgres"
du = "postgres"
dp = "defender32"
dh = "127.0.0.1"
dbp = "5433"
dt = "table1"

cs = "dbname=%s user=%s password=%s host=%s port=%s" % (dn, du, dp, dh, dbp)


def postgres_version():
    print(connection.get_dsn_parameters(), '\n')
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You connected to ", record, "\n")


def create_database():
    query = """create database postgres_db"""
    cursor.execute(query)


def create_table():
    sql_create_table = 'CREATE TABLE table_of_clients (id int PRIMARY KEY, users text, password text, cash int, stock int)'
    
    cursor.execute(sql_create_table)
    print("Creating table:{0}")


def insert_data(v1,v2):
    insertion = ("insert into test (cash,user_name) values (%s,%s)")
    cursor.executemany(insertion, (v1,v2))

def select_all(table_name):
    sql = 'select * from %s'
    cursor.executemany(sql, table_name)
    print(cursor.fetchall())

