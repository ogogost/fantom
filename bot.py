import my_sql_module
import random
import time
import sqlite3


def generator_of_shit(con):
    while True or (flag_of_bot is True):
        time.sleep((random.randint(0,3)))
        my_sql_module.insert_sql_table(con, ((random.randint(0,100),(random.randint(0,100)))))
        print('line generated')
        return my_sql_module.get_line_from_table(con,'all')