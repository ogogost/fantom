import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
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


def name_gen(a,b):
    length_name = random.randint(a,b)
    name = ""
    for i in range(length_name):
        name = name + chr(random.randint(97,122))
    return name.capitalize()

time1 = time.time()

N = 5
names_list = []

for i in tqdm(range(N)):
    a = tuple((list([name_gen(3,7)]),(list([name_gen(6,9)]))))
    names_list.append(a)

# surnames_list = []

# for i in tqdm(range(N)):
#     b = tuple(list([name_gen(5,10)]))
#     surnames_list.append(b)

print("length:" + str(len(names_list)), names_list)
# print("length:" + str(len(surnames_list)), surnames_list)
#
# sum_list = ((list), (surnames_list))
# print(len(sum_list), "sum_list:" + str(sum_list))

connection = psycopg2.connect(cs)
cursor = connection.cursor()
sql = ("INSERT INTO test(user_name, user_surname) VALUES(%s, %s)")
cursor.executemany(sql, names_list)
connection.commit()
cursor.close()

print('time:', time.time() - time1, 'sec')

