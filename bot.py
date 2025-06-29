import my_sql_module
import random
import time
import sqlite3

# shared flag controlling the generator loop
flag_of_bot = True


def generator_of_shit(con):
    """Insert random data until ``flag_of_bot`` becomes ``False``."""
    global flag_of_bot
    while flag_of_bot:
        time.sleep(random.randint(0, 3))
        my_sql_module.insert_sql_table(
            con,
            (random.randint(0, 100), random.randint(0, 100))
        )
        print('line generated')
        return my_sql_module.get_line_from_table(con, 'all')
