from multiprocessing import Process, Queue  # модуль для многопроцессовой работы, и работы с очередями
import server_module2 as s  # модуль для работы по сети
import PostgreSQL_2 as PS  # модуль для работы с БД постгрес
from psycopg2 import Error  # выдача кода ошибок
import psycopg2  # модуль для работы с постгрес
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def main_circle(q):
	PS.connection = None
	PS.cursor = None
	connection = psycopg2.connect(PS.cs)
	connection.autocommit = False
	connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
	cursor = connection.cursor()
	insertion = ("insert into test2 (cash,user_name) values (%s,%s)")

	while True:
		data = q.get()
		try:
			v1 = data.split(',')
			cursor.execute(insertion, v1)
			print('[Полученные данные (test2)] % s' % v1)
			sql = 'select * from test2'
			cursor.execute(sql)
			print(cursor.fetchall())
		except (Exception, Error) as error:
			print("Error", error)


def add_circle(q):
	PS.connection = None
	PS.cursor = None
	connection = psycopg2.connect(PS.cs)
	connection.autocommit = False
	connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
	cursor = connection.cursor()
	insertion = ("insert into test (cash,user_name) values (%s,%s)")
	while True:
		data = q.get()
		try:
			v1 = data.split(',')
			cursor.execute(insertion, v1)
			print('[Полученные данные (test3)] % s' % v1)
			sql = 'select * from test'
			cursor.execute(sql)
			print(cursor.fetchall())
		except (Exception, Error) as error:
			print("Error", error)


def socket_server_start(que1, que2):
	s.start_server(que1, que2)


if __name__ == '__main__':
	queue = Queue()
	queue2 = Queue()
	p1 = Process(target=main_circle, args=((queue),))
	p1.start()
	p2 = Process(target=socket_server_start, args=((queue), (queue2)))
	p2.start()
