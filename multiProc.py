from multiprocessing import Process
import time
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

dn = "postgres_db"
du = "postgres"
dp = "defender32"
dh = "127.0.0.1"
dbp = "5433"
dt = "table1"

cs = "dbname=%s user=%s password=%s host=%s port=%s" % (dn, du, dp, dh, dbp)

def insert_data(name):
    connection = None
    cursor = None

    try:
        connection = psycopg2.connect(cs)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        print('start of connection:' + str(name))
        time.sleep(5)
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

time1 = time.time()

if __name__ == '__main__':
    i = None
    proc = Process(target=insert_data, args=(i,))
    for i in range(3):
        proc.start(i)

    print(time.time() - time1)
