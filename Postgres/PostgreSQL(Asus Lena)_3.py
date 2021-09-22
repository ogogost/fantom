import psycopg2
import random
import time
from tqdm import tqdm


dn = "postgres"
du = "postgres"
dp = "Wizard132"
dh = "127.0.0.1"
dbp = "5432"
dt = "table1"
cs = "dbname=%s user=%s password=%s host=%s port=%s" % (dn, du, dp, dh, dbp)


def name_gen(min_size_name, max_size_name):
    length_name = random.randint(min_size_name, max_size_name)
    name = ""
    for names in range(length_name):
        name = name + chr(random.randint(97, 122))
    return name.capitalize()


time1 = time.time()
N = 1000
data = []

for i in tqdm(range(N)):
    a = tuple((list([name_gen(3, 7)]), (list([name_gen(6, 9)]))))
    data.append(a)

# print("length:" + str(len(data)), data)
# print(type(data[0][0]))

connection = psycopg2.connect(cs)
cursor = connection.cursor()
sql = "INSERT INTO test(user_name, user_surname) VALUES(%s, %s)"
cursor.executemany(sql, data)

# cursor.execute("SELECT * from test")
# print(cursor.fetchall())
# print(type(cursor.fetchall()))
# print(len(cursor.fetchall()))

connection.commit()
cursor.close()

print('time:', time.time() - time1, 'sec')
