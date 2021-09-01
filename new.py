import my_sql_module
import sqlite3
import bot
# from sqlite3 import Error

data_base_path = 'TEST_1.db'
con = sqlite3.connect(data_base_path)

my_sql_module.sql_table(con)
# my_sql_module.insert_sql_table(con,('example1', 'forest1'))
# my_sql_module.insert_sql_table(con,('example2', 'forest2'))
# my_sql_module.insert_sql_table(con,('example3', 'forest3'))
# my_sql_module.insert_sql_table(con,('example4', 'forest4'))
# my_sql_module.insert_sql_table(con,('example5', 'forest5'))

flag_of_bot = True
# bot.generator_of_shit(con)

print(my_sql_module.get_line_from_table(con, 'all'))